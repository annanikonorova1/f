from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')

def hello_world():
    return render_template('hello.html')

@app.route('/main')
def main():
    return render_template('main.html')


@app.route('/comp/')
def comp():
    return render_template('comp.html')


@app.route('/tv/')
def tv():
    return render_template('tv.html')


@app.route('/nout/')
def nout():
    return render_template('nout.html')


if __name__ == '__main__':
    app.run()
