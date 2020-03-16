# Verðum að importa session
from flask import Flask, render_template, session, request
app = Flask(__name__)


app.config['SECRET_KEY'] = 'Leyno'

vorur = [[0,"Baked beans",399,"bakedbeans.jpg"],[1,"Black beans",400,"blackbeans.png"],[2,"Green beans",401,"greenbeans.png"],[3,"White beans",402,"whitebeans.png"]]


@app.route('/')
def index():
    vara = []
    if 'karfa' in session:
        vara = session['karfa']

    fjoldi = len(vara)
    return render_template("index.html",vorur=vorur, karfa=karfa,fjoldi=fjoldi)


# Eyðum session
@app.route('/off')
def sessionoff():
    if 'karfa' in session:
        session.pop('karfa', None)
        return '<h3>Karfa deleted</h3><h3><a href="/">Home</a></h3>'
    else:
        return '<h3>Session was not set</h3><h3><a href="/">Home</a></h3>'

@app.route('/deletus/<int:id>')
def deletus(id):
    heildarverd = 0
    vara = []
    if karfa in session:
        session.pop['karfa', id]
        vara = session['karfa']
        for i in vara:
            heildarverd += vorur[i][2]

    fjoldi = len(vara)
    return render_template("karfa.html",fjoldi=fjoldi,vara=vara,vorur=vorur,heildarverd=heildarverd)

@app.route('/karfa')
def karfa():
    heildarverd = 0
    vara = []
    if 'karfa' in session:
        vara = session['karfa']
        for i in vara:
            heildarverd += vorur[i][2]

    fjoldi = len(vara)

    return render_template("karfa.html",fjoldi=fjoldi,vara=vara,vorur=vorur,heildarverd=heildarverd)

@app.route('/vara/<int:id>')
def vara(id):
    vara = []
    fjoldi = 0
    if 'karfa' in session:
        vara = session['karfa']
        vara.append(id)
        session['karfa'] = vara
        fjoldi = len(vara)
    else:
        vara.append(id)
        session['karfa'] = vara

    return render_template("index.html",vorur=vorur,fjoldi=fjoldi)


if __name__ == "__main__":
	app.run(debug=True)
