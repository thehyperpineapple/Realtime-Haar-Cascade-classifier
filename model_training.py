import cv2
import numpy as np
from PIL import Image
import os


recognizer = cv2.face.LBPHFaceRecognizer_create()
detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# function to get the images and label data
def getImagesAndLabels(path):

    imagePaths = [os.path.join(path,f) for f in os.listdir(path)]     
    faceSamples=[]
    ids = []

    for imagePath in imagePaths:

        PIL_img = Image.open(imagePath).convert('L') # convert it to grayscale
        img_numpy = np.array(PIL_img,'uint8')


        id = int(os.path.split(imagePath)[1][:1]) 
        print(id)
        faces = detector.detectMultiScale(img_numpy)

        for (x,y,w,h) in faces:
            faceSamples.append(img_numpy[y:y+h,x:x+w])
            ids.append(id)

    return faceSamples,ids

print ("\n Training faces.")
faces,ids = getImagesAndLabels('images')
print(faces,ids)
recognizer.train(faces, np.array(ids))

# Save the model
recognizer.write('trainer4.yml')

# Print the number of unique faces trained and end program
print("\n {0} faces trained. Exiting Program".format(len(np.unique(ids))))

