from flask import Flask,render_template

famms_app = Flask(__name__)

@famms_app.route('/')
def home():
    return render_template('index.html',title='product')


if __name__ == '__main__':
    famms_app.run(debug=True,port=7777)


  