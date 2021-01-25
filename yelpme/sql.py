# coding=utf-8
"""SQL queries."""


create_zip_codes_table_query = """
    CREATE TABLE IF NOT EXISTS zip_codes (
        id INT AUTO_INCREMENT PRIMARY KEY,
        zip_code INT UNIQUE
    )
    """

create_cities_table_query = """
    CREATE TABLE IF NOT EXISTS cities (
        id INT AUTO_INCREMENT PRIMARY KEY,
        city_name VARCHAR(40) UNIQUE
    )
    """

create_businesses_table_query = """
    CREATE TABLE IF NOT EXISTS businesses (
        id INT AUTO_INCREMENT PRIMARY KEY,
        title VARCHAR(255) NOT NULL,
        website VARCHAR(255),
        rating FLOAT,
        google_rating FLOAT,
        phone VARCHAR(13),
        loc_address VARCHAR(150),
        city_id INT NOT NULL,
        zip_code_id INT NOT NULL,
        longitude FLOAT(15, 12),
        latitude FLOAT(15, 12),
        FOREIGN KEY (city_id) REFERENCES cities (id),
        FOREIGN KEY (zip_code_id) REFERENCES zip_codes (id)
    )
    """

create_tags_table_query = """
    CREATE TABLE IF NOT EXISTS tags (
        id INT AUTO_INCREMENT PRIMARY KEY,
        alias VARCHAR(40) UNIQUE,
        title VARCHAR(150)
    )
    """

create_business_on_tags_table_query = """
    CREATE TABLE IF NOT EXISTS business_on_tags (
        id INT AUTO_INCREMENT PRIMARY KEY,
        tag_id INT NOT NULL,
        business_id INT NOT NULL,
        FOREIGN KEY (tag_id) REFERENCES tags (id),
        FOREIGN KEY (business_id) REFERENCES businesses (id)
    )
    """


insert_cities = """
    INSERT IGNORE INTO cities (city_name)
    VALUES (%s)
"""


insert_zip_codes = """
    INSERT IGNORE INTO zip_codes (zip_code)
    VALUES (%s)
"""

insert_businesses = """
    INSERT INTO businesses (
        title,
        rating,
        google_rating,
        website,
        latitude,
        longitude,
        loc_address,
        phone,
        city_id,
        zip_code_id
    )
    VALUES
    (%s, %s, %s, %s, %s, %s, %s, %s,
    (SELECT id FROM cities WHERE city_name=%s),
    (SELECT id FROM zip_codes WHERE zip_code=%s)
    )
"""

insert_tags = """
    INSERT IGNORE INTO tags (alias, title)
    VALUES (%s, %s)
"""


insert_business_on_tags = """
    INSERT IGNORE INTO business_on_tags (business_id, tag_id)
    VALUES
    (
        (SELECT id FROM businesses WHERE title=%s),
        (SELECT id FROM tags WHERE alias=%s)
    )
"""
