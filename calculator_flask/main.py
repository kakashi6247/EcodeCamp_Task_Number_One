from flask import Flask, render_template, request

app = Flask(__name__)

def calculate(expression):
    try:
        return eval(expression)
    except Exception as e:
        return "Error"

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ''
    if request.method == 'POST':
        expression = request.form.get('expression', '')
        result = calculate(expression)
    return render_template('calculator.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
