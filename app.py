from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/run_model', methods=['POST', 'GET'])
def get_text():
    given_movie = request.form['movie']
    return render_template("index.html", movie_chose = given_movie)


if __name__ == '__main__':
    app.run(debug=True)
