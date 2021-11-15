import os

def flaskEnvSetup():
    os.environ["FLASK_APP"] = "aWaifu/web"
    os.environ["FLASK_ENV"] = "production"
    os.system("flask run")