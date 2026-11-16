-- Write your query below
SELECT w.name as warehouse_name, 
    SUM(CASE
        WHEN w.product_id = p.product_id THEN
            p.width * p.length * p.height * w.units
        ELSE 0
    END) AS volume
FROM warehouse w
LEFT JOIN products p ON p.product_id = w.product_id
GROUP BY w.name