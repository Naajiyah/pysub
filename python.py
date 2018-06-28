import subscene, requests,zipfile,io

parser = argparse.ArgumentParser('This is a program that downloads movie subtitles from subscene.com')
parser.add_argument('-lang', dest='language', default=DEFAULT_LANGUAGE, help='The language of the subtitles to be downloaded. Default is ' + DEFAULT_LANGUAGE)
parser.add_argument('-dir', dest='folder', default=DEFAULT_SCAN_FOLDER, help='Folder to be scanned for movies. Also the download folder. Default is ' + DEFAULT_SCAN_FOLDER)
args = parser.parse_args()

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

def searchAndDownloadSubtitle(movie_name, download_directory, language='English'):
    subtitles = searchSubtitles(movie_name, language)
    if not subtitles is None:
        downloadSubtitle(subtitles[0], movie_name, download_directory)

print("Downloads Started...")
[searchAndDownloadSubtitle(movie_name, args.folder, args.language) for movie_name in os.listdir(args.folder)]
print("...Downloads Finished")
