-- Task 3

/* Display the name of a group of goods,
   the total quantity for a group of goods in descending order of quantity
 */

SELECT category_title,
COUNT(*) FROM categories
JOIN products USING (category_id)
GROUP BY category_title
ORDER BY COUNT DESC;