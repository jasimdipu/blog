FROM mysql/mysql-server:8.0

COPY ./database/mysql/mysql_db.sh /docker-entrypoint-initdb.d/
RUN chmod +x /docker-entrypoint-initdb.d/mysql_db.sh