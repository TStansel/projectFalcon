from flask import Flask, render_template, request
import spotipy
from Song import Song

app = Flask(__name__)
app.config['DEBUG'] = True

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
            return render_template('base.html',name0=addedSongs[0].getName(), artist0=addedSongs[0].getArtist(), album0=addedSongs[0].getAlbum(),
                               score0=addedSongs[0].getScore(), name1=addedSongs[1].getName(), artist1=addedSongs[1].getArtist(), album1=addedSongs[1].getAlbum(),
                               score1=addedSongs[1].getScore(), name2=addedSongs[2].getName(), artist2=addedSongs[2].getArtist(), album2=addedSongs[2].getAlbum(),
                               score2=addedSongs[2].getScore(), name3=addedSongs[3].getName(), artist3=addedSongs[3].getArtist(), album3=addedSongs[3].getAlbum(),
                               score3=addedSongs[3].getScore(), name4=addedSongs[4].getName(), artist4=addedSongs[4].getArtist(), album4=addedSongs[4].getAlbum(),
                               score4=addedSongs[4].getScore(), name5=addedSongs[5].getName(), artist5=addedSongs[5].getArtist(), album5=addedSongs[5].getAlbum(),
                               score5=addedSongs[5].getScore(), name6=addedSongs[6].getName(), artist6=addedSongs[6].getArtist(), album6=addedSongs[6].getAlbum(),
                               score6=addedSongs[6].getScore(), name7=addedSongs[7].getName(), artist7=addedSongs[7].getArtist(), album7=addedSongs[7].getAlbum(),
                               score7=addedSongs[7].getScore(), name8=addedSongs[8].getName(), artist8=addedSongs[8].getArtist(), album8=addedSongs[8].getAlbum(),
                               score8=addedSongs[8].getScore(), name9=addedSongs[9].getName(), artist9=addedSongs[9].getArtist(), album9=addedSongs[9].getAlbum(),
                               score9=addedSongs[9].getScore())
    if len(addedSongs) == 9:
        return render_template('base.html', name0=addedSongs[0].getName(), artist0=addedSongs[0].getArtist(), album0=addedSongs[0].getAlbum(),
                               score0=addedSongs[0].getScore(), name1=addedSongs[1].getName(), artist1=addedSongs[1].getArtist(), album1=addedSongs[1].getAlbum(),
                               score1=addedSongs[1].getScore(), name2=addedSongs[2].getName(), artist2=addedSongs[2].getArtist(), album2=addedSongs[2].getAlbum(),
                               score2=addedSongs[2].getScore(), name3=addedSongs[3].getName(), artist3=addedSongs[3].getArtist(), album3=addedSongs[3].getAlbum(),
                               score3=addedSongs[3].getScore(), name4=addedSongs[4].getName(), artist4=addedSongs[4].getArtist(), album4=addedSongs[4].getAlbum(),
                               score4=addedSongs[4].getScore(), name5=addedSongs[5].getName(), artist5=addedSongs[5].getArtist(), album5=addedSongs[5].getAlbum(),
                               score5=addedSongs[5].getScore(), name6=addedSongs[6].getName(), artist6=addedSongs[6].getArtist(), album6=addedSongs[6].getAlbum(),
                               score6=addedSongs[6].getScore(), name7=addedSongs[7].getName(), artist7=addedSongs[7].getArtist(), album7=addedSongs[7].getAlbum(),
                               score7=addedSongs[7].getScore(), name8=addedSongs[8].getName(), artist8=addedSongs[8].getArtist(), album8=addedSongs[8].getAlbum(),
                               score8=addedSongs[8].getScore())
    if len(addedSongs) == 8:
        return render_template('base.html', name0=addedSongs[0].getName(), artist0=addedSongs[0].getArtist(), album0=addedSongs[0].getAlbum(),
                               score0=addedSongs[0].getScore(), name1=addedSongs[1].getName(), artist1=addedSongs[1].getArtist(), album1=addedSongs[1].getAlbum(),
                               score1=addedSongs[1].getScore(), name2=addedSongs[2].getName(), artist2=addedSongs[2].getArtist(), album2=addedSongs[2].getAlbum(),
                               score2=addedSongs[2].getScore(), name3=addedSongs[3].getName(), artist3=addedSongs[3].getArtist(), album3=addedSongs[3].getAlbum(),
                               score3=addedSongs[3].getScore(), name4=addedSongs[4].getName(), artist4=addedSongs[4].getArtist(), album4=addedSongs[4].getAlbum(),
                               score4=addedSongs[4].getScore(), name5=addedSongs[5].getName(), artist5=addedSongs[5].getArtist(), album5=addedSongs[5].getAlbum(),
                               score5=addedSongs[5].getScore(), name6=addedSongs[6].getName(), artist6=addedSongs[6].getArtist(), album6=addedSongs[6].getAlbum(),
                               score6=addedSongs[6].getScore(), name7=addedSongs[7].getName(), artist7=addedSongs[7].getArtist(), album7=addedSongs[7].getAlbum(),
                               score7=addedSongs[7].getScore())
    if len(addedSongs) == 7:
        return render_template('base.html', name0=addedSongs[0].getName(), artist0=addedSongs[0].getArtist(), album0=addedSongs[0].getAlbum(),
                               score0=addedSongs[0].getScore(), name1=addedSongs[1].getName(), artist1=addedSongs[1].getArtist(), album1=addedSongs[1].getAlbum(),
                               score1=addedSongs[1].getScore(), name2=addedSongs[2].getName(), artist2=addedSongs[2].getArtist(), album2=addedSongs[2].getAlbum(),
                               score2=addedSongs[2].getScore(), name3=addedSongs[3].getName(), artist3=addedSongs[3].getArtist(), album3=addedSongs[3].getAlbum(),
                               score3=addedSongs[3].getScore(), name4=addedSongs[4].getName(), artist4=addedSongs[4].getArtist(), album4=addedSongs[4].getAlbum(),
                               score4=addedSongs[4].getScore(), name5=addedSongs[5].getName(), artist5=addedSongs[5].getArtist(), album5=addedSongs[5].getAlbum(),
                               score5=addedSongs[5].getScore(), name6=addedSongs[6].getName(), artist6=addedSongs[6].getArtist(), album6=addedSongs[6].getAlbum(),
                               score6=addedSongs[6].getScore())
    if len(addedSongs) == 6:
        return render_template('base.html', name0=addedSongs[0].getName(), artist0=addedSongs[0].getArtist(), album0=addedSongs[0].getAlbum(),
                               score0=addedSongs[0].getScore(), name1=addedSongs[1].getName(), artist1=addedSongs[1].getArtist(), album1=addedSongs[1].getAlbum(),
                               score1=addedSongs[1].getScore(), name2=addedSongs[2].getName(), artist2=addedSongs[2].getArtist(), album2=addedSongs[2].getAlbum(),
                               score2=addedSongs[2].getScore(), name3=addedSongs[3].getName(), artist3=addedSongs[3].getArtist(), album3=addedSongs[3].getAlbum(),
                               score3=addedSongs[3].getScore(), name4=addedSongs[4].getName(), artist4=addedSongs[4].getArtist(), album4=addedSongs[4].getAlbum(),
                               score4=addedSongs[4].getScore(), name5=addedSongs[5].getName(), artist5=addedSongs[5].getArtist(), album5=addedSongs[5].getAlbum(),
                               score5=addedSongs[5].getScore())
    if len(addedSongs) == 5:
        return render_template('base.html',name0=addedSongs[0].getName(), artist0=addedSongs[0].getArtist(), album0=addedSongs[0].getAlbum(),
                               score0=addedSongs[0].getScore(), name1=addedSongs[1].getName(), artist1=addedSongs[1].getArtist(), album1=addedSongs[1].getAlbum(),
                               score1=addedSongs[1].getScore(), name2=addedSongs[2].getName(), artist2=addedSongs[2].getArtist(), album2=addedSongs[2].getAlbum(),
                               score2=addedSongs[2].getScore(), name3=addedSongs[3].getName(), artist3=addedSongs[3].getArtist(), album3=addedSongs[3].getAlbum(),
                               score3=addedSongs[3].getScore(), name4=addedSongs[4].getName(), artist4=addedSongs[4].getArtist(), album4=addedSongs[4].getAlbum(),
                               score4=addedSongs[4].getScore())
    if len(addedSongs) == 4:
        return render_template('base.html',name0=addedSongs[0].getName(), artist0=addedSongs[0].getArtist(), album0=addedSongs[0].getAlbum(),
                               score0=addedSongs[0].getScore(), name1=addedSongs[1].getName(), artist1=addedSongs[1].getArtist(), album1=addedSongs[1].getAlbum(),
                               score1=addedSongs[1].getScore(), name2=addedSongs[2].getName(), artist2=addedSongs[2].getArtist(), album2=addedSongs[2].getAlbum(),
                               score2=addedSongs[2].getScore(), name3=addedSongs[3].getName(), artist3=addedSongs[3].getArtist(), album3=addedSongs[3].getAlbum(),
                               score3=addedSongs[3].getScore())
    if len(addedSongs) == 3:
        return render_template('base.html', name0=addedSongs[0].getName(), artist0=addedSongs[0].getArtist(), album0=addedSongs[0].getAlbum(),
                               score0=addedSongs[0].getScore(), name1=addedSongs[1].getName(), artist1=addedSongs[1].getArtist(), album1=addedSongs[1].getAlbum(),
                               score1=addedSongs[1].getScore(), name2=addedSongs[2].getName(), artist2=addedSongs[2].getArtist(), album2=addedSongs[2].getAlbum(),
                               score2=addedSongs[2].getScore())
    if len(addedSongs) == 2:
        return render_template('base.html', name0=addedSongs[0].getName(), artist0=addedSongs[0].getArtist(), album0=addedSongs[0].getAlbum(),
                               score0=addedSongs[0].getScore(), name1=addedSongs[1].getName(), artist1=addedSongs[1].getArtist(), album1=addedSongs[1].getAlbum(),
                               score1=addedSongs[1].getScore())
    if len(addedSongs) == 1:
        return render_template('base.html', name0=addedSongs[0].getName(), artist0=addedSongs[0].getArtist(), album0=addedSongs[0].getAlbum(),
                               score0=addedSongs[0].getScore())



