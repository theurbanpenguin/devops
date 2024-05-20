FROM mysql
ENV MYSQL_ROOT_PASSWORD=rootpassword
ENV MYSQL_USER=myuser
ENV MYSQL_PASSWORD=mypassword

COPY init.sql /docker-entrypoint-initdb.d/

EXPOSE 3306