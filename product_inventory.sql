CREATE DATABASE Product_inventory;
USE Product_inventory;

CREATE TABLE inventory (
    product_id INT,
    warehouse_id INT,
    date DATE,
    quantity INT
);
INSERT INTO inventory (product_id, warehouse_id, date, quantity)
VALUES
    (1, 1, '2023-08-01', 100),
    (1, 2, '2023-08-01', 150),
    (1, 1, '2023-08-02', 120),
    (2, 1, '2023-08-01', 50),
    (2, 2, '2023-08-01', 80),
    (2, 1, '2023-08-02', 70),
    (1, 2, '2023-08-03', 130),
    (2, 2, '2023-08-03', 90);
  
  SELECT
    product_id,
    warehouse_id,
    SUM(quantity) AS total_quantity
FROM
    inventory
WHERE
    (product_id, warehouse_id, date) IN (
        SELECT
            product_id,
            warehouse_id,
            MAX(date) AS latest_date
        FROM
            inventory
        GROUP BY
            product_id,
            warehouse_id
    )
GROUP BY
    product_id,
    warehouse_id;
