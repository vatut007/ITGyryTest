CREATE TABLE Categories (
    category_id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    parent_id INT,
    CONSTRAINT fk_categories_parent
        FOREIGN KEY (parent_id)
        REFERENCES Categories(category_id)
        ON DELETE SET NULL
);

CREATE TABLE Products (
    product_id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    quantity INT NOT NULL CHECK (quantity >= 0),
    price DECIMAL(10, 2) NOT NULL CHECK (price > 0),
    category_id INT NOT NULL,
    CONSTRAINT fk_products_category
        FOREIGN KEY (category_id)
        REFERENCES Categories(category_id)
        ON DELETE RESTRICT
);

CREATE TABLE Clients (
    client_id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    address VARCHAR(500)
);

CREATE TABLE Orders (
    order_id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    client_id INT NOT NULL,
    order_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_orders_client
        FOREIGN KEY (client_id)
        REFERENCES Clients(client_id)
        ON DELETE RESTRICT
);

CREATE TABLE OrderItems (
    order_item_id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    order_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL CHECK (quantity > 0),
    unit_price DECIMAL(10, 2) NOT NULL CHECK (unit_price > 0),
    CONSTRAINT fk_orderitems_order
        FOREIGN KEY (order_id)
        REFERENCES Orders(order_id)
        ON DELETE CASCADE,
    CONSTRAINT fk_orderitems_product
        FOREIGN KEY (product_id)
        REFERENCES Products(product_id)
        ON DELETE RESTRICT
);