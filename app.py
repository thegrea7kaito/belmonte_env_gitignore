from flask import Flask
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

app = Flask(__name__)

# Access variables from .env
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['DATABASE_URL'] = os.getenv('DATABASE_URL')

@app.route('/')
def home():
    return "Environment variables loaded successfully!"

if __name__ == '__main__':
    app.run(debug=True)
