FROM ubuntu:18.04

RUN apt-get update && \
    apt-get install -y build-essential curl && \
    apt-get install unzip && \
    apt-get update && apt-get install -y software-properties-common gcc && \
    add-apt-repository -y ppa:deadsnakes/ppa && \
    apt-get update && apt-get install -y python3.6 python3-distutils python3-pip python3-apt && \
    apt-get update && apt-get install -y git && \
    apt-get install -y python3.6-venv && \
    python3.6 -m pip install pip --upgrade && \
    python3.6 -m pip install wheel


WORKDIR /app
COPY . /app/
RUN rm ./uplink
RUN curl -L https://github.com/storj/storj/releases/latest/download/uplink_linux_amd64.zip -o uplink_linux_amd64.zip && unzip -o uplink_linux_amd64.zip
ENV UPLINK_CONFIG='./uplink --config-dir="/app/Storj/Uplink"'
RUN python3.6 -m pip install -r requirements.txt
EXPOSE 5000
CMD gunicorn app:app