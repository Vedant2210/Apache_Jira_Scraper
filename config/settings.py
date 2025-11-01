# config/settings.py

"""
Configuration file for the Apache Jira Scraper
"""

# -------------------- JIRA API SETTINGS --------------------
# Base REST API endpoint for Apache JIRA
JIRA_BASE_URL = "https://issues.apache.org/jira/rest/api/2/search"

# Default Apache projects to scrape
DEFAULT_PROJECTS = ["HADOOP", "SPARK", "KAFKA"]

# Maximum number of issues to fetch per project
MAX_ISSUES_PER_PROJECT = 100

# Number of issues fetched per API call
MAX_RESULTS_PER_REQUEST = 50


# -------------------- NETWORK & RATE LIMIT SETTINGS --------------------
REQUEST_TIMEOUT = 10
MAX_RETRIES = 5
BACKOFF_FACTOR = 2
RATE_LIMIT_DELAY = 2


# -------------------- DATA STORAGE PATHS --------------------
# Raw JSON responses from API
RAW_DATA_PATH = "./data/raw"

# Cleaned / processed JSONL data for LLM
PROCESSED_PATH = "./data/processed"

# Checkpoint data (last fetched issue, etc.)
CHECKPOINT_PATH = "./data/checkpoints"


# -------------------- LOGGING SETTINGS --------------------
LOG_PATH = "./logs"