@app.route('/search_results', methods=['POST'])
def searchResults():
    render_template('search_results.html')
    ar = request.form['artist']
    tr = request.form['track']
    al = request.form['album']
    results = str(searchCriteria(ar,tr,al))
    songResults= testing(results)
    if len(songResults) == 0:
        return render_template('search_results.html',artist0='',album0 = '',name0='',score0='',artist1='',album1 = '',name1='',score1='',artist2='',album2 = '',name2='',score2='',artist3='',album3 = '',name3='',score3='',artist4='',album4 = '',name4='',score4='',artist5='',album5 = '',name5='',score5='',artist6='',album6 = '',name6='',score6='',artist7='',album7 = '',name7='',score7='',artist8='',album8 = '',name8='',score8='',artist9='',album9 = '',name9='',score9='')
    if len(songResults) >=10:
            return render_template('search_results.html', name0=songResults[0].getName(), artist0=songResults[0].getArtist(), album0=songResults[0].getAlbum(),
                               score0=songResults[0].getScore(), name1=songResults[1].getName(), artist1=songResults[1].getArtist(), album1=songResults[1].getAlbum(),
                               score1=songResults[1].getScore(), name2=songResults[2].getName(), artist2=songResults[2].getArtist(), album2=songResults[2].getAlbum(),
                               score2=songResults[2].getScore(), name3=songResults[3].getName(), artist3=songResults[3].getArtist(), album3=songResults[3].getAlbum(),
                               score3=songResults[3].getScore(), name4=songResults[4].getName(), artist4=songResults[4].getArtist(), album4=songResults[4].getAlbum(),
                               score4=songResults[4].getScore(), name5=songResults[5].getName(), artist5=songResults[5].getArtist(), album5=songResults[5].getAlbum(),
                               score5=songResults[5].getScore(), name6=songResults[6].getName(), artist6=songResults[6].getArtist(), album6=songResults[6].getAlbum(),
                               score6=songResults[6].getScore(), name7=songResults[7].getName(), artist7=songResults[7].getArtist(), album7=songResults[7].getAlbum(),
                               score7=songResults[7].getScore(), name8=songResults[8].getName(), artist8=songResults[8].getArtist(), album8=songResults[8].getAlbum(),
                               score8=songResults[8].getScore(), name9=songResults[9].getName(), artist9=songResults[9].getArtist(), album9=songResults[9].getAlbum(),
                               score9=songResults[9].getScore())
    if len(songResults) == 9:
        return render_template('search_results.html',name0=songResults[0].getName(), artist0=songResults[0].getArtist(), album0=songResults[0].getAlbum(),
                               score0=songResults[0].getScore(), name1=songResults[1].getName(), artist1=songResults[1].getArtist(), album1=songResults[1].getAlbum(),
                               score1=songResults[1].getScore(), name2=songResults[2].getName(), artist2=songResults[2].getArtist(), album2=songResults[2].getAlbum(),
                               score2=songResults[2].getScore(), name3=songResults[3].getName(), artist3=songResults[3].getArtist(), album3=songResults[3].getAlbum(),
                               score3=songResults[3].getScore(), name4=songResults[4].getName(), artist4=songResults[4].getArtist(), album4=songResults[4].getAlbum(),
                               score4=songResults[4].getScore(), name5=songResults[5].getName(), artist5=songResults[5].getArtist(), album5=songResults[5].getAlbum(),
                               score5=songResults[5].getScore(), name6=songResults[6].getName(), artist6=songResults[6].getArtist(), album6=songResults[6].getAlbum(),
                               score6=songResults[6].getScore(), name7=songResults[7].getName(), artist7=songResults[7].getArtist(), album7=songResults[7].getAlbum(),
                               score7=songResults[7].getScore(), name8=songResults[8].getName(), artist8=songResults[8].getArtist(), album8=songResults[8].getAlbum(),
                               score8=songResults[8].getScore())
    if len(songResults) == 8:
        return render_template('search_results.html',name0=songResults[0].getName(), artist0=songResults[0].getArtist(), album0=songResults[0].getAlbum(),
                               score0=songResults[0].getScore(), name1=songResults[1].getName(), artist1=songResults[1].getArtist(), album1=songResults[1].getAlbum(),
                               score1=songResults[1].getScore(), name2=songResults[2].getName(), artist2=songResults[2].getArtist(), album2=songResults[2].getAlbum(),
                               score2=songResults[2].getScore(), name3=songResults[3].getName(), artist3=songResults[3].getArtist(), album3=songResults[3].getAlbum(),
                               score3=songResults[3].getScore(), name4=songResults[4].getName(), artist4=songResults[4].getArtist(), album4=songResults[4].getAlbum(),
                               score4=songResults[4].getScore(), name5=songResults[5].getName(), artist5=songResults[5].getArtist(), album5=songResults[5].getAlbum(),
                               score5=songResults[5].getScore(), name6=songResults[6].getName(), artist6=songResults[6].getArtist(), album6=songResults[6].getAlbum(),
                               score6=songResults[6].getScore(), name7=songResults[7].getName(), artist7=songResults[7].getArtist(), album7=songResults[7].getAlbum(),
                               score7=songResults[7].getScore())
    if len(songResults) == 7:
        return render_template('search_results.html',name0=songResults[0].getName(), artist0=songResults[0].getArtist(), album0=songResults[0].getAlbum(),
                               score0=songResults[0].getScore(), name1=songResults[1].getName(), artist1=songResults[1].getArtist(), album1=songResults[1].getAlbum(),
                               score1=songResults[1].getScore(), name2=songResults[2].getName(), artist2=songResults[2].getArtist(), album2=songResults[2].getAlbum(),
                               score2=songResults[2].getScore(), name3=songResults[3].getName(), artist3=songResults[3].getArtist(), album3=songResults[3].getAlbum(),
                               score3=songResults[3].getScore(), name4=songResults[4].getName(), artist4=songResults[4].getArtist(), album4=songResults[4].getAlbum(),
                               score4=songResults[4].getScore(), name5=songResults[5].getName(), artist5=songResults[5].getArtist(), album5=songResults[5].getAlbum(),
                               score5=songResults[5].getScore(), name6=songResults[6].getName(), artist6=songResults[6].getArtist(), album6=songResults[6].getAlbum(),
                               score6=songResults[6].getScore())
    if len(songResults) == 6:
        return render_template('search_results.html',name0=songResults[0].getName(), artist0=songResults[0].getArtist(), album0=songResults[0].getAlbum(),
                               score0=songResults[0].getScore(), name1=songResults[1].getName(), artist1=songResults[1].getArtist(), album1=songResults[1].getAlbum(),
                               score1=songResults[1].getScore(), name2=songResults[2].getName(), artist2=songResults[2].getArtist(), album2=songResults[2].getAlbum(),
                               score2=songResults[2].getScore(), name3=songResults[3].getName(), artist3=songResults[3].getArtist(), album3=songResults[3].getAlbum(),
                               score3=songResults[3].getScore(), name4=songResults[4].getName(), artist4=songResults[4].getArtist(), album4=songResults[4].getAlbum(),
                               score4=songResults[4].getScore(), name5=songResults[5].getName(), artist5=songResults[5].getArtist(), album5=songResults[5].getAlbum(),
                               score5=songResults[5].getScore())
    if len(songResults) == 5:
        return render_template('search_results.html',name0=songResults[0].getName(), artist0=songResults[0].getArtist(), album0=songResults[0].getAlbum(),
                               score0=songResults[0].getScore(), name1=songResults[1].getName(), artist1=songResults[1].getArtist(), album1=songResults[1].getAlbum(),
                               score1=songResults[1].getScore(), name2=songResults[2].getName(), artist2=songResults[2].getArtist(), album2=songResults[2].getAlbum(),
                               score2=songResults[2].getScore(), name3=songResults[3].getName(), artist3=songResults[3].getArtist(), album3=songResults[3].getAlbum(),
                               score3=songResults[3].getScore(), name4=songResults[4].getName(), artist4=songResults[4].getArtist(), album4=songResults[4].getAlbum(),
                               score4=songResults[4].getScore())
    if len(songResults) == 4:
        return render_template('search_results.html',name0=songResults[0].getName(), artist0=songResults[0].getArtist(), album0=songResults[0].getAlbum(),
                               score0=songResults[0].getScore(), name1=songResults[1].getName(), artist1=songResults[1].getArtist(), album1=songResults[1].getAlbum(),
                               score1=songResults[1].getScore(), name2=songResults[2].getName(), artist2=songResults[2].getArtist(), album2=songResults[2].getAlbum(),
                               score2=songResults[2].getScore(), name3=songResults[3].getName(), artist3=songResults[3].getArtist(), album3=songResults[3].getAlbum(),
                               score3=songResults[3].getScore())
    if len(songResults) == 3:
        return render_template('search_results.html',name0=songResults[0].getName(), artist0=songResults[0].getArtist(), album0=songResults[0].getAlbum(),
                               score0=songResults[0].getScore(), name1=songResults[1].getName(), artist1=songResults[1].getArtist(), album1=songResults[1].getAlbum(),
                               score1=songResults[1].getScore(), name2=songResults[2].getName(), artist2=songResults[2].getArtist(), album2=songResults[2].getAlbum(),
                               score2=songResults[2].getScore())
    if len(songResults) == 2:
        return render_template('search_results.html',name0=songResults[0].getName(), artist0=songResults[0].getArtist(), album0=songResults[0].getAlbum(),
                               score0=songResults[0].getScore(), name1=songResults[1].getName(), artist1=songResults[1].getArtist(), album1=songResults[1].getAlbum(),
                               score1=songResults[1].getScore())
    if len(songResults) == 1:
        return render_template('search_results.html',name0=songResults[0].getName(), artist0=songResults[0].getArtist(), album0=songResults[0].getAlbum(),
                               score0=songResults[0].getScore())

