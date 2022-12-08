FROM python:3.8-slim
ENV PYTHONUNBUFFERED=1
RUN mkdir /var/www
COPY requirements.txt /var/www/
RUN cd /var/www && \
    python3 -m pip install -r requirements.txt
COPY app.py .
ENTRYPOINT ["gunicorn", "app:app", "--bind=0.0.0.0:8000", "--workers=4", "--log-level=debug", "--reload"]
