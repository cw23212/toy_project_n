from  model import sql
def index_ctrl():
    ai1={"twosome":"Twosome Place","cu_ai":"CU AI센터점","collabo_lab":"AI 콜라보랩","bigbear8":"빅베어8"}
    li=[]
    for key,value in ai1.items():
        sel=sql.select(key)
        if(sel=="nonExistent"):
            continue
        co=int(sel[1])
        if co==1:
            cong="여유"
            color="info"
        elif co==2:
            cong="보통"
            color="warning"
        elif co==3:
            cong="혼잡"
            color="danger"
        else:
            continue
        p={"location":value,"cong":cong,"color":color}
        li.append(p)
    return li