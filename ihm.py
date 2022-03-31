import globals
import os
import sys
import shutil
import plotly.graph_objects as go
from plotly.subplots import make_subplots

path = os.path.dirname(__file__)[:os.path.dirname(__file__).rfind('\\')]
sys.path.append(path)
try:
    shutil.copy(path+"\\candle_sample.txt", "candle_sample.txt")
except:
    print("Fichier déjà copié")
globals.affichage = True
#print(sys.path)
import main_simple

for i in range(6):
    plot1 = go.Candlestick(x=globals.data[i][4], name="Chandelles", open=globals.data[i][0], high=globals.data[i][2], low=globals.data[i][3], close=globals.data[i][1])
    plot2 = go.Scatter(x=globals.data[i][4], y=globals.argent, name='Notre argent', marker=dict(color='rgb(34,163,192)'))
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    fig.add_trace(plot1)
    fig.add_trace(plot2, secondary_y=True)
    fig.update_layout(title=f"{globals.symboles[i]}'s adjusted stock price", yaxis_title="Prix ($)", xaxis_title="Temps")
    fig.show()

print("""Nous nous sommes inspirés de : https://towardsdatascience.com/the-simplest-way-to-create-an-interactive-candlestick-chart-in-python-ee9c1cde50d8
Par ailleurs Geoffroy nous a aidé pour les fichiers de variables ultra globales!""")