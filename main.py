#!/usr/bin/env python
from flask import Flask, render_template, Response, request, url_for, redirect, send_from_directory, jsonify, abort, flash, session
from werkzeug.utils import secure_filename
from nocache import nocache
from image_processing import crop, binarize, resize, face_detection, webcam
import os

path=os.path.abspath(__file__);
path2= os.path.dirname(path);
UPLOAD_DIRECTORY = path2+'/tmp'
if not os.path.exists(UPLOAD_DIRECTORY):
    os.makedirs(UPLOAD_DIRECTORY)

ALLOWED_EXTENSIONS = set(['.png','.jpg','.jpeg'])
def allowed_file(filename):
    return '.' in filename and \
      filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

app = Flask(__name__, static_folder=UPLOAD_DIRECTORY)
app.config['UPLOAD_FOLDER'] = UPLOAD_DIRECTORY
app.config['file_extension'] = '.png'

#upload file
@app.route('/uploads/<path:filename>')
def download_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)

#nocache
@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r

#homepage
@app.route('/')
def index():
    return render_template('index.html')
  

#upload de arquivos
@app.route('/upload_image/', methods = ['GET', 'POST', 'OPTIONS' ])
def upload_file():
  if request.method == 'POST':
    f = request.files['file']
    filename, file_extension = os.path.splitext(secure_filename(f.filename))
    f.save(os.path.join(UPLOAD_DIRECTORY, 'img'+file_extension))
    app.config['file_extension'] = file_extension
    return redirect(url_for('uploaded_image'))
  return render_template('upload_image.html')  

#operational page
@app.route('/uploaded_image/', methods = ['GET', 'POST'])
@nocache
def uploaded_image():
    file_ext=app.config['file_extension']
    img_name = 'img'+file_ext
    if request.method == 'POST':
      if request.form['submit_button'] == 'crop':
          x = int(request.form['x'])
          y = int(request.form['y'])
          dx = int(request.form['dx'])
          dy = int(request.form['dy'])
          img_name = os.path.join(UPLOAD_DIRECTORY,'img'+file_ext)
          crop.crop(img_name,x,y,dx,dy)
          return redirect(url_for('uploaded_image'))
      if request.form['submit_button'] == 'resize':
          x = int(request.form['x'])
          y = int(request.form['y'])
          img_name = os.path.join(UPLOAD_DIRECTORY,'img'+file_ext)
          resize.resize(img_name,x,y)            
          return redirect(url_for('uploaded_image'))
      if request.form['submit_button'] == 'binarize':
          r = int(request.form['r'])
          g = int(request.form['g'])
          b = int(request.form['b'])
          k = int(request.form['k'])
          img_name = os.path.join(UPLOAD_DIRECTORY,'img'+file_ext)
          binarize.binarize(img_name, r, g, b, k)
          return redirect(url_for('uploaded_image')) 
      if request.form['submit_button'] == 'face':
          scalef = float(request.form['scalef'])
          minnb = int(request.form['minnb'])
          img_name = os.path.join(UPLOAD_DIRECTORY,'img'+file_ext)
          face_detection.face_detection(img_name, scalef, minnb)
          return redirect(url_for('uploaded_image'))                       
      if request.form['submit_button'] == 'homepage':
          return redirect(url_for('index'))                           
    return render_template('uploaded_image.html', img = img_name, crop_img = 'crop_'+img_name, resize_img = 'resize_'+img_name, binarize_img = 'binarize_'+img_name, face_img = 'face_'+img_name)

# save the image as a picture
@app.route('/cam_rec', methods=['GET','POST'])
def cam_rec():
    if webcam.webcam():
    	return redirect(url_for('uploaded_image'))	

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True, use_reloader=True)

