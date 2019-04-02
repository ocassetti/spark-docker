FROM alpine:3.9

COPY src/spark.sh /etc/profile.d/spark.sh
COPY src/.bashrc /root/.bashrc
COPY src/prime-ivy-spark.sh /root/prime-ivy-spark.sh
COPY src/pip-requirements.txt /root/pip-requirements.txt
COPY src/pkgs-setup.sh /root/pkgs-setup.sh
ENV SPARK_PKG_URL="https://github.com/ocassetti/spark-docker/raw/master/spark-2.3.3/pkgs/spark-2.3.3-bin-hadoop2.7.tgz"
RUN /bin/sh /root/pkgs-setup.sh && \
    ln -s /usr/include/locale.h /usr/include/xlocale.h && \
    pip3 install --upgrade pip && \
    pip3 install -r /root/pip-requirements.txt && \
    cd /opt && \
    wget ${SPARK_PKG_URL} -O spark.tgz &&\
    tar xzfv spark.tgz  && \
    ln -s spark-2.3.3-bin-hadoop2.7 spark && \
    cd / && \
    ln -s /usr/bin/python3 /usr/bin/python && \
    cd /root && \
    chmod a+x /root/prime-ivy-spark.sh && \
    bash /root/prime-ivy-spark.sh


ENTRYPOINT  ["/bin/bash", "/mnt/workspace/run-jupyter.sh"]
