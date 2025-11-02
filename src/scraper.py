

import os
import time
import requests
from typing import List, Dict, Any

from config.settings import (
    JIRA_BASE_URL,
    MAX_ISSUES_PER_PROJECT,
 
    CHECKPOINT_PATH,
    RATE_LIMIT_DELAY,
     RAW_DATA_PATH,
    REQUEST_TIMEOUT,
    MAX_RETRIES,
    BACKOFF_FACTOR
)

from src.logger import get_logger
from src.utils import save_json, load_checkpoint, save_checkpoint

logger = get_logger("scraper")


class JiraScraper:
    """Scraper for Apache Jira issues with retry, checkpoint, and fault tolerance."""

    def __init__(self):
        os.makedirs(RAW_DATA_PATH, exist_ok=True)
        os.makedirs(CHECKPOINT_PATH, exist_ok=True)
        self.session = requests.Session()
        self.session.headers.update({"User-Agent": "ApacheJiraScraper/1.0"})

    def _get_with_retries(self, url: str, params: Dict[str, Any]) -> requests.Response:
        """Handle retries, backoff, and 429/5xx responses."""
        for attempt in range(1, MAX_RETRIES + 1):
            try:
                response = self.session.get(url, params=params, timeout=REQUEST_TIMEOUT)

                # Handle rate limiting
                if response.status_code == 429:
                    logger.warning(f"Rate limit hit (429). Sleeping {RATE_LIMIT_DELAY * attempt}s...")
                    time.sleep(RATE_LIMIT_DELAY * attempt)
                    continue

                # Retry on 5xx server errors
                if response.status_code >= 500:
                    logger.warning(f"Server error {response.status_code}. Retrying (attempt {attempt})...")
                    time.sleep(BACKOFF_FACTOR ** attempt)
                    continue

                response.raise_for_status()
                return response

            except requests.RequestException as e:
                logger.error(f"Request failed (attempt {attempt}/{MAX_RETRIES}): {e}")
                time.sleep(BACKOFF_FACTOR ** attempt)

        raise Exception(f"Failed after {MAX_RETRIES} attempts to fetch {url}")

    def fetch_issues(self, project_key: str, max_issues: int = MAX_ISSUES_PER_PROJECT) -> List[Dict[str, Any]]:
        """Fetch issues for a given project with pagination and checkpoint recovery."""
        logger.info(f"Starting fetch for project: {project_key}")
        start_at = load_checkpoint(project_key)
        all_issues: List[Dict[str, Any]] = []
        if start_at is None:
            start_at=0;

        while start_at < max_issues:
            params = {
                "jql": f"project={project_key} ORDER BY created DESC",
                "startAt": start_at,
                "maxResults": 50,  # Jira's recommended limit per page
                "fields": "summary,description,comment,created,updated,status,priority,assignee,reporter,labels"
            }

            try:
                response = self._get_with_retries(JIRA_BASE_URL, params)
                data = response.json()

                issues = data.get("issues", [])
                if not issues:
                    logger.info(f"No more issues for {project_key}. Stopping.")
                    break

                all_issues.extend(issues)
                save_json(data, os.path.join(RAW_DATA_PATH, f"{project_key}_{start_at}.json"))

                logger.info(f"Fetched {len(issues)} issues from {project_key} (startAt={start_at})")

                start_at += len(issues)
                save_checkpoint(project_key, start_at)

                time.sleep(RATE_LIMIT_DELAY)

            except Exception as e:
                logger.error(f"Error fetching {project_key} at {start_at}: {e}")
                time.sleep(RATE_LIMIT_DELAY)

        logger.info(f"Completed fetch for project {project_key}. Total issues: {len(all_issues)}")
        return all_issues
