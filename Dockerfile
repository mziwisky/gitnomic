FROM ubuntu:xenial

USER root
RUN apt-get update && apt-get install -y \
    mongodb \
    python3-pip \
    && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \
    && pip3 install --upgrade pip

WORKDIR /usr/src/app

CMD ["./start.sh"]
