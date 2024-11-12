from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/c2f/<value>")
def convert_temperature(value):
    try:
       fahrenheit = float(value) * 9 / 5 + 32
       fahrenheit = round(fahrenheit, 3)  # Round to three decimal places
    except:
       return render_template('index.html')

    return render_template('convert1.html', var1=value, var2=fahrenheit)


@app.route("/f2c/<value>")
def convert_f2c_temperature(value):
    try:
        celcius = 1/9*5*(float(value)-32)
        celcius = round(celcius, 3)
    except:
        return render_template('index.html')

    return render_template('convert2.html', var1=value, var2=celcius)

#if __name__ == '__main__':
#    app.run(debug=True, host="0.0.0.0", port=80)
