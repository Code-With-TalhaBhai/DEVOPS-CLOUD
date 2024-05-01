FROM ubuntu:22.04
RUN mkdir talha
RUN apt update

FROM python:latest
RUN pip install poetry
WORKDIR /code
ADD main.py pyproject.toml /code/
RUN poetry config virtualenvs.create false
RUN poetry install
CMD ["poetry","run","uvicorn","main:app","--host","0.0.0.0","--reload"]
