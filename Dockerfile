FROM alpine

RUN apk --no-cache add \
  python3

WORKDIR /app

COPY requirements.txt /app

RUN pip3 install -r requirements.txt

COPY . /app

RUN pip3 install .

EXPOSE 5000

CMD ["python3", "run.py"]

