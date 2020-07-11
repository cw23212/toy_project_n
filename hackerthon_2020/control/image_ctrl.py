from flask import request,render_template
from model import sql
from control.thread_image_queu import input_queue
from datetime import datetime
import os
def image():
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
        # elif file.location == '':
            # return "location not"
        else:
            filename = file.filename
            date=datetime.now().strftime('%m%d_%H%M_')
            file_path=os.path.join(os.getcwd(),"var",date+filename)
            file.save(file_path)
            # res=sql.update(request.form['location'],cong)
            input_queue(file_path,request.form['location'] )
            return "image uploaded</br><a href='/image'>back</a>"
    else:
        return render_template("form.html")

def image_congretion(file):
    return hash(file)%10