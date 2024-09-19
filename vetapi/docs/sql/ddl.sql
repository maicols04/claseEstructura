-- Cambiar base de datos:
use vetbd;

CREATE TABLE client (
    id_cliente INT PRIMARY KEY AUTO_INCREMENT,
    id_type  VARCHAR(10) NOT NULL,
    id_number  VARCHAR(13) NOT NULL,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    phone_number VARCHAR(20) NOT NULL,
    email VARCHAR(255) NOT NULL,
    address VARCHAR(255)
);
CREATE UNIQUE INDEX index_doc ON client(id_type, id_number);

CREATE TABLE pet (
    id_pet INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    kind VARCHAR(50),
    breed VARCHAR(50),
    id_client INT,
    FOREIGN KEY (id_client) REFERENCES client(id_cliente)
);

