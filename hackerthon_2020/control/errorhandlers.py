from flask import Blueprint
er=Blueprint("error_handle",__name__)

@er.app_errorhandler(400)
def err400(err):
    return "400"

@er.app_errorhandler(404)
def err404(err):
    return "404"

@er.app_errorhandler(500)
def err500(err):
    return "sql class error"
