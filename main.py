# Import de flask
# Encore un commentaire
## again comment
"""Super fichier avec des trucs dedans"""

from flask import Flask
#comment
app = Flask(__name__)
#comment
@app.route('/')
#comment
def index():
    return "Hello world !" #comment
#comment
if __name__ == "__main__":
    #comment
    app.run()
