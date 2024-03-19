from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_numbers():
    if request.method == 'POST':
        try:
            n = int(request.form['n'])
            if n <= 0:
                return render_template('index.html', error='Please enter a positive integer.')
            random_numbers = [(index + 1, random.randint(1, 100)) for index in range(n)]
            return render_template('index.html', random_numbers=random_numbers)
        except ValueError:
            return render_template('index.html', error='Please enter a valid integer.')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)




