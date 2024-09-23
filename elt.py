import sqlite3
import pandas as pd

# Connect to the database
conn = sqlite3.connect('power_data.db')
c = conn.cursor()

# Create the sum_daily_demand table (30-day moving average)
c.execute("""
    CREATE TABLE IF NOT EXISTS sum_daily_demand AS
    SELECT 
        DATE(timestamp) AS date, 
        SUM(demand) AS total_daily_demand,
        CASE
            WHEN COUNT(*) OVER (ORDER BY DATE(timestamp) ROWS BETWEEN 29 PRECEDING AND CURRENT ROW) = 30
            THEN AVG(SUM(demand)) OVER (ORDER BY DATE(timestamp) ROWS BETWEEN 29 PRECEDING AND CURRENT ROW)
            ELSE NULL
        END AS moving_avg_30_days
    FROM stg_power_data
    GROUP BY DATE(timestamp);
""")

# Create the sum_weekly_demand table (4-week moving average)
c.execute("""
    CREATE TABLE IF NOT EXISTS sum_weekly_demand AS
    WITH weekly_data AS (
        SELECT 
            strftime('%Y-%W', DATE(timestamp)) AS year_week, 
            SUM(demand) AS total_weekly_demand
        FROM stg_power_data
        GROUP BY strftime('%Y-%W', DATE(timestamp))
    )
    SELECT 
        year_week,
        total_weekly_demand,
        CASE
            WHEN COUNT(*) OVER (ORDER BY year_week ROWS BETWEEN 3 PRECEDING AND CURRENT ROW) = 4
            THEN AVG(total_weekly_demand) OVER (ORDER BY year_week ROWS BETWEEN 3 PRECEDING AND CURRENT ROW)
            ELSE NULL
        END AS moving_avg_4_weeks
    FROM weekly_data;
""")

# Create the sum_monthly_demand table (6-month moving average)
c.execute("""
    CREATE TABLE IF NOT EXISTS sum_monthly_demand AS
    WITH monthly_data AS (
        SELECT 
            strftime('%Y-%m', DATE(timestamp)) AS year_month, 
            SUM(demand) AS total_monthly_demand
        FROM stg_power_data
        GROUP BY strftime('%Y-%m', DATE(timestamp))
    )
    SELECT 
        year_month,
        total_monthly_demand,
        CASE
            WHEN COUNT(*) OVER (ORDER BY year_month ROWS BETWEEN 5 PRECEDING AND CURRENT ROW) = 6
            THEN AVG(total_monthly_demand) OVER (ORDER BY year_month ROWS BETWEEN 5 PRECEDING AND CURRENT ROW)
            ELSE NULL
        END AS moving_avg_6_months
    FROM monthly_data;
""")

# Create the sum_yearly_demand table (2-year moving average)
c.execute("""
    CREATE TABLE IF NOT EXISTS sum_yearly_demand AS
    WITH yearly_data AS (
        SELECT 
            strftime('%Y', DATE(timestamp)) AS year, 
            SUM(demand) AS total_yearly_demand
        FROM stg_power_data
        GROUP BY strftime('%Y', DATE(timestamp))
    )
    SELECT 
        year,
        total_yearly_demand,
        CASE
            WHEN COUNT(*) OVER (ORDER BY year ROWS BETWEEN 1 PRECEDING AND CURRENT ROW) = 2
            THEN AVG(total_yearly_demand) OVER (ORDER BY year ROWS BETWEEN 1 PRECEDING AND CURRENT ROW)
            ELSE NULL
        END AS moving_avg_2_years
    FROM yearly_data;
""")

print("Finish ELT")

# Commit the changes and close the connection
conn.commit()
conn.close()
