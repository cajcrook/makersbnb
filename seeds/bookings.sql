
DROP TABLE IF EXISTS bookings CASCADE;
DROP SEQUENCE IF EXISTS bookings_id_seq CASCADE;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS bookings_id_seq;
CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    guest_id int,
    start_date text,
    approved BOOLEAN,
    pending BOOLEAN,
    space_id int

);
-- Finally, we add any records that are needed for the tests to run
INSERT INTO bookings (guest_id, start_date, approved, pending, space_id) VALUES

(2, '14-09-2024', True, False, 2),
(1, '17-09-2024', False, True, 2),
(4, '18-09-2024', True, False, 1),
(4, '14-09-2024', False, True, 4),
(1, '19-09-2024', False, True, 3),
(3, '15-09-2024', True, False, 2),
(2, '12-09-2024', False, True, 1);

