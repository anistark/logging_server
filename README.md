# Simple Message Based Central Logging System in python


For starters, used mysql for db. But can be replaced with ElasticSearch as to enhance performance on scaling.


## Setup

 - Clone the repo
 - install dependecies 
 ```
 pip install -r requirements.txt
 ```
 - Setup Flask env
 ```
 export FLASK_APP=server.py
 ```
 - Create config file
 ```
 cp config_example.py config.py
 ```


## Configuration

1. Add all necessary config data in config.py 

2. Create a database with the provided name and table accordingly.


## Execution

1. Run the
```
python zmqclient.py
```
on the client systems, i.e. various different machines where the logs are scattered

2. Run the 
```
python zmqserver.py
```
on our central server where we want to centralise the logging system

3. (Optional) To debug run : 
   ```
   export FLASK_DEBUG=1
    ```

4. Run the Flask web server
```
flask run
```

5. Open **localhost:5000** on local system and view it as a table

6. To view statistics, go to **localhost:5000/stats**


