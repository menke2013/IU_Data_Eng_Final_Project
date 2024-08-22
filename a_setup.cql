-- Create a keyspace
CREATE KEYSPACE IF NOT EXISTS sensorbase WITH REPLICATION = { 'class' : 'SimpleStrategy', 'replication_factor' : '1' };

-- Create a table
CREATE TABLE IF NOT EXISTS sensorbase.table1 (
sensor text ,
co float,
humidity float,
light Boolean, 
lpg float,
motion Boolean,
smoke float,
temp float,
time_stamp timestamp,  
PRIMARY KEY ((sensor, light), time_stamp)
);

CREATE INDEX ON sensorbase.table1 (co)
USING 'SAI'
;

CREATE INDEX ON sensorbase.table1 (humidity)
USING 'SAI'
;

CREATE INDEX ON sensorbase.table1 (lpg)
USING 'SAI'
;

CREATE INDEX ON sensorbase.table1 (smoke)
USING 'SAI'
;

CREATE INDEX ON sensorbase.table1 (temp)
USING 'SAI'
;


copy sensorbase.table1 (sensor, co, humidity, light, lpg, motion, smoke, temp, time_stamp) FROM '/docker-entrypoint-initdb.d/data_updated.csv' WITH DELIMITER=',' and HEADER=FALSE;