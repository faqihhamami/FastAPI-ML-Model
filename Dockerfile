FROM python:3.9

WORKDIR /fastapi-sales-pred

ADD . /fastapi-sales-pred

RUN pip install -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8900"]