from flask import Flask, render_template
import os

# Initialize Flask app
# Flask expects HTML files to be in a folder named 'templates'
app = Flask(__name__, template_folder='templates')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/health')
def health():
    return "OK", 200

if __name__ == '__main__':
    # Render assigns a port automatically
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
