import pyshorteners as ps
from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/')
def link():
   return render_template('link.html')
@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      link = request.form.get("url")
      server= request.form.get("server")
      url= ps.Shortener().tinyurl.short(link)
      return render_template("result.html",link=url)
@app.errorhandler(404)
def page_not_found(e):
   return render_template('404.html'),404
if __name__ == '__main__':
   app.run(debug = True)
