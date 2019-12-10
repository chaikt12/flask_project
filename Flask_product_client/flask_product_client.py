# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 09:58:00 2019

@author: mycp2ej0
"""

from flask import Flask, render_template, request, redirect

import requests


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Fetch form data
        #add_operation = request.form
        mod=""
        print(request.form)
        if request.form['price']=="highest_price":
            price=request.form['price']
            data={"price":price}
            requests.post("http://192.168.43.140:5000/",json=data, headers={"content-type":"application/json"})
            mod = "highest_price"
        elif request.form['price']=="range_price":
            rangeprice=request.form['price']
            data={"rangeprice":rangeprice}
            print(data)
            requests.post("http://192.168.43.223:5000/",json=data, headers={"content-type":"application/json"})
            mod="range_price"
        elif request.form['price']=="item_count":
            itemcount=request.form['price']
            data={"itemcount":itemcount}
            requests.post("http://192.168.43.140:5000/",json=data, headers={"content-type":"application/json"})
            mod="item_count"
     
        return redirect('/test?mod=' + mod)
    return render_template('index_product.html')

@app.route('/test')
def test():
    if request.method == 'GET':
        mod = request.args.get("mod")
        
        if mod=='highest_price':
            #PARAMS = {'key1': 'value1', 'key2': 'value2'}
            r=requests.get("http://192.168.43.140:5000/product_price")
            print(r.json())
            return render_template('display_product.html',productPrice=r.json())
        elif mod=='range_price':
            r=requests.get("http://192.168.43.223:5000/range_price")
            print(r.json())
            #return r.content
            return render_template('display_range_price.html',productPrice=r.json())
        elif mod=='item_count':
            r=requests.get("http://192.168.43.140:5000/count")
            return render_template('display_item_count.html',productPrice=r.json())
     
    
if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)