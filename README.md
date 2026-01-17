# NFL Fantasy Data Engineering Pipeline

## Project Overview
This is an end-to-end Data Engineering project designed to ingest, store, and transform NFL player statistics for fantasy football analysis.

The goal of this project is to build a modern ELT (Extract, Load, Transform) pipeline that mirrors enterprise-grade data architectures. It automates the retrieval of raw data from the `nfl_data_py` library, moves it into a cloud-based Data Lake (Azure), and models it for downstream analytics.

## Learning Objectives & Tech Stack
* **Cloud Infrastructure:** Microsoft Azure (Data Lake Gen2, Azure SQL, Data Factory).
* **Data Engineering:** Designing ELT pipelines, handling raw vs. processed data zones.
* **Python Scripting:** Automating data extraction and API interaction.
* **DevOps & CI/CD:** Using GitHub Actions for automated testing and deployment.
* **Data Modeling:** Structuring data into Star Schemas (Facts & Dimensions) for efficient querying.

## Architecture
1.  **Extraction (Python):** Scripts fetch weekly player stats and roster data from the `nfl_data_py` library.
2.  **Ingestion (Azure Data Lake):** Raw CSVs are uploaded to Azure Blob Storage (Bronze Layer).
3.  **Orchestration (Azure Data Factory):** Triggers run on a weekly schedule (Tuesday mornings) to capture finalized game data.
4.  **Transformation (SQL/DBT):** Data is cleaned and modeled into `fact_weekly_stats` and `dim_players` tables.

## How to Run Locally

### Prerequisites
* Python 3.11+
* Azure Storage Account (for cloud upload)

### Setup
1.  Clone the repository:
    ```bash
    git clone https://github.com/cshigh22/nfl_data.git
    ```
2.  Create and activate a virtual environment:
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # Windows: .venv\Scripts\activate
    ```
3.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4.  Run the extraction script:
    ```bash
    python src/extract.py
    ```
OR

# 1. Create the virtual environment
python -m venv .venv

# 2. Activate it
# Windows:
.venv\Scripts\activate
# Mac/Linux:
source .venv/bin/activate

# 3. Install the libraries we discussed
pip install nfl_data_py pandas azure-storage-blob azure-identity python-dotenv
