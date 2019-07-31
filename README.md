# flask
### How to setup
1. install virutal env or make sure you have virutal env installed on your machine
2. Install python3 or make sure you have python 3 on your machine
3. Run ```virtualenv -p `which python3` venv```
4. Run `pip install -r requirements.txt`
5. Start up the app using `gunicorn wsgi:app`
7. To run the tests run `python project.py test`