urbanmaps
=========

maps of urban things


Install
---------

From the root of the git repo

`cp urbanmaps/example.settings.py urbanmaps/settings.py`

Next, go get an api key from [CloudMade](http://cloudmade.com)

Then, edit urbanmaps/settings.py and insert the api key into CLOUDMADE_KEY="..."

Make sure you have django installed
`pip install django`

Now make the databases:
`python manage.py syncdb`

Finally, start up the webserver
`python manage.py runserver`
