# face_recog_flask_server

Use virtualenv to create a virtual env with python version 3.7.0 

E.g.

virtualenv --python="C:\Users\panch\AppData\Local\Programs\Python\Python37\python.exe" fd3

Then activate the virtualenv.

Then, run pip install -r req.txt


The data should be post to the endpoint (given in the image) using multipart-form with files.

Success response:
{
  "results": true,
  "status": 1
}

Failure response:
{
  "results": false,
  "status": 1
}

Error respone:
{
  "error": "400 Bad Request: The browser (or proxy) sent a request that this server could not understand.",
  "status": 0
}

![image](https://user-images.githubusercontent.com/60831483/229718052-7c279773-f0d5-4b5a-ad85-e196055a7ed3.png)
