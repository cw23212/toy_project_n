create database class;
use class;
create table user(ind INT NOT NULL AUTO_INCREMENT PRIMARY KEY,  id varchar(10) UNIQUE, passwd varchar(10));
INSERT INTO user(id,passwd) VALUES('19011234','1234');

create table class(class varchar(10) NOT NULL unique, h9 binary default 0 , h9_5  binary default 0 , h10 binary default 0 , h10_5 binary default 0 , h11 binary default 0 , h11_5 binary default 0 , h12 binary default 0 , h12_5 binary default 0 , h13 binary default 0 , h13_5 binary default 0 , h14 binary default 0 , h14_5 binary default 0 , h15 binary default 0 , h15_5 binary default 0 , h16 binary default 0 , h16_5 binary default 0 , h17 binary default 0 , h17_5 binary default 0 , h18 binary default 0 , h18_5 binary default 0 , h19 binary default 0 , h19_5 binary default 0 , h20 binary default 0 , h20_5 binary default 0 , h21 binary default 0 , h21_5 binary default 0 );
insert into class(class) VALUES("B201") ,("B202") ,("B203") ,("B204") ,("B205") ,("B101") ,("B102") ,("B103") ,("B104") ,("B105") ,("101") ,("102") ,("103") ,("104") ,("105") ,("201") ,("202") ,("203") ,("204") ,("205") ,("301") ,("302") ,("303") ,("304") ,("305") ,("401") ,("402") ,("403") ,("404") ,("405");