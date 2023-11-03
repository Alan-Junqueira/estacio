from flask import Flask, request, render_template

app = Flask(__name__)

app.debug = True


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/ola/')
@app.route('/ola/<name>')
def ola_mundo(name="mundo"):
    return render_template("hello.html", name=name)


@app.route('/login', methods=['GET', 'POST'])
def logar():
    if request.method == 'POST':
        return "Recebeu post! Fazer login!"
    else:
        return "Recebeu get! Exibir FORM de login."


if __name__ == '__main__':
    app.run(host="0.0.0.0")
