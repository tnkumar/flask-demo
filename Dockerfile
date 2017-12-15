from ubuntu

run apt-get update && apt-get -y dist-upgrade && \
    apt-get install -y python python-pip && \
    pip install -U pip
add . /app
workdir /app
run pip install -r requirements.txt
