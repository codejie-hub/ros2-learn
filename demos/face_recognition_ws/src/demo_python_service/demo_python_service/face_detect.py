import cv2
import face_recognition

def main():
    test_path='/home/wp/learn_ros/demos/face_recognition_ws/src/demo_python_service/resource/default.jpeg'
    image=cv2.imread(test_path)
    face_locations=face_recognition.face_locations(image,1,"hog")
    for top,right,bottom,left in face_locations:
        cv2.rectangle(image,(left,top),(right,bottom),(255,0,0),4)
    cv2.imshow("Face detect result",image)
    cv2.waitKey(0)

# if __name__=='__main__':
#     main()