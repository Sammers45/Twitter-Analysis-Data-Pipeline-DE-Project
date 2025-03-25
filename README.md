# 🐦 Twitter Analysis Data Engineering Pipeline

This project automates the process of collecting, transforming, and storing Twitter data using a modern ETL pipeline architecture. Built with **Python**, **Airflow**, and deployed on an **AWS EC2 Ubuntu instance**, it connects to the **Twitter API** to extract tweet metrics from public accounts (e.g., Elon Musk), and structures them into CSV files for downstream use.

---

## 🚀 Features

- Fetches live tweet data using Twitter API (via Tweepy)
- Automates ETL process using Apache Airflow
- Orchestrated workflows scheduled and triggered via Airflow UI
- Runs on scalable Amazon EC2 (Ubuntu)
- Uses Git for version control
- Supports environment isolation with pipx

---

## 📁 Project Structure


---

## 🛠️ Tools & Technologies

- **Python 3.7+**
- **Apache Airflow**
- **Tweepy (Twitter API)**
- **Pandas**
- **AWS EC2 (Ubuntu)**
- **pipx (optional)**
- **Git**

---

## 🧱 Pipeline Process

### 1. **Extraction**
Connects to Twitter API and retrieves recent tweets of a target user using their username and bearer token authentication.

### 2. **Transformation**
Structures and cleans the raw tweet data, extracting key information like:
- Tweet text
- Like counts
- Retweet counts
- Created timestamp

### 3. **Loading**
The final transformed data is saved into a local CSV file (e.g., `elonmusk.csv`). Can be extended to save to S3.

### 4. **Automation via Airflow**
- DAG defines the sequence of tasks in the ETL pipeline.
- Runs manually or automatically at scheduled intervals.
- Logs and retry mechanisms provided by Airflow.

---

## ☁️ Deployment (AWS EC2)

The project is deployed on an Ubuntu EC2 instance:
- SSH into instance
- Install dependencies (Python, pip, pipx, Airflow)
- Clone the repo and place files under `~/airflow/dags/`
- Start Airflow webserver and scheduler

---

## 🔧 Git Workflow

- `git clone <repo-url>`
- `git checkout -b <feature-branch>`
- `git add . && git commit -m "message"`
- `git push origin <branch>`

---

## 🔐 Twitter API Access

To use the project, create a Twitter Developer App and generate a Bearer Token:
- https://developer.twitter.com/

Paste the token into the ETL script (`twitter_etl.py`) in the appropriate variable.

---

## 📌 Future Enhancements

- Store data in Amazon S3 or a database (e.g., PostgreSQL, Redshift)
- Add analytics/visualization layer
- Dockerize the setup for easier deployment
