FROM python:alpine

WORKDIR app

RUN apk add --no-cache  musl-dev mariadb-connector-c-dev gcc
RUN --mount=type=bind,source=requirements.txt,target=/tmp/requirements.txt \
    pip install --no-input --no-cache-dir --requirement /tmp/requirements.txt gunicorn mysqlclient

COPY manage.py .docker/entrypoint.sh ./
COPY buzzers_n_hoopers ./buzzers_n_hoopers
COPY assets ./assets
COPY common ./common
COPY clubber ./clubber
COPY matchup ./matchup

EXPOSE 8000

ENTRYPOINT ["/bin/ash", "/app/entrypoint.sh"]