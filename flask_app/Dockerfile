FROM python:3.6.1-alpine

COPY . /app

WORKDIR /app

COPY requirements.txt .

RUN \
 apk add --no-cache postgresql-libs && \
 apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
 apk add --no-cache python3-dev libffi-dev gcc && \
 pip3 install --upgrade pip && \
 python3 -m pip install -r requirements.txt && \
 apk --purge del .build-deps

EXPOSE 5000

CMD [ "python3", "run.py" ]
