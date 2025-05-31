# GCP Sales Data Pipeline

This project simulates a real-time sales data pipeline on Google Cloud using:

- **Cloud Functions** for publishing data to Pub/Sub
- **Pub/Sub** to stream data
- **BigQuery** as raw and modeled data store
- **Dataform** for SQL-based data modeling
- **Cloud Composer (Airflow)** to orchestrate the workflow

## 💡 Architecture
![Pipeline Architecture](https://github.com/user-attachments/assets/c2bbc7c7-1b39-462f-b876-8a9c00f8fdf8)


## 🚀 Components

- **Cloud Function**: Publishes fake sales orders using Faker
- **Pub/Sub**: Streams the messages
- **BigQuery**: Stores raw and processed data
- **Dataform**: Builds star schema from raw events
- **Composer DAG**: Triggers function and Dataform sequentially

## 🗂 DAG

![Airflow Dag](https://github.com/user-attachments/assets/0197a3aa-21a6-4dee-b1a9-c23f99001555)


## 📊 Data Model

![Data Model](https://github.com/user-attachments/assets/7f6d5e0d-62c8-457c-994c-f2aa3d9e55a4)


## ✅ How to Run

1. Deploy the Cloud Function using GCP Console/CLI
2. Set up Pub/Sub and BigQuery raw table
3. Create and link a Dataform repository
4. Set up Composer DAG to orchestrate the full pipeline

---

## 📦 Requirements

- GCP Project
- Python 3.8+
- Libraries:
  ```bash
  pip install faker google-cloud-pubsub
