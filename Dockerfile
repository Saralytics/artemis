FROM python:3.11

RUN apt-get update
COPY Pipfile Pipfile.lock ./
RUN pip install --upgrade pip && pip install pipenv && pipenv install --system --ignore-pipfile --deploy && pipenv --clear

COPY src/ /app
WORKDIR /app
ENV PYTHONPATH "/app"

ENV PORT 5000
EXPOSE 5000

ENTRYPOINT ["uwsgi"]
CMD ["--ini", "artemis.ini"]
