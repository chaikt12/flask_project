# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 09:58:00 2019

@author: mycp2ej0
"""

from flask import Flask, render_template, request, redirect

import requests
import json

ip1="http://10.215.7.56:3000/" #ip for webservice 1
ip2="http://10.215.7.56:4000/" #ip for webservice 2
ip3="http://10.215.7.56:5000/" #ip for webservice 3

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Fetch form data
        #add_operation = request.form
        mod=""
        print(request.form)
        if request.form['price']=="highest_price":
            # price=request.form['price']
            # data={"price":price}
            # requests.post(ip1,json=data, headers={"content-type":"application/json"})
            mod = "highest_price"
        elif request.form['price']=="range_price":
            # rangeprice=request.form['price']
            # data={"rangeprice":rangeprice}
            # print(data)
            # requests.post(ip2,json=data, headers={"content-type":"application/json"})
            mod="range_price"
        elif request.form['price']=="item_count":
            # itemcount=request.form['price']
            # data={"itemcount":itemcount}
            # requests.post(ip3,json=data, headers={"content-type":"application/json"})
            mod="item_count"
        elif request.form['price']=="all":
            print('come here')
            # price=request.form['price']
            # data={"price":price}
            # requests.post(ip1,json=data, headers={"content-type":"application/json"})
            # requests.post(ip2,json=data, headers={"content-type":"application/json"})
            # requests.post(ip3,json=data, headers={"content-type":"application/json"})
            mod='all'
        return redirect('/test?mod=' + mod)
    return render_template('index_product.html')

@app.route('/test')
def test():
    if request.method == 'GET':
        mod = request.args.get("mod")
        
        if mod=='highest_price':
            #PARAMS = {'key1': 'value1', 'key2': 'value2'}
            r=requests.get(ip1+"product_price")
            pretty_json = json.loads(r.text)
            print (json.dumps(pretty_json, indent=2))
            # print(r.json())
            # return r.content
            return render_template('display_product.html',productPrice=r.json())
        elif mod=='range_price':
            r=requests.get(ip2+"range_price")
            pretty_json = json.loads(r.text)
            print (json.dumps(pretty_json, indent=2))
            #return r.content
            return render_template('display_range_price.html',productPrice=r.json())
        elif mod=='item_count':
            r=requests.get(ip3+"count")
            pretty_json = json.loads(r.text)
            print (json.dumps(pretty_json, indent=2))
            return render_template('display_item_count.html',productPrice=r.json())
        elif mod=='all':
            r=requests.get(ip1+"product_price")
            x=requests.get(ip2+"range_price")
            w=requests.get(ip3+"count")
            return render_template('display_all.html',productPrice=r.json(), rangePrice=x.json(), itemCount=w.json())
    
if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)