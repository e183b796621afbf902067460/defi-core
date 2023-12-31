# Use the official ClickHouse image as the base image
FROM clickhouse/clickhouse-server:23.1-alpine

COPY ./docker-entrypoint-initdb.d/ /docker-entrypoint-initdb.d/
COPY ./scripts/sed.sh sed.sh

ARG KAFKA_BROKER_LIST
ARG KAFKA_TOPIC_LIST
ARG KAFKA_GROUP_NAME

ARG CLICKHOUSE_DB

ARG IS_DEV
RUN if [ ! -z "$IS_DEV" ] ; then \
    bash sed.sh KAFKA_BROKER_LIST ${KAFKA_BROKER_LIST}; \
fi
RUN if [ ! -z "$IS_DEV" ] ; then \
    bash sed.sh KAFKA_TOPIC_LIST ${KAFKA_TOPIC_LIST}; \
fi
RUN if [ ! -z "$IS_DEV" ] ; then \
    bash sed.sh KAFKA_GROUP_NAME ${KAFKA_GROUP_NAME}; \
fi

RUN if [ ! -z "$IS_DEV" ] ; then \
    bash sed.sh CLICKHOUSE_DB ${CLICKHOUSE_DB}; \
fi
