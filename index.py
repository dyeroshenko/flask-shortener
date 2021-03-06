from flask import Flask, request, jsonify, redirect, render_template
from manager import Manager
app = Flask(__name__)
manager = Manager()

@app.route('/<hashed_id>', methods=['GET'])
def redirect_to_original_page(hashed_id):
    id = hashed_id
    
    try: 
        url = manager.get_full_url_for_redirect(id)
        return redirect(url, code=302)
    except:
        # Replace with 404 template 
        return 'ID is invalid or not in our database yet'


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
        
        return jsonify(manager.get_shortened_url(id))
    
    else: 
        return jsonify({'status': 'Not OK! No URL id provided to read'})

@app.route('/api/get_full_stats', methods=['GET'])
def get_stats():
    return jsonify(manager.show_all_urls())

@app.route('/usage', methods = ['GET'])
def usage_dash():
    titles = ('#', 'Short ID', 'Timestamp-added(CET)', 'Domain', 'Full URL', 'Visits')
    result = manager.get_full_data_from_db()

    return render_template(
                            'stats.html',
                            titles = titles,
                            result = result
                            )

@app.route('/host', methods = ['GET'])
def check_host()
    return request.args

if __name__ == '__main__':
    app.run(debug = True)