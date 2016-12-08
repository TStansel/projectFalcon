from flask import Flask, render_template, request,url_for,redirect
import spotipy
from Song import Song

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def hello_world():
    global addedSongs
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
    global songResults
    ar = request.form['artist']
    tr = request.form['track']
    al = request.form['album']
    results = str(searchCriteria(ar,tr,al))

    songResults= testing(results)
    playlistSearch()

    if len(songResults) == 0:
        return render_template('base.html',artist0='',album0 = '',name0='',score0='',artist1='',album1 = '',name1='',score1='',artist2='',album2 = '',name2='',score2='',artist3='',album3 = '',name3='',score3='',artist4='',album4 = '',name4='',score4='',artist5='',album5 = '',name5='',score5='',artist6='',album6 = '',name6='',score6='',artist7='',album7 = '',name7='',score7='',artist8='',album8 = '',name8='',score8='',artist9='',album9 = '',name9='',score9='')
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


@app.route('/add', methods=['POST'])
def addingSongs():
        global songResults
        global addedSongs
        btnID = request.form['Add']
        if btnID == 'Add0':
            songResults[0].upVote()
            addedSongs.append(songResults[0])
            songResults.remove(songResults[0])
        if btnID == 'Add1':
            songResults[1].upVote()
            addedSongs.append(songResults[1])
            songResults.remove(songResults[1])
        if btnID == 'Add2':
            songResults[2].upVote()
            addedSongs.append(songResults[2])
            songResults.remove(songResults[2])
        if btnID == 'Add3':
            songResults[3].upVote()
            addedSongs.append(songResults[3])
            songResults.remove(songResults[3])
        if btnID == 'Add4':
            songResults[4].upVote()
            addedSongs.append(songResults[4])
            songResults.remove(songResults[4])
        if btnID == 'Add5':
            songResults[5].upVote()
            addedSongs.append(songResults[5])
            songResults.remove(songResults[5])
        if btnID == 'Add6':
            songResults[6].upVote()
            addedSongs.append(songResults[6])
            songResults.remove(songResults[6])
        if btnID == 'Add7':
            songResults[7].upVote()
            addedSongs.append(songResults[7])
            songResults.remove(songResults[7])
        if btnID == 'Add8':
            songResults[8].upVote()
            addedSongs.append(songResults[8])
            songResults.remove(songResults[8])
        if btnID == 'Add9':
            songResults[9].upVote()
            addedSongs.append(songResults[9])
            songResults.remove(songResults[9])
        btnID = 'waiting'
        return hello_world()
@app.route('/vote',methods=['POST'])
def trackVoting():
    global addedSongs
    voteID = request.form['vote']
    if voteID == 'Up0':
        addedSongs[0].upVote()
    if voteID == 'Down0':
        addedSongs[0].downVote()
    if voteID == 'Up1':
        addedSongs[1].upVote()
    if voteID == 'Down1':
        addedSongs[1].downVote()
    if voteID == 'Up2':
        addedSongs[2].upVote()
    if voteID == 'Down2':
        addedSongs[2].downVote()
    if voteID == 'Up3':
        addedSongs[3].upVote()
    if voteID == 'Down3':
        addedSongs[3].downVote()
    if voteID == 'Up4':
        addedSongs[4].upVote()
    if voteID == 'Down4':
        addedSongs[4].downVote()
    if voteID == 'Up5':
        addedSongs[5].upVote()
    if voteID == 'Down5':
        addedSongs[5].downVote()
    if voteID == 'Up6':
        addedSongs[6].upVote()
    if voteID == 'Down6':
        addedSongs[6].downVote()
    if voteID == 'Up7':
        addedSongs[7].upVote()
    if voteID == 'Down7':
        addedSongs[7].downVote()
    if voteID == 'Up8':
        addedSongs[8].upVote()
    if voteID == 'Down8':
        addedSongs[8].downVote()
    if voteID == 'Up9':
        addedSongs[9].upVote()
    if voteID == 'Down9':
        addedSongs[9].downVote()
    voteID = 'waiting'
    addedSongs = playlistSort(addedSongs)
    return hello_world()


def playlistAdd(results):
    global addedSongs
    for i in results:
        if i.getAdded():
            addedSongs.append(i)
    return addedSongs

def playlistSearch():
    global addedSongs
    global songResults
    for results in songResults:
        for addsong in addedSongs:
            if addsong.getURI()==results.getURI():
                songResults.pop(songResults.index(results))

def swap(addedSongs,idx1,idx2):
    temp = addedSongs[idx1]
    addedSongs[idx1] = addedSongs[idx2]
    addedSongs[idx2] = temp

def playlistSort(addedSongs):
    print 'sorting'
    global addedSongsScore
    for i in addedSongs:
        addedSongsScore.append(i.getScore())
    temp=addedSongs
    newMax = False
    if len(addedSongs) >1:
         #go through sorted list of scores
         for i in range(len(addedSongs)-1):
            print 'first loop'
            maxIdx = i
            j = i+1
            while j<len(addedSongs):
                if temp[j].getScore()>temp[i].getScore():
                    print 'new max'
                    maxIdx = j
                    newMax = True
                j = j+1
            if newMax:
                swap(temp,i,maxIdx)
                print 'swapped'
            newMax = False
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
addedSongs = []
addedSongsScore = []
songResults = []


def testing (res):
    global songResults
    global uriResults
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

def setSongResults(results):
    global songResults
    songResults = results


def setAddedSongs(songs):
    global addedSongs
    addedSongs = songs

if __name__ == '__main__':
    app.run(debug=True)
