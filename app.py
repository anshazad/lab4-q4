import json
from flask import Flask, render_template, request, jsonify   

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("InputOutput.html")    
    

@app.route("/submitJSON", methods=["POST"])
def processJSON(): 
    jsonStr = request.get_json()
    # print(jsonStr)
    jsonObj = json.loads(jsonStr)
    response = ""
    temp1 = jsonObj['temp1']
    temp2 = jsonObj['temp2']
    l1 = temp1.split(",")
    l2 = temp2.split(",")
    for i in range(len(l2)):
        l2[i] = l2[i].lower()
    f = []
    for ele in l1:
        if ele.lower() in l2:
            f.append(ele)
    response += str(f)
    return response
    
    
if __name__ == "__main__":
    app.run(debug=True)
    
    
