CREATE VIEW Top5_BestSelling_Products AS
WITH RecursiveCategory AS (
    SELECT
        category_id,
        name,
        category_id AS root_id
    FROM Categories
    WHERE parent_id IS NULL

    UNION ALL

    SELECT
        c.category_id,
        c.name,
        rc.root_id root_id
    FROM Categories c
    INNER JOIN RecursiveCategory rc ON c.parent_id = rc.category_id
),
ProductRootCategory AS (
    SELECT
        p.product_id,
        p.name AS product_name,
        rc.root_id,
        rc.name AS root_category_name
    FROM Products p
    JOIN RecursiveCategory rc ON p.category_id = rc.category_id
)
SELECT
    prc.product_name AS "Наименование товара",
    prc.root_category_name AS "Категория 1-го уровня",
    SUM(oi.quantity) AS "Общее количество проданных штук"
FROM OrderItems oi
JOIN Orders o ON oi.order_id = o.order_id
JOIN ProductRootCategory prc ON oi.product_id = prc.product_id
WHERE o.order_date >= CURRENT_DATE - INTERVAL '1 month'  -- последний месяц
GROUP BY prc.product_id, prc.product_name, prc.root_category_name
ORDER BY "Общее количество проданных штук" DESC
LIMIT 5;