from flask import Flask as fk, render_template as rt, request as rq
from pytube import YouTube # temporally
import os # temporally

app = fk(__name__)

# index
@app.route('/')
def index():
    return rt('index.html')

@app.route('/youtube-downloader')
def youtube_downloader():
    return rt('pages/youtube-downloader.html')

# TODO: SEND THE FOLLOWING CODE TO THE NEW UBICATION IN /scripts/py/youtube-downloader ***CLEAR CODE***
@app.route('/youtube-download', methods=['POST'])
def youtube_dowload():
    # get video parameters here from html
    url_link = str(rq.form['url_link'])
    video_quality = str(rq.form['video_quality'])

    # FIXME: (18-07-2024) THE USER WILL INSERT THE C: DIRECTORY TO GO THE VIDEO DOWNLOADED
    # FIXME: (18-07-2024) SEE THE OPTIONS UNAVALIABLES
    # TODO: (18-07-2024) ADD MORE DOWNLOAD OPTIONS
    try:
        # Set connection with youtube with get a video link
        yt = YouTube(url_link)
        stream = yt.streams.filter(res = video_quality).first()

        # Download in especific directory
        os.path.join('Downloads', f'{yt.title}.mp4')
        stream.download(output_path='Downloads')

        return rt('pages/youtube-downloader.html', result_download = 'Descargado Satisfactoriamente')
    except Exception as e:
        return rt('pages/youtube-downloader.html', result_download = 'Hubo un error en la descarga del video')


if __name__ == '__main__':
    app.run(debug=True, port=4000)