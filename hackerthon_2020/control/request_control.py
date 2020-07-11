from model import sql
import base64
def request_ctrl(location):
    res=sql.select(location)
    if res=="nonExistent":
        return res
    res=base64.decodestring(res[2].encode())
    # res=str(res)
    return res