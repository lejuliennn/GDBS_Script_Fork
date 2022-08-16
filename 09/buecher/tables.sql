DROP TABLE IF EXISTS BuchExemplar;
CREATE TABLE BuchExemplar(
	ISBN integer NOT NULL PRIMARY KEY,
	InventarNr integer,
	Titel varchar(127),
	Autor integer);


DROP TABLE IF EXISTS Ausleihe;
CREATE TABLE Ausleihe(
 ISBN integer,
 InventarNr varchar(127),
 KundenNr integer,
 PRIMARY KEY (ISBN, KundenNr),
 FOREIGN KEY(ISBN) REFERENCES BuchExemplar(ISBN),
 FOREIGN KEY(InventarNr) REFERENCES BuchExemplar(InventarNr));

