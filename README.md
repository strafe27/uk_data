# Gridwatch Energy Data Engineering Project

This data engineering project focuses on ingesting energy data from **Gridwatch**, processing it to generate summaries on a yearly, monthly, and weekly basis, and visualizing the results using **Power BI**. The goal is to provide insights into UK energy consumption patterns over time.

## Tools Used:
- **SQLite**: For storing and querying the processed data in a local database.
- **Power BI**: For creating interactive visualizations and dashboards.

## Project Workflow:

### 1. Data Ingestion
   The project starts with the ingestion of energy data from Gridwatch. The data is collected periodically and stored in SQLite for further processing.

### 2. Data Cleaning and Transformation
   After ingestion, the data is cleaned to remove any inconsistencies or missing values. This step includes formatting the dates, handling missing or erroneous entries, and ensuring that the data is in a suitable format for analysis.

### 3. Data Warehouse Modeling
   The cleaned data is then transformed into a data warehouse structure. Fact tables and dimension tables are created to support efficient querying and summarization. Key metrics such as total demand, peak demand, and moving averages are stored in the warehouse for easy access.

### 4. Data Summarization
   Yearly, monthly, and weekly summaries are generated using SQL queries. These summaries provide insights into energy consumption trends, including identifying peak demand periods, comparing year-over-year changes, and analyzing seasonal variations.

### 5. Visualization in Power BI
   The summarized data is visualized using **Power BI**. The dashboards include interactive graphs and charts that allow users to explore the data, view trends over time, and gain actionable insights into energy consumption.

## How to Use This Repository:
1. Clone the repository to your local machine.
2. Set up the SQLite database and ingest the Gridwatch data.
3. Run the cleaning and transformation scripts to prepare the data.
4. Use Power BI to connect to the SQLite database and load the prepared data.
5. Open the Power BI report to view the visualizations.

---

This project provides a framework for monitoring and analyzing energy data from Gridwatch, with the goal of understanding the UK's energy consumption patterns and visualizing them effectively.
