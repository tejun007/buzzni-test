# Docker for client using regular flask and vuejs
FROM python:3.6.5-slim
MAINTAINER tejunlee007@gmail.com

# set the working directory in the container to /client
WORKDIR /client

# add the current directory to the container as /client
ADD ./ /client

# Set PATHs
ENV PATH=$PATH:/client
ENV PYTHONPATH=$PYTHONPATH:/client

# execute everyone's favorite pip command, pip install -r
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# unblock port 5000 for the Flask app to run on
EXPOSE 5000

# execute the Flask app
CMD ["python", "run.py"]


