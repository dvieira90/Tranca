#!/usr/bin/python3
from flask import Flask, request, jsonify, render_template, url_for, redirect, flash
import os, json

app = Flask(__name__)
app.secret_key = 'alura'

a = os.listdir('db')
lista_portas = []
code = {}

for b in a:
    with open('db/'+b, 'r') as arq:
        f = arq.read()
        lista_portas.append(json.loads(f))

for i in lista_portas:
    code[i['porta']] = 'none'

@app.route('/', methods=['GET',])
def urls():
    data = {"get_usuarios":"/v1/users", "get_code":"/v1/code"}
    return jsonify(data)

@app.route('/v1/users', methods=['GET',])
def get_usuarios():
    obj = '{"none":"none"}'
    porta = request.args.get('porta')
    for p in lista_portas:
        if porta == p['porta']:
            obj = json.dumps(p)
    code[porta] = 'none'
    return obj, 202

@app.route('/v1/code', methods=['GET',])
def get_code():
    porta = request.args.get('porta')
    data = {'code':code[porta]}
    obj = jsonify(data)
    print(code[porta])
    return obj, 202

@app.route('/v1/comando', methods=['GET',])
def comando():
    porta = request.args.get('porta')
    comando = request.args.get('comando')
    code[porta] = comando
    flash(' Comando Executado')
    return redirect(url_for('home'))

@app.route('/home', methods=['GET',])
def home():
        return render_template('home.html', titulo='Portaria')

if __name__ == '__main__':
    app.run(debug=True, host='10.0.1.196')