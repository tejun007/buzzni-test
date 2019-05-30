# Docker for server
FROM python:3.6.5-slim
MAINTAINER tejunlee007@gmail.com

# working directory
WORKDIR /server

# copy current directory to /server in docker container
ADD ./ /server

# Set PATHs
ENV PATH=$PATH:/server
ENV PYTHONPATH=$PYTHONPATH:/server

# execute everyone's favorite pip command, pip install -r
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# unblock port 5000 for the Flask app to run on
EXPOSE 5001

# execute the Flask app
CMD ["python", "run.py"]

