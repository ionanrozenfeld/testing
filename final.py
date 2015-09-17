from flask import Flask, make_response, render_template,request, send_file
import pandas as pd
import numpy as np
import matplotlib as plt

from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import urllib2
import StringIO


app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template("my-form.html")

@app.route('/', methods=['POST'])
def image_png():    

    #ticker='goog'
    ticker = request.form['text']
    url = "https://www.quandl.com/api/v3/datasets/WIKI/"
    url = url+ticker+'.csv'
    response = urllib2.urlopen(url)
    df=pd.read_csv(response)
    
    #plt.figure()
    image=df[['Close','Adj. Close']].plot()
    fig=image.get_figure()
    canvas=FigureCanvas(fig)
    png_output = StringIO.StringIO()
    canvas.print_png(png_output)
    response=make_response(png_output.getvalue())
    response.headers['Content-Type'] = 'image/png'
    return response


if __name__ == "__main__":
    app.run(port=33507)