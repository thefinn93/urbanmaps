urbanmaps
=========

maps of urban things


Install
=========
cd urbanmaps
cp example.settings.py settings.py
# Go get an api key from http://cloudmade.com/
# edit settings.py and insert it into CLOUDFLARE_KEY="..."
pip install django
cd ..
python manage.py runserver
