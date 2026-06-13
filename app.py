import os
from flask import Flask
from dotenv import load_dotenv
from controllers.auth_bp import auth_bp

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")

app.register_blueprint(auth_bp)

if __name__ == "__main__":
    app.run(debug=True) 