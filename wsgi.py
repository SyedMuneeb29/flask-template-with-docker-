# will be used for global running
# gunicorn --bind 0.0.0.0:8000 wsgi:app

from apps_backend import app

if __name__ == "__main__" :
    app.run()
