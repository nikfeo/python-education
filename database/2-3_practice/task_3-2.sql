-- Task 2

/* Display the names and email addresses of all users
   sorted by city and by name (alphabetically)
 */

SELECT first_name, email FROM users
ORDER BY city, first_name;