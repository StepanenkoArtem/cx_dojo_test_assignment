# coding=utf-8
"""SQL queries."""


create_zip_codes_table_query = """
    CREATE TABLE zip_codes (
        id INT AUTO_INCREMENT PRIMARY KEY,
        zip_code INT UNIQUE
    )
    """

create_cities_table_query = """
    CREATE TABLE cities (
        id INT AUTO_INCREMENT PRIMARY KEY,
        city_name VARCHAR(40)
    )
    """

create_businesses_table_query = """
    CREATE TABLE businesses (
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
    CREATE TABLE tags (
        id INT AUTO_INCREMENT PRIMARY KEY,
        alias VARCHAR(40) UNIQUE,
        title VARCHAR(150)
    )
    """

create_business_tags_query = """
    CREATE TABLE business_tags (
        id INT AUTO_INCREMENT PRIMARY KEY,
        tag_id INT NOT NULL,
        business_id INT NOT NULL,
        FOREIGN KEY (tag_id) REFERENCES tags (id),
        FOREIGN KEY (business_id) REFERENCES businesses (id)
    )
    """
