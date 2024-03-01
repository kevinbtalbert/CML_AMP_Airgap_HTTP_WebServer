from flask import Flask, render_template, Response
import os

app = Flask(__name__)

@app.route('/')
def home():
    # Renders the homepage with links to the YAML files.
    return render_template('index.html'

@app.route('/community-amp-catalog.yaml')
def community():
    yaml_file_path = os.getcwd() + '/templates/community-amp-catalog.yaml'
    
    # Reading the YAML file content
    with open(yaml_file_path, 'r') as file:
        yaml_content = file.read()
    
    # Returning the YAML content with the appropriate MIME type
    return Response(yaml_content, mimetype='text/plain')

@app.route('/official-amp-catalog.yaml')
def official():
    yaml_file_path = os.getcwd() + '/templates/official-amp-catalog.yaml'
    
    # Reading the YAML file content
    with open(yaml_file_path, 'r') as file:
        yaml_content = file.read()
    
    # Returning the YAML content with the appropriate MIME type
    return Response(yaml_content, mimetype='text/plain')

def main():
    app.run(host='127.0.0.1',
            port=int(os.getenv('CDSW_APP_PORT')),
            debug=True)

if __name__ == '__main__':
    main()