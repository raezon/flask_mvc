#!/bin/bash

# Exit script on any error
set -e

# Define colors for output (optional)
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Check if docker-compose.yml exists
if [ ! -f "docker-compose.yml" ]; then
    echo -e "${RED}Error: docker-compose.yml not found in the current directory.${NC}"
    exit 1
fi

echo -e "${GREEN}Building Docker images...${NC}"
docker-compose build

echo -e "${GREEN}Starting Docker containers...${NC}"
docker-compose up -d

echo -e "${GREEN}Docker containers are running!${NC}"

# List running containers
docker ps

# Show additional info
echo -e "\n${GREEN}Access your services:${NC}"
echo -e "  Flask App:     http://localhost:8000"
echo -e "  phpMyAdmin:    http://localhost:8070"

# End of script
