FROM python:3.8
LABEL authors="ACULHA"
COPY ./requirements.txt /requirements.txt
RUN pip install --no-cache-dir --upgrade -r /requirements.txt
WORKDIR /code
COPY ./ /code
CMD ["python3", "app.py"]

# docker build -t sentimental_api .
# docker run -d --restart always -p 8080:8080 sentimental_api
# docker save save image-name > image-name.tar
# docker load < dosya.tar