from flask import Flask, render_template
app=Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')
    # return 'Hello,Tannu!'

@app.route('/myintro')
def intro():
    return 'Hello everyone,nice to meet you'

if __name__ == "__main__":
    app.run(debug=True)

