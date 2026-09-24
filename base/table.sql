-- ============================================================
-- 1. ROLES
-- ============================================================

CREATE TABLE roles (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE
);


-- ============================================================
-- 2. USERS
-- ============================================================

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    role_id INT NOT NULL,

    CONSTRAINT fk_users_role
        FOREIGN KEY (role_id)
        REFERENCES roles(id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
);


-- ============================================================
-- 3. PRODUCTS CATEGORIES
-- ============================================================

CREATE TABLE products_categories (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE
);


-- ============================================================
-- 4. PRODUCTS
-- ============================================================

CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    selling_price NUMERIC(10, 2) NOT NULL,
    category_id INT NOT NULL,

    CONSTRAINT chk_products_selling_price
        CHECK (selling_price > 0),

    CONSTRAINT fk_products_category
        FOREIGN KEY (category_id)
        REFERENCES products_categories(id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
);


-- ============================================================
-- 5. PRODUCTION
-- ============================================================

CREATE TABLE production (
    id SERIAL PRIMARY KEY,
    product_id INT NOT NULL,
    quantity INT NOT NULL,
    created_by INT NOT NULL,
    production_date TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT chk_production_quantity
        CHECK (quantity > 0),

    CONSTRAINT fk_production_product
        FOREIGN KEY (product_id)
        REFERENCES products(id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,

    CONSTRAINT fk_production_user
        FOREIGN KEY (created_by)
        REFERENCES users(id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
);


-- ============================================================
-- 6. STATUS
-- ============================================================

CREATE TABLE status (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE
);


-- ============================================================
-- 7. TRANSACTIONS
-- ============================================================

CREATE TABLE transactions (
    id SERIAL PRIMARY KEY,
    product_id INT NOT NULL,
    quantity INT NOT NULL,
    vendeur  VARCHAR(100) NOT NULL,
    unit_price NUMERIC(10, 2) NOT NULL,
    status_id INT NOT NULL,
    transaction_date TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    created_by INT NOT NULL,

    CONSTRAINT chk_transactions_quantity
        CHECK (quantity > 0),

    CONSTRAINT chk_transactions_unit_price
        CHECK (unit_price > 0),

    CONSTRAINT fk_transactions_product
        FOREIGN KEY (product_id)
        REFERENCES products(id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,

    CONSTRAINT fk_transactions_status
        FOREIGN KEY (status_id)
        REFERENCES status(id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,

    CONSTRAINT fk_transactions_created_by
        FOREIGN KEY (created_by)
        REFERENCES users(id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
);


-- ============================================================
-- 8. TRANSACTION HISTORY
-- ============================================================

CREATE TABLE transaction_history (
    id SERIAL PRIMARY KEY,
    transaction_id INT NOT NULL,
    updated_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    created_by INT NOT NULL,

    CONSTRAINT fk_transaction_history_transaction
        FOREIGN KEY (transaction_id)
        REFERENCES transactions(id)
        ON UPDATE CASCADE
        ON DELETE CASCADE,

    CONSTRAINT fk_transaction_history_user
        FOREIGN KEY (created_by)
        REFERENCES users(id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
);


-- ============================================================
-- 9. EXPENSES
-- ============================================================

CREATE TABLE expenses (
    id SERIAL PRIMARY KEY,
    description TEXT NOT NULL,
    amount NUMERIC(10, 2) NOT NULL,
    expense_date TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    created_by INT NOT NULL,

    CONSTRAINT chk_expenses_amount
        CHECK (amount > 0),

    CONSTRAINT fk_expenses_created_by
        FOREIGN KEY (created_by)
        REFERENCES users(id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
);


-- ============================================================
-- 10. EXPENSE HISTORY
-- ============================================================

CREATE TABLE expense_history (
    id SERIAL PRIMARY KEY,
    expense_id INT NOT NULL,
    updated_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    created_by INT NOT NULL,

    CONSTRAINT fk_expense_history_expense
        FOREIGN KEY (expense_id)
        REFERENCES expenses(id)
        ON UPDATE CASCADE
        ON DELETE CASCADE,

    CONSTRAINT fk_expense_history_user
        FOREIGN KEY (created_by)
        REFERENCES users(id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
);


-- ============================================================
-- 11. STOCK
-- ============================================================

CREATE TABLE stock (
    id SERIAL PRIMARY KEY,
    product_id INT NOT NULL UNIQUE,
    quantity INT NOT NULL DEFAULT 0,
    last_updated TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT chk_stock_quantity
        CHECK (quantity >= 0),

    CONSTRAINT fk_stock_product
        FOREIGN KEY (product_id)
        REFERENCES products(id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
);


-- ============================================================
-- 12. TYPE MOUVEMENT
-- ============================================================

CREATE TABLE type_mouvement (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE
);


-- ============================================================
-- 13. STOCK HISTORY
-- ============================================================

CREATE TABLE stock_history (
    id SERIAL PRIMARY KEY,
    stock_id INT NOT NULL,
    quantity_ajouter_ou_enleve INT NOT NULL,
    updated_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    created_by INT NOT NULL,
    type_mouvement_id INT NOT NULL,

    CONSTRAINT chk_stock_history_quantity
        CHECK (quantity_ajouter_ou_enleve <> 0),

    CONSTRAINT fk_stock_history_stock
        FOREIGN KEY (stock_id)
        REFERENCES stock(id)
        ON UPDATE CASCADE
        ON DELETE CASCADE,

    CONSTRAINT fk_stock_history_user
        FOREIGN KEY (created_by)
        REFERENCES users(id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,

    CONSTRAINT fk_stock_history_type
        FOREIGN KEY (type_mouvement_id)
        REFERENCES type_mouvement(id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
);