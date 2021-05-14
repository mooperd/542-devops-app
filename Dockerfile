FROM python
WORKDIR /app

COPY requirements.txt /app

RUN pip install -r requirements.txt && apt-get update && apt-get install mysql-client -y 

COPY . /app

EXPOSE 8080

CMD ./start.sh
