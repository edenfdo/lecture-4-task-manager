FROM python:3.12-slim

WORKDIR /workspace

COPY . /workspace

RUN chmod +x .github/scripts/entrypoint.sh

ENTRYPOINT ["bash", "/workspace/.github/scripts/entrypoint.sh"]