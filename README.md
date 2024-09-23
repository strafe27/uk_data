# Gridwatch Energy Data Engineering Project

This data engineering project focuses on ingesting energy data from **Gridwatch**, processing it to generate summaries on a yearly, monthly, and weekly basis, and visualizing the results using **Power BI**. The goal is to provide insights into UK energy consumption patterns over time.

## Tools Used:
- **SQLite**: For storing and querying the processed data in a local database.
- **Power BI**: For creating interactive visualizations and dashboards.

## Project Workflow:

### 1. Data Ingestion
   The project starts with the ingestion of energy data from Gridwatch. The data is collected from 2011 until 2024.

### 2. Data Cleaning and Transformation
   After ingestion, the data is cleaned to remove any inconsistencies or missing values.
   Checks includes - Duplication checks, Null checks, Removal of rows where demand is '0'
   This step also includes formatting the dates, handling missing or erroneous entries, and ensuring that the data is in a suitable format for analysis.
   Data is then saved into a bronze layer

### 3. Data Warehouse Modeling
   The cleaned data is then transformed into a data warehouse structure.Key metrics such as total demand, peak demand, and moving averages are stored in the warehouse for easy access.

### 4. Data Summarization
   Yearly, monthly, and weekly summaries are generated using SQL queries. These summaries provide insights into energy consumption trends, including identifying peak demand periods, comparing year-over-year changes, and analyzing seasonal variations.

<p align="center">
  <img src="https://github.com/user-attachments/assets/700d0fa8-2a52-4ef3-97cf-45d1315f9396" alt="Data Pipeline Diagram"/>
</p>

### 5. Visualization in Power BI
   The summarized data is visualized using **Power BI**. The dashboards include interactive graphs and charts that allow users to explore the data, view trends over time, and gain actionable insights into energy consumption.

<p align="center">
  <img src="https://github.com/user-attachments/assets/4b183c2f-4326-4c28-9350-0e9453cdbcad" alt="Data Pipeline Diagram"/>
</p>
The CSV and db data can be found in data.rar
