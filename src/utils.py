import os, json, time
from tenacity import retry, wait_exponential, stop_after_attempt

def save_json(data,path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def load_json(path):
    if not os.path.exists(path): return {}
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def save_checkpoint(project, issue_key):
    os.makedirs("data/checkpoints", exist_ok=True)
    with open(f"data/checkpoints/{project}_checkpoint.json", "w") as f:
        json.dump({"last_issue": issue_key}, f)

def load_checkpoint(project):
    path = f"data/checkpoints/{project}_checkpoint.json"
    if os.path.exists(path):
        return load_json(path).get("last_issue")
    return None

def exponential_backoff_retry():
    return retry(wait=wait_exponential(multiplier=1, min=2, max=30),
                 stop=stop_after_attempt(5))
