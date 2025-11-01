# main.py
from src.scraper import JiraScraper
from src.transform import DataTransformer
from src.logger import get_logger
from config.settings import DEFAULT_PROJECTS, MAX_ISSUES_PER_PROJECT

logger = get_logger("main")

if __name__ == "__main__":
    logger.info(" Apache Jira Scraper started...")

    scraper = JiraScraper()
    transformer = DataTransformer()

    for project in DEFAULT_PROJECTS:
        logger.info(f"🔍 Scraping project: {project}")
        issues = scraper.fetch_issues(project, max_issues=MAX_ISSUES_PER_PROJECT)

        transformer.process_and_save(issues, project)

    logger.info(" All projects processed successfully.")
