FROM remote-docker.artifactory.swisscom.com/debian:bullseye-slim


ENV http_proxy http://server-proxy.corproot.net:8080
ENV https_proxy http://server-proxy.corproot.net:8080

ENV no_proxy 127.0.0.1,localhost,corproot.net,swissptt.ch,jira.swisscom.com,artifactory.swisscom.com,bin.swisscom.com,git.swisscom.com,dev-scapp-corp.swisscom.com,*.dev-scapp-corp.swisscom.com,dev-scapp-console.swisscom.com,*.dev-scapp-console.swisscom.com,scapp-corp.swisscom.com,*.scapp-corp.swisscom.com,scapp-console.swisscom.com,*.scapp-console.swisscom.com,svc.cluster.local,sccloudres.net
USER root

WORKDIR /flask-simple-app


RUN apt-get update && apt-get install -y --no-install-recommends \
        python3 \
        python3-pip \
        wget \
        curl \
        netcat \
        && apt-get update

COPY . .
RUN pip3 install --no-cache -r requirements.txt

EXPOSE 5000
#CMD [ "python3", "-m" , "flask", "--app app", "run"]
#CMD ["flask --app app run"]
CMD ["flask", "run", "--host", "0.0.0.0"]