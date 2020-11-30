# moteur-de-recherche

# prerequisites : 
- nodeJS installed globally 
- python 3
- pip
- npm installed globally if not installed with nodeJS
- Access-Control-Allow-Origin installed as extension on Google Chrome and activated

All the following commands should be run within a terminal

# install all python dependencies by running

pip install -r requirements.txt --user

(if some packages are requisite, please install)

# within frontend directory - install vue dependencies

npm install

# to run vue server (frontend)

npm run serve

then go on the link showed on the terminal

# within the root directory - to run flask server (backend)

python .\backend\flask_server.py

# you can modify running port by modifying that file (flask_server.py)

app.run(port=port_number)

then modifify port number in axios request port in Similarities.vue within frontend folder

