# Use Python 3.9 base image
FROM python:3.9

# Set the working directory in the container
WORKDIR .

RUN mkdir /CTF

# Copy the local project files into the container
COPY . /CTF

# Install project dependencies
RUN pip install -e /CTF

# Set up the database and configurations
RUN r8 sql init --origin http://localhost:8000 && \
    r8 settings set scoring true && \
    r8 settings set register true && \
    r8 sql file /CTF/config.sql

# Expose the port the app runs on
EXPOSE 8000 8201 8202 8205

# Start the application
CMD ["r8", "run"]

