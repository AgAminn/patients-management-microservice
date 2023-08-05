#!/bin/bash
echo starting test

docker run -it --name pep8test -v /src/app.py:/code eeacms/pep8:latest

echo done - logs below
docker logs pep8test

echo removing container
docker rm pep8test
