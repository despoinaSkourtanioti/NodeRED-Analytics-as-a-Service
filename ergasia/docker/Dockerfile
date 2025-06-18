FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY smoking-model.py .
COPY smoking.csv .

EXPOSE 5000
CMD ["python", "smoking-model.py"]