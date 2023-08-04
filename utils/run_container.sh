#!/bin/bash

# Define variables
IMAGE_NAME="flask-app"
CONTAINER_NAME="my_flask_container"
build_and_prune_image() {
    # Build the image with no cache
    docker image build --no-cache=true -t flask-app -f docker/Dockerfile .
    # Prune dangling images
    docker image prune --filter "dangling=true"
}

# Build the container from the image
# # Check if the container is running
if docker images | grep -q $IMAGE_NAME; then
    echo "Docker image already built"
    read -p "Do you want to update it? (y/N): " response
    # Convert the user's response to lowercase (to handle both 'Y' and 'y')
    response=${response,,}
    # Check the user's response
    if [[ "$response" == "y" ]]; then
        build_and_prune_image
        echo "Image $IMAGE_NAME updated successfully."
    else
        echo "Image $IMAGE_NAME not updated. Exiting..."
    fi
else
    echo "Failed to find image, building starting..."
    build_and_prune_image
fi
#docker image build --no-cache=true -t flask-app -f docker/Dockerfile . docker image prune --filter "dangling=true"


# Run the container
docker run -d -p 5000:5000 --name $CONTAINER_NAME $IMAGE_NAME

# Check if the container is running
if docker ps | grep -q $CONTAINER_NAME; then
    echo "Container is running!"
else
    echo "Failed to start the container."
    docker rm --force $CONTAINER_NAME
fi



# Wait for 3 seconds before testing
echo "Waiting for 3 seconds before testing..."
sleep 3

# Check if the container is running
if docker container inspect $CONTAINER_NAME &> /dev/null; then
    # Make an HTTP request to the endpoint and check the response status
    response_status=$(curl -s -o /dev/null -w "%{http_code}" http://localhost:5000/)

    if [ "$response_status" -eq 200 ]; then
        echo "Container '$CONTAINER_NAME' is running and the endpoint returned a response status of 200."
    else
        echo "Container '$CONTAINER_NAME' is running, but the endpoint returned a response status of $response_status."
    fi
else
    echo "Container '$CONTAINER_NAME' is not running. Start the container before testing."
fi

# Test the container by making a sample request (adjust the endpoint as per your app)
# SAMPLE_ENDPOINT="http://localhost:5000/"
# RESPONSE=$(curl -s $SAMPLE_ENDPOINT)

# docker logs $CONTAINER_NAME

# Check if the response is correct
# if [ "$RESPONSE" == "Hello, World!" ]; then
#     echo "Container is working correctly."
# else
#     echo "Container is not responding as expected."
# fi
# docker rm --force $CONTAINER_NAME
