from flask import Flask,render_template,url_for
from config import config
from control import errorhandlers,image_ctrl,request_control,index_ctrl
from model import sql,sql_ini

application=Flask(__name__)
application.register_blueprint(errorhandlers.er)
# app.register_blueprint(image.im)

@application.route("/",endpoint="index")
def index_route():
    return render_template("slid.html",content=index_ctrl.index_ctrl())

@application.route("/image",methods=['GET','POST'])
def image_route():
    return image_ctrl.image()


@application.route('/request/')
def request_default_route():
    return "temporary value"


@application.route('/request/<location>')
def request_route(location):
    res=request_control.request_ctrl(location)
    return res

#thread
from control import thread_image_queu

if __name__=='__main__':
    application.debug=config["dubug"]
    application.run(host=config['host'])
