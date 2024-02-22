FROM python:3.9
ENV APP_PORT=4000
WORKDIR /app

RUN pip install flask requests

COPY . .

CMD ["python", "app.py"]