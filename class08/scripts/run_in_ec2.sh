sudo su
sudo apt-get update
sudo apt install -y git docker.io docker-compose
git clone https://github.com/lvgalvao/api-scheduler-python-rds.git /app
cd /app
sudo docker build -t api-schedule-app .
sudo docker run -d \
--name api-schedule-app-container \
-e DB_HOST=<endereco-rds> \
-e DB_USER=<usuario> \
-e DB_PASS=<senha> \
-e DB_NAME=<nome-do-banco> \
api-schedule-app