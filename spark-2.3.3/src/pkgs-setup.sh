#/bin/#!/bin/sh

apk \
add \
--no-cache \
--virtual=.build-dependencies

apk add --no-cache \
wget \
bash \
ca-certificates \
openjdk8-jre \
nss \
libpng \
libpng-dev \
libpng-utils \
freetype \
freetype-dev \
make \
automake \
gcc \
gfortran \
g++ \
python3 \
python3-dev \
bash-completion \
bash-doc \
tar \
curl \
curl-dev \
libcurl
