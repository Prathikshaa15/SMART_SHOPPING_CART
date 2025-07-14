import tensorflow as tf
from keras.models import load_model
from keras.preprocessing import image
import numpy as np
import os, sys, warnings
if not sys.warnoptions:
    warnings.simplefilter("ignore")
from flask import Flask, request, send_file

def detect():
    
    # dimensions of our images
    img_width, img_height = 256, 256 
    model = load_model('C:\\xampp\\htdocs\\Smart_Shopping_Cart\\Final Dataset\\models\\model_ex-019_acc-0.985577.h5')
    model.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy'])
    img = tf.keras.utils.load_img('C:\\xampp\\htdocs\\Smart_Shopping_Cart\\temp.jpg', target_size=(img_width, img_height))
    x = tf.keras.utils.img_to_array(img)
    x = np.expand_dims(x, axis=0)

    images = np.vstack([x])
    classes = (model.predict(images, batch_size=10) > 0.5).astype("int32")
    if classes[0][0] == 1: 
        item = "3Roses" 
    elif classes[0][1] == 1: 
        item = "Colin"
    elif classes[0][2] == 1: 
        item = "Henko"
    elif classes[0][3] == 1:
        item = "lays-10"
    elif classes[0][4] == 1:
        item = "Mysoresandal-Soap"
    elif classes[0][5] == 1:
        item = "Oreo-30"
    elif classes[0][6] == 1:
        item = "Vim-Bar"
    elif classes[0][7] == 1:
        item = "colgate"
    elif classes[0][8] == 1:
        item = "hamam"
    elif classes[0][9] == 1:
        item = "harpic-bathroom"
    elif classes[0][10] == 1:
        item = "lays-y"
    elif classes[0][11] == 1:
        item = "snickers"
        
    return item	
	
	

app = Flask(__name__)

@app.route("/")
def hello():
	return detect()


if __name__ == '__main__':
    app.run(debug=True, port=80)

# dimensions of our images
img_width, img_height = 256, 256
