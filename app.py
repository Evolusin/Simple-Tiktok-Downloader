from flask import Flask, render_template, request, send_file
import os
import yt_dlp as youtube_dl
import sched
import time
import uuid

app = Flask(__name__)
scheduler = sched.scheduler(time.time, time.sleep)

def delete_files():
    '''
    This function deletes all files in the downloads folder.
    '''
    folder = 'downloads'
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        if os.path.isfile(file_path):
            os.remove(file_path)

@app.route('/', methods=['GET', 'POST'])
def index():
    """
    This function handles the index route of the application.
    It accepts both GET and POST requests.
    If a POST request is received, it extracts the URL from the form data,
    downloads the video using youtube_dl library, renames the file to a unique
    filename, schedules a task to delete the file after 10 minutes, and returns
    the downloaded video as an attachment.
    If a GET request is received, it renders the index.html template.

    Returns:
        If a POST request is received and the video is downloaded successfully,
        it returns the downloaded video as an attachment.
        If any error occurs during the process, it returns an error message.
        If a GET request is received, it renders the index.html template.
    """
    if request.method == 'POST':
        url = request.form['url']
        try:
            # Configuration for youtube_dl
            ydl_opts = {
                'outtmpl': 'downloads/%(title)s.%(ext)s',
                'format': 'best'
            }
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                info_dict = ydl.extract_info(url, download=True)
                video_filename = ydl.prepare_filename(info_dict)
                # change name of file to uuid 
                new_filename = str(uuid.uuid4()) + '.mp4'
                os.rename(video_filename, 'downloads/' + new_filename)
                video_filename = 'downloads/' + new_filename
            # Run the delete_files function after 10 minutes
            scheduler.enter(600, 1, delete_files)

            return send_file(video_filename, as_attachment=True)
        except Exception as e:
            return f"Error: {e}"
    return render_template('index.html')

if __name__ == '__main__':
    # Create the downloads folder if it does not exist
    if not os.path.exists('downloads'):
        os.makedirs('downloads')
    app.run(debug=True)
