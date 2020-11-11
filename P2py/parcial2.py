from flask import Flask, url_for, request, redirect
from jinja2 import Template, Environment, FileSystemLoader
File_loader = FileSystemLoader("carp")
env = Environment(loader=File_loader)
app = Flask(__name__)
def UpDown(palabra):
    nuevapal = ""
    for i in range(len(palabra)):
        letra = palabra[i]
        if( i % 2 == 0):
            nuevapal = nuevapal + letra.upper()
        else:
            nuevapal = nuevapal + letra.lower()
    
    return nuevapal
def Naive(palabra):
    palabra = palabra.lower()
    palabra = palabra.replace("a", "@").replace("e", "3").replace("i", "!").replace("o", "0").replace("u", ")")
    return palabra
     
def vowel(palabra):
    palabra = palabra.lower()
    count = 0
    for y in range(len(palabra)):
        if(palabra[y] == "a" or palabra[y] == "e" or palabra[y] == "i" or palabra[y] == "o" or palabra[y] == "u"):
            count = count + 1
    return count
def cons(palabra):
    palabra = palabra.lower()
    palabra = palabra.replace(" ", "")
    count = 0
    for y in range(len(palabra)):
        if(palabra[y] == "a" or palabra[y] == "e" or palabra[y] == "i" or palabra[y] == "o" or palabra[y] == "u" or palabra[y] == "-" or palabra[y] == "."):
            pass
        else:
            count = count + 1
    return count
listado = []
@app.route('/hand', methods=["GET", "POST"])
def hand():  
    listado[:] = []
    if request.method == 'POST':
        han = request.form['han']
        listado.append(han)
        listado.append(han[::-1])
        listado.append(len(han.replace(" ", "")))
        listado.append(vowel(han))
        listado.append(cons(han))
        listado.append(UpDown(han))
        listado.append(Naive(han))
        listado.append(han.lower())
        listado.append(han.upper())
        return redirect(url_for('index'))
    template = env.get_template('hand.html')
    return template.render()
@app.route('/')
def index():
    template = env.get_template('index.html')
    return template.render(lista=listado)
#cuando sale error, en el handler, solo borre el /han que sale arriba y dejelo /. Y si funciona solo no lo manda desde el boton
# no se porque

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)