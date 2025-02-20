




"Add Environment Variable" and add the following:

Key	Value (Example)	Description
DEBUG	False	Disable debug mode in production
SECRET_KEY	your-secret-key	Keep this secret (generate one using python -c "import secrets; print(secrets.token_hex(32))")
DATABASE_URL	postgres://user:password@host:port/dbname	PostgreSQL connection string from Render
ALLOWED_HOSTS	your-app-name.onrender.com	Your Render domain
CORS_ALLOWED_ORIGINS	https://your-frontend.vercel.app	Allow frontend access
DJANGO_SUPERUSER_USERNAME	admin	Superuser username (optional)
DJANGO_SUPERUSER_EMAIL	admin@example.com	Superuser email (optional)
DJANGO_SUPERUSER_PASSWORD	yourpassword	Superuser password (optional)


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

Hostname
An internal hostname used by your Render services.

dpg-curbcqa3esus73dlptpg-a

Port
5432

Database
eapidb

Username
eapidbowner



Create PostgreSQL Database & User
Access PostgreSQL CLI:
bash
Copy
sudo -u postgres psql  # On Linux/macOS
psql -U postgres       # On Windows (if installed with default settings)
Create a New Database:
sql
Copy
CREATE DATABASE switch_db;
Create a Database User and Set a Password:
sql
Copy
CREATE USER switch_user WITH PASSWORD 'yourpassword';
Grant Permissions to the User:
sql
Copy
ALTER ROLE switch_user SET client_encoding TO 'utf8';
ALTER ROLE switch_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE switch_user SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE switch_db TO switch_user;
Exit PostgreSQL CLI:
sql
Copy
\q


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
