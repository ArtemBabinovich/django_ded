FROM python:3.10
ENV PYTHONNUNBUFFERED 1
WORKDIR /django_ded
COPY . .
RUN pip install --upgrade pip
RUN pip install gunicorn
RUN pip install -r requirements.txt
CMD ["gunicorn", "--bind", ":8000", "--workers", "2", "ded.wsgi:application"]