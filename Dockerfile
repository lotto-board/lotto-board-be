FROM postgres:13

ENV POSTGRES_DB=lotto
ENV POSTGRES_USER=lotto
ENV POSTGRES_PASSWORD=lotto
ENV LANG=C.UTF-8
ENV TZ=Asia/Seoul

#COPY ./my.cnf /etc/postgresql/postgresql.conf

COPY ./sql-scripts/ /docker-entrypoint-initdb.d/

# 포트 설정
EXPOSE 3306
