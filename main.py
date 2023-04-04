import cv2
import face_recognition
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/face_recognition', methods=['POST'])
def mface_recognition():
    try:
        file = request.files['image1']
        file.save('image1.jpg')

        file = request.files['image2']
        file.save('image2.jpg')

        # Get the image file from the request and name it image1.jpg and image2.jpg

        # Load the jpg files into numpy arrays
        image1 = face_recognition.load_image_file("image1.jpg")
        image2 = face_recognition.load_image_file("image2.jpg")

        # Get the face encodings for each face in each image file
        image1_encoding = face_recognition.face_encodings(image1)[0]
        image2_encoding = face_recognition.face_encodings(image2)[0]

        # Compare faces and return True / False
        results = face_recognition.compare_faces([image1_encoding], image2_encoding)
        # # print(results[0])
        # # print(type(results))
        # res = bool(results[0] == True)

        # print(False == results[0])
        # # return jsonify(res)

        return jsonify({'results': bool(results[0]), "status": 1})
    except Exception as e:
        return jsonify({'error': str(e), "status": 0})

if __name__ == '__main__':
    app.run(debug=True)