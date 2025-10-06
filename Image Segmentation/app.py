from flask import Flask, render_template, request, redirect
import cv2
import os
import numpy as np
from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_FOLDER = 'C:/Users/Joel John Joseph/Desktop/Trimester5/IA/CAC2'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def segment_image(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, thresholded = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY)
    edges = cv2.Canny(gray, 50, 150)
    
    mask = np.zeros(image.shape[:2], np.uint8)
    rect = (50, 50, image.shape[1] - 50, image.shape[0] - 50)
    bgd_model = np.zeros((1, 65), np.float64)
    fgd_model = np.zeros((1, 65), np.float64)
    cv2.grabCut(image, mask, rect, bgd_model, fgd_model, 5, cv2.GC_INIT_WITH_RECT)
    mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')
    result_grabcut = image * mask2[:, :, np.newaxis]

    return thresholded, edges, result_grabcut

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(file.filename))
            file.save(filename)

            thresholded, edges, result_grabcut = segment_image(filename)

            return render_template('result.html',
                                   original_image=filename,
                                   thresholded_image=filename + '_thresholded.jpg',
                                   edges_image=filename + '_edges.jpg',
                                   grabcut_image=filename + '_grabcut.jpg')

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
