# FastAPI <-> OpenAPI Auto-Generated Client

This repository shows how we can easily auto-generate FastAPI clients via the OpenAPI schema that is automatically generated by FastAPI.

## Running the example

### Setting up

- First, activate a virtual environment
- Install requirements for the server: `pip install -r server/requirements.txt`
- Auto-generate a client using the server's OpenAPI schema and pip install it as `my_server_client` package:
  `./client/scripts/install_server_client.sh`

### Running the exampple

- Run the server: `python -m server.main`
- Run the client that will create a user and list users with the auto-generated client: `python -m client.main`