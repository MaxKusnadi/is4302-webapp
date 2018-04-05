# IS4302
## Architecture
This follows *MVC* model

`app.models` is where we define the models for our database

`app.views` is where we serve html pages for the front end

`app.controller` is where we control the data flow i.e. what to show, what to store in the database

be`app.blockchain` is where we call the blockchain rest server

## How to setup
- Clone this
- Using python 3, install all the dependencies. `pip install -r requirements.txt`
- Setup a postgresql database. Create a super user. Create a table called **'blockchain'**. Update the database address in `config.py`
- Run `run.py` i.e. `python run.py`
