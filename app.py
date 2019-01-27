from flask import (g, request, render_template, Flask)
from constants import *
import pandas as pd
import redis
import json

app = Flask(__name__)

# connection creator with redis
def init_db():
    db = redis.StrictRedis(host=DB_HOST, port=DB_PORT, db=DB_NO)
    return db
 
 
@app.before_request
def before_request():
    g.db = init_db()

@app.route('/')
def view_bhav():
	# these columns are shown on the UI
	columns = ['SC_CODE', 'SC_NAME', 'OPEN', 'CLOSE', 'PREVCLOSE', 'LAST', 'LOW', 'HIGH', 'NET_TURNOV']
	# use msgpack to read redis data into pandas df
	bhav_df = pd.read_msgpack(g.db.get("bhav"))
	bhav_df = bhav_df[columns]
	# json conversion
	bhav_records = json.loads(bhav_df.to_json(orient='records'))
	return render_template('bhav_list.html', bhav_records=bhav_records, columns=columns)


if __name__ == "__main__":
	app.run(host='0.0.0.0', port=5000, debug=True)
