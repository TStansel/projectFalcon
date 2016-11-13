class htmlWriter:

    def __init__(self,songsAdded,htmlFile):
        self.songsAdded = songsAdded
        self.htmlFile = htmlFile

    def format(self):
        f = open(self.htmlFile,'w')
        message = """<table >
    <tr>
       <th><h2>Rank</h2></th>
       <th><h2>Title</h2>
           <h2>Author|Album</h2></th>
       <th><h2>Score</h2></th>
       <th><h2>Up Down</h2></th>
    </tr>
    <tr>
       <td><h3 type="bold">1</h3></td>
       <td><h3>Hey Brother</h3>
           <h3>Avicii|True</h3></td>
       <td><h3>112</h3></td>
        <form action="/" method="POST">
             <td>
                 <input type="button" name="vote1" value="Up" id="up">
                 <input type="button" name= "vote1" value="Down" id="down">
             </td>
        </form>
    </tr>
</table>