from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'This is my first API call!'

@app.route('/post', methods=["POST"])
def testpost():
     input_json = request.get_json(force=True) 
     dictToReturn = {'text':input_json['text']}
     return jsonify(dictToReturn)

# Load the model
model = pickle.load(open('model.pkl','rb'))
labels ={
  0: "versicolor",   
  1: "setosa",
  2: "virginica"
}

@app.route('/api',methods=['POST'])
def predict():
    # Get the data from the POST request.
	data = request.get_json(force=True)
	predict = model.predict(data['feature'])
	return jsonify(predict[0].tolist())

if __name__ == "__main__":
    app.run(host='0.0.0.0')