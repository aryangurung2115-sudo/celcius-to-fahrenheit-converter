from flask import Flask, render_template, request

app = Flask(__name__)

def convert_temperature(value, conversion_type):
    if conversion_type == "CtoF":
        return (value * 9/5) + 32
    elif conversion_type == "FtoC":
        return (value - 32) * 5/9
    elif conversion_type == "CtoK":
        return value + 273.15
    elif conversion_type == "KtoC":
        return value - 273.15
    elif conversion_type == "FtoK":
        return (value - 32) * 5/9 + 273.15
    elif conversion_type == "KtoF":
        return (value - 273.15) * 9/5 + 32

@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    if request.method == 'POST':
        try:
            value = float(request.form['temperature'])
            conversion = request.form['conversion']
            converted = convert_temperature(value, conversion)
            result = round(converted, 2)
        except ValueError: 
            result = "Invalid input! Please enter a number."

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
