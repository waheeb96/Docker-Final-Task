FROM 3.10.5-slim-buster
WORKDIR /code
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
COPY . . 
CMD ["py", "main.py"]