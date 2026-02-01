SELECT
    c.name AS "category",
    COUNT(sub.category_id) AS "number_of_child_elements"
FROM Categories c
LEFT JOIN Categories sub ON c.category_id = sub.parent_id
GROUP BY c.category_id, c.name
ORDER BY "number_of_child_elements" DESC;