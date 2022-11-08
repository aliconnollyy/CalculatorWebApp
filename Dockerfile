FROM python:latest
WORKDIR /app
COPY . /app/
CMD [ "python", "./calcGUI.py" ]
