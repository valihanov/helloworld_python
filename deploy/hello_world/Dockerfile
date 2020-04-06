FROM python:3.6-alpine

ENV prometheus_multiproc_dir /tmp/prometheus_multiproc_dir

RUN mkdir -p /tmp/prometheus_multiproc_dir

ADD src/requirements.txt /

RUN pip3 install -r requirements.txt

ADD src/*.py /

ENTRYPOINT [ "gunicorn", "-c", "gunicorn_config.py", "-w", "4", "-b", "0.0.0.0:5000", "wsgi:app" ]

EXPOSE 5000/tcp
