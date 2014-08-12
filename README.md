selfieclub-testing
==================

High level integration/functional testing of selfieclub &amp; VolleyBackend REST APIs.

This is an example followed from http://seminar.io/2013/09/27/testing-your-rest-client-in-python/:
The purpose of the example is to learn how to test a rest api using python's unittest library.

Here's the basic layout of the project:

“client.py” file creates a json object of the github user. “test_user" file also contains a json object.

“test_client.py” file checks if the value of key "name" in the json object from “client.py” matches the value of key "name" in the json object from “test_user”. In this case the value of key "name" = “Test User” in both json objects.


To Execute the Program:
  -type “nosetests” in the project directory.
  This command will search for the “test_client.py” file and execute the program from there.
  If there are no errors, the output should looking something like this: 
  
  .
  ----------------------------------------------------------------------
  Ran 1 test in 0.062s

  OK
