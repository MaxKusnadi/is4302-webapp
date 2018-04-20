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
- Create an instance of each participant: Customer, Insurance Company, Custodian Bank, Regulator.
- Issue an identity to each of the instance.
- There would be a total of 4 rest servers such as:
- ./start_rest_server.sh -i 1 -p 3001 -c cust1@is4302proj (Customer)
- ./start_rest_server.sh -i 2 -p 3002 -c comp1@is4302proj (InsuranceCompany)
- ./start_rest_server.sh -i 3 -p 3003 -c custo1@is4302proj (CustodianBank)
- ./start_rest_server.sh -i 4 -p 3004 -c reg1@is4302proj (Regulator)
- Start the rest server using your desired port and **update `app.blockchain.__init__.py` with the correct URLs and port numbers**

### Setting up web app
- Clone this repo
- Install [Python 3](https://www.python.org/downloads/)
- Install [postgresql](https://www.postgresql.org/download/)
- Install all the dependencies. `pip install -r requirements.txt`
- Setup a postgresql database. Create a super user. Create a table called **'blockchain'**. Update the database address in `config.py`. If the file doesn't exist, copy `config.py.sample` and rename it to `config.py`
- Upgrade the database scheme. `python manage.py db upgrade`
- Run the app. `python run.py`

### Creating accounts
- Go to `localhost:8000/admin`
- Fill in username, password and role
- If everything works, you will be directed to login page
- If it doesn't, check whether you have set up your database correctly or whether the composer rest server runs properly. Check out the log in the terminal for more info

### Running test cases
- Go to the root folder
- Run `. start_test.sh`
- It will show you the test case results as well as the code coverage
- The test cases are written under `test_cases` folder. Do take note that this web app is not heavily tested due to time constraint

Any issues contact [here](mailto:max.kusnadi@gmail.com)
