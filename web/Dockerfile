FROM python:3.10
WORKDIR D:/docker/flaskdemo
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY .. .
CMD ["python", "app.py"]