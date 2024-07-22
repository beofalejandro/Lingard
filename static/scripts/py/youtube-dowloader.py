from flask import Flask as fk, render_template as rt, request as rq
from pytube import YouTube
import os

app = fk(__name__)

# DOWNLOADER
@app.route('/youtube-download', methods=['POST'])
def youtube_dowload():
    # get the video link and the quality for this 
    url_link = str(rq.form['url_link'])
    video_quality = str(rq.form['video_quality'])

    try:
        # Set connection with youtube with get a video link
        yt = YouTube(url_link)
        stream = yt.streams.filter(res = video_quality).first()

        # Download in especific directory
        os.path.join('Downloads', f'{yt.title}.mp4')
        stream.download(output_path='Downloads')

        # return in the document
        return rt('index.html', result_download = 'Descargado Satisfactoriamente')
    except Exception as e:
        return rt('index.html', result_download = 'Hubo un error en la descarga del video')
