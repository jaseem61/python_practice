import face_recognition
import os
import cv2
import keyboard

known_faces_dir="known_faces"
count=1
tolerance=0.6
frame_thickness=3
font_thickness=2
model="hog"

print("loading known faces")

known_faces=[]
known_names=[]

for name in os.listdir(known_faces_dir):
    for filename in os.listdir(f"{known_faces_dir}/{name}"):
        image=face_recognition.load_image_file(f"{known_faces_dir}/{name}/{filename}")
        encoding=face_recognition.face_encodings(image)
        if encoding:
            known_faces.append(encoding)
            known_names.append(name)

print("processing unknown faces")

cap=cv2.VideoCapture(0)

while True:
    ret,image=cap.read()
    locations=face_recognition.face_locations(image,model=model)
    encodings=face_recognition.face_encodings(image,locations)

    for face_encoding, face_location in zip(encodings,locations):
        count=count+1
        results=face_recognition.compare_faces(known_faces,face_encoding,tolerance=0.3)
        match=None
        if bool(results):
            print(count)
            match= known_names[0]
            print(f"Match found:{match}")

            top_left=(face_location[3],face_location[0])
            bottom_right=(face_location[1],face_location[2])

            color=[0,255,0]

            cv2.rectangle(image,top_left,bottom_right,color,frame_thickness)

            top_left=(face_location[3],face_location[2])
            bottom_right=(face_location[1],face_location[2]+22)
            cv2.rectangle(image,top_left,bottom_right,color,cv2.FILLED)
            cv2.putText(image,match,(face_location[3]+10,face_location[2]+15),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0),font_thickness)
    cv2.imshow(filename,image)
    cv2.waitKey(1)
    if(keyboard.is_pressed('q')):
        break
