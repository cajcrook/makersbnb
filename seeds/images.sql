DROP TABLE IF EXISTS images CASCADE;
DROP SEQUENCE IF EXISTS images_id_seq CASCADE;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS images_id_seq;
CREATE TABLE  images (
    id SERIAL PRIMARY KEY,
    image_url text,
    space_id int
);

INSERT INTO images ( image_url , space_id) VALUES ( 'https://i.pinimg.com/originals/12/e5/e2/12e5e2ff898d74466e4be09d98d5c8bf.jpg',1);
INSERT INTO images ( image_url , space_id) VALUES ( 'https://mybestplace.com/uploads/2021/07/Drina-River-House-Serbia-COVER.jpg',2);
INSERT INTO images ( image_url , space_id) VALUES ( 'https://vwartclub.com/media/projects/6572/1.jpg',3);
INSERT INTO images ( image_url , space_id) VALUES ( 'https://wodnesprawy.pl/wp-content/uploads/2023/12/Wodne-Sprawy_27_2023-7.jpg',4);
INSERT INTO images ( image_url , space_id) VALUES ( 'https://mybestplace.com/uploads/2021/07/Drina-River-House-Serbia-COVER.jpg',5);

