import cv2
import numpy as np

def empty(pos):
    pass   

def create_tuning_window():
    cv2.namedWindow("Tuning")
    cv2.createTrackbar("h_min","Tuning",0,180,empty)
    cv2.createTrackbar("h_max","Tuning",180,180,empty)
    cv2.createTrackbar("s_min","Tuning",0,255,empty)
    cv2.createTrackbar("s_max","Tuning",255,255,empty)
    cv2.createTrackbar("v_min","Tuning",0,255,empty)
    cv2.createTrackbar("v_max","Tuning",255,255,empty)
        
def get_tuning_params():
    trackbar_names = ["h_min","h_max","s_min","s_max","v_min","v_max"]
    return {key:cv2.getTrackbarPos(key, "Tuning") for key in trackbar_names}
       

img=cv2.imread("/home/wwd9861/PythonImageWorkspace/OpenCV/tennisball.jpg")
hsv_img=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
create_tuning_window()

while True:
    tuning_params=get_tuning_params()

    hsv_lower=np.array([tuning_params["h_min"], tuning_params["s_min"], tuning_params["v_min"]])
    hsv_upper=np.array([tuning_params["h_max"], tuning_params["s_max"], tuning_params["v_max"]])
    hsv_filter=cv2.inRange(hsv_img,hsv_lower,hsv_upper)
    tuning_image=cv2.bitwise_and(img,img,mask=hsv_filter)
    cv2.imshow("Tuning",tuning_image)
    if cv2.waitKey(1)==ord('q'):
        break

cv2.destroyAllWindows()