
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template, request, make_response


app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/InpBruun')
def InpBruun():
    return render_template('inpbruun.html')

@app.route('/CalcBruun',methods=['POST'])
def CalcBruun():
    while True:
        try:
            _SLR = float(request.form['SeaLevelRise'])
            _DOC = float(request.form['DepthofClosure'])
            _BBH = float(request.form['BermHeight'])
            _EAZ = float(request.form['Extent'])
            break
        except ValueError:
            return render_template('error.html')

    return render_template('calcbruun.html', CalcResult=((_SLR*_EAZ)/(_DOC + _BBH)))

@app.route('/MatPlot')
def MatPlot():
    return render_template('matplot.html')

@app.route("/MatPlotImage",methods=['POST'])
def MatPlotImage():
    import matplotlib
    matplotlib.use('Agg')

    import matplotlib.pyplot as plt
    import numpy as np
    from cStringIO import StringIO

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    xs = np.linspace(-10, 10, 1000)
    ax.plot(xs, np.sin(xs), label='sin(x)')
    ax.plot(xs, np.cos(xs), label='cos(x)')
    ax.legend()


    io = StringIO()
    fig.savefig(io, format='png')
    data = io.getvalue().encode('base64')

    return render_template('matplotimage.html', ResultPNG = data)


@app.route("/Image")
def Image():
    import datetime
    import StringIO
    import random

    from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
    from matplotlib.figure import Figure
    from matplotlib.dates import DateFormatter

    fig=Figure()
    ax=fig.add_subplot(111)
    x=[]
    y=[]
    now=datetime.datetime.now()
    delta=datetime.timedelta(days=1)
    for i in range(10):
        x.append(now)
        now+=delta
        y.append(random.randint(0, 1000))
    ax.plot_date(x, y, '-')
    ax.xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))
    fig.autofmt_xdate()
    canvas=FigureCanvas(fig)
    png_output = StringIO.StringIO()
    canvas.print_png(png_output)
    response=make_response(png_output.getvalue())
    response.headers['Content-Type'] = 'image/png'
    return response

if __name__ == "__main__":
    app.run()