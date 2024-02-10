FROM python:3.9
LABEL authors="Pedro Turriago Sanchez"

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app app/
COPY model model/

#COPY test.csv .
RUN mkdir "data"

#ENTRYPOINT ["python", "main.py"]
ENTRYPOINT ["top", "-b"]