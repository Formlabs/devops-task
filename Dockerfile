FROM python:3.9.1
RUN pip install --upgrade virtualenv
ADD . /devops-task
WORKDIR /devops-task
RUN /devops-task/build.sh
ENTRYPOINT ["/devops-task/run.sh"]
