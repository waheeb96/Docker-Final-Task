FROM python:3.10.5-alpine
WORKDIR /code
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
COPY . . 
CMD ["python3", "main.py"]
