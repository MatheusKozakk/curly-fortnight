FROM python:3.13

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip
RUN pip install "fastapi[standard]" uvicorn[standard]

EXPOSE 80
CMD [ "fastapi", "run", "main.py", "--port", "80"]
