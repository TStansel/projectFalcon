from flask import Flask, render_template
import spotipy
from Song import Song

def playlistAdd(songResults):
    for i in songResults:
        if i.getAdded():
            addedSongs.append(i)
    return addedSongs

def playlistSort(addedSongs):
    for i in addedSongs:
        addedSongsScore.append(i.getScore())
    addedSongsScore.sort()
    addedSongsScore.reverse()
    temp=[]
    #go through sorted list of scores
    for i in addedSongsScore:
        #go through unsorted songs
        for j in range(len(addedSongs)):
            #check for same score
            if addedSongs[j].getScore()==i:
                #check for duplication
                if j>0 and len(temp) != 0:
                    if temp[j-1].getURI() != addedSongs[j].getURI():
                        temp.append(addedSongs[j])
                        continue
                else:
                    temp.append(addedSongs[j])
                    continue
    return temp

def searchCriteria(artistName,trackName,albumName):
    # if nothing
    if artistName == "" and trackName == "" and albumName == "":
        # do nothing
        results = ""

    # only album
    elif artistName == "" and trackName == "":
        results = spotify.search(q="album:" + albumName, limit=10, type="track")

    # only artist
    elif albumName == "" and trackName == "":
        results = spotify.search(q="artist:" + artistName, limit=10, type="track")

    # only track
    elif artistName == "" and albumName == "":
        results = spotify.search(q="track:" + trackName, limit=10, type="track")

    # no artist
    elif artistName == "":
        results = spotify.search(q="track:" + trackName + " album:" + albumName, limit=10, type="track")

    # no track
    elif trackName == "":
        results = spotify.search(q="artist:" + artistName + " album:" + albumName, limit=10, type="track")

    # no album
    elif albumName == "":
        results = spotify.search(q="artist:" + artistName + " track:" + trackName, limit=10, type="track")

    # everything
    else:
        results = spotify.search(q="album:" + albumName + " artist:" + artistName + " track:" + trackName, limit=10,
                                 type="track")
    return results

def searchToString(songResults):
    temp=""
    for i in songResults:
        temp += i.toString()+'\n'
    text = "<br />".join(temp.split("\n"))
    return text

app = Flask(__name__)

spotify = spotipy.Spotify()


uriResults = []
songResults = []
addedSongs = []
addedSongsScore = []

artistName="Imagine Dragons"
trackName="Radioactive"
albumName="Night Visions"


results=str(searchCriteria(artistName,trackName,albumName))

end=0
for i in range(10):
    start=results.find('track:',end)
    end=results.find("\'",start)
    uriResults.append("spotify:"+results[start:end])

for i in uriResults:
    if str(i).find('track:') != -1:
        temp = Song(i)
        songResults.append(temp)

songResults[0].makeAdded()
songResults[1].makeAdded()

songResults[1].upVote()

addedSongs=playlistAdd(songResults)

addedSongs=playlistSort(addedSongs)
"""
for i in addedSongs:
    print i.toString()

print len(songResults)
for i in songResults:
    print i.toString()

    '<p> <label>Artist:</label>' \
           '<textarea>cols = "80" > Testing </textarea></p>'

spotify = spotipy.Spotify()
songInfo = spotify.track(uriResults[0])
print songInfo['album']['name']
"""



@app.route('/')
def hello_world():
    return render_template('base.html')

@app.route('/search_results', methods=['POST'])
def searchResults():
    return searchToString(songResults)
if __name__ == '__main__':
    app.run()
