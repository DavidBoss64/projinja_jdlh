##EJERCICIO 4: RSS FEED
#En este ejercicio, vamos a crear una aplicación Flask que muestre las últimas noticias de un feed
from flask import Flask, render_template, request, url_for, redirect
import feedparser

app= Flask(__name__)

@app.route('/')
def index():
    url = "http://feeds.bbci.co.uk/news/rss.xml"
    feed = feedparser.parse(url)
    noticias = feed.entries[:5]  # Obtener las primeras 5 noticias
    return render_template('index.html', url=url, noticias=noticias)

if __name__ == '__main__':
    app.run(debug=True)
