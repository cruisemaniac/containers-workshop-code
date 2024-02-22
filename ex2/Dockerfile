FROM python:3.9
ENV APP_PORT=4000
WORKDIR /app

RUN pip install flask

COPY . .

CMD ["python", "app.py"]