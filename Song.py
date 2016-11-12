import spotipy
class Song:

    def __int__(self,uri,artist,name,genre,score,added,length):
        self.uri = uri
        self.artist = artist
        self.name = name
        self.genre = genre
        self.score = score
        self.added = added
        self.length = length
    def __init__(self,uri):
        self.uri = uri


    def __str__(self):
        return 'Name:'+self.name+'\tArtist:'+self.artist+'\tGenre:'+self.genre+'\tScore:'+self.score

    def getAdded (self):
        return self.added
    def getURI(self):
        return self.uri
    def getArtist(self):
        return self.artist
    def getName(self):
        return self.name
    def getGenre(self):
        return self.genre
    def getScore(self):
        return self.score
    def getLength(self):
        return self.length
    def increaseScore(self):
        self.score = self.score+1
    def setAdded(self,bool):
        self.addded=bool
