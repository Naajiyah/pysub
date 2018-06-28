import subscene, requests,zipfile,io

def searchSubtitles(title, language='ALL'):
    try:
        film = subscene.search(title)
        return film.subtitles if language == 'ALL' else [sub for sub in film.subtitles if sub.language.lower()==language.lower()]
    except(urllib.error.HTTPError,urllib.error.URLError):
        print("Error")

def downloadSubtitle(subtitle, movie_directory, download_directory):
    r = requests.get(subtitle.zipped_url)
    if r.ok:
        z = zipfile.ZipFile(io.BytesIO(r.content))
        z.extractall(download_directory+movie_directory)

