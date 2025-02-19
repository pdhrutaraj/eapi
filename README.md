prakash@DESKTOP-C26OAB4:~$ sudo -u postgres psql
[sudo] password for prakash:
psql (17.2 (Ubuntu 17.2-1.pgdg24.04+1))
Type "help" for help.

postgres=#  create database eapidb;
CREATE DATABASE
postgres=#  create user eapidbowner with password 'eapibowner';
CREATE ROLE
postgres=# grant all on database eapidb to eapidbowner;
GRANT
postgres=# GRANT ALL PRIVILEGES ON DATABASE eapidb TO eapidbowner;
GRANT
postgres=# alter database eapidb owner to eapidbowner;
ALTER DATABASE
postgres=# \q
