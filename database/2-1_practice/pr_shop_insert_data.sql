COPY Users(user_id, email, password, first_name, last_name, middle_name,
          is_staff, country, city, address)
FROM  '/usr/src/csv/users.csv'
DELIMITER ',' CSV;

COPY Order_status(order_status_id, status_name)
FROM  '/usr/src/csv/order_statuses.csv'
DELIMITER ',' CSV;

COPY Categories(category_id, category_title, category_description)
FROM  '/usr/src/csv/categories.csv'
DELIMITER ',' CSV;

COPY Carts(cart_id, Users_user_id, subtotal, total, timestamp)
FROM  '/usr/src/csv/carts.csv'
DELIMITER ',' CSV;

COPY Orders(order_id, Carts_cart_id, Order_status_order_status_id, shipping_total,
            total, created_at, updated_at)
FROM  '/usr/src/csv/orders.csv'
DELIMITER ',' CSV;

COPY Products(product_id, product_title, product_description, in_stock, price,
             slug, category_id)
FROM  '/usr/src/csv/products.csv'
DELIMITER ',' CSV;

COPY Cart_product(carts_cart_id, products_product_id)
FROM  '/usr/src/csv/cart_products.csv'
DELIMITER ',' CSV;