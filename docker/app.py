from flask import Flask, request

app = Flask(__name__)

def miles_to_km(miles):
    return miles * 1.60934

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        miles = float(request.form['miles'])
        km = miles_to_km(miles)
        return f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Conversion Result</title>
        </head>
        <body>
            <h1>Conversion Result</h1>
            <p>{miles} miles is equal to {km} kilometers.</p>
            <a href="/">Go back</a>
        </body>
        </html>
        """
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Miles to Kilometers Converter</title>
    </head>
    <body>
        <h1>Miles to Kilometers Converter</h1>
        <form action="/" method="post">
            <label for="miles">Miles:</label>
            <input type="text" id="miles" name="miles" required>
            <button type="submit">Convert</button>
        </form>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

