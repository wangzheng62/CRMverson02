from flask import Flask,redirect,url_for,render_template,request,flash
from func import DBserver,Crm,Product,Orderlist,Employee,Customer

app = Flask(__name__)
app.secret_key = 'some_secret'

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/customermain')
def customermain():
    return render_template('customermain.html')
@app.route('/ordermain')
def ordermain():
    return render_template('ordermain.html')
@app.route('/productmain')
def prouductmain():
    return render_template('productmain.html')
@app.route('/employeemain')
def employeemain():
    return render_template('employeemain.html')
#客户页
@app.route('/customernow')
def customernow():
	return render_template('customermain.html',welcome="本功能尚未开放")
@app.route('/customersearch')
def customersearch():
	return render_template('customermain.html',welcome="本功能尚未开放")
@app.route('/customeradd')
def customeradd():
	return render_template('customermain.html',welcome="本功能尚未开放")
@app.route('/customeranalyze')
def customeranalyze():
	return render_template('customermain.html',welcome="本功能尚未开放")
#客户页功能
@app.route('/addcustomer',methods=["post"])
def addcustomer():
    res=request.form.to_dict()
    print(res)
    res["__employee_Id"]="123"
    l=Customer(**res)
    l.save()
    return  render_template('customermain.html')

#产品页
@app.route('/productnow')
def productnow():
	return render_template('productmain.html',welcome="本功能尚未开放")
@app.route('/productsearch')
def productsearch():
	res=Product.fetchall()
	res.insert(0,Product.colnames())
	return render_template('productmain.html',productlist=res)
@app.route('/productadd')
def productadd():
	res=Product.desc()
	return render_template('productmain.html',productform=res,bindurl='addproduct')
@app.route('/productanalyze')
def productanalyze():
	return render_template('productmain.html',welcome="本功能尚未开放")
#产品页功能
@app.route('/nowproduct',methods=["get","post"])
def nowproduct():
	return render_template('productmain.html',welcome="本功能尚未开放")
@app.route('/searchproduct',methods=["get","post"])
def searchproduct():
	return render_template('productmain.html',welcome="本功能尚未开放")
@app.route('/addproduct',methods=["get","post"])
def addproduct():
	res=request.form.to_dict()
	p=Product(**res)
	if p.save():
		flash("添加成功")
	else:
		flash("添加失败")
	return redirect(url_for("productadd"))
@app.route('/analyzeproduct',methods=["get","post"])
def analyzeproduct():
	return render_template('productmain.html',welcome="本功能尚未开放")
#订单页
#产品页
@app.route('/ordernow')
def ordernow():
	return render_template('ordermain.html',welcome="本功能尚未开放")
@app.route('/ordersearch')
def ordersearch():
	res=Orderlist.fetchall()
	res.insert(0,Orderlist.colnames())
	return render_template('ordermain.html',orderlist=res)
@app.route('/orderadd')
def orderadd():
	res=Orderlist.desc()
	return render_template('ordermain.html',orderform=res,bindurl='addorder')
@app.route('/orderanalyze')
def orderanalyze():
	return render_template('ordermain.html',welcome="本功能尚未开放")
#产品页功能
@app.route('/noworder',methods=["get","post"])
def noworder():
	return render_template('ordermain.html',welcome="本功能尚未开放")
@app.route('/searchorder',methods=["get","post"])
def searchorder():
	return render_template('ordermain.html',welcome="本功能尚未开放")
@app.route('/addorder',methods=["get","post"])
def addorder():
	res=request.form.to_dict()
	o=Orderlist(**res)
	if p.save():
		flash("添加成功")
	else:
		flash("添加失败")
	return redirect(url_for("orderadd"))
@app.route('/analyzeorder',methods=["get","post"])
def analyzeorder():
	return render_template('ordermain.html',welcome="本功能尚未开放")		
	
if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)

