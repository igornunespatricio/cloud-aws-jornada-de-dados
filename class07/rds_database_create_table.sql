DROP TABLE IF EXISTS sales;

-- Create sales table with optimal data types and constraints
CREATE TABLE sales (
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    sales_date DATETIME NOT NULL,
    client VARCHAR(100) NOT NULL,
    product VARCHAR(50) NOT NULL,
    amount DECIMAL(10,2) NOT NULL CHECK (amount > 0),
    unit_price DECIMAL(10,2) NOT NULL CHECK (unit_price > 0),
    total DECIMAL(12,2) NOT NULL CHECK (total > 0),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    INDEX idx_sales_date (sales_date),
    INDEX idx_client (client),
    INDEX idx_product (product)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Insert 50 sample sales records
INSERT INTO sales (sales_date, client, product, amount, unit_price, total) VALUES
('2024-01-15 09:30:00', 'ABC Corporation', 'Laptop Pro', 2, 1200.00, 2400.00),
('2024-01-16 14:20:00', 'XYZ Ltd', 'Wireless Mouse', 15, 25.50, 382.50),
('2024-01-17 11:15:00', 'Tech Solutions Inc', 'Mechanical Keyboard', 5, 89.99, 449.95),
('2024-01-18 16:45:00', 'Global Enterprises', 'Monitor 24"', 3, 299.99, 899.97),
('2024-01-19 10:00:00', 'Startup Innovations', 'USB-C Hub', 8, 45.75, 366.00),
('2024-01-20 13:30:00', 'Digital Creations', 'Webcam HD', 12, 79.99, 959.88),
('2024-01-21 15:20:00', 'Cloud Systems', 'SSD 1TB', 6, 129.99, 779.94),
('2024-01-22 09:45:00', 'Data Analytics Co', 'Laptop Stand', 10, 35.00, 350.00),
('2024-01-23 14:10:00', 'Mobile Apps LLC', 'Phone Case', 25, 19.99, 499.75),
('2024-01-24 11:30:00', 'Web Services Ltd', 'Router WiFi 6', 4, 149.99, 599.96),
('2024-01-25 16:00:00', 'E-commerce Partners', 'Tablet 10"', 3, 399.99, 1199.97),
('2024-02-01 10:15:00', 'ABC Corporation', 'Docking Station', 7, 199.99, 1399.93),
('2024-02-02 13:45:00', 'Financial Systems', 'External HDD 2TB', 9, 89.99, 809.91),
('2024-02-03 15:30:00', 'Healthcare Solutions', 'Monitor Arm', 5, 75.50, 377.50),
('2024-02-04 09:20:00', 'Education First', 'Chromebook', 12, 249.99, 2999.88),
('2024-02-05 14:50:00', 'Retail Chain Co', 'Barcode Scanner', 8, 120.00, 960.00),
('2024-02-06 11:10:00', 'Logistics Express', 'Rugged Tablet', 2, 899.99, 1799.98),
('2024-02-07 16:25:00', 'Manufacturing Inc', 'Industrial PC', 1, 1500.00, 1500.00),
('2024-02-08 10:40:00', 'Consulting Group', 'Noise Cancelling Headphones', 6, 299.99, 1799.94),
('2024-02-09 13:15:00', 'Legal Services', 'Document Scanner', 3, 450.00, 1350.00),
('2024-02-10 15:45:00', 'Marketing Agency', 'Graphics Tablet', 4, 199.99, 799.96),
('2024-02-12 09:35:00', 'Real Estate Partners', 'IP Camera', 10, 89.99, 899.90),
('2024-02-13 14:05:00', 'Travel Company', 'Portable Charger', 20, 29.99, 599.80),
('2024-02-14 11:25:00', 'Food Services Ltd', 'POS Terminal', 5, 399.99, 1999.95),
('2024-02-15 16:30:00', 'Entertainment Corp', 'Gaming Console', 3, 499.99, 1499.97),
('2024-02-16 10:50:00', 'Fitness Centers', 'Smartwatch', 8, 199.99, 1599.92),
('2024-02-17 13:40:00', 'Automotive Group', 'Diagnostic Tool', 2, 750.00, 1500.00),
('2024-02-18 15:10:00', 'Energy Solutions', 'UPS 1500VA', 6, 199.99, 1199.94),
('2024-02-19 09:55:00', 'Construction Ltd', 'Rugged Laptop', 2, 1299.99, 2599.98),
('2024-02-20 14:20:00', 'Pharmaceuticals', 'Medical Tablet', 4, 899.99, 3599.96),
('2024-03-01 11:05:00', 'ABC Corporation', 'Monitor 27"', 3, 349.99, 1049.97),
('2024-03-02 15:35:00', 'Tech Solutions Inc', 'Server Rack', 1, 1200.00, 1200.00),
('2024-03-03 10:25:00', 'Digital Creations', 'Microphone Studio', 5, 149.99, 749.95),
('2024-03-04 13:50:00', 'Cloud Systems', 'NAS Storage', 2, 599.99, 1199.98),
('2024-03-05 16:15:00', 'E-commerce Partners', 'Barcode Printer', 4, 299.99, 1199.96),
('2024-03-06 09:40:00', 'Mobile Apps LLC', 'Smartphone', 15, 699.99, 10499.85),
('2024-03-07 14:30:00', 'Web Services Ltd', 'Network Switch', 3, 199.99, 599.97),
('2024-03-08 11:20:00', 'Financial Systems', 'Financial Calculator', 12, 45.00, 540.00),
('2024-03-09 15:55:00', 'Healthcare Solutions', 'Medical Monitor', 2, 899.99, 1799.98),
('2024-03-10 10:10:00', 'Education First', 'Projector', 6, 399.99, 2399.94),
('2024-03-11 13:25:00', 'Retail Chain Co', 'Cash Register', 8, 299.99, 2399.92),
('2024-03-12 16:40:00', 'Logistics Express', 'GPS Tracker', 25, 49.99, 1249.75),
('2024-03-13 09:30:00', 'Manufacturing Inc', 'PLC Controller', 3, 450.00, 1350.00),
('2024-03-14 14:15:00', 'Consulting Group', 'Video Conferencing System', 2, 799.99, 1599.98),
('2024-03-15 11:45:00', 'Legal Services', 'Document Shredder', 4, 199.99, 799.96),
('2024-03-16 15:20:00', 'Marketing Agency', 'Digital Signage', 3, 599.99, 1799.97),
('2024-03-17 10:35:00', 'Real Estate Partners', 'Smart Lock', 15, 79.99, 1199.85),
('2024-03-18 13:10:00', 'Travel Company', 'Portable WiFi', 10, 89.99, 899.90),
('2024-03-19 16:25:00', 'Food Services Ltd', 'Kitchen Display', 5, 349.99, 1749.95),
('2024-03-20 09:50:00', 'Entertainment Corp', 'VR Headset', 4, 399.99, 1599.96);

-- Verify the inserted data
SELECT COUNT(*) as total_records FROM sales;

-- Display sample of the data
SELECT * FROM sales ORDER BY sales_date LIMIT 10;