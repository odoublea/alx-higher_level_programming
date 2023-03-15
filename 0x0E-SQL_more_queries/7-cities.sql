-- Create the database hbtn_0d_usa 
-- the table cities(in the database hbtn_0d_usa)
-- on the MySQL server
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS  hbtn_0d_usa.cities (
	id INT PRIMARY KEY AUTO_INCREMENT NOT NULL UNIQUE,
	state_id INT NOT NULL,
	FOREIGN KEY(state_id)
		REFERENCES states(id),
	name VARCHAR(256) NOT NULL
	)
