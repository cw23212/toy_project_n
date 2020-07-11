from flask import Blueprint,request,redirect,url_for
im=Blueprint("image",__name__,url_prefix="/image/")
from .thread_image_queu import input_queue
import os
import time
@im.route("/",methods=['GET','POST'])
def image():
    i=1
    if request.method == 'POST':
        if 'file' not in request.files:
            # flash('No file part')
            return "file not"
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            # flash('No selected file')
            return "file name not"
        else:
            filename = file.filename
            filepath=os.path.join(os.getcwd(),"var",filename)
            file.save(filepath)
            input_queue(filepath)
            return "succes"
    else:
        return "OK"
