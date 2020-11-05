FROM python:3.8.5

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY /P2py .

CMD ["python", "parcial2.py"]