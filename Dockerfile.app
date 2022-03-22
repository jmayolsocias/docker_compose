FROM python:3.7-alpine

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
ENV FLASK_APP /app/app.py

EXPOSE 8080

CMD ["python3", "app.py"]
