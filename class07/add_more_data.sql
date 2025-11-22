-- Use the same database
USE rds_database;

-- Insert 10 additional sales records with recent dates
INSERT INTO sales (sales_date, client, product, amount, unit_price, total) VALUES
('2024-03-21 10:15:00', 'Tech Innovations LLC', 'Bluetooth Speaker', 8, 59.99, 479.92),
('2024-03-22 14:30:00', 'Global Retail Group', 'Security Camera', 12, 129.99, 1559.88),
('2024-03-23 11:45:00', 'Digital Marketing Pro', 'Social Media Kit', 5, 199.99, 999.95),
('2024-03-24 16:20:00', 'Healthcare Plus', 'Medical Scale Digital', 7, 89.50, 626.50),
('2024-03-25 09:30:00', 'Financial Advisors Inc', 'Biometric Scanner', 3, 349.99, 1049.97),
('2024-03-26 13:15:00', 'Smart Home Solutions', 'Smart Thermostat', 15, 149.99, 2249.85),
('2024-03-27 15:40:00', 'Education Network', 'Interactive Whiteboard', 2, 799.99, 1599.98),
('2024-03-28 10:50:00', 'Logistics Partners', 'Handheld Terminal', 6, 299.99, 1799.94),
('2024-03-29 14:25:00', 'Creative Studios', '4K Video Camera', 4, 899.99, 3599.96),
('2024-03-30 11:10:00', 'Environmental Systems', 'Air Quality Monitor', 10, 199.99, 1999.90);

-- Verify the new records were added
SELECT COUNT(*) as total_records FROM sales;

-- Display the 10 most recent sales
SELECT id, sales_date, client, product, amount, unit_price, total 
FROM sales 
ORDER BY sales_date DESC 
LIMIT 10;

-- Optional: Show sales summary by client for the new records
SELECT 
    client,
    COUNT(*) as transaction_count,
    SUM(total) as total_revenue
FROM sales 
WHERE sales_date >= '2024-03-21'
GROUP BY client
ORDER BY total_revenue DESC;