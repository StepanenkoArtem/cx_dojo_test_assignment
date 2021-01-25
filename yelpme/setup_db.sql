CREATE TABLE yelp.zip_codes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    zip_code INT UNIQUE
);

CREATE TABLE yelp.cities (
    id INT AUTO_INCREMENT PRIMARY KEY,
    city_name VARCHAR(40)
);

CREATE TABLE yelp.businesses (
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
);

CREATE TABLE yelp.tags (
    id INT AUTO_INCREMENT PRIMARY KEY,
    alias VARCHAR(40) UNIQUE,
    title VARCHAR(150)
);

CREATE TABLE yelp.business_tags (
    id INT AUTO_INCREMENT PRIMARY KEY,
    tag_id INT NOT NULL,
    business_id INT NOT NULL,
    FOREIGN KEY (tag_id) REFERENCES tags (id),
    FOREIGN KEY (business_id) REFERENCES businesses (id)
);


INSERT INTO yelp.cities (city_name)
VALUES ("San Francisco");

INSERT INTO yelp.zip_codes (zip_code)
VALUES (94110), (94121), (94103), (94115), (94117);

INSERT INTO yelp.businesses (title, rating, google_rating, website, latitude, longitude, loc_address, phone, city_id, zip_code_id)
VALUES 
("Beloved Cafe", 4.5, 4.6, "http://www.belovedsf.com/",37.75235,-122.41925, "3338 24th St", '+14158006546', (SELECT id FROM yelp.cities WHERE city_name='San Francisco'), (SELECT id FROM yelp.zip_codes WHERE zip_code=94110)),
("Home Coffee Roasters",  4.5, 4.6, "http://homecoffeesf.com/", 37.782323, -122.480993, "2018 Clement St", "+14157029244", (SELECT id FROM yelp.cities WHERE city_name='San Francisco'), (SELECT id FROM yelp.zip_codes WHERE zip_code=94121)),
("Vega Coffee", 4.5, 4.7, "http://centocoffee.com/", 37.7745635, -122.410969, "1246 Folsom St", "+14156406843", (SELECT id FROM yelp.cities WHERE city_name='San Francisco'), (SELECT id FROM yelp.zip_codes WHERE zip_code=94103)),
("Jane on Fillmore", 4.0, 4.3, "http://itsjane.com/", 37.78934, -122.43423, "2123 Fillmore St", "+14159315263", (SELECT id FROM yelp.cities WHERE city_name='San Francisco'), (SELECT id FROM yelp.zip_codes WHERE zip_code=94115)),
("Cafe Réveille", 4.0, 4.5, "http://www.cafereveille.com/", 37.7710554824632, -122.432099291995, "201 Steiner St", "+14155292034", (SELECT id FROM yelp.cities WHERE city_name='San Francisco'),(SELECT id FROM yelp.zip_codes WHERE zip_code=94117));


INSERT INTO yelp.tags (alias, title)
VALUES 
("coffee","Coffee & Tea"),
("juicebars", "Juice Bars & Smoothies"),
("coffeeroasteries", "Coffee Roasteries"),
("bakeries", "Bakeries"),
("breakfast_brunch","Breakfast & Brunch"),
("cafes","Cafes"),
("sandwiches","Sandwiches"),
("vegan", "Vegan")
;

INSERT INTO yelp.business_tags (business_id, tag_id)
VALUES 
((SELECT id FROM yelp.businesses WHERE title="Beloved Cafe"), (SELECT id FROM yelp.tags WHERE alias="coffee")),
((SELECT id FROM yelp.businesses WHERE title="Beloved Cafe"), (SELECT id FROM yelp.tags WHERE alias="juicebars")),
((SELECT id FROM yelp.businesses WHERE title="Beloved Cafe"), (SELECT id FROM yelp.tags WHERE alias="vegan")),

((SELECT id FROM yelp.businesses WHERE title="Home Coffee Roasters"), (SELECT id FROM yelp.tags WHERE alias="coffee")),
((SELECT id FROM yelp.businesses WHERE title="Home Coffee Roasters"), (SELECT id FROM yelp.tags WHERE alias="coffeeroasteries")),

((SELECT id FROM yelp.businesses WHERE title="Vega Coffee"), (SELECT id FROM yelp.tags WHERE alias="coffee")),

((SELECT id FROM yelp.businesses WHERE title="Jane on Fillmore"), (SELECT id FROM yelp.tags WHERE alias="coffee")),
((SELECT id FROM yelp.businesses WHERE title="Jane on Fillmore"), (SELECT id FROM yelp.tags WHERE alias="bakeries")),
((SELECT id FROM yelp.businesses WHERE title="Jane on Fillmore"), (SELECT id FROM yelp.tags WHERE alias="breakfast_brunch")),

((SELECT id FROM yelp.businesses WHERE title="Cafe Réveille"), (SELECT id FROM yelp.tags WHERE alias="breakfast_brunch")),
((SELECT id FROM yelp.businesses WHERE title="Cafe Réveille"), (SELECT id FROM yelp.tags WHERE alias="cafes")),
((SELECT id FROM yelp.businesses WHERE title="Cafe Réveille"), (SELECT id FROM yelp.tags WHERE alias="sandwiches"));


SELECT yelp.businesses.title as business, tags.title as tag
FROM yelp.business_tags
JOIN yelp.businesses on yelp.business_tags.business_id =  yelp.businesses.id
JOIN yelp.tags on yelp.business_tags.tag_id = yelp.tags.id
WHERE yelp.business_tags.business_id = yelp.businesses.id;