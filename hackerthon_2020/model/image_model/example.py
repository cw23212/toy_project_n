import main_detect

getImgAddress = "C:\\Users\\psj28\\Documents\\GitHub\\hackerthon_2020\\var\\cafe_2person.jpg"
getPlace = "cafe_dream"

# 이미지 경로 와 위치정보를 인자로 넘겨준다 (둘다 문자열) , 딕셔너리를 반환
return_dict = main_detect.getNumberOfPerson(getImgAddress, getPlace)

# check return_dict

# print(return_dict)

# TODO -send (return_dict) to front

