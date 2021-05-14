FROM python
WORKDIR /app

COPY requirements.txt /app

RUN pip install -r requirements.txt

COPY . /app

EXPOSE 8080

CMD ["gunicorn", "-b", "0.0.0.0:8080", "--access-logfile", "-", "wsgi:app"]
