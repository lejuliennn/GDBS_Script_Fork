DROP TABLE IF EXISTS Abteilung;
CREATE TABLE Abteilung(
	AbtID integer NOT NULL PRIMARY KEY,
	Standort varchar(127),
	Name varchar(127),
	Budget integer);


DROP TABLE IF EXISTS Personal;
CREATE TABLE Personal(
 AbtID integer,
 Name varchar(127),
 Gehalt integer,
 Bonus integer,
 PRIMARY KEY (AbtID, Name),
 FOREIGN KEY(AbtID) REFERENCES Abteilung(AbtID));

