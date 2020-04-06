import os

from flask import Flask
from healthcheck import HealthCheck
from prometheus_flask_exporter.multiprocess import GunicornPrometheusMetrics
import redis

try:
    redis_client = redis.Redis(host="redis", port=6379, password="secret-pass")
except redis.RedisError as e:
    print(e) 

app = Flask(__name__)

metrics = GunicornPrometheusMetrics(app)

metrics.info('app_info', 'Application info', version='1.0')

health = HealthCheck()

def redis_available():
    redis_client.info()
    return True, "Redis OK"

health.add_check(redis_available)

app.add_url_rule("/healthcheck", "healthcheck", view_func=lambda: health.run())

@app.route('/readycheck')
def ready():
    return 'App ready!'

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
