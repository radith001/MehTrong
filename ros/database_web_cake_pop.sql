
drop database cake_pop_db;
create database cake_pop_db;
use cake_pop_db;

show tables;
desc categories;
desc users;
select * from users;
select * from categories;
select * from order_items;
select *from products;
desc products;
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    phone bigint
);
INSERT INTO users (id, name, email, password, phone) VALUES
 (1, 'Ivanka', 'ivanka@gmail.com', 'ivanka', '0834749302883'),
 (2, 'rosita', 'rosita@gmail.com', 'sita', '085692539070'),
 (3, 'giras', 'giras@gmail.com', 'giras', '0836472477992'),
 (4, 'ghani', 'ghani@gmail.com', 'ghani', '038476623398');

CREATE TABLE categories (
    category_id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(50) NOT 
    NULL UNIQUE,
    description TEXT NULL,
    
    created_at TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (category_id)
);
INSERT INTO categories (category_id, name, description) VALUES
(1, 'Birthday Cake', 'Kue ulang tahun berbagai ukuran dan desain.'),
(2, 'Cookies', 'Beragam pilihan cookies premium.'),
(3, 'Custom Cake', 'Kue yang dapat dipesan sesuai keinginan.');

CREATE TABLE products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    category_id int,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    price DECIMAL(10, 2) NOT NULL,
    image_url VARCHAR(255) NOT NULL,
    stock INT DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (category_id) REFERENCES categories(category_id)
);
INSERT INTO products (product_id, name, category_id, price, stock, image_url, description, created_at) VALUES
(1, 'Brownies Cake', 1, 100000, 20, 'assets/images/imageProduk/brownis.png', 'Brownies yang lezat dan padat ini terbuat dari kakao berkualitas tinggi, memberikan rasa yang kaya dan tekstur fudgy yang sempurna. Brownies ini dilapisi dengan ciptaan coklat yang membuat setiap gigitan semakin nikmat dan memuaskan.', '2024-12-11 18:49:23'),
(2, 'Birthday Cake', 1, 250000, 10, 'assets/images/imageProduk/birthday1.png', 'Rayakan momen istimewa Anda dengan kue ulang tahun spesial ini, yang memiliki lapisan sponge cake lembut, isi krim yang lezat, dan hiasan warna-warni. Kue ini sempurna untuk pesta ulang tahun atau acara spesial lainnya, menjadikannya cara manis untuk merayakan.', '2024-12-11 18:49:23'),
(3, 'Chunky Cookies', 2, 80000, 50, 'assets/images/imageProduk/cookies3.png', 'Kue kering tebal dan kenyal ini dipenuhi dengan potongan coklat besar dan bahan lainnya yang lezat. Sempurna untuk camilan manis, chunky cookies ini menawarkan tekstur yang renyah dan rasa yang meleleh di mulut.', '2024-12-11 18:49:23'),
(4, 'Birthday Cake', 1, 150000, 50, 'assets/images/imageProduk/birthday2.png', 'Sebuah variasi menyegarkan dari kue ulang tahun klasik. Dengan lapisan kue lembut yang diisi dengan buttercream yang kaya, kue ini dihias dengan taburan sprinkles dan potongan coklat besar, sempurna untuk perayaan ulang tahun apapun.', '2024-12-11 18:49:23'),
(5, 'Croissants', 2, 90000, 50, 'assets/images/imageProduk/croissants.png', 'Croissant yang renyah dan lembut ini dipanggang dengan bahan-bahan terbaik untuk menghasilkan lapisan luar yang garing dan bagian dalam yang lembut serta empuk. Ideal untuk sarapan atau camilan sore.', '2024-12-11 18:49:23'),
(6, 'Cookies Cake', 2, 80000, 50, 'assets/images/imageProduk/cookies1.png', 'Kue kering ini lembut dan kenyal, dipenuhi dengan potongan coklat besar, membuatnya menjadi camilan yang tak bisa ditolak. Dengan keseimbangan manis dan kaya rasa.', '2024-12-11 18:49:23'),
(7, 'Cookies Cake', 2, 50000, 50, 'assets/images/imageProduk/cookies2.png', 'Sebuah variasi dari cookie klasik, dengan tekstur yang sedikit berbeda namun tetap mempertahankan rasa yang luar biasa. Potongan red velvet besar yang meleleh sempurna di setiap gigitan.', '2024-12-11 18:49:23'),
(8, 'Puding', 2, 25000, 50, 'assets/images/imageProduk/puding.png', 'Puding yang lembut dan krimi ini adalah hidangan penutup yang sempurna untuk mereka yang suka camilan ringan namun memuaskan. Kaya rasa, puding ini terbuat dari bahan-bahan terbaik untuk menciptakan tekstur halus yang meleleh di mulut.', '2024-12-11 18:49:23'),
(9, 'Cake Donut', 1, 70000, 50, 'assets/images/imageProduk/donat.png', 'Donat kami yang lembut dan mengembang ini digoreng sempurna dan dilapisi dengan glasir gula yang halus. Tersedia dalam berbagai rasa, donat ini sangat cocok untuk sarapan, camilan sore, atau sekadar memuaskan keinginan manis Anda kapan saja.', '2024-12-11 18:49:23'),
(10, 'Cake Lotus', 1, 110000, 50, 'assets/images/imageProduk/lotus.png', 'Sebuah kue kering renyah dengan rasa rempah yang dibuat dari bahan terbaik dan dilapisi dengan karamel krimi yang lembut. Kombinasi manis dan gurih yang sempurna, kue kering ini menjadi teman yang sempurna untuk secangkir kopi atau teh.', '2024-12-11 18:49:23'),
(11, 'Custom Cake', 3, 200000, 50, 'assets/images/imageProduk/custom.png', 'Ingin sesuatu yang spesial? Kue custom kami dirancang untuk memenuhi kebutuhan unik Anda, baik untuk ulang tahun, pernikahan, atau acara apapun. Anda bisa memilih rasa, desain, dan ukuran sesuai dengan selera untuk membuat acara Anda tak terlupakan. Harga dapat disesuaikan dengan desain dan ukuran kue.', '2024-12-11 18:49:23'),
(12, 'Tiramisu Cake', 1, 130000, 50, 'assets/images/imageProduk/tiramisu.png', 'Hidangan penutup klasik Italia yang terbuat dari lapisan ladyfingers yang direndam dalam espresso dan krim mascarpone. Tiramisu kami kaya, lembut, dan memiliki keseimbangan rasa kopi dan manis yang sempurna. Cocok untuk para pencinta dessert yang menginginkan rasa autentik Italia.', '2024-12-11 18:49:23');

