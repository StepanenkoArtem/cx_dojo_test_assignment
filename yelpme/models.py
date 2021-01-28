from peewee import CharField, FloatField, ForeignKeyField, IntegerField

class Cities:
    city_id = IntegerField(primary_key=True)
    city_title = CharField(100)


class Business:
    # id INT AUTO_INCREMENT PRIMARY KEY,
    yelp_id = CharField(max_length=40)
    # title VARCHAR(255) NOT NULL,
    name = CharField(max_length=100)
    # website VARCHAR(255),
    website = CharField(max_length=100)
    # rating FLOAT,
    rating = FloatField()
    # google_rating FLOAT,
    google_rating = FloatField()
    # phone VARCHAR(13),
    phone = CharField(13)
    # loc_address VARCHAR(150),
    location = CharField(150)
    # city_id INT NOT NULL,
    city_id = ForeignKeyField(Cities)
    # zip_code_id INT NOT NULL,
    # longitude FLOAT(15, 12),
    longitude = FloatField()
    # latitude FLOAT(15, 12),
    latitude = FloatField
    # FOREIGN KEY (city_id) REFERENCES cities (id),
    # FOREIGN KEY (zip_code_id) REFERENCES zip_codes (id)