/* Task 4 */

/* 4.1 Display the average of all completed trades */
SELECT AVG(total) AS average_amount FROM orders
WHERE order_status_order_status_id = 4;

/* 4.2 Display the maximum deal amount for the 3rd quarter of 2020 */
SELECT MAX(total) AS max_deal_amount FROM orders
WHERE order_status_order_status_id = 4
AND created_at BETWEEN '2020-01-07' AND '2020-09-30';