from flask import Flask, request, jsonify
from manager import Manager
app = Flask(__name__)
manager = Manager()

@app.route('/', methods=['GET'])
def hello():
    #Stats dashboard
    return 'Home page!'

@app.route('/api/add_url', methods=['GET'])
def add_url():
    if 'url' in request.args:
        url = request.args['url']

        return jsonify(manager.verify_url_and_add_to_db(url))

    else:
        return jsonify({'status': 'Not OK! No URL parameter'})

@app.route('/api/get_url', methods=['GET'])
def get_url():
    if 'id' in request.args:
        id = request.args['id']
        
        return jsonify(manager.get_and_decode_shortened_url(id))
    
    else: 
        return jsonify({'status': 'Not OK! No URL id provided to read'})

@app.route('/api/get_stats', methods=['GET'])
def get_stats():
    return jsonify(manager.show_all_urls())




if __name__ == '__main__':
    app.run(debug = True)