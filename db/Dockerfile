FROM mariadb:10.5

WORKDIR /db
COPY python2023.sql /docker-entrypoint-initdb.d/

EXPOSE 3306

# MariaDBを実行
CMD ["mysqld"]