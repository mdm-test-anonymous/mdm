FROM python:3.8.5

WORKDIR /opt/app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

RUN pip install .

EXPOSE 5000

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]
