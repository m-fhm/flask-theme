from flask import Flask,render_template,url_for

ab=Flask(__name__)

@ab.route('/')
def index():
    return render_template('index.html')
# ab.run()

if __name__ == "__main__":
    ab.run(debug=True)



