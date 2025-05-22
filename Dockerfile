FROM python:3.11-slim

RUN adduser --disabled-password --gecos '' appuser
USER appuser

WORKDIR /app

COPY app/ /app/
RUN pip install --no-cache-dir -r requirements.txt

ENV DB_HOST=db
ENV DB_USER=root
ENV DB_PASSWORD=senha123
ENV DB_NAME=dimdim

CMD ["python", "main.py"]
