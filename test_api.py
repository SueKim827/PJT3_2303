from flask import Flask, request, render_template
from camera import Camera


app = Flask(__name__)


@app.route('/')
def input_image():
    return render_template('input_image.html')

@app.route('/submit',methods=['POST'])
def submit():
    image = request.args.get('image')

    print(type(image))
    return image


@app.route('/result_speech')
def result_speech():
    
    return render_template('result_speech.html')

if __name__ =='__main__':
    app.run(host='127.0.0.1', port = 5000)
