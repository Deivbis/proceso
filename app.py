from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # 'index.html' debe estar en la carpeta 'templates'

@app.route('/formativa')
def formativa ():
    return render_template('formativa.html')

@app.route('/disciplinaria')
def disciplinaria ():
    return render_template('disciplinaria.html')



if __name__ == '__main__':
    app.run(debug=True)