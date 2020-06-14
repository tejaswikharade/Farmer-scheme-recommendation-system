from flask import Flask,render_template,request
import teju

app = Flask(__name__)
@app.route('/')
def index():
	return render_template('home.html')

@app.route('/first')
def first():
	query_index=1
	query_index=int(query_index)
	ans=teju.predict(query_index)



	return render_template('first.html',ans=ans)


@app.route('/sec')
def sec():
	query_index=2
	query_index=int(query_index)
	ans=teju.predict(query_index)



	return render_template('sec.html',ans=ans)
@app.route('/thi')
def thi():
	query_index=3
	query_index=int(query_index)
	ans=teju.predict(query_index)



	return render_template('thi.html',ans=ans)
@app.route('/fou')
def fou():
	query_index=4
	query_index=int(query_index)
	ans=teju.predict(query_index)



	return render_template('fou.html',ans=ans)
@app.route('/fif')
def fif():
	query_index=5
	query_index=int(query_index)
	ans=teju.predict(query_index)



	return render_template('fif.html',ans=ans)
@app.route('/six')
def six():
	query_index=6
	query_index=int(query_index)
	ans=teju.predict(query_index)



	return render_template('six.html',ans=ans)
@app.route('/sev')
def sev():
	query_index=7
	query_index=int(query_index)
	ans=teju.predict(query_index)



	return render_template('sev.html',ans=ans)
@app.route('/eig')
def eig():
	query_index=8
	query_index=int(query_index)
	ans=teju.predict(query_index)



	return render_template('eig.html',ans=ans)
@app.route('/nin')
def nin():
	query_index=9
	query_index=int(query_index)
	ans=teju.predict(query_index)



	return render_template('nin.html',ans=ans)
@app.route('/ten')
def ten():
	query_index=10
	query_index=int(query_index)
	ans=teju.predict(query_index)



	return render_template('ten.html',ans=ans)

app.run(debug=True)

