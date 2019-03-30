FROM alpine:3.9

COPY pkgs/spark-2.3.3-bin-hadoop2.7.tgz /opt/
COPY src/spark.sh /etc/profile.d/spark.sh
COPY src/.bashrc /root/.bashrc
COPY src/prime-ivy-spark.sh /root/prime-ivy-spark.sh
COPY src/pip-requirements.txt /root/pip-requirements.txt
COPY src/pkgs-setup.sh /root/pkgs-setup.sh

RUN /bin/sh /root/pkgs-setup.sh && \
    pip3 install --upgrade pip && \
    cd /opt && \
    tar xzfv spark-2.3.3-bin-hadoop2.7.tgz  && \
    ln -s spark-2.3.3-bin-hadoop2.7 spark && \
    cd / && \
    ln -s /usr/bin/python3 /usr/bin/python && \
    cd /root && \
    chmod a+x /root/prime-ivy-spark.sh && \
    bash /root/prime-ivy-spark.sh

ENTRYPOINT  ["/bin/bash" ]
