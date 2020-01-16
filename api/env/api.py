import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True


# Create some test data for our catalog in the form of a list of dictionaries.
knjige = [
    {'id': 0,
     'naslov': 'A Fire Upon the Deep',
     'avtor': 'Vernor Vinge',
     'izdana': 1992},
    {'id': 1,
     'naslov': 'The Ones Who Walk Away From Omelas',
     'avtor': 'Ursula K. Le Guin',
     'izdana': 1973},
    {'id': 2,
     'naslov': 'Dhalgren',
     'avtor': 'Samuel R. Delany',
     'izdana': 1975}
]

#nova = '{"id" : 3, "naslov" : "The Silmarillion", "avtor" : "J. R. R. Tolkien", "izdaja" : 1977}'
@app.route('/', methods=['GET'])
def home():
    return 'Imamo knjige za sposodit!'

@app.route("/knjiga/<id>", methods=['GET'])
def vrni_knjigo(id):
    result = []
    id = int(id)
    for knjiga in knjige:
        if knjiga['id'] == id:
            result.append(knjiga)
    return jsonify(result)

# A route to return all of the available entries in our catalog.
@app.route('/knjige', methods=['GET'])
def vrni_vse():
    return jsonify(knjige)
    

# A route to return all of the available entries in our catalog.
@app.route('/novaKnjiga', methods=['POST'])
def dodaj_knjigo():
    id = request.json['id']
    naslov = request.json['naslov']
    avtor = request.json['avtor']
    izdana = request.json['izdana']
    novaKnjiga = {'id' : id, 'naslov' : naslov, 'avtor' : avtor, 'izdana' : izdana}
    knjige.append(novaKnjiga)
    return jsonify(novaKnjiga)
    
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=80)