CREATE TABLE orders (
    id INT AUTO_INCREMENT PRIMARY KEY,
    order_id VARCHAR(20) NOT NULL UNIQUE,
    nama VARCHAR(100),
    email VARCHAR(100),
    telepon VARCHAR(15),
    alamat TEXT,
    pesan TEXT,
    total_payment DECIMAL(10,2),
    payment_method VARCHAR(50),
    order_date DATETIME,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


CREATE TABLE order_items (
    id INT AUTO_INCREMENT PRIMARY KEY,
    order_id VARCHAR(20),
    product_id VARCHAR(20),
    product_name VARCHAR(100),
    product_price DECIMAL(10,2),
    product_quantity INT,
    subtotal DECIMAL(10,2),
    FOREIGN KEY (order_id) REFERENCES orders(order_id)
);

CREATE TABLE status (
    status_id INT AUTO_INCREMENT PRIMARY KEY,
    status_name VARCHAR(100) NOT NULL
);

-- Tambahkan beberapa data status
INSERT INTO status (status_name) VALUES
('Pesanan Selesai'),
('Pesanan Sedang Dibuat'),
('Pengajuan Pembatalan Diterima'),
('Pesanan Sedang Dikirim');

ALTER TABLE orders ADD COLUMN status_id INT;
ALTER TABLE orders ADD FOREIGN KEY (status_id) REFERENCES status(status_id);

-- Update status_id untuk pesanan yang ada
UPDATE orders SET status_id = 1 WHERE order_id = '365383920'; -- Pesanan Selesai
UPDATE orders SET status_id = 2 WHERE order_id = '365383921'; -- Pesanan Sedang Dibuat
UPDATE orders SET status_id = 3 WHERE order_id = '365383929'; -- Pengajuan Pembatalan

ALTER TABLE order_items DROP FOREIGN KEY order_items_ibfk_1;

ALTER TABLE order_items 
ADD CONSTRAINT order_items_ibfk_1 
FOREIGN KEY (order_id) 
REFERENCES orders(order_id) 
ON DELETE CASCADE;


-- tambah produk
DELIMITER $$

CREATE PROCEDURE AddProduct(
    IN p_name VARCHAR(100),
    IN p_category_id INT,
    IN p_price DECIMAL(10,2),
    IN p_stock INT,
    IN p_image_url VARCHAR(255),
    IN p_description TEXT
)
BEGIN
    INSERT INTO products (name, category_id, price, stock, image_url, description, created_at)
    VALUES (p_name, p_category_id, p_price, p_stock, p_image_url, p_description, NOW());
    
    SELECT LAST_INSERT_ID() AS product_id;
END $$

DELIMITER ;


CALL AddProduct(
    'strawberry cake roll',
    2,
    50000,
    20,
    'assets/images/imageProduk/strawberrycakeroll.png',
    'Kue strawberry yang lembut dengan rasa yang kaya, sempurna untuk berbagai acara.'
);

-- menambah user
DELIMITER $$

CREATE PROCEDURE AddUser(
    IN p_name VARCHAR(100),
    IN p_email VARCHAR(100),
    IN p_password VARCHAR(255),
    IN p_phone BIGINT
)
BEGIN
    INSERT INTO users (name, email, password, phone) 
    VALUES (p_name, p_email, p_password, p_phone);
END $$

DELIMITER ;

CALL AddUser('Alice Johnson', 'alice@example.com', 'mypassword', 1231231234);

select * from users;

-- updet password
UPDATE users
SET password = 'newsecurepassword'
WHERE email = 'user@example.com';
