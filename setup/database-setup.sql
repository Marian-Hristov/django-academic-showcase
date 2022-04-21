DROP DATABASE IF EXISTS "academic-showcase-db";

CREATE DATABASE "academic-showcase-db"
    WITH 
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'English_Canada.1252'
    LC_CTYPE = 'English_Canada.1252'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1;

COMMENT ON DATABASE "academic-showcase-db"
    IS 'Database for academic showcase app';

GRANT ALL ON DATABASE "academic-showcase-db" TO postgres;

GRANT TEMPORARY, CONNECT ON DATABASE "academic-showcase-db" TO PUBLIC;

-- Role: academy-admin
DROP ROLE IF EXISTS "academy-admin";

CREATE ROLE "academy-admin" WITH
  LOGIN
  NOSUPERUSER
  INHERIT
  CREATEDB
  NOCREATEROLE
  REPLICATION
  ENCRYPTED PASSWORD 'SCRAM-SHA-256$4096:fqjvydTMHby1lF+fCrc+7A==$UsRKkxjYW99JhDqpMOHag9J30M1vWlnWTfeKV7KobAw=:YreK3xt49Tk0A9GJ4QKmEmODgjSJO2RG1Zcvzs+kofM=';

COMMENT ON ROLE "academy-admin" IS 'Academic showcase admin user';

GRANT ALL ON DATABASE "academic-showcase-db" TO "academy-admin";