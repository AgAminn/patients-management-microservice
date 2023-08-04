#!/bin/bash

# Set the variable for the Jenkins home directory
jenkins_home="jenkins_home"

# Execute the docker run command with the variable
docker run -d -p 8080:8080 -p 50000:50000 -v "$jenkins_home":/var/jenkins_home \
         --name jenkins_server jenkins/jenkins:lts
