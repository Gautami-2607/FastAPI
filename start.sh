pip install --upgrade pip
pip install -r requirements.txt
uvicorn main:app --reload
# uvicorn (web server): Starts our application
# Reload it to update modified code

docker-compose -f Docker-compose.yml build
docker-compose -f Docker-compose.yml up