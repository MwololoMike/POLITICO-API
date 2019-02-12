# POLITICO-API
### Endpoints

|   ENDPOINT  | METHOD | FUNCTIONALITY |
|:---:|:---:|:---:|
| /parties                |  GET     |  Gets the list of all Parties  |
| /offices                |  GET     |  Gets the list of all offices |
| /offices/<office_id>    |  GET     |  Gets a specific office with the specified id |
| /parties/<party_id>     |  GET     |  Gets a specific party with the specified id |
| /offices                |  POST    |  Adds an office to the office list  |
| /parties                |  POST    |  Adds a party to the party list |
| /parties/<party_id>/name|  PATCH   |  Updates the name of a specific party  |
| /parties/<party_id>     |  DELETE  |  Deletes a specific party




## Testing the APP 
1. Activate the environment;
   `. venv/bin/activate`
   
2. Run the app on flask;<br>
   `export FLASK_ENV=development`<br>
   `export FLASK_DEBUG=1`<br>
   `export FLASK_APP=run.py`<br>
   `flask run`
   
 3. Testing on postman;<br>
    * Copy the link produced in your local terminal and open it on postman or a similar application.
    * Using the above specified endpoints, test each function by selecting a method and the endpoint associated to the task you wish to perform