

import os
import json
from config.settings import PROCESSED_PATH
from src.logger import get_logger

logger = get_logger("transformer")

class DataTransformer:
    def __init__(self):
        os.makedirs(PROCESSED_PATH, exist_ok=True)

    def process_and_save(self, issues, project_name):
        """
        Process JIRA issues and append as JSONL (one JSON object per line).
        """
        logger.info(f"Processing {len(issues)} issues for project {project_name}")

        processed_issues = []

        # Example transformation logic
        for issue in issues:
            fields = issue.get("fields", {})
            processed = {
                "id": issue.get("id"),
                "key": issue.get("key"),
                "summary": fields.get("summary"),
                "status": fields.get("status", {}).get("name"),
                "assignee": fields.get("assignee", {}).get("displayName") if fields.get("assignee") else None,
                "created": fields.get("created"),
                "updated": fields.get("updated"),
                "description": fields.get("description"),
                "project": project_name
            }
            processed_issues.append(processed)

        # Save (append mode)
        output_file = os.path.join(PROCESSED_PATH, f"{project_name}_processed.jsonl")

        with open(output_file, "a", encoding="utf-8") as f:
            for item in processed_issues:
                f.write(json.dumps(item, ensure_ascii=False) + "\n")

        logger.info(f"Processed data appended to: {output_file}")
