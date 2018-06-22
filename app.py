from flask import Flask,jsonify,request,render_template
import datetime
from time import gmtime, strftime

app = Flask(__name__)
# showtime = strftime("%Y-%m-%d %H:%M:%S", gmtime())
showtime = strftime("%Y-%m-%d", gmtime())
bdatas = {
    "nature":[
    {
    	"id":"N1",
      "name":"naturepic",
      "description":"hello"
    },
    {
    	"id":"N2",
      "name":"naturepic2",
      "description":"hello2"
    }
    ]
}

@app.route('/')
def home():
  return render_template('index.html')

#get /bdata
@app.route('/bdata')
def get_bdatas():
  return jsonify({'bdatas': bdatas})
  #pass

if __name__ == "__main__":
    app.run()