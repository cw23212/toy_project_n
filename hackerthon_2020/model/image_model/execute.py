
import sys
import os
from pathlib import Path
origin_path=os.getcwd()
sys.path.insert(0,str(Path(__file__).parent) )
os.chdir(str(Path(__file__).parent))
import main_detect


def image_getNum(image_path,location):
    try:
        origin_path=os.getcwd()
        os.chdir(str(Path(__file__).parent))
        # base=os.getcwd()
        # getImgAddress = os.path.join(base,"input_images_and_videos","cafe_2person.jpg")
        getPlace = location#"cafe_dream" 
        # 이미지 경로 와 위치정보를 인자로 넘겨준다 (둘다 문자열) , 딕셔너리를 반환
        return_dict = main_detect.getNumberOfPerson(image_path, getPlace)
    finally:
        os.chdir(origin_path)
    return return_dict
os.chdir(origin_path)
# check return_dict

# TODO -send (return_dict) to front

