-- here the name of database is 'world_countries' 
-- And I supposed you have create the postgis extension on your database


-- import shp with command tools for windows (cmd)
-- shp2pgsql -I "C:\work\arcpy\natural_earth_vector\10m_cultural\ne_10m_admin_0_countries.shp" public.world | psql -U postgres -d world_countries
 -- If you import with windows gui tools, run the following renmae statement
 -- ALTER TABLE ne_10m_admin_0_countries RENAME TO world;


 -- find the srid of one column

SELECT find_srid('public', 'world', 'geom');

 -- Default srid when import is 0, now change it to WGS84

SELECT UpdateGeometrySRID('world', 'geom', 4326);

 -- create table points

CREATE TABLE points (id serial PRIMARY KEY, lon float NOT NULL, lat float NOT NULL);

 -- copy point data (only coordinates infomation) to table
 COPY points(lon, lat)
FROM 'c:/work/face_cut0.txt' DELIMITER E'\t' csv;

 -- Add geometry field

ALTER TABLE points ADD COLUMN geom geometry(point, 4326);

 -- Add data to geometry field

UPDATE points
SET geom = st_setsrid(st_makepoint(points.lon, points.lat), 4326);

 -- Create index on point

CREATE INDEX points_idx ON points USING gist(geom);

 -- Spatial query, this line need more improvement

 -- Before the following select
 -- you may run this to redirect the output to file
 -- (psql) \o 'c:/work/output.csv'

SELECT a.lon,
       a.lat,
       b.name
FROM points a,
     world b
WHERE st_intersects(a.geom, b.geom);

-- Time test for LIMIT N:
-- When N = ...
-- 100 using 28ms
-- 1000 using 113ms
-- 2000 using 204ms √ Best One now !
-- 2500 using 279ms
-- 3000 using 597ms
-- 5000 using 2193ms
-- 8000 using 4614ms
-- 10000 using 6171ms
