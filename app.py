# will be used to run locally via : // globally also if gunicorn not using
# flask run

from apps_backend import app

if __name__ == "__main__" :
    app.run(debug=True)
