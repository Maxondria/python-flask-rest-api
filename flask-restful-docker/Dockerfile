FROM python:3.7-alpine

WORKDIR /app

ADD requirements.txt .

RUN pip install -r requirements.txt

# COPY . /app

CMD ["flask", "run", "-h", "0.0.0.0", "-p", "5000"]