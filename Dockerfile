FROM tiangolo/uwsgi-nginx-flask:python3.6

WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt

