class Song:

    def __init__(self, str):
        if ',' in str:
            arr = str.split(',')
            self.setTitle(arr[0])
            self.setArtist(arr[1])
            self.setGenre(arr[2])
            self.setLength(arr[3])
        else:
            self.setTitle(str[0:str.index('  ')])
            str = str[str.index('  '):str.__len__()].strip()
            self.setArtist(str[0:str.index('  ')])
            str = str[str.index('  '):str.__len__()].strip()
            self.setGenre(str[0:str.index('  ')])
            str = str[str.index('  '):str.__len__()].strip()
            self.setLength(str)

    def setTitle(self, ti):
        self.title = ti

    def setArtist(self, ar):
        self.artist = ar

    def setGenre(self, ge):
        self.genre = ge

    def setLength(self, le):
        self.length = le

    def __repr__(self):
        return repr((self.title,self.artist,self.genre,self.length))

    def toString(self):
        return '{},{},{},{}'.format(self.title, self.artist, self.genre, self.length)

    def __eq__(self, other):
        if(self.title != other.title):
            return False
        if(self.artist != other.artist):
            return False
        return True

    def __str__(self):
        return '%-50s %-19s %-20s %-5s' % (self.title, self.artist, self.genre, self.length)