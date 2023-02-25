FROM python:3.9.13-slim

COPY ../requirements/requirements.txt /main/requirements.txt
RUN pip install --upgrade pip -r /main/requirements.txt

WORKDIR /main

COPY ../app  /main/app
COPY ../configs/logger_cfg.yaml /main/configs/logger_cfg.yaml
COPY ../configs/settings.toml /main/configs/settings.toml
COPY ../configs/.secrets.toml /main/configs/.secrets.toml

