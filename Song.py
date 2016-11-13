import spotipy
class Song:

    def __int__(self,uri,artist,name,score,added,length,expli):
        self.uri = uri
        self.artist = artist
        self.name = name
        self.score = score
        self.added = added
        self.length = length
        self.explicit = expli
    def __init__(self,uri):
        self.uri = uri
        spotify = spotipy.Spotify()
        songInfo = spotify.track(self.uri)
        self.artist = []
        for x in songInfo['artists']:
            self.artist.append(x['name'])
        self.name = songInfo['name']
        self.score = 0
        self.length = songInfo['duration_ms'] / 1000
        self.explicit = songInfo['explicit']
        self.album = songInfo['album']['name']
        self.added=False

    def toString(self):
        woo = 'Name: '+self.name+' Artist: '+self.artistsToString()+' Album: '+self.album
        return woo

    def getAdded (self):
        return self.added
    def getAlbum(self):
        return self.album
    def getURI(self):
        return self.uri
    def getArtist(self):
        return self.artistsToString()
    def getName(self):
        return self.name
    def getExplicit(self):
        return self.explicit
    def getScore(self):
        return self.score
    def getLength(self):
        return self.length
    def upVote(self):
        self.score = self.score+1
    def downVote(self):
        self.score = self.score-1
    def makeAdded(self):
        self.added=True
        self.score=1
    def artistsToString(self):
        str = ""
        if len(self.artist) != 1:
            for i in self.artist:
             str= str+ i +','
        else:
            str = self.artist[0]
        return str
