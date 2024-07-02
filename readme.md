# Short and Long Polling strategies example on python(FastAPI server)

## Project structure:
- FastAPI server which has 3 endpoints: 
  - for supporting short polling strategy
  - for supporting long polling strategy
  - for data updating for testing purposes
- short polling client
- long polling client

## How to run
- server
```console
python3 main.py
```
- short polling client
```console
python3 short_poll_client.py
```
- long polling client
```console
python3 long_poll_client.py
```

## docs (available after server start)
- http://localhost:8000/docs


## FLOW
- run server
- run one of the clients(or both)
- wait from 5 to 50 seconds(just to see difference)
- trigger POST endpoint to update data(you can do it via [swagger](http://localhost:8000/docs#/default/update_status_update_status_post) in docs or via postman)
- see the result

## Result explained
- for short polling strategy you will see several logs "Unexpected status code: 404" which mean that data has been trying to be received several times
- for long polling strategy you will not see such logs because it's been waiting all data during one and only request
- if you will wait 60 and more seconds you will see that both clients are ended by timeout
