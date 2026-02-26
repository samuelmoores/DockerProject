# Use the latest Alpine Linux as the base image.
# Alpine is a minimal Linux distro (~5MB), ideal for keeping container images small.
FROM alpine:latest

# Update Alpine's package index so we can install up-to-date packages
RUN apk update
# Install Python 3 using Alpine's package manager (apk)
RUN apk add python3

# Set the working directory inside the container.
# All subsequent commands (COPY, CMD, etc.) will run relative to this path.
# The directory is created automatically if it doesn't exist.
WORKDIR /usr/app/src

# Copy app.py from the local build context (the folder docker-compose points to)
# into the current WORKDIR inside the container
COPY app.py ./

# The default command to run when the container starts.
# Uses exec form (JSON array) rather than shell form, which is best practice
# as it ensures the process receives OS signals like SIGTERM correctly.
CMD ["python3", "./app.py"]