/* Task 3 */

/* 3.1 Display products with a price of more than 80.00
   and less than or equal to 150.00
   */
SELECT * FROM products
WHERE price BETWEEN 80.00 AND 150.00;

SELECT * FROM products
WHERE price > 80.00 AND price <= 150.00;

/* 3.2 Display orders placed after 01.10.2020 (created_at) */
SELECT * FROM orders
WHERE created_at > '2020-10-01';

/* 3.3 Display orders received in the first half of 2020 */
SELECT * FROM orders
WHERE created_at BETWEEN '2020-01-01' AND '2020-06-01';

SELECT * FROM orders
WHERE created_at >= '2020-01-01' AND created_at <= '2020-06-30';

/* 3.4 Display products of categories 7, 11, 18 */
SELECT * FROM products
WHERE category_id = 7 OR category_id = 11 OR category_id = 18;

SELECT * FROM products
WHERE category_id IN (7, 11, 18);

/* 3.5 Display unfinished orders as of 31.12.2020 */
SELECT * FROM orders
WHERE order_status_order_status_id IN (1, 2, 3)
AND created_at <= '2020-12-31';

/* 3.6 Display all baskets that were created, but the order was never placed */
SELECT cart_id FROM carts
EXCEPT
SELECT carts_cart_id FROM orders;
