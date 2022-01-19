FROM python:3.9.0

WORKDIR /home/

RUN git clone https://github.com/duskite/django_pinterest_ex.git

WORKDIR /home/pragmatic/

RUN pip install -r requirements.txt

RUN echo "SECRET_KEY=django-insecure-zxi7p*@05q=8nj%qfew%&6qo(r-2r@7b^i5q($j9f#w_%r#i7_" > .env

RUN python manage.py migrate

EXPOSE 8000

CMD ["python", "manage.py","runserver", "0.0.0.0:8000"]