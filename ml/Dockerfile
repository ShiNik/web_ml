FROM python:3.7.6

WORKDIR /usr/src

RUN mkdir ml

COPY ./dependencies/requirements.txt ./ml/tmp/requirements.txt
RUN pip install --no-cache-dir -r ./ml/tmp/requirements.txt

COPY . ./ml

CMD [ "python", "./ml/app.py" ]