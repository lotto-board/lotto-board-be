CREATE TABLE IF NOT EXISTS shop (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    location VARCHAR(255) NOT NULL,
    first_prize_count INTEGER,
    second_prize_count INTEGER
);

insert into shop (name, location, first_prize_count, second_prize_count)
values ('스파2', '노원구2', 14, 56);