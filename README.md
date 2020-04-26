* Copy the content from `.env-example` to `.env` and set the value.
* Run `docker-compose up -d`, it will pull postgresql and initialize a demo database.
* Create a virtual environment with python 3 ( I used Python version 3.8.2) and install all the packages with `pip install -r requirements.txt`.
* To create the tables from models run `flask db upgrade`.
* Run the app with `flask run`.