#!/bin/bash

# Number of containers to create
N=100  # Pass the number of containers as the first argument

# Network name
NETWORK_NAME="ddos_network"

# Base IP address for the network (adjust based on your subnet)
BASE_IP="192.168.100."

# Docker image name
IMAGE_NAME="http_flood_test"

# Start containers
for i in $(seq 1 "$N"); do
    CONTAINER_NAME="ddos_bot_$i"
    CONTAINER_IP="${BASE_IP}$((i + 1))" # Ensure the IP range starts after the gateway

    echo "Starting container: $CONTAINER_NAME with IP: $CONTAINER_IP"

    docker run -d \
        --name "$CONTAINER_NAME" \
        --net "$NETWORK_NAME" \
        --ip "$CONTAINER_IP" \
        "$IMAGE_NAME"
done

echo "Started $N containers in the $NETWORK_NAME network."
