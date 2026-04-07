#EJERCICIO 5 Gestor de noticias con multiples fuentes RSS
#En este ejercicio, vamos a crear una aplicación Flask que muestre las últimas noticias de varias
from flask import Flask, render_template
import feedparser

app = Flask(__name__)


FUENTES = [
    {
        "id": "BBC",
        "nombre": "BBC News",
        "url": "http://feeds.bbci.co.uk/news/rss.xml",
    },
    {
        "id": "CNN",
        "nombre": "CNN News",
        "url": "http://rss.cnn.com/rss/edition.rss",
    },
    {
        "id": "elpais",
        "nombre": "El Pais",
        "url": "https://feeds.elpais.com/mrss-s/pages/ep/site/elpais.com/portada",
    }
]

@app.route("/")
def index():
    return render_template('index.html', fuentes=FUENTES)

@app.route('/noticias/<fuente_id>')
def mostrar_noticias(fuente_id):
    fuente = next((f for f in FUENTES if f['id'] == fuente_id), None)           
    feed = feedparser.parse(fuente['url'])
    noticias = feed.entries[:5]  # Obtener las primeras 5 noticias
    return render_template('noticias.html', fuente=fuente, noticias=noticias)


if __name__ == "__main__":
    app.run(debug=True)
