
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

@app.route('/MatPlot2')
def MatPlot2():
    return render_template('matplot2.html')

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

@app.route("/MatPlotImage2",methods=['POST'])
def MatPlotImage2():
    import matplotlib.pyplot as plt
    from cStringIO import StringIO

    while True:
        try:
            PathCoords = request.form['PathCoords']
            break
        except ValueError:
            return render_template('error.html')

    import ast
    verts = ast.literal_eval(PathCoords)


    fig = plt.figure()
    ax = fig.add_subplot(111)

    xs, ys = zip(*verts)
    ax.plot(xs, ys, 'x--', lw=2, color='black', ms=10)

    for i in range(len(verts)):
        listTuple = list(verts[i])
        listTuple.insert(2, 'P'+str(i))
        ax.text(listTuple[0]-0.15,listTuple[1]+0.1,listTuple[2])

    ax.set_xlim(min([x[0] for x in verts])-0.5, max([x[0] for x in verts])+0.5)
    ax.set_ylim(min([x[1] for x in verts])-0.5, max([x[1] for x in verts])+0.5)

    io = StringIO()
    fig.savefig(io, format='png')
    data = io.getvalue().encode('base64')
    return render_template('matplotimage.html', ResultPNG = data)



@app.route("/Image")
def Image():
    import matplotlib.pyplot as plt
    from matplotlib.path import Path
    import matplotlib.patches as patches
    from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
    import StringIO

    verts = [
        (0., 0.),  # P0
        (0.2, 1.), # P1
        (1., 0.8), # P2
        (0.8, 0.), # P3
        ]

    codes = [Path.MOVETO,
             Path.CURVE4,
             Path.CURVE4,
             Path.CURVE4,
             ]

    path = Path(verts, codes)

    fig = plt.figure()
    ax = fig.add_subplot(111)
    patch = patches.PathPatch(path, facecolor='none', lw=2)
    ax.add_patch(patch)

    xs, ys = zip(*verts)
    ax.plot(xs, ys, 'x--', lw=2, color='black', ms=10)

    ax.text(-0.05, -0.05, 'P0')
    ax.text(0.15, 1.05, 'P1')
    ax.text(1.05, 0.85, 'P2')
    ax.text(0.85, -0.05, 'P3')

    ax.set_xlim(-0.1, 1.1)
    ax.set_ylim(-0.1, 1.1)

    canvas=FigureCanvas(fig)
    png_output = StringIO.StringIO()
    canvas.print_png(png_output)
    response=make_response(png_output.getvalue())
    response.headers['Content-Type'] = 'image/png'
    return response

if __name__ == "__main__":
    app.run()