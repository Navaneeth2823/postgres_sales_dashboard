-- Monthly Sales per Region
CREATE OR REPLACE VIEW monthly_sales_per_region AS
SELECT 
    DATE_TRUNC('month', order_date) AS month,
    region,
    SUM(sales) AS total_sales
FROM sales
GROUP BY month, region
ORDER BY month, region;


-- Top Customers
CREATE OR REPLACE VIEW top_customers AS
SELECT 
    customer_name,
    SUM(sales) AS total_sales
FROM sales
GROUP BY customer_name
ORDER BY total_sales DESC
LIMIT 10;  -- Top 10 customers

-- Category Growth
CREATE OR REPLACE VIEW category_growth AS
SELECT 
    DATE_TRUNC('month', order_date) AS month,
    category,
    SUM(sales) AS total_sales
FROM sales
GROUP BY month, category
ORDER BY month, category;