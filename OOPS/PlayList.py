class PlayList : 
    '''This is an playlist class'''

    #static variable
    AppName = 'YouTube Music'

    @classmethod
    def tellAppName(cls):
        print(cls.AppName)
    
    @staticmethod # these are generalize methods
    def doSomething(what:str):
        print(f'theek {what} hai')

    @staticmethod
    def stopDoingSomething(what:str):
        print(f'paisa lagea {what} rokne keliye !')

    # constructor
    def __init__(self,name:str,songs:list,gener :str):
        self.name = name
        self.songs = songs
        self.gener = gener
    
    #instance method
    def details(self):
        print(f'Name : {self.name}')
        print(f'Songs : {self.songs}')
        print(f'Gener : {self.gener}')
    
    def addSong(self,song:dict) :
        self.songs.append(song)
        print(self.songs)

p1 = PlayList("Instrumental",["chanakya",'garaj','kautilya'],'Indian Classic Instrumental')
p1.details()

p1.tellAppName()
p1.doSomething('padna')
p1.stopDoingSomething('padna')