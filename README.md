# PPA-1 && PPA-2
 Intro to Unit Testing & T/BDD using Python3 and pytest

 For the full project breakdown, see the wiki. https://github.com/kbass40/PPA-1/wiki

# Windows Installation for Windows 10
1. First, make sure to install Python3 on your Windows machine via the Windows download
    - Python for Windows: https://www.python.org/downloads/windows/
2. Next make sure to install the dependent modules (pytest and coverage.py)
    - Simply type the following command 'pip install -r requirements.txt'. This will have pip install all the dependent modules for our project.
3. For convience, a batch files are included to run the project via the terminal
    - Navigate to the project directory and run the following batch files:
        - up : to start the database in a docker container
    - Then you can run either / both the terminal application or the flask app:
        - run : to start the terminal application
        - flask : to start the flask application
    - NOTE: The database needs to be active to ensure these run properly.
4. For test suites, simply type 'pytest' to execute all tests.



# Ubuntu installation instruciotns:

sudo apt-get install python3

sudo apt-get install python3-pip

sudo apt-get docker-compose

pip3 install -U pytest

pip3 install -U pytest

pip3 install mysql-connector-python

pip3 install pytest_mock

pip3 install flask

pip3 install connexion

pip3 install flask_wtf

pip3 install json2html

# How to run on Linux: 
 
 sudo service docker start
 
 docker-compose up
 
 python3 ppa-1.py 

# or for test suite: 
 
 sudo service docker start
 
 docker-compose up
 
 python3 -m pytest 


# How to run the Flask Application
 
 sudo service docker start
 
 docker-compose up
 
 python3 flask_app.py
 
 then in a browser navigate to localhost:5000

 # API Routing
 - /get-bmi : Returns a json object of all the bmi queries stored in the database.
 - /post-bmi : Uses in-query parameters to try an execute a bmi request. If successful will return 201, if failure it will return a 404. 

 - /get-email : Returns a json object of all the email verification queries stored in the database.
 - /post-email : Uses in-query parameters to try an execute a email verification request. If successful will return 201 and the result, if failure it will return a 404. 
