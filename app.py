from flask import Flask
import os
from flask_wtf.csrf import CSRFProtect


app = Flask(__name__)

csrf = CSRFProtect(app)

@app.route("/")
def pagina_inicial():
    return "Entrega Final"

@app.route('/bug')
def bad():                                                                                                                                        
    try:                                                                                                                                          
        raise TypeError()                                                                                                                         
    except TypeError as e:                                                                                                                        
        print(e)                                                                                                                      

if __name__ == '__main__':
    port = os.getenv('PORT')
    app.run('0.0.0.0', port=port)