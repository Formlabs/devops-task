FROM python:3.10.4-alpine3.16
WORKDIR /helloapp

COPY . .
RUN pip3 install -r requirements.txt
RUN addgroup -g 2000 helloapp
RUN adduser -H -D --uid 2000 -G helloapp helloapp && chown -R helloapp /helloapp

USER helloapp
ENTRYPOINT ["gunicorn", "--bind", "0.0.0.0:8080", "-w", "2", "helloapp.app:app"]
