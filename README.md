openssl req -new -newkey rsa:4096 -x509 -sha256 -days 365 -nodes -out www.hello_world.com.crt -keyout www.hello_world.com.key

# Dockerized hello-world app

## Usage
When a  GET request is sent to to /hello endpoint, this service returns a JSON response with the following content:
> { "hello": "world" }

## How to start the service
Move to the root directory of the project and execute the following command:
> docker-compose up

## Software requirements
- docker service running:
- docker-compose
- python 3
- pip

## Architecture

This microservice has two components:
- A python application listening on port 8080
- A nginx reverse proxy listening on ports 80 and 443, working as follows:
  - Requests on port 80 are redirected to port 443
  - Requests on port 443 are passed to the python app (port 8080)

## Certificate
The HTTPS service requires an SSL certificate and key. A self-signed certificate can be created as follows:
> openssl req -new -newkey rsa:4096 -x509 -sha256 -days 365 -nodes -out www.hello_world.com.crt -keyout www.hello_world.com.key

This command will generate to files:
- www.hello_world.com.crt
- www.hello_world.com.key

These two files need to be copied in the certificate folder before running the service.

To prevent

## Rationale for choosing this solution:
The rationale to choose this solution over others has been simplicity and trying to minimaze resource consumption:
- Docker-compose have been chosen because it doesn't require any previous set up
- Nginx has been chosen over Apache for being more lightweight
- Python language has been selected for being simpler and quicker than most languages to develop a webapp.








