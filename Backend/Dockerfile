FROM python:3.12
EXPOSE 5000

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

WORKDIR /app

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD ["flask", "run"]

# # STAGE 1

# FROM python:3.12 AS build

# # Keeps Python from generating .pyc files in the container
# ENV PYTHONDONTWRITEBYTECODE=1

# # Turns off buffering for easier container logging
# ENV PYTHONUNBUFFERED=1

# WORKDIR /app

# ENV FLASK_APP=app.py
# ENV FLASK_RUN_HOST=0.0.0.0

# COPY . .

# RUN pip install -r requirements.txt

# # STAGE 2
# FROM python:3.12-slim

# WORKDIR /app

# COPY --from=build /app .


# EXPOSE 5000

# ENTRYPOINT ["python3.5"]

# CMD ["flask", "run"]