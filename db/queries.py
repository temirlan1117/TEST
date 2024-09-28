CREATE_TABLE_PRODUCTS = """
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        name_product VARCHAR(255),
        category_product VARCHAR(255),
        size_product VARCHAR(255),
        price_product VARCHAR(255),
        product_id VARCHAR(255),
        photo TEXT
    )
"""

INSERT_PRODUCTS_QUERY = """
    INSERT INTO products (name_product, category_product, size_product, price_product, product_id, photo)
    VALUES (?, ?, ?, ?, ?, ?)
"""