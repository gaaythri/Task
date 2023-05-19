import os

from flask import Flask, render_template, request
import ffmpeg

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():
    video_1 = request.files['video_1']
    video_2 = request.files['video_2']
    if not os.path.exists('static/videos'):
        os.makedirs('static/videos')
    if video_1.filename == '':
        return 'No video selected'
    if video_2.filename == '':
        return 'No video selected'
    video_1.save('static/videos/' + video_1.filename)
    video_2.save('static/videos/' + video_2.filename)
    video_1_meta = ffmpeg.probe('static/videos/' + video_1.filename)["streams"]
    video_2_meta = ffmpeg.probe('static/videos/' + video_2.filename)["streams"]
    return render_template('preview.html', video_name=video_1.filename, ref_name=video_2.filename,
                           video_1_meta=video_1_meta, video_2_meta=video_2_meta)


if __name__ == '__main__':
    app.run(debug=True)