@app.route('/add', methods=['GET'])
def addingSongs():
        if request.method == 'GET':
            btnID = request.form['btn']
        if btnID == '0':
            songResults[0].upVote()
            addedSongs.append(songResults[0])
            songResults.remove(0)
        if btnID == '1':
            songResults[1].upVote()
            addedSongs.append(songResults[1])
            songResults.remove(1)
        if btnID == '2':
            songResults[2].upVote()
            addedSongs.append(songResults[2])
            songResults.remove(2)
        if btnID == '3':
            songResults[3].upVote()
            addedSongs.append(songResults[3])
            songResults.remove(3)
        if btnID == '4':
            songResults[4].upVote()
            addedSongs.append(songResults[4])
            songResults.remove(4)
        if btnID == '5':
            songResults[5].upVote()
            addedSongs.append(songResults[5])
            songResults.remove(5)
        if btnID == '6':
            songResults[6].upVote()
            addedSongs.append(songResults[6])
            songResults.remove(6)
        if btnID == '7':
            songResults[7].upVote()
            addedSongs.append(songResults[7])
            songResults.remove(7)
        if btnID == '8':
            songResults[8].upVote()
            addedSongs.append(songResults[8])
            songResults.remove(8)
        if btnID == '9':
            songResults[9].upVote()
            addedSongs.append(songResults[9])
            songResults.remove(9)
        return render_template('base.html')
@app.route('/vote',methods=['POST'])
def trackVoting():
    return 'vote test'
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
    return songResults

addedSongs = playlistAdd(songResults)

addedSongs = playlistSort(addedSongs) # final playlist


if __name__ == '__main__':
    app.run()
