-- Task 1

/* 1.1 Create a new table potential customers
   with fields id, email, name, surname, second_name, city */
CREATE TABLE potential_customers(
    id SERIAL,
    email VARCHAR(150),
    name VARCHAR(100),
    surname VARCHAR(100),
    second_name VARCHAR(100),
    city VARCHAR(50)
);

-- Fill in the data in the table
INSERT INTO potential_customers (email, name, surname, second_name, city)
VALUES
       ('ricardo@mail.com', 'John', 'Don', 'Ricardo', 'Vice city'),
       ('daniels@mail.com', 'Jack', 'Daniels', 'Tennessee', 'Kentucky'),
       ('busheni@mail.com', 'Steve', 'Busheni', 'Fernie', 'Los Santos'),
       ('legol@mail.com', 'Legolas', 'Leafson', 'Tranduil', 'Ithilien'),
       ('nikfeo@mail.com', 'Nik', 'Feoktistov', 'Leonid', 'Kharkiv'),
       ('stitch@mail.com', 'Eugen', 'Merchen', 'Stitch', 'London'),
       ('maxred@mail.com', 'Max', 'Kruds', 'Reddison', 'Paris'),
       ('somegirl@17mail.com', 'Bath', 'Miller', 'Montes', 'city 17'),
       ('pstarlora@pmail.com', 'Lora', 'Taylor', 'PStar', 'Kiyv'),
       ('iontr@mail.com', 'Mey', 'Thramp', 'Ion', 'New York'),
       ('belutti@mail.com', 'Monica', 'Belutti', 'Lafema', 'San Francisco'),
       ('banann@mail.com', 'Ann', 'Steveson', 'Ban', 'Los Angeles'),
       ('likeaboss@bossmail.com', 'Besty', 'Offers', 'Truster', 'city 17'),
       ('lagkot@mail.com', 'Lagerta', 'surname12', 'Shmagerta', 'Kottegat'),
       ('ragkot@mail.com', 'Ragnar', 'surname13', 'Sagnar', 'Kottegat'),
       ('lokishmoki@mail.com', 'Loki', 'Odinson', 'Shmoki', 'Asgaard'),
       ('thorphtor@mail.com', 'Thor', 'Odinson', 'Phtor', 'Asgaard');

-- Print names and email of potential and existing users from city 17
SELECT name, email
FROM potential_customers
WHERE city = 'city 17'
UNION
SELECT first_name, email
FROM users
WHERE city = 'city 17';
