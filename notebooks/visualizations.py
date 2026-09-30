import psycopg2
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Connect to PostgreSQL
conn = psycopg2.connect(
    dbname="olist",
    user="archit",
    host="localhost",
    port="5432"
)

# Query 1 — Monthly Revenue
query = """
SELECT 
    DATE_TRUNC('month', o.order_purchase_timestamp) AS month,
    ROUND(SUM(p.payment_value)::numeric, 2) AS total_revenue
FROM orders o
LEFT JOIN order_payments p ON o.order_id = p.order_id
WHERE o.order_status NOT IN ('cancelled', 'unavailable')
AND o.order_purchase_timestamp >= '2017-01-01'
AND o.order_purchase_timestamp <= '2018-08-31'
GROUP BY 1
ORDER BY 1;
"""

df = pd.read_sql(query, conn)
conn.close()

# Plot
plt.figure(figsize=(12, 5))
plt.plot(df['month'], df['total_revenue'], marker='o', color='steelblue', linewidth=2)
plt.title('Monthly Revenue Trend (Jan 2017 - Aug 2018)', fontsize=14)
plt.xlabel('Month')
plt.ylabel('Total Revenue (R$)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('notebooks/01_monthly_revenue.png', dpi=150)
plt.show()
print("Chart saved")

# Chart 2 — Top 10 Categories by Revenue
conn = psycopg2.connect(dbname="olist", user="archit", host="localhost", port="5432")

query2 = """
SELECT ct.product_category_name_english AS category,
    ROUND(SUM(oi.price)::numeric, 2) AS total_revenue
FROM orders o
LEFT JOIN order_items oi ON o.order_id = oi.order_id
LEFT JOIN products p ON oi.product_id = p.product_id
LEFT JOIN category_translation ct ON p.product_category_name = ct.product_category_name
WHERE o.order_status NOT IN ('cancelled', 'unavailable')
AND o.order_purchase_timestamp >= '2017-01-01'
AND o.order_purchase_timestamp <= '2018-08-31'
AND ct.product_category_name_english IS NOT NULL
GROUP BY 1
ORDER BY 2 DESC
LIMIT 10;
"""

df2 = pd.read_sql(query2, conn)
conn.close()

plt.figure(figsize=(12, 6))
sns.barplot(data=df2, x='total_revenue', y='category', color='steelblue')
plt.title('Top 10 Product Categories by Revenue', fontsize=14)
plt.xlabel('Total Revenue (R$)')
plt.ylabel('Category')
plt.tight_layout()
plt.savefig('notebooks/02_top_categories.png', dpi=150)
plt.show()
print("Chart 2 saved")

# Chart 3 — Revenue by State
conn = psycopg2.connect(dbname="olist", user="archit", host="localhost", port="5432")

query3 = """
SELECT c.customer_state AS state,
    ROUND(SUM(op.payment_value)::numeric, 2) AS total_revenue
FROM orders o
LEFT JOIN order_payments op ON o.order_id = op.order_id
LEFT JOIN customers c ON o.customer_id = c.customer_id
WHERE o.order_status NOT IN ('cancelled', 'unavailable')
AND o.order_purchase_timestamp >= '2017-01-01'
AND o.order_purchase_timestamp <= '2018-08-31'
GROUP BY 1
ORDER BY 2 DESC
LIMIT 10;
"""

df3 = pd.read_sql(query3, conn)
conn.close()

plt.figure(figsize=(12, 6))
sns.barplot(data=df3, x='state', y='total_revenue', color='steelblue')
plt.title('Top 10 States by Revenue', fontsize=14)
plt.xlabel('State')
plt.ylabel('Total Revenue (R$)')
plt.tight_layout()
plt.savefig('notebooks/03_revenue_by_state.png', dpi=150)
plt.show()
print("Chart 3 saved")

# Chart 4 — Payment Type Breakdown
conn = psycopg2.connect(dbname="olist", user="archit", host="localhost", port="5432")

query4 = """
SELECT op.payment_type,
    COUNT(DISTINCT o.order_id) AS total_orders,
    ROUND(SUM(op.payment_value)::numeric, 2) AS total_revenue
FROM orders o
LEFT JOIN order_payments op ON o.order_id = op.order_id
WHERE o.order_status NOT IN ('cancelled', 'unavailable')
AND o.order_purchase_timestamp >= '2017-01-01'
AND o.order_purchase_timestamp <= '2018-08-31'
AND op.payment_type != 'not_defined'
GROUP BY 1
ORDER BY 2 DESC;
"""

df4 = pd.read_sql(query4, conn)
conn.close()

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Orders by payment type
sns.barplot(data=df4, x='payment_type', y='total_orders', color='steelblue', ax=ax1)
ax1.set_title('Orders by Payment Type', fontsize=13)
ax1.set_xlabel('Payment Type')
ax1.set_ylabel('Total Orders')

# Revenue by payment type
sns.barplot(data=df4, x='payment_type', y='total_revenue', color='coral', ax=ax2)
ax2.set_title('Revenue by Payment Type', fontsize=13)
ax2.set_xlabel('Payment Type')
ax2.set_ylabel('Total Revenue (R$)')

plt.tight_layout()
plt.savefig('notebooks/04_payment_types.png', dpi=150)
plt.show()
print("Chart 4 saved")

# Chart 5 — Cohort Retention Heatmap
conn = psycopg2.connect(dbname="olist", user="archit", host="localhost", port="5432")

query5 = """
WITH first_order AS (
    SELECT c.customer_unique_id,
        MIN(o.order_purchase_timestamp) AS first_order_date
    FROM orders o
    LEFT JOIN customers c ON o.customer_id = c.customer_id
    GROUP BY c.customer_unique_id
),
cohort_orders AS (
    SELECT c.customer_unique_id,
        DATE_TRUNC('month', fo.first_order_date) AS cohort_month,
        EXTRACT(YEAR FROM AGE(o.order_purchase_timestamp, fo.first_order_date)) * 12 +
        EXTRACT(MONTH FROM AGE(o.order_purchase_timestamp, fo.first_order_date)) AS month_offset
    FROM orders o
    LEFT JOIN customers c ON o.customer_id = c.customer_id
    LEFT JOIN first_order fo ON c.customer_unique_id = fo.customer_unique_id
    WHERE o.order_purchase_timestamp >= '2017-01-01'
    AND o.order_purchase_timestamp <= '2018-08-31'
)
SELECT cohort_month,
    month_offset,
    COUNT(DISTINCT customer_unique_id) AS customers
FROM cohort_orders
GROUP BY 1, 2
ORDER BY 1, 2;
"""

df5 = pd.read_sql(query5, conn)
conn.close()

# Pivot for heatmap
df5['cohort_month'] = pd.to_datetime(df5['cohort_month']).dt.strftime('%Y-%m')
cohort_pivot = df5.pivot_table(index='cohort_month', columns='month_offset', values='customers')

# Calculate retention percentage
cohort_size = cohort_pivot[0]
retention = cohort_pivot.divide(cohort_size, axis=0) * 100

plt.figure(figsize=(16, 8))
sns.heatmap(retention, 
            annot=True, 
            fmt='.1f',
            cmap='YlOrRd_r',
            mask=retention.isnull(),
            vmin=0, vmax=5)
plt.title('Cohort Retention Rate (%) by Month', fontsize=14)
plt.xlabel('Months Since First Order')
plt.ylabel('Cohort Month')
plt.tight_layout()
plt.savefig('notebooks/05_cohort_heatmap.png', dpi=150)
plt.show()
print("Chart 5 saved")