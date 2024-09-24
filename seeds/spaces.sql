-- The job of this file is to reset all of our important database tables.
-- And add any data that is needed for the tests to run.
-- This is so that our tests, and application, are always operating from a fresh
-- database state, and that tests don't interfere with each other.

-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS spaces CASCADE;
DROP SEQUENCE IF EXISTS spaces_id_seq CASCADE;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS spaces_id_seq;
CREATE TABLE spaces (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    short_description VARCHAR(255),
    price_per_night INTEGER,
    dates TEXT[],
    user_id INTEGER
);


-- Finally, we add any records that are needed for the tests to run
INSERT INTO spaces (name, short_description, price_per_night, dates, user_id) VALUES ('Ocean Oasis', 'Small apartment in a big ocean',534, '{"18-09-2024"}', 1);
INSERT INTO spaces (name, short_description, price_per_night, dates, user_id) VALUES ('River Retreat', 'The retreat on the river',71, '{"14-09-2024","15-09-2024"}', 2);
INSERT INTO spaces (name, short_description, price_per_night, dates, user_id) VALUES ('Sea Shed', 'Not much more than a shed by the sea',33, '{"19-09-2024"}', 3);
INSERT INTO spaces (name, short_description, price_per_night, dates, user_id) VALUES ('Igloo', 'A cool place to chill out',101, '{}', 4);
INSERT INTO spaces (name, short_description, price_per_night, dates, user_id) VALUES ('Waterfall Windows', 'Do not sleep too close to the edge',1045, '{"15-09-2024"}', 1);





