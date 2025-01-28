# The builder image, used to build the virtual environment
FROM python:3.11-buster as builder
#FROM --platform=linux/amd64 python:3.11-buster as builder

RUN pip install poetry

EXPOSE 8509
HEALTHCHECK CMD curl --fail http://localhost:8509/_stcore/health

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

WORKDIR /app

COPY src ./src
COPY pyproject.toml poetry.lock ./
RUN touch README.md

RUN poetry install --without dev && rm -rf $POETRY_CACHE_DIR -vvv

# The runtime image, used to just run the code provided its virtual environment
FROM python:3.11-slim-buster as runtime
#FROM --platform=linux/amd64 python:3.11-buster as runtime

WORKDIR /app

ENV VIRTUAL_ENV=/app/.venv \
    PATH="/app/.venv/bin:$PATH"
#    METAFLOW_USER="Metaflow_User" \
#    METAFLOW_ARGO_EVENTS_EVENT="argo-events-webhookmetaflow-event" \
#    METAFLOW_ARGO_EVENTS_EVENT_BUS="default" \
#    METAFLOW_ARGO_EVENTS_EVENT_SOURCE="argo-events-webhook" \
#    METAFLOW_ARGO_EVENTS_INTERNAL_WEBHOOK_URL="http://argo-events-webhook-eventsource-svc:12000/metaflow-event" \
#    METAFLOW_ARGO_EVENTS_SERVICE_ACCOUNT="{{ project-name }}" \
#    METAFLOW_ARGO_EVENTS_WEBHOOK_URL="http://localhost:12000/metaflow-event" \
#    METAFLOW_DEFAULT_METADATA="service" \
#    METAFLOW_KUBERNETES_NAMESPACE="metaflow" \
#    METAFLOW_KUBERNETES_SERVICE_ACCOUNT="{{ project-name }}" \
#    METAFLOW_SERVICE_INTERNAL_URL="http://metaflow-metaflow-service.metaflow:8080" \
#    METAFLOW_SERVICE_URL="http://localhost:8080"

COPY --from=builder ${VIRTUAL_ENV} ${VIRTUAL_ENV}
COPY --from=builder /app/src /app/src
COPY create_workflows.sh logging.yaml ./
RUN chmod 777 create_workflows.sh

ENTRYPOINT ["python", "-m", "{{ project_name }}.main"]
