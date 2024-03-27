from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/telecaster')
def telecaster():
    return render_template('telecaster.html')

@app.route('/les-paul')
def les_paul():
    return render_template('les_paul.html')

@app.route('/stratocaster')
def stratocaster():
    return render_template('stratocaster.html')

@app.route('/semi_acustica')
def semi_acustica():
    return render_template('semi_acustica.html')

if __name__ == '__main__':
    app.run(debug=True)
