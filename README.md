========================

This is the development repository for the Hell World Kind of Django Application


Standalone Testing
------------------

You can run the tests by running the following command

        $ ./run_tests


Development and HTTP Server
--------------------------------

This repository comes with a simple development and test server so that is possible to develop
and test in an isolated environment. In order to use the test server, it is recommended that you
make a new dedicated Python virtual-environment:

```
virtualenv hell_world_env (just do this once)

source hell_world_env/bin/activate

pip install -r requirements.txt

./manage.py syncdb
./manage.py migrate

./manage.py runserver (run the test server)
```

API END POINT
-------------

You can view all the list of the users info by hitting the url

```
$BASEURL/helloworld/v1/users_info
```