from flask import Flask as fk, render_template as rt, request as rq
from pytube import YouTube # temporally
import os # temporally

app = fk(__name__)

# index
@app.route('/')
def index():
    return rt('index.html')

@app.route('/python-youtube-download')
def youtube_downloader():
    return rt('pages/youtube-downloader.html')

# TODO: SEND THE FOLLOWING CODE TO THE NEW UBICATION IN /scripts/py/youtube-downloader ***CLEAR CODE***
# FIXME: (18-07-2024) THE USER WILL INSERT THE C: DIRECTORY TO GO THE VIDEO DOWNLOADED
# FIXME: (18-07-2024) SEE THE OPTIONS UNAVALIABLES
# TODO: (18-07-2024) ADD MORE DOWNLOAD OPTIONS
@app.route('/videodownload', methods=['POST'])
def videodownloader():
    url_link = str(rq.form['url_link'])
    video_quality = str(rq.form['video_quality'])
    try:
        # Set connection with youtube with get a video
        yt = YouTube(url_link)
        stream = yt.streams.filter(res = video_quality).first()
        os.path.join('Downloads', f'{yt.title}.mp4')
        stream.download(output_path='Downloads')

        return rt('pages/youtube-downloader.html', download_status = 'Descargado Satisfactoriamente')
    except Exception as e:
        return rt('pages/youtube-downloader.html', download_status = f'Error en la descarga del video, Error: {str(e)}')


if __name__ == '__main__':
    app.run(port=5000, debug=True)