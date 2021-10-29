FROM python:3.9.1
ADD . /devops-task
WORKDIR /devops-task
RUN /devops-task/build.sh
ENTRYPOINT ["/devops-task/run.sh"]
