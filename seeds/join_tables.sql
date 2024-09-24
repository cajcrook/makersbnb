-- One user can have many spaces
CREATE TABLE users_spaces(
  users_id int,
  spaces_id int,
  constraint fk_post foreign key(users_id) references users(id) on delete cascade,
  constraint fk_tag foreign key(spaces_id) references spaces(id) on delete cascade,
  PRIMARY KEY (users_id, spaces_id)
);

-- One space can have many bookings
CREATE TABLE spaces_bookings(
  spaces_id int,
  bookings_id int,
  constraint fk_post foreign key(spaces_id) references spaces(id) on delete cascade,
  constraint fk_tag foreign key(bookings_id) references bookings(id) on delete cascade,
  PRIMARY KEY (spaces_id, bookings_id)
);

-- One user can have many bookings
CREATE TABLE users_bookings(
  users_id int,
  bookings_id int,
  constraint fk_post foreign key(users_id) references users(id) on delete cascade,
  constraint fk_tag foreign key(bookings_id) references bookings(id) on delete cascade,
  PRIMARY KEY (users_id, bookings_id)
);


-- One space can have many images
CREATE TABLE spaces_images(
  spaces_id int,
  images_id int,
  constraint fk_post foreign key(spaces_id) references spaces(id) on delete cascade,
  constraint fk_tag foreign key(images_id) references images(id) on delete cascade,
  PRIMARY KEY (spaces_id, images_id)
);