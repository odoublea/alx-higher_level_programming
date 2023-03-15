-- List cities of California that can be found in the database hbtn_0d_usa
SELECT id, name FROM states
WHERE states_id = (SELECT name FROM cities WHERE state_id = 1)
ORDER BY id
