from flask import Flask, render_template, url_for
import pandas as pd
import matplotlib.pyplot as plt
import os

app = Flask(__name__)

# Calea către directorul curent (directoriul în care se află app.py)
current_dir = os.path.dirname(os.path.abspath(__file__))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/plot_all')
def plot_all():
    data_path = os.path.join(current_dir, 'data.csv')
    date = pd.read_csv(data_path)
    plot = date.plot()

    # TITLU
    plt.title('Toate valorile', pad=20)  

    img_path = os.path.join(current_dir, 'static', 'plot_all.png')
    plot.figure.savefig(img_path)
    plt.close(plot.figure)
    return f'<a href="{url_for("plot_all")}" target="_blank"><img src="{url_for("static", filename="plot_all.png")}" alt="Plot All"></a>'

@app.route('/plot_first/<int:X>')
def plot_first(X):
    data_path = os.path.join(current_dir, 'data.csv')
    date = pd.read_csv(data_path)
    plot = date.iloc[:X, :].plot()

    # TITLU
    plt.title('Al doilea grafic', pad=20) 

    img_path = os.path.join(current_dir, 'static', 'plot_first.png')
    plot.figure.savefig(img_path)
    plt.close(plot.figure)
    return f'<a href="{url_for("plot_first", X=X)}" target="_blank"><img src="{url_for("static", filename="plot_first.png")}" alt="Plot First"></a>'

@app.route('/plot_last/<int:Y>')
def plot_last(Y):
    data_path = os.path.join(current_dir, 'data.csv')
    date = pd.read_csv(data_path)
    columns_to_plot = ['Durata', 'Puls']
    plot = date[columns_to_plot].tail(Y).plot()

    # TITLU
    plt.title('Al treilea grafic', pad=20)  

    img_path = os.path.join(current_dir, 'static', 'plot_last.png')
    plot.figure.savefig(img_path)
    plt.close(plot.figure)
    return f'<a href="{url_for("plot_last", Y=Y)}" target="_blank"><img src="{url_for("static", filename="plot_last.png")}" alt="Plot Last"></a>'

if __name__ == '__main__':
    app.run(debug=True)
