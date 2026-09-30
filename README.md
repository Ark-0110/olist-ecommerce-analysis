# Olist E-Commerce Business Analytics

End-to-end SQL and Python analysis of 100,000+ orders from Olist, 
Brazil's largest e-commerce platform. Built to demonstrate business-focused 
analytics skills including data quality assessment, cohort analysis, 
seller performance evaluation, and customer behavior insights.

## Tech Stack
- PostgreSQL — database and all analytical queries
- Python (pandas, matplotlib, seaborn) — data visualization
- DBeaver — SQL client
- GitHub — version control

## Data Source
Dataset: Brazilian E-Commerce Public Dataset by Olist  
Source: https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce  
Note: Data files not included in repo due to size — download directly 
from Kaggle and place CSVs in the /data folder before running queries.

## Key Business Findings

### 1. Revenue Trends
- Clear upward trend Jan 2017 through Jan 2018, driven by order 
  volume not higher spend per order
- Average order value stable at R$142-163 throughout — growth 
  is purely acquisition driven
- November 2017 Black Friday spike clearly visible in data

### 2. Product Categories
- Health & Beauty leads revenue through volume (8,791 orders, R$130 avg)
- Watches & Gifts achieves similar revenue with half the orders 
  due to high avg price (R$200)
- Two distinct models: volume-driven vs value-driven categories

### 3. Delivery Performance
- Most sellers deliver 3-6 days ahead of estimated date
- Olist sets conservative delivery estimates — good for customer experience
- Best seller delivers 42 days early, worst delivers 1 day late

### 4. Customer Retention (Cohort Analysis)
- Month-1 retention rate under 1% across all 20 cohorts
- November 2017 cohort: 7,304 new customers, only 28 returned next month
- Olist is almost entirely acquisition-dependent — retention is negligible
- Recommendation: loyalty programs and re-engagement campaigns needed

### 5. Seller Quality
- Top 20 worst-rated active sellers all below 3.5/5 avg score
- Customers continue buying from low-rated sellers — price overrides quality
- Recommendation: implement seller rating thresholds with review process

### 6. Geographic Distribution
- SP (São Paulo) generates R$5.9M — 940x more orders than smallest state
- Smaller states show higher avg order value (R$200-249)
- Growth opportunity in underserved northern and northeastern states

### 7. Payment Behavior
- Credit card dominates: 76,248 orders, R$12.5M revenue
- Credit card customers average 3.5 installments — installments 
  enable higher value purchases
- Boleto (cash-equivalent) serves customers without credit access

## Data Quality Notes
- Clean analysis window: January 2017 through August 2018
- November 2016 missing entirely from dataset
- September-October 2018 show near-zero orders — data trails off
- All findings scoped to clean 20-month window

## Visualizations
Charts saved in /notebooks folder:
- Monthly revenue trend
- Top 10 categories by revenue
- Revenue by state
- Payment type breakdown
- Cohort retention heatmap
