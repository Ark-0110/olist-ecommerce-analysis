## Data Source
Dataset: Brazilian E-Commerce Public Dataset by Olist
Source: https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce
Download the CSVs and place them in the /data folder before running queries
Note: Data files not included in repo due to size — download directly from Kaggle

### Dataset Notes
- Raw uncleaned dataset requiring data quality investigation
- Issues identified: missing months, near-zero periods at boundaries, sparse early data
- Cleaning decisions documented and justified before analysis

### Data Quality Finding — Clean Window
- September/October 2016: sparse early data, platform just launching
- November 2016: completely missing from dataset
- December 2016: only 1 order — clear data gap
- September/October 2018: near zero orders — dataset trails off
- Clean reliable window: January 2017 through August 2018
- All trend analysis scoped to this 20-month period

### Monthly Revenue Findings (Clean Window: Jan 2017 - Aug 2018)
- Clear upward revenue trend from Jan 2017 through Jan 2018
- Growth driven by order volume increase, not higher spend per order
- Average order value remains stable (R$142 - R$163 throughout) indicating growth is volume-driven not spend-driven
- November 2017 shows clear spike — consistent with Black Friday effect
- Revenue growth plateaus and fluctuates from early 2018 onwards
- Suggests customer acquisition was primary growth driver

### Revenue by Category Findings
- Top 5 categories by revenue: health_beauty, watches_gifts, 
  bed_bath_table, sports_leisure, computers_accessories
- Revenue rank and order volume rank don't always match
- health_beauty leads revenue through volume (8,791 orders) 
  at moderate price (R$130 avg)
- watches_gifts achieves similar revenue with half the orders 
  due to high average price (R$200)
- bed_bath_table has highest order volume in top 5 (9,412) but 
  ranks 3rd in revenue — cheapest category at R$93 avg price
- Two distinct business models visible: volume-driven (health_beauty, 
  bed_bath_table) vs value-driven (watches_gifts, cool_stuff)
