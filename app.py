from flask import Flask,jsonify,request,render_template
import datetime
from time import gmtime, strftime

app = Flask(__name__)
# showtime = strftime("%Y-%m-%d %H:%M:%S", gmtime())
showtime = strftime("%Y-%m-%d", gmtime())
bdatas = [{
    'id'  :'1',
    'name': 'My blogdata',
    # 'items': [{'name':'my item', 'price': 15.99 }]
    'description':'Blah blah black sheep',
    'stamp':showtime
}]

@app.route('/')
def home():
  return render_template('index.html')

#post /bdata data: {name :}
@app.route('/bdata' , methods=['POST'])
def create_bdata():
  request_data = request.get_json()
  new_bdata = {
    'name':request_data['name'],
    'items':[]
  }
  bdatas.append(new_bdata)
  return jsonify(new_bdata)
  #pass

#get /bdata/<name> data: {name :}
@app.route('/bdata/<string:name>')
def get_bdata(name):
  for bdata in bdatas:
    if bdata['name'] == name:
          return jsonify(bdata)
  return jsonify ({'message': 'bdata not found'})
  #pass

#get /bdata
@app.route('/bdata')
def get_bdatas():
  return jsonify({'bdatas': bdatas})
  #pass

#post /bdata/<name> data: {name :}
@app.route('/bdata/<string:name>/item' , methods=['POST'])
def create_item_in_bdata(name):
  request_data = request.get_json()
  for bdata in bdatas:
    if bdata['name'] == name:
        new_item = {
            'name': request_data['name'],
            'price': request_data['price']
        }
        bdata['items'].append(new_item)
        return jsonify(new_item)
  return jsonify ({'message' :'bdata not found'})
  #pass

#get /bdata/<name>/item data: {name :}
@app.route('/bdata/<string:name>/item')
def get_item_in_bdata(name):
  for bdata in bdatas:
    if bdata['name'] == name:
        return jsonify( {'items':bdata['items'] } )
  return jsonify ({'message':'bdata not found'})

  #pass

app.run(port=5000)