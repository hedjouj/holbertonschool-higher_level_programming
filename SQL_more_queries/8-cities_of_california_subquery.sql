-- list all cities of california in database 
use hbtn_0d_usa;
SELECT id, name from cities
WHERE state_id = (
    SELECT id from states WHERE name = 'California'
)
ORDER BY id ASC;
