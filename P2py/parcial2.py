from flask import Flask, url_for, request, redirect
from jinja2 import Template, Environment, FileSystemLoader
File_loader = FileSystemLoader("carp")
env = Environment(loader=File_loader)
app = Flask(__name__)
def UpDown(palabra):
    for i in range(len(palabra)):
        if((i % 2) != 0):
            palabra[i].upper()
        else:
            palabra[i].lower()
    return palabra
def Naive(palabra):
    palabra.lower()
    for i in range(5):
        for y in range(len(palabra)):
            if(i == 0):
                y = palabra.find("a", y)
                if( y != 1):
                    palabra[y] = "@"
                    y = y + 1 
            if(i == 1):
                y = palabra.find("e", y)
                if( y != 1):
                    palabra[y] = "3"
                    y = y + 1
            if(i == 2):
                y = palabra.find("i", y)
                if( y != 1):
                    palabra[y] = "!"
                    y = y + 1
            if(i==3):
                y = palabra.find("o", y)
                if( y != 1):
                    palabra[y] = "0"
                    y = y + 1
            if(i==4):
                y = palabra.find("u", y)
                if( y != 1):
                    palabra[y] = ")"
                    y = y + 1
    return palabra   
def vowel(palabra):
    palabra.lower()
    count = 0
    for y in range(len(palabra)):
        if(palabra[y] == "a" or palabra[y] == "e" or palabra[y] == "i" or palabra[y] == "o" or palabra[y] == "u"):
            count = count + 1
    return count
def cons(palabra):
    palabra.lower()
    count = 0
    for y in range(len(palabra)):
        if(palabra[y] != "a" or palabra[y] != "e" or palabra[y] != "i" or palabra[y] != "o" or palabra[y] != "u"):
            count = count + 1
    return count
listado = []
@app.route('/hand', methods=["GET", "POST"])
def hand():  
    if request.method == 'POST':
        han = request.form['han']
        listado.append(han[::-1])
        listado.append(len(han))
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