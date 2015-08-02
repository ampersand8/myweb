"""Cloud Foundry test"""
from flask import Flask, render_template
import os
 
app = Flask(__name__)
 
port = int(os.getenv("VCAP_APP_PORT"))


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/pulp_manager')
def pulp_manager():
    return render_template('pulp_manager.html')



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
