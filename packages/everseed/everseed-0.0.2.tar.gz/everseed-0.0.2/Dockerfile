FROM python:3 as builder

RUN addgroup everseed
RUN adduser --ingroup everseed everseed

USER everseed

WORKDIR /usr/src/app

COPY requirements.txt /tmp/requirements.txt
RUN pip install  --disable-pip-version-check --no-cache-dir -r /tmp/requirements.txt

COPY --chown=everseed:everseed entrypoint ./

ADD --chown=everseed:everseed src/everseed/everseed.py ./

USER root

ENTRYPOINT ["/usr/src/app/entrypoint"]