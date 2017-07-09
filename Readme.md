## NOTICE:

This repository is still under construction to be more generalized for wider consumption. 

# Build your Docker Image

`docker build -t ns-init .`

# RUn your Docker Container

```
docker run \
-dt \
--name=ns-init \
-e NSIP=172.16.0.11 \
-e USERNAME=nsroot \
-e PASSWORD=nsroot \
-e DOCKERHOST=172.16.0.5 \
-e VIP1=172.16.0.20 \
-e VIP2=172.16.0.21 \
-e VIP3=172.16.0.23 \
-e DNS=8.8.8.8 \
-e HOSTNAME=NS1 \
-e VSERVER=lb_vsrvr_webapp-https \
-e VSERVER1=lb_vsrvr_webapp-http \
-e VSERVER2=lb_vsrvr_website-http \
-e SERVICE1=srvc_https-website \
-e SERVICE2=srvc_http-website \
-v /path/to/vip-input:/vip-input \
ns-init
```