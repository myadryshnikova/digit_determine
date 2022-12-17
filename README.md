# digit-determine

To install the dependencies:
```bash
poetry install
```

To run the project:
```bash
docker compose -f docker-compose.yml up --build run-api-locally
```


`Photo recognition endpoint:`

POST - http://localhost:4001/api/digit/determine

`Endpoint to write photos to a folder:`

POST - http://localhost:4001/api/digit/save_photo_label/`label:int`
