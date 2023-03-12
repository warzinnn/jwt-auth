CREATE TABLE IF NOT EXISTS users (
    email VARCHAR NOT NULL,
    username VARCHAR NOT NULL,
    passwd VARCHAR NOT NULL,
    role VARCHAR NOT NULL,
    PRIMARY KEY(email)
);


INSERT INTO users (email, username, passwd, role) VALUES ('admin@email.com', 'admin', '$2b$12$91PDBI/A9nh5GjLo1upqXun.IBQcN7lvd8O1xfqyNIxEISIkzLCDW', 'admin');

INSERT INTO users (email, username, passwd, role) VALUES ('user@email.com', 'user_1', '$2b$12$y5eGcBI/1kIFiu7nnKH3Au7JaeNiS5jhZZx/vEvBa36vrNw3e2bD6', 'user');

INSERT INTO users (email, username, passwd, role) VALUES ('backoffice@email.com', 'bo_1', '$2b$12$r1qPNbhA6Jh9YPE90qUt.eiiflaKPBsq4nmvY0RO.L9suEJNQFuI2', 'backoffice');

