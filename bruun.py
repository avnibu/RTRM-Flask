
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template, request


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

if __name__ == "__main__":
    app.run()