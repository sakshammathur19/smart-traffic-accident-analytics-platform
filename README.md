# 🚦 Smart Traffic & Accident Analytics Platform

> **A Near Real-Time Data Engineering Solution for Smart City Traffic Monitoring using AWS S3, Databricks, PySpark, Delta Lake, Power BI, and AWS SNS.**

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![AWS](https://img.shields.io/badge/AWS-S3%20%7C%20SNS-orange?logo=amazonaws)
![Databricks](https://img.shields.io/badge/Databricks-Data%20Engineering-red?logo=databricks)
![PySpark](https://img.shields.io/badge/PySpark-Big%20Data-yellow)
![Power BI](https://img.shields.io/badge/Power%20BI-Dashboard-F2C811?logo=powerbi)
![Delta Lake](https://img.shields.io/badge/Delta%20Lake-Medallion-blue)

---

# 📖 Project Overview

Urban traffic congestion and road accidents are major challenges in modern smart cities. Traditional traffic management systems rely on manual monitoring and historical reports, making it difficult to detect incidents quickly.

This project demonstrates a **Near Real-Time Data Engineering Pipeline** that continuously simulates traffic events, ingests data into a cloud data lake, processes it using the **Medallion Architecture (Bronze → Silver → Gold)**, generates business insights, visualizes analytics in **Power BI**, and sends **AWS SNS email alerts** for critical traffic situations.

---

# 🎯 Project Objectives

- Simulate continuous traffic sensor events
- Build a scalable cloud-based data pipeline
- Process streaming-like data using Databricks Auto Loader
- Clean and validate traffic records
- Detect congestion and accident hotspots
- Generate business-ready analytics
- Visualize insights using interactive Power BI dashboards
- Send automated emergency alerts using AWS SNS

---

# 🏗️ Solution Architecture

```text
                 Python Traffic Simulator
                          │
                          ▼
                  AWS S3 Data Lake
               (Raw Traffic Events)
                          │
                          ▼
            Databricks Auto Loader
         (Continuous File Ingestion)
                          │
                          ▼
               Bronze Delta Table
                 (Raw Data Layer)
                          │
                          ▼
      PySpark Cleaning & Validation
                          │
                          ▼
               Silver Delta Table
                (Clean Data Layer)
                          │
                          ▼
         PySpark Business Analytics
                          │
        ┌─────────────────┼──────────────────┐
        ▼                 ▼                  ▼
 Gold Congestion   Gold Accident      Gold Emergency
    Analysis         Hotspots             Alerts
        │                 │                  │
        └─────────────────┼──────────────────┘
                          ▼
                 Power BI Dashboards
                          │
                          ▼
             AWS SNS Email Notifications
```

---

# 🔄 Project Workflow

```text
Python Simulator
        │
        ▼
AWS S3 Landing
        │
        ▼
Databricks Auto Loader
        │
        ▼
Bronze Layer
        │
        ▼
Silver Layer
        │
        ▼
Gold Layer
        │
        ├────────────► AWS SNS
        │                 │
        │                 ▼
        │            Email Alert
        ▼
Power BI Dashboard
```

---

# 🥉 Bronze Layer

**Purpose**

Stores raw traffic events exactly as received from the simulator.

**Output Table**

```
bronze_traffic_events
```

---

# 🥈 Silver Layer

**Purpose**

Cleans and validates raw traffic data.

### Transformations

- Remove duplicate records
- Handle missing values
- Validate average speed
- Validate vehicle count
- Standardize road names
- Convert timestamps
- Add processing timestamp

**Output Table**

```
silver_traffic_cleaned
```

---

# 🥇 Gold Layer

## 🚗 Traffic Congestion Analytics

**Output Table**

```
gold_congestion_analysis
```

Business Rules

| Average Speed | Congestion Level |
|---------------|------------------|
| < 20 km/h | High Congestion |
| 20–50 km/h | Medium Congestion |
| > 50 km/h | Normal Traffic |

---

## 🚨 Accident Hotspots

**Output Table**

```
gold_accident_hotspots
```

Provides:

- Road-wise accident count
- High-risk locations
- Accident frequency analysis

---

## 🚑 Emergency Alerts

**Output Table**

```
gold_emergency_alerts
```

Business Rule

```
Accident = TRUE
AND
High Congestion
        ↓
Critical Alert
```

Critical alerts are published through **AWS SNS Email Notifications**.

---

# 📊 Power BI Dashboards

The project includes three interactive dashboards.

## Executive Dashboard

- Total Vehicles
- Average Speed
- Critical Alerts
- Accident Count
- Weather Distribution

---

## Congestion Analysis Dashboard

- Road-wise Congestion
- Speed Trends
- Vehicle Distribution
- Congestion Heat Analysis

---

## Accident Intelligence Dashboard

- Accident Hotspots
- Emergency Alerts
- Risk Analysis
- Road-wise Accident Summary

---

# 📧 AWS SNS Notification

Whenever a critical traffic event is detected:

```
Accident = TRUE
AND
High Congestion
```

↓

An email notification is automatically sent.

Example

```
🚨 SMART TRAFFIC ALERT

Road : MI Road

Priority : Critical

Vehicle Count : 645

Average Speed : 12 km/hr

Action Required:
Immediate traffic diversion.
```

---

# 🛠 Technology Stack

| Category | Technology |
|----------|------------|
| Programming | Python |
| Cloud Storage | AWS S3 |
| Notification | AWS SNS |
| Data Platform | Databricks |
| Processing | Apache Spark |
| Language | PySpark |
| Storage | Delta Lake |
| Architecture | Medallion Architecture |
| Visualization | Power BI |

---

# 📂 Project Structure

```
smart-traffic-accident-analytics-platform
│
├── simulator/
├── databricks/
├── powerbi/
├── architecture/
├── sample_data/
├── docs/
├── images/
├── README.md
└── LICENSE
```

---

# ▶️ How to Run

### 1. Run Python Simulator

Generates continuous traffic events and uploads them to AWS S3.

### 2. Run Bronze Notebook

Ingest new JSON files using Databricks Auto Loader.

### 3. Run Silver Notebook

Clean and validate traffic records.

### 4. Run Gold Notebook

Generate congestion analytics, accident hotspots, and emergency alerts.

### 5. Run SNS Notebook

Send email alerts for critical traffic situations.

### 6. Refresh Power BI

Visualize the latest traffic analytics.

---

# 💼 Business Benefits

- Near Real-Time Traffic Monitoring
- Congestion Detection
- Accident Hotspot Identification
- Automated Emergency Alerts
- Interactive Business Dashboards
- Reduced Manual Monitoring
- Scalable Cloud Data Pipeline
- Smart City Decision Support

---

# 🚀 Future Scope

- Live IoT Sensor Integration
- Apache Kafka Streaming
- Predictive Traffic Analytics
- Machine Learning Models
- Mobile Notification App
- AI-based Traffic Forecasting

---

# 👨‍💻 Author

**Saksham Mathur**

Final Year B.Tech Project

---

# ⭐ If you found this project useful, consider giving it a Star!
