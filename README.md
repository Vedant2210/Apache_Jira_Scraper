
# 🐘 Apache JIRA Scraper

## 📘 Overview
The **Apache JIRA Scraper** is a Python-based project designed to fetch, process, and store issue data from **Apache JIRA projects** such as **HADOOP**, **SPARK**, and **KAFKA**.

It scrapes **publicly available data** from the [Apache JIRA](https://issues.apache.org/jira/) website, transforms it into a structured format, and saves it as `.jsonl` (JSON Lines) files for easy analysis.

---

## 🚀 Features

- 🔍 Scrapes issue data (title, ID, description, status, reporter, etc.)
- 🧹 Cleans and structures raw data into JSONL format
- 📂 Automatically saves processed data in organized folders
- ⚙️ Customizable configuration for projects and issue limits
- 🪵 Built-in logging for monitoring scraping progress
- ⚡ Lightweight and modular Python design

---

---

## 🏗️ Project Structure

```bash
apache-jira-scraper/
│
├── config/
│   └── settings.py           # Configuration variables (projects, limits)
│
├── data/
│   └── processed/            # Output folder for JSONL files
│
├── src/
│   ├── scraper.py            # Core scraping logic
│   ├── transform.py          # Data transformation and saving
│   └── logger.py             # Logging setup
│
├── main.py                   # Main entry point
├── requirements.txt          # Project dependencies
└── README.md                 # Documentation


yaml
Copy code

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Vedant2210/Apache_Jira_Scraper.git
cd Apache_Jira_Scraper
2️⃣ Create a Virtual Environment
bash
Copy code
python -m venv venv
3️⃣ Activate the Virtual Environment
Windows:

bash
Copy code
venv\Scripts\activate
macOS/Linux:

bash
Copy code
source venv/bin/activate
4️⃣ Install Dependencies
bash
Copy code
pip install -r requirements.txt
▶️ Usage
Run the Scraper
bash
Copy code
python main.py
The scraper will start fetching issues for all projects listed in your settings.py file.

By default, it will process:

ini
Copy code
DEFAULT_PROJECTS = ["HADOOP", "SPARK", "KAFKA"]
Output Format
All processed issues will be stored in:

bash
Copy code
data/processed/{project_name}_issues.jsonl
Each line in the .jsonl file represents one issue in JSON format, for example:

json
Copy code
{"id": "HADOOP-1001", "summary": "Fix namenode error", "status": "Open", "reporter": "user123"}
{"id": "SPARK-2020", "summary": "Improve shuffle performance", "status": "Closed", "reporter": "dev456"}
🧠 Key Concepts Covered
Web Scraping (requests, BeautifulSoup)

Data Cleaning & Transformation

File Handling (JSONL format)

Logging & Error Handling

Modular Python Project Structure

Configuration Management

Automation using Scripts

⚖️ Notes & Guidelines
✅ Use only publicly available data from Apache JIRA.

⏳ Respect rate limits — avoid overloading the Apache servers.

🧪 You may use alternative APIs or innovative scraping methods.

🤖 LLM-assisted coding is allowed, but you must understand your approach.

🧩 Future Enhancements
Add sentiment analysis on issue descriptions

Integrate with Apache JIRA REST API for faster data access

Build a simple dashboard for visualization

Store data in a database (e.g., SQLite or PostgreSQL)
