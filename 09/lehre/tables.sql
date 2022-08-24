DROP TABLE IF EXISTS Prof;
CREATE TABLE Prof(
	ProfID integer NOT NULL PRIMARY KEY,
	Nachname varchar(127),
	Lehrstuhlbezeichnung varchar(127),
	PA_Nr integer);


DROP TABLE IF EXISTS Liest;
CREATE TABLE Liest(
 VL_Nr integer,
 PA_Nr integer,
 Nachname varchar(127));
 
DROP TABLE IF EXISTS Prueft;
CREATE TABLE Prueft(
	Pruefer integer,
	VL_Nr integer,
	PA_Nr integer,
	Matrikel integer,
	Note float);
	
DROP TABLE IF EXISTS Student;
CREATE TABLE Student(
	Matrikel integer NOT NULL PRIMARY KEY,
	Name varchar(127));

