
get admin token:
curl -X POST http://192.168.1.100:8000/api/token/ \
  -H "Content-Type: application/json" \
  -d '{"username": "admin", "password": "admin"}

create switch 1:
curl -X POST http://192.168.1.100:8000/api/switches/ \
     -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQwMDQ1MzA2LCJpYXQiOjE3Mzk5NTg5MDYsImp0aSI6ImExMDAxZGRiMzI1ZTQxNWNiMTJhYWNhOTU5ZDI1MDg0IiwidXNlcl9pZCI6MX0.n3mxYwHdrToyxtc8fdoRiM3kJQV4cXhuFAImA2C6u-Q" \
     -H "Content-Type: application/json" \
     -d '{"name": "switch_1", "state": false}'

make switch 1 on:
curl -X PATCH http://192.168.1.100:8000/api/switches/1/ \
     -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQwMDQ1MzA2LCJpYXQiOjE3Mzk5NTg5MDYsImp0aSI6ImExMDAxZGRiMzI1ZTQxNWNiMTJhYWNhOTU5ZDI1MDg0IiwidXNlcl9pZCI6MX0.n3mxYwHdrToyxtc8fdoRiM3kJQV4cXhuFAImA2C6u-Q" \
     -H "Content-Type: application/json" \
     -d '{"state": true}'

get switches:
curl -X GET http://192.168.1.100:8000/api/switches/ \
-H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQwMDQ1MzA2LCJpYXQiOjE3Mzk5NTg5MDYsImp0aSI6ImExMDAxZGRiMzI1ZTQxNWNiMTJhYWNhOTU5ZDI1MDg0IiwidXNlcl9pZCI6MX0.n3mxYwHdrToyxtc8fdoRiM3kJQV4cXhuFAImA2C6u-Q"

Summary of cURL Commands
Action	Method	URL	Headers & Body
Login (Get JWT)	POST	/api/token/	{"username": "...", "password": "..."}
Create Switch	POST	/api/switches/	{"name": "Switch 1", "state": false}
List Switches	GET	/api/switches/	Authorization: Bearer <token>
Get Switch by ID	GET	/api/switches/1/	Authorization: Bearer <token>
Update Switch	PATCH	/api/switches/1/	{"state": true}
Delete Switch	DELETE	/api/switches/1/	Authorization: Bearer <token>

sql:
prakash@DESKTOP-C26OAB4:~$ sudo -u postgres psql
[sudo] password for prakash:
psql (17.2 (Ubuntu 17.2-1.pgdg24.04+1))
Type "help" for help.

postgres=#  create database eapidb;
CREATE DATABASE
postgres=#  create user eapidbowner with password 'eapidbowner';
CREATE ROLE
postgres=# grant all on database eapidb to eapidbowner;
GRANT
postgres=# GRANT ALL PRIVILEGES ON DATABASE eapidb TO eapidbowner;
GRANT
postgres=# alter database eapidb owner to eapidbowner;
ALTER DATABASE
postgres=# \q
