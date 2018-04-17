# IS4302 Project: Income Insurance Use Case by Tut 4 Group 5
## Architecture
This follows *MVC* model

`app.models` is where we define the models for our database

`app.views` is where we serve html pages for the front end

`app.controller` is where we control the data flow i.e. what to show, what to store in the database

`app.blockchain` is where we call the blockchain rest server

## How to setup
### Setting up blockchain
- Upload `is4302proj.bna` to *composer-playground*
- Start the rest server using your desired port and **update `app.blockchain.__init__.py` with the correct URLs and port numbers**

### Setting up web app
- Clone this repo
- Install [Python 3](https://www.python.org/downloads/)
- Install [postgresql](https://www.postgresql.org/download/)
- Install all the dependencies. `pip install -r requirements.txt`
- Setup a postgresql database. Create a super user. Create a table called **'blockchain'**. Update the database address in `config.py`. If the file doesn't exist, copy `config.py.sample` and rename it to `config.py`
- Upgrade the database scheme. `python manage.py db upgrade`
- Run the app. `python run.py`

Any issues contact [here](mailto:max.kusnadi@gmail.com)
