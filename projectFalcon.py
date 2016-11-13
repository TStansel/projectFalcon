from flask import Flask, render_template, request
import spotipy
from Song import Song

app = Flask(__name__)

@app.route('/')
def hello_world():
    if request.method == 'POST"':
        if request.form['vote1'] == 'Up':
            addedSongs[0].upVote()
        elif request.form['vote1'] == 'Down':
            addedSongs[0].downVote()
    if len(addedSongs) == 0:
        return render_template('base.html',artist0='',album0 = '',name0='',score0='',artist1='',album1 = '',name1='',score1='',artist2='',album2 = '',name2='',score2='',artist3='',album3 = '',name3='',score3='',artist4='',album4 = '',name4='',score4='',artist5='',album5 = '',name5='',score5='',artist6='',album6 = '',name6='',score6='',artist7='',album7 = '',name7='',score7='',artist8='',album8 = '',name8='',score8='',artist9='',album9 = '',name9='',score9='')
    if len(addedSongs) >=10:
            return render_template('base.html',name0= addedSongs[0],artist0= addedSongs[0],album0= addedSongs[0],score0=addedSongs[0],name1 = addedSongs[1],artist1 = addedSongs[1],album1 = addedSongs[1],score1 = addedSongs[1],name2 = addedSongs[2],artist2 = addedSongs[2],album2 = addedSongs[2],score2 = addedSongs[2],name3 = addedSongs[3],artist3 = addedSongs[3],album3 = addedSongs[3],score3 = addedSongs[3],name4 = addedSongs[4],artist4 = addedSongs[4],album4 = addedSongs[4],score4 = addedSongs[4],name5 = addedSongs[5],artist5 = addedSongs[5],album5 = addedSongs[5],score5 = addedSongs[5],name6 = addedSongs[6],artist6 = addedSongs[6],album6 = addedSongs[6],score6 = addedSongs[6], name7 = addedSongs[7],artist7 = addedSongs[7],album7 = addedSongs[7],score7 = addedSongs[7], name8 = addedSongs[8],artist8 = addedSongs[8], album8 = addedSongs[8],score8 = addedSongs[8], name9 = addedSongs[9],artist9 = addedSongs[9],album9 = addedSongs[9],score9 = addedSongs[9])
    if len(addedSongs) == 9:
        return render_template('base.html', name0=addedSongs[0], artist0=addedSongs[0], album0=addedSongs[0],
                               score0=addedSongs[0], name1=addedSongs[1], artist1=addedSongs[1], album1=addedSongs[1],
                               score1=addedSongs[1], name2=addedSongs[2], artist2=addedSongs[2], album2=addedSongs[2],
                               score2=addedSongs[2], name3=addedSongs[3], artist3=addedSongs[3], album3=addedSongs[3],
                               score3=addedSongs[3], name4=addedSongs[4], artist4=addedSongs[4], album4=addedSongs[4],
                               score4=addedSongs[4], name5=addedSongs[5], artist5=addedSongs[5], album5=addedSongs[5],
                               score5=addedSongs[5], name6=addedSongs[6], artist6=addedSongs[6], album6=addedSongs[6],
                               score6=addedSongs[6], name7=addedSongs[7], artist7=addedSongs[7], album7=addedSongs[7],
                               score7=addedSongs[7], name8=addedSongs[8], artist8=addedSongs[8], album8=addedSongs[8],
                               score8=addedSongs[8])
    if len(addedSongs) == 8:
        return render_template('base.html', name0=addedSongs[0], artist0=addedSongs[0], album0=addedSongs[0],
                               score0=addedSongs[0], name1=addedSongs[1], artist1=addedSongs[1], album1=addedSongs[1],
                               score1=addedSongs[1], name2=addedSongs[2], artist2=addedSongs[2], album2=addedSongs[2],
                               score2=addedSongs[2], name3=addedSongs[3], artist3=addedSongs[3], album3=addedSongs[3],
                               score3=addedSongs[3], name4=addedSongs[4], artist4=addedSongs[4], album4=addedSongs[4],
                               score4=addedSongs[4], name5=addedSongs[5], artist5=addedSongs[5], album5=addedSongs[5],
                               score5=addedSongs[5], name6=addedSongs[6], artist6=addedSongs[6], album6=addedSongs[6],
                               score6=addedSongs[6], name7=addedSongs[7], artist7=addedSongs[7], album7=addedSongs[7],
                               score7=addedSongs[7])
    if len(addedSongs) == 7:
        return render_template('base.html', name0=addedSongs[0], artist0=addedSongs[0], album0=addedSongs[0],
                               score0=addedSongs[0], name1=addedSongs[1], artist1=addedSongs[1], album1=addedSongs[1],
                               score1=addedSongs[1], name2=addedSongs[2], artist2=addedSongs[2], album2=addedSongs[2],
                               score2=addedSongs[2], name3=addedSongs[3], artist3=addedSongs[3], album3=addedSongs[3],
                               score3=addedSongs[3], name4=addedSongs[4], artist4=addedSongs[4], album4=addedSongs[4],
                               score4=addedSongs[4], name5=addedSongs[5], artist5=addedSongs[5], album5=addedSongs[5],
                               score5=addedSongs[5], name6=addedSongs[6], artist6=addedSongs[6], album6=addedSongs[6],
                               score6=addedSongs[6])
    if len(addedSongs) == 6:
        return render_template('base.html', name0=addedSongs[0], artist0=addedSongs[0], album0=addedSongs[0],
                               score0=addedSongs[0], name1=addedSongs[1], artist1=addedSongs[1], album1=addedSongs[1],
                               score1=addedSongs[1], name2=addedSongs[2], artist2=addedSongs[2], album2=addedSongs[2],
                               score2=addedSongs[2], name3=addedSongs[3], artist3=addedSongs[3], album3=addedSongs[3],
                               score3=addedSongs[3], name4=addedSongs[4], artist4=addedSongs[4], album4=addedSongs[4],
                               score4=addedSongs[4], name5=addedSongs[5], artist5=addedSongs[5], album5=addedSongs[5],
                               score5=addedSongs[5])
    if len(addedSongs) == 5:
        return render_template('base.html', name0=addedSongs[0], artist0=addedSongs[0], album0=addedSongs[0],
                               score0=addedSongs[0], name1=addedSongs[1], artist1=addedSongs[1], album1=addedSongs[1],
                               score1=addedSongs[1], name2=addedSongs[2], artist2=addedSongs[2], album2=addedSongs[2],
                               score2=addedSongs[2], name3=addedSongs[3], artist3=addedSongs[3], album3=addedSongs[3],
                               score3=addedSongs[3], name4=addedSongs[4], artist4=addedSongs[4], album4=addedSongs[4],
                               score4=addedSongs[4])
    if len(addedSongs) == 4:
        return render_template('base.html', name0=addedSongs[0], artist0=addedSongs[0], album0=addedSongs[0],
                               score0=addedSongs[0], name1=addedSongs[1], artist1=addedSongs[1], album1=addedSongs[1],
                               score1=addedSongs[1], name2=addedSongs[2], artist2=addedSongs[2], album2=addedSongs[2],
                               score2=addedSongs[2], name3=addedSongs[3], artist3=addedSongs[3], album3=addedSongs[3],
                               score3=addedSongs[3])
    if len(addedSongs) == 3:
        return render_template('base.html', name0=addedSongs[0], artist0=addedSongs[0], album0=addedSongs[0],
                               score0=addedSongs[0], name1=addedSongs[1], artist1=addedSongs[1], album1=addedSongs[1],
                               score1=addedSongs[1], name2=addedSongs[2], artist2=addedSongs[2], album2=addedSongs[2],
                               score2=addedSongs[2])
    if len(addedSongs) == 2:
        return render_template('base.html', name0=addedSongs[0], artist0=addedSongs[0], album0=addedSongs[0],
                               score0=addedSongs[0], name1=addedSongs[1], artist1=addedSongs[1], album1=addedSongs[1],
                               score1=addedSongs[1])
    if len(addedSongs) == 1:
        return render_template('base.html', name0=addedSongs[0], artist0=addedSongs[0], album0=addedSongs[0],
                               score0=addedSongs[0])



@app.route('/search_results', methods=['POST'])
def searchResults():
    render_template('search_results.html')
    ar = request.form['artist']
    tr = request.form['track']
    al = request.form['album']
    results = str(searchCriteria(ar,tr,al))
    return testing(results)

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
        results = spotify.search(q="ytrack:" + trackName + " album:" + albumName, limit=10, type="track")

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



spotify = spotipy.Spotify()

uriResults = []
songResults = []
addedSongs = []
addedSongsScore = []

def testing (res):
    end = 0
    songResults = []
    uriResults = []
    for i in range(10):
        start = res.find('track:', end)
        end = res.find("\'", start)
        uriResults.append("spotify:" + res[start:end])

    for i in uriResults:
        if str(i).find('track:') != -1:
            temp = Song(i)
            songResults.append(temp)
    return searchToString(songResults)

addedSongs = playlistAdd(songResults)

addedSongs = playlistSort(addedSongs) # final playlist


if __name__ == '__main__':
    app.run()
