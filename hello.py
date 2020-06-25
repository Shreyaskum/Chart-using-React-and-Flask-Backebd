from flask import Flask
from flask import request
import json
from flask_cors import CORS, cross_origin
import pandas as pd
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

df = pd.read_csv(
    r'C:/Users/Shreyas/Desktop/datasets_596958_1073629_Placement_Data_Full_Class.csv')
a = df.to_json()
arr = json.loads(a)
b = arr["gender"]
g = arr["status"]


@app.route("/hsc_p")
@cross_origin()
def hsc():
    if request.args.get("val", None) == "Male":
        temp = {}
        c = arr["hsc_p"]
        for i in range(213):
            d = str(i)
            if b[d] == "M":
                temp[d] = c[d]
        return temp
    elif request.args.get("val", None) == "Female":
        temp = {}
        c = arr["hsc_p"]
        for i in range(213):
            d = str(i)
            if b[d] == "F":
                temp[d] = c[d]
        return temp
    elif request.args.get("val", None) == "placed":
        temp = {}
        c = arr["hsc_p"]
        for i in range(213):
            d = str(i)
            if g[d] == "Placed":
                temp[d] = c[d]
        return temp
    elif request.args.get("val", None) == "not placed":
        temp = {}
        c = arr["hsc_p"]
        for i in range(213):
            d = str(i)
            if g[d] == "Not Placed":
                temp[d] = c[d]
        return temp
    else:
        return(arr["hsc_p"])


@app.route("/ssc_p")
@cross_origin()
def ssc():
    c = arr["ssc_p"]
    if request.args.get("val", None) == "Male":
        temp = {}
        for i in range(213):
            d = str(i)
            if b[d] == "M":
                temp[d] = c[d]
        return temp
    elif request.args.get("val", None) == "Female":
        temp = {}
        for i in range(213):
            d = str(i)
            if b[d] == "F":
                temp[d] = c[d]
        return temp
    elif request.args.get("val", None) == "placed":
        temp = {}
        for i in range(213):
            d = str(i)
            if g[d] == "Placed":
                temp[d] = c[d]
        return temp
    elif request.args.get("val", None) == "not placed":
        temp = {}
        for i in range(213):
            d = str(i)
            if g[d] == "Not Placed":
                temp[d] = c[d]
        return temp
    else:
        return(arr["ssc_p"])


@app.route("/degree_p")
@cross_origin()
def degree():
    c = arr["degree_p"]
    if request.args.get("val", None) == "Male":
        temp = {}
        for i in range(213):
            d = str(i)
            if b[d] == "M":
                temp[d] = c[d]
        return temp
    elif request.args.get("val", None) == "Female":
        temp = {}
        for i in range(213):
            d = str(i)
            if b[d] == "F":
                temp[d] = c[d]
        return temp
    elif request.args.get("val", None) == "placed":
        temp = {}
        for i in range(213):
            d = str(i)
            if g[d] == "Placed":
                temp[d] = c[d]
        return temp
    elif request.args.get("val", None) == "not placed":
        temp = {}
        for i in range(213):
            d = str(i)
            if g[d] == "Not Placed":
                temp[d] = c[d]
        return temp
    else:
        return(arr["degree_p"])


@app.route("/etest_p")
@cross_origin()
def etest():
    c = arr["etest_p"]
    if request.args.get("val", None) == "Male":
        temp = {}
        for i in range(213):
            d = str(i)
            if b[d] == "M":
                temp[d] = c[d]
        return temp
    elif request.args.get("val", None) == "Female":
        temp = {}
        for i in range(213):
            d = str(i)
            if b[d] == "F":
                temp[d] = c[d]
        return temp
    elif request.args.get("val", None) == "placed":
        temp = {}
        for i in range(213):
            d = str(i)
            if g[d] == "Placed":
                temp[d] = c[d]
        return temp
    elif request.args.get("val", None) == "not placed":
        temp = {}
        for i in range(213):
            d = str(i)
            if g[d] == "Not Placed":
                temp[d] = c[d]
        return temp
    else:
        return(arr["etest_p"])


@app.route("/mba_p")
@cross_origin()
def mba():
    c = arr["mba_p"]
    if request.args.get("val", None) == "Male":
        temp = {}
        for i in range(213):
            d = str(i)
            if b[d] == "M":
                temp[d] = c[d]
        return temp
    elif request.args.get("val", None) == "Female":
        temp = {}
        for i in range(213):
            d = str(i)
            if b[d] == "F":
                temp[d] = c[d]
        return temp
    elif request.args.get("val", None) == "placed":
        temp = {}
        for i in range(213):
            d = str(i)
            if g[d] == "Placed":
                temp[d] = c[d]
        return temp
    elif request.args.get("val", None) == "not placed":
        temp = {}
        for i in range(213):
            d = str(i)
            if g[d] == "Not Placed":
                temp[d] = c[d]
        return temp
    else:
        return(arr["mba_p"])


if __name__ == "__main__":
    app.run()
