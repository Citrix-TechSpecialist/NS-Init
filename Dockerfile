FROM python:2-alpine
MAINTAINER Americas - Readiness Networking Tech Specialists <#Americas-Readiness-Networking-Tech-Specialists@citrite.net>
LABEL Name="ns-init" Version="1" Release="1"

RUN mkdir /scripts ; mkdir /vip-input
COPY ./ /scripts/
RUN apk add --no-cache git lftp openssh
#RUN pip install requests
RUN cd /scripts/nitro-python-1.0/ ; python setup.py install
RUN rm -rf /scripts/nitro-python-1.0/
RUN chmod 777 /scripts/uploadcerts.sh ; chmod 777 /scripts/configNS.py
CMD /scripts/uploadcerts.sh ; python /scripts/configNS.py
