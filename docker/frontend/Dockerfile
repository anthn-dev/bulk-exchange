# Use an official Node.js runtime as a base image
FROM node:21.2.0-alpine

# Set the working directory in the container
ARG APP_HOME=/home/app

WORKDIR ${APP_HOME}

# Copy package.json and package-lock.json to the working directory
COPY frontend/package*.json ./

# Install app dependencies
RUN npm install --legacy-peer-deps

# Copy the entire application to the working directory
COPY . .

# Build the React app
WORKDIR /home/app/frontend/

RUN npm install -g serve

RUN npm run build

# Expose the port that the app will run on
EXPOSE 3000

# Define the command to run the application
CMD ["npm", "run", "deploy"]
