FROM python:3.9

RUN mkdir /app
WORKDIR /app

COPY ./requirements.txt ./
RUN pip install -r requirements.txt
COPY . .

#CMD [ "python3", "./src/manage.py", "runserver", "0.0.0.0:8000"]
