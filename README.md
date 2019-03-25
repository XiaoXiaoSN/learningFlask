# meow

## Run
```
pip install -e .
cp config.py.default app/config.py
export FLASK_APP=app
export FLASK_ENV=development
flask run
```

Or on Windows CMD
```
pip install -e .
copy config.py.default app/config.py
set FLASK_APP=app
set FLASK_ENV=development
flask run
```
