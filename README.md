# Counter HTTP API Server

This is a simple HTTP API server application written in Flask that wraps a counter and exposes the following operations:

* /get: Returns the counter value, 0 by default.
* /increase: Adds 1 to the counter value and returns it.
* /decrease: Decreases 1 from the counter value and returns it.

The counter value is persisted into either a database or a file on the server.


## Getting Started

To run the application, you need to have Docker and Docker Compose installed on your system.

1. Clone this repository:

`git clone https://github.com/your_username/counter-http-api-server.git
cd counter-http-api-server`

2. Build and Run the Docker image:

`docker-compose up`

This will start the API server on port 9090. You can test the API endpoints using a tool like curl or a web browser:

* http://localhost:9090/get: Returns the current counter value
* http://localhost:9090/increase: Adds 1 to the counter value and returns it
* http://localhost:9090/decrease: Decreases 1 from the counter value and returns it


## Persistence

The counter value is persisted into a file named data/counter.txt by default. You can change this location by modifying the data volume in the docker-compose.yml file.