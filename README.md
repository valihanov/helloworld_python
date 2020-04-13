# hello_world

This is a "Hello world" dockerized Python web application with Prometheus monitoring and Grafana dashboard.

## Installation

Build and run docker-compose services from ./deploy dir.

```bash
cd ./deploy
docker-compose build
docker-compose up -d
```

These commands should start application, Prometheus, Grafana.

The application and other services should be available under the following links, if you are opening links not from the host where you started docker-compose, than you should replace 'localhost' with the address of you docker-compose host:

* [localhost:5000](http://localhost:5000) - application
* [http://localhost:5000/healthcheck](http://localhost:5000/healthcheck) - application's healthcheck endpoint.
* [http://localhost:5000/readycheck](http://localhost:5000/readycheck) - application's readiness endpoint.
* [http://localhost:9091/metrics](http://localhost:9091/metrics) - application's metrics.
* [http://localhost:9090](http://localhost:9090) - Prometheus
* [http://localhost:3000](http://localhost:3000) - Grafana. It uses default admin:admin credentials.

## License

This project is licensed under the terms of the WTFPL license. For more information, please see [LICENSE.txt](LICENSE.txt)

## Authors

* **Ruslan Valikhanov** [valihanovr@yandex.ru](mailto:valihanovr@yandex.ru)
