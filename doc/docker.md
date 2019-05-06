# Docker setup

## Run

```
docker-compose up
```

When everything is up, launch the worker:
```
docker exec -it exodus "start-worker"
```

The exodus container automatically:
- Create the database
- Make migration
- Import trackers from the main instance
- Start the frontend of exodus


## Aliases

You can use the command
```
docker exec -it exodus /entrypoint.sh "<command>"
```
to make actions, where `<command>` can be:
- `create-db`: Create the database and apply migrations
- `create-user`: Create a Django user
- `import-trackers`: Import all trackers from the main exodus instance
- `start-frontend`: Start the web server
- `start-worker`: Start the exodus worker

