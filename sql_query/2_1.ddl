SELECT
    c.name AS "client_name",
    COALESCE(SUM(oi.quantity * oi.unit_price), 0) AS "summ"
FROM Clients c
LEFT JOIN Orders o ON c.client_id = o.client_id
LEFT JOIN OrderItems oi ON o.order_id = oi.order_id
GROUP BY c.client_id, c.name
ORDER BY "summ" DESC;