# Import de flask
# Encore un commentaire
## again comment
"""Super fichier avec des trucs dedans"""

from flask import Flask

app = Flask(__name__)
@app.route('/')
def index():
    return "Hello world !"

if __name__ == "__main__":
    app.run()
