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

izposoje = [
    {
        'idKnjige' : 0,
        'ime' : 'Gregor',
        'priimek' : 'Zadnik'
    },
    {
        'idKnjige' : 2,
        'ime' : 'Jure',
        'priimek' : 'Jesenšek'
    }
    ]

#novaKnjiga = '{"id" : 3, "naslov" : "The Silmarillion", "avtor" : "J. R. R. Tolkien", "izdaja" : 1977}'
#novaIzposoja = 
@app.route('/', methods=['GET'])
def home():
    return 'Imamo knjige za sposodit!'

# Najde knjigo z idjem id ter jo vrne
@app.route("/knjiga/<id>", methods=['GET'])
def vrni_knjigo(id):
    result = []
    id = int(id)
    for knjiga in knjige:
        if knjiga['id'] == id:
            result.append(knjiga)
    return jsonify(result)

# Najde izposoje za iporabnika z imenom ime    
@app.route("/izposoje/<ime>", methods=['GET'])
def vrni_izposoje_uporabnika(ime):
    result = []
    for izposoja in izposoje:
        if izposoja['ime'] == ime:
            result.append(izposoja)
    return jsonify(result)

# A route to return all of the available entries in our catalog.
@app.route('/knjige', methods=['GET'])
def vrni_knjige():
    return jsonify(knjige)
    
# Prikaze vse izposoje
@app.route('/izposoje', methods=['GET'])
def vrni_izposoje():
    return jsonify(izposoje)
    

# Doda novo knjigo
@app.route('/novaKnjiga', methods=['POST'])
def dodaj_knjigo():
    id = request.json['id']
    naslov = request.json['naslov']
    avtor = request.json['avtor']
    izdana = request.json['izdana']
    novaKnjiga = {'id' : id, 'naslov' : naslov, 'avtor' : avtor, 'izdana' : izdana}
    knjige.append(novaKnjiga)
    return jsonify(novaKnjiga)

# Naredi izposojo za podatke, ki jih je uporabnik vnesel, ce knjiga se ni izposojena
@app.route('/izposodiKnjigo', methods=['POST'])
def izposodi_knjigo():
    idKnjige = request.json['idKnjige']
    ime = request.json['ime']
    priimek = request.json['priimek']
    for izposoja in izposoje:
        if izposoja['idKnjige'] == idKnjige:
            return "Knjiga je ze izposojena!"
    novaIzposoja = {'idKnjige' : idKnjige, 'ime' : ime, 'priimek' : priimek}
    izposoje.append(novaIzposoja)
    return jsonify(novaIzposoja)
    
# Vrne knjigo z IDjem id
@app.route('/vrniKnjigo', methods=['POST'])
def vrni_izposojeno_knjigo():
    idKnjige = request.json['idKnjige']
    for izposoja in izposoje:
        if izposoja['idKnjige'] == idKnjige:
            izposoje.remove(izposoja)
            return "Knjiga uspesno vrnjena."
    return "Knjiga se ni izposojena."
    
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=80)