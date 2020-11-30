# moteur-de-recherche

# prerequisites : 
- nodeJS installed globally 
- python 3
- pip
- npm installed globally if not installed with nodeJS

# you should install all python dependencies

pip install -r requirements.txt --user

# within frontend directory - install vue dependencies

npm install

# to run vue server :

npm run serve

# within backend directory - to run flask server

python flask_server.py

# you can modify running port by modifying that file (flask_server.py)

app.run(port=port_number)

then modifify port number in axios request

