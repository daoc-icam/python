# para usar Flask necesita haberlo instalado en su entorno previamente:
# pip install flask

from flask import Flask, request, session
from random import randint

app = Flask(__name__)

app.secret_key = 'MI_CLAVE_PARA_SESSION'

formulario = '''
    <p>Adivine un número entre 1 y 10</p>
    <form action='go'>
        Ingrese un número:<br/>
        <input type="text" name="num"/><br/>
        <input type="submit" value='Enviar'/>
    </form>
'''

@app.route('/')
def inicia():
    session['rndNum'] = randint(1,10)
    session['intento'] = 1
    return formulario

@app.route('/go')
def juega():
    try:
        num = int(request.args['num'])
        if num == session['rndNum']:
            respuesta = f'''
                <h2>Felicitaciones</h2>
                <h3>Adivinaste en {session['intento']} intentos</h3>
                <a href='/'>Reiniciar</a>
            '''
        else:
            session['intento'] += 1
            respuesta = formulario
    except:
        respuesta = "<h1>Debe ingresar un número !!!!!!!!</h1>" + formulario
    
    return respuesta

if __name__ == '__main__':
    app.run()