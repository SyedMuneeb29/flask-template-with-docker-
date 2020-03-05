# will be used for global running when deployed on digital ocean 
# gunicorn --bind 0.0.0.0:8000 wsgi:app

from apps_backend import app

if __name__ == "__main__" :
    app.run()
