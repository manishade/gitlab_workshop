FROM remote-docker.artifactory.swisscom.com/python:3.8-slim
WORKDIR /opt
COPY requirements.txt .
COPY tests .
RUN pip install -r requirements.txt -i https://artifactory.swisscom.com/artifactory/api/pypi/pypi-remote/simple
CMD ["tini","--","/opt/jenkins/bin/entrypoint.sh"]