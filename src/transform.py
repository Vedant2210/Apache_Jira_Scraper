# # src/transform.py

# import os
# import json
# from typing import List, Dict, Any
# from config.settings import RAW_DATA_PATH, PROCESSED_PATH
# from src.utils import save_json
# from src.logger import get_logger

# logger = get_logger("transformer")

# class DataTransformer:
#     def __init__(self):
#         os.makedirs(PROCESSED_PATH, exist_ok=True)

#     def transform_issue(self, issue: Dict[str, Any]) -> Dict[str, Any]:
#         """Convert raw Jira issue JSON to structured JSONL format."""
#         fields = issue.get("fields", {})

#         transformed = {
#             "id": issue.get("id"),
#             "key": issue.get("key"),
#             "project": fields.get("project", {}).get("key"),
#             "title": fields.get("summary"),
#             "status": fields.get("status", {}).get("name"),
#             "priority": fields.get("priority", {}).get("name"),
#             "assignee": fields.get("assignee", {}).get("displayName") if fields.get("assignee") else None,
#             "reporter": fields.get("reporter", {}).get("displayName") if fields.get("reporter") else None,
#             "labels": fields.get("labels", []),
#             "created": fields.get("created"),
#             "updated": fields.get("updated"),
#             "description": fields.get("description"),
#             "comments": self._extract_comments(fields),
#         }

#         return transformed

#     def _extract_comments(self, fields: Dict[str, Any]) -> List[str]:
#         """Extract comments from issue fields."""
#         comments = fields.get("comment", {}).get("comments", [])
#         return [c.get("body", "") for c in comments if c.get("body")]

#     def transform_project(self, project_key: str):
#         """Read raw JSON files for a project, transform, and save to processed folder."""
#         logger.info(f"Transforming data for project: {project_key}")
#         project_files = [
#             f for f in os.listdir(RAW_DATA_PATH) if f.startswith(project_key)
#         ]

#         all_transformed = []
#         for file_name in project_files:
#             file_path = os.path.join(RAW_DATA_PATH, file_name)
#             try:
#                 with open(file_path, "r", encoding="utf-8") as f:
#                     data = json.load(f)
#                     issues = data.get("issues", [])
#                     for issue in issues:
#                         all_transformed.append(self.transform_issue(issue))
#             except Exception as e:
#                 logger.error(f"Error processing {file_name}: {e}")

#         output_path = os.path.join(PROCESSED_PATH, f"{project_key}_transformed.jsonl")
#         with open(output_path, "w", encoding="utf-8") as f:
#             for item in all_transformed:
#                 f.write(json.dumps(item) + "\n")

#         logger.info(f"Saved {len(all_transformed)} transformed issues to {output_path}")


# import os
# import json
# from typing import List, Dict, Any
# from config.settings import RAW_DATA_PATH, PROCESSED_PATH
# from src.utils import save_json
# from src.logger import get_logger

# logger = get_logger("transform")


# class DataTransformer:
#     """Transform raw Jira issue data into a clean, structured format for analysis or LLM input."""

#     def __init__(self):
#         os.makedirs(PROCESSED_PATH, exist_ok=True)

#     def _transform_issue(self, issue: Dict[str, Any]) -> Dict[str, Any]:
#         """Extract relevant fields and flatten nested structures."""
#         fields = issue.get("fields", {})
#         return {
#             "key": issue.get("key"),
#             "summary": fields.get("summary"),
#             "description": fields.get("description"),
#             "created": fields.get("created"),
#             "updated": fields.get("updated"),
#             "status": fields.get("status", {}).get("name"),
#             "priority": fields.get("priority", {}).get("name"),
#             "assignee": fields.get("assignee", {}).get("displayName") if fields.get("assignee") else None,
#             "reporter": fields.get("reporter", {}).get("displayName") if fields.get("reporter") else None,
#             "labels": fields.get("labels", []),
#             "comment_count": len(fields.get("comment", {}).get("comments", [])),
#         }

#     def process_and_save(self, issues: List[Dict[str, Any]], project_name: str) -> None:
#         """Transform all issues and save as processed JSON."""
#         if not issues:
#             logger.warning(f"No issues to process for project: {project_name}")
#             return

#         logger.info(f"Processing {len(issues)} issues for project {project_name}")

#         processed = [self._transform_issue(issue) for issue in issues]

#         file_path = os.path.join(PROCESSED_PATH, f"{project_name}_processed.json")
#         save_json(processed, file_path)

#         logger.info(f"Processed data saved: {file_path}")





# import os
# import json
# from config.settings import PROCESSED_PATH
# from src.logger import get_logger

# logger = get_logger("transformer")

# class DataTransformer:
#     def __init__(self):
#         os.makedirs(PROCESSED_PATH, exist_ok=True)

#     def process_and_save(self, issues, project_name):
#         """
#         Process JIRA issues and save as JSONL (one JSON object per line).
#         """
#         logger.info(f"Processing {len(issues)} issues for project {project_name}")

#         processed_issues = []

#         # Example transformation logic
#         for issue in issues:
#             fields = issue.get("fields", {})
#             processed = {
#                 "id": issue.get("id"),
#                 "key": issue.get("key"),
#                 "summary": fields.get("summary"),
#                 "status": fields.get("status", {}).get("name"),
#                 "assignee": fields.get("assignee", {}).get("displayName") if fields.get("assignee") else None,
#                 "created": fields.get("created"),
#                 "updated": fields.get("updated"),
#                 "description": fields.get("description"),
#                 "project": project_name
#             }
#             processed_issues.append(processed)

#         # Save as JSONL (each issue on a new line)
#         output_file = os.path.join(PROCESSED_PATH, f"{project_name}_processed.jsonl")

#         with open(output_file, "w", encoding="utf-8") as f:
#             for item in processed_issues:
#                 f.write(json.dumps(item, ensure_ascii=False) + "\n")

#         logger.info(f"Processed data saved: {output_file}")


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
