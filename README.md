selfieclub-testing
==================

High level integration/functional testing of selfieclub &amp; VolleyBackend REST APIs.

Here's the basic layout of the project:

“client.py” file creates a json object of the github user.

“test_user" file also contains a json object.

“test_client.py” file checks if the name field in the json object from “client.py” matches the name field in the json object from “test_user”. In this case the name field = “Test User”.


To Execute the Program:
  -type “nosetests” in the project directory.
  This command will search for the “test_client.py” file and execute the program from there.

