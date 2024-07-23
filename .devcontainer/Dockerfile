FROM mcr.microsoft.com/vscode/devcontainers/python:3.12

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update \
   && apt-get upgrade -y  \
   && apt-get autoremove -y \
   && apt-get clean -y \

ENV DEBIAN_FRONTEND=dialog

RUN pip install poetry
RUN pip install --upgrade pip
RUN pip install colored