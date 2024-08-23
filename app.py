# -*- coding: utf-8 -*-

from flask import Flask, render_template_string
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

@app.route('/')
def plot():

    partidas = ['Partida 1', 'Partida 2', 'Partida 3', 'Partida 4', 'Partida 5']
    expulsões = [2, 1, 3, 0, 4]

    plt.figure(figsize=(10, 6))
    plt.bar(partidas, expulsões, color='red')
    plt.xlabel('Partidas')
    plt.ylabel('Número de Expulsões')
    plt.title('Número de Expulsões por Partida no Campeonato Italiano')


    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()

 
    return render_template_string('<img src="data:image/png;base64,{{ plot_url }}"/>', plot_url=plot_url)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
