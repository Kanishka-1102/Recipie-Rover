from flask import Flask, jsonify
import nltk
from app import app  # Import your Flask app

# Initialize Flask app
app = Flask(__name__)

# Define some example routes
@app.route("/")
def home():
    return jsonify(message="Hello from Vercel!")

if __name__ == "__main__":
    app.run(debug=True)
