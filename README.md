Employee Performance Analytics

A complete Employee Performance Analytics System built with Python, SQLite, Pandas, Streamlit, and REST APIs, designed to collect, analyze, and visualize employee performance data.

The project combines internal employee data with external task information from APIs to compute performance metrics and display them in an interactive dashboard.

📌 Project Overview

This project demonstrates an end-to-end data workflow, including:

Database creation and management with SQLite

Fetching and merging internal performance data and external API tasks

Data cleaning, transformation, and calculation of metrics

Interactive dashboard for visualization using Streamlit

It can be used for HR analytics, employee performance tracking, or as a learning resource for Python data analytics projects.

🏗️ Features
1. Database Management

Creates an SQLite database with tables:

employee (stores employee details)

performance (stores task completion and hours worked)

Inserts sample data automatically

Provides a reset/clean functionality via database_clean.py

2. Data Integration

Fetches employee and performance data from SQLite

Fetches task data from a public API (jsonplaceholder.typicode.com)

Merges both datasets into a single DataFrame

Cleans and prepares data for analysis

3. Analytics

Calculates task efficiency per employee:

task_efficiency = (tasks_completed + tasks_from_API) / hours_worked


Compares internal vs external tasks completed

Handles missing values and ensures clean, accurate metrics

4. Interactive Dashboard

Built using Streamlit

Displays employee performance tables

Shows bar charts for:

Task efficiency per employee

Tasks completed via API

Provides a real-time interactive dashboard

📂 Project Structure
Employee_Performance_Analytics/
│
├── database.py              # Creates DB and inserts sample data
├── fetch_sql.py             # Reads employee & performance data from SQLite
├── fetch_api.py             # Fetches task data from external API
├── process_data.py          # Merges, cleans, and calculates metrics
├── database_clean.py        # Clears database records
├── dashboard.py             # Streamlit dashboard UI
├── employee_performance.db  # SQLite database (auto-generated)
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation

🚀 How to Run
1️⃣ Install dependencies
pip install pandas streamlit requests

2️⃣ Setup database
python database.py

3️⃣ Merge and process data
python process_data.py

4️⃣ Run the dashboard
streamlit run dashboard.py

🎯 Technologies Used

Python

SQLite

Pandas

Requests (REST API)

Streamlit

Data visualization and analytics

💡 Use Cases

HR analytics and performance dashboards

Employee productivity tracking

Real-world ETL (Extract–Transform–Load) practice

Learning full-stack data analytics with Python

Interactive dashboards for small organizations
