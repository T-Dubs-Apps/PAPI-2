from flask import Flask, render_template
import os

app = Flask(__name__)

# Route for the main page
@app.route('/')
def index():
    # This looks for index.html inside the 'templates' folder
    return render_template('index.html')

if __name__ == '__main__':
    # Render assigns a port automatically (default 10000)
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)