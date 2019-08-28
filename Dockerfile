FROM python:3.7-slim
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
ENV FLASK_APP main.py
CMD ["-m","flask","run"]
