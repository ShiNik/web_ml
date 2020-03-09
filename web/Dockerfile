FROM python:3.7.6

WORKDIR /usr/src

RUN mkdir web

COPY ./dependencies/requirements.txt ./web/tmp/requirements.txt
RUN pip install --no-cache-dir -r ./web/tmp/requirements.txt

COPY . ./web

CMD [ "python", "./web/run.py" ]