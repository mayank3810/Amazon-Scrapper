from flask import Flask, render_template ,request , jsonify ,make_response
from selenium import webdriver
from time import sleep
app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/pass_val',methods=['POST'])
def pass_val():
    websiteurl=request.args.get('value')
    #wbsiteurlstring= str(websiteurl)
    print(type(websiteurl))
    return websiteurl

@app.route('/my-link/')
def my_link():
    print ('I got clicked!')
    #ref_link ="""&tag=festivalkart2-21"""
    website = pass_val()
    print('                     **************************                  ')
    print(type(website))
    print(website)
    return 'Click.'

if __name__ == '__main__':
  app.run(debug=True)