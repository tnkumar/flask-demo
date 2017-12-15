This is a demo using flask as a web interface.

To use this demo you need the following:

- docker
- docker-compose

To install docker-compose, run the following:

sudo apt-get install python-all python-pip
sudo pip install docker-compose

To run this demo, run the following in the directory 
where this README.txt is located:

1. docker-compose build
2. docker-compose up -d

After this has finished, run the following in the web browser:

http://<your ip>:5000

You might have to open port on the amazon firewall since its running on port 5000.
