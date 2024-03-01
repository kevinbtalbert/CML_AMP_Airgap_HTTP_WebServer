from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def home():
    # Renders the homepage with links to the YAML files.
    return render_template('index.html')

@app.route('/files/<filename>')
def files(filename):
    # Serves the YAML files from the 'files' directory.
    return send_from_directory('files', filename)

if __name__ == '__main__':
    app.run(host='127.0.0.1',
            port=int(os.getenv('CDSW_APP_PORT')),
            debug=True)
