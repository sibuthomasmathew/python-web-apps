# Stage 1 - Install build dependencies
FROM python:3.8-alpine

WORKDIR /app

COPY *.py requirements.txt ./

RUN adduser -D python-user \
    && pip3 install --no-cache-dir --upgrade pip \
    && pip3 install --no-cache-dir -r requirements.txt

USER python-user

EXPOSE 5000

CMD [ "python", "app.py"]
