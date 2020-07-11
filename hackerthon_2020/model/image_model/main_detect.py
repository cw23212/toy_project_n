from input_images_and_videos.utils import backbone
from api import object_counting_api
import cv2
import datetime


## 혼잡도 일단 수동으로...
def cal_complexity(num_person):
    if 0<=num_person and num_person<=2:
        return 'Low'
    elif 2<=num_person and num_person<=6:
        return 'Normal'
    else:
        return 'High'


def getNumberOfPerson(img,place):

    input_video = img

    detection_graph, category_index = backbone.set_model('ssd_mobilenet_v2_coco_2018_03_29', 'mscoco_label_map.pbtxt')

    is_color_recognition_enabled = 0

    result = object_counting_api.single_image_object_counting(input_video, detection_graph, category_index, is_color_recognition_enabled) # targeted objects counting
    
    cv2.destroyAllWindows()
    info_dict={}
    try:
        idx = result.find('person')
        info = result[idx:idx+11]

        #print(info)
        #print(int(info[-1]))

        complexity = cal_complexity(int(info[-1]))
        info_dict = {}

        info_dict['person'] = int(info[-1])
        info_dict['place']= place
        info_dict['complexity'] = complexity
        info_dict['time']=datetime.datetime.now().strftime('%Y-%m-%d-%H-%M')
    except:
        info_dict['person']= None
        info_dict['person'] = None
        info_dict['place']= None
        info_dict['complexity'] = None
        info_dict['time']=None
    
    return info_dict


# 호출 예시
#dit1 = getNumberOfPerson('./input_images_and_videos/cafe_2person.jpg',"cafe_dream")
#dit2 = getNumberOfPerson('./input_images_and_videos/cafe_4person.jpg',"jaejoo_molbbang")
# check returned value

#print(dit1,dit2)
