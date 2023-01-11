#name: Kheir Eddine Nizar
#mcgill id: 261104927
import note as nf
class Melody:
    """
    A class to represent a Melody.
    instance attributes:
    * notes: list
    * title: str
    * author: str
    
    
    """
    def __init__(self,filename):
        """
        (str)->NoneType
        Creates an object of type Melody.
        >>> happy_birthday = Melody("birthday.txt")
        >>> happy_birthday.notes[2].duration
        0.5
        
        >>> hot_cross_buns = Melody("hotcrossbuns.txt")
        >>> print(hot_cross_buns.notes[0])
        0.5 B 4 natural
        
        >>> hot_cross_buns = Melody("hotcrossbuns.txt")
        >>> print(len(hot_cross_buns.notes)+hot_cross_buns.notes[5].octave)
        21
        """
        self.notes=[]
        f=open(filename,'r')
        string_list_notes=[]
        check=False
        i=0
        for line in f:
            if i==0:
                self.title=line[:-1]
            elif i==1:
                self.author=line[:-1]
            else:
                one_note_list=line.split()
                string_list_notes.append(one_note_list)
            i+=1
        i=0
        while i<len(string_list_notes):
            if len(string_list_notes[i])==3:
                line_note=nf.Note(float(string_list_notes[i][0]),string_list_notes[i][1])
            else:
                line_note=nf.Note(float(string_list_notes[i][0]),string_list_notes[i][1],int(string_list_notes[i][2]),\
                                  string_list_notes[i][3].lower())
            if string_list_notes[i][-1]=='true':
                string_list_notes[i][-1]='hehe'
                if not check:
                    j=i
                else:
                    i=j-1
                check=not check
            self.notes.append(line_note)   
            i+=1
        f.close()
        
        
    def play(self,player):
        """
        (player)->None
        takes a music player object as explicit input, and calls the play method on each Note object of the notes instance attribute in
        order, passing the music player object each time as argument.
        """
        for note in self.notes:
            note.play(player)
    
    def get_total_duration(self):
        """
        ()->float
        takes no explicit inputs and returns the total duration of the song as a float.
        >>> happy_birthday = Melody("birthday.txt")
        >>> happy_birthday.get_total_duration()
        13.0
        
        >>> hotcrossbuns=Melody("hotcrossbuns.txt")
        >>> hotcrossbuns.get_total_duration()
        5.0
        
        >>> ms=Melody("mysong.txt")
        >>> ms.get_total_duration()
        30.0
        """
        total_duration=0
        for note in self.notes:
            total_duration+=note.duration
        return total_duration    
    def change_octave(self,plus_minus):
        """
        (int)->bool
        It adds an integer to the octave of all notes in the song returns True. However, a note’s octave cannot be reduced below 1 or past 7.
        If that would happen, then do not lower any octaves and instead return False.
        >>> happy_birthday = Melody("birthday.txt")
        >>> happy_birthday.change_octave(-1)
        True
        
        >>> ms = Melody("mysong.txt")
        >>> ms.change_octave(-500000000)
        False
        
        >>> hotcrossbuns=Melody("hotcrossbuns.txt")
        >>> hotcrossbuns.change_octave(+1)
        True
        """
        
        for note in self.notes:
            if not note.OCTAVE_MIN<=note.octave+plus_minus<=note.OCTAVE_MAX and note.pitch!='R':
                return False
        for note in self.notes:
            note.octave=note.octave+plus_minus
        return True
    
    def lower_octave(self):
        """
        ()->bool
        It reduces the octave of all notesin the song by 1 and returns True. However, a note’s octave cannot be reduced below 1. If
        thatwould happen, then do not lower any octaves and instead return False.
        >>> happy_birthday = Melody("birthday.txt")
        >>> happy_birthday.lower_octave()
        True
        
        >>> ms = Melody("mysong.txt")
        >>> ms.lower_octave()
        False
        
        >>> hotcrossbuns=Melody("hotcrossbuns.txt")
        >>> hotcrossbuns.lower_octave()
        True
        """    
        return self.change_octave(-1)
    
    def upper_octave(self):
        """
        ()->bool
        takes no explicit inputs. It increases the octave of all notes in the song by 1 and returns True. However, a note’s octave cannot
        be increased past 7. If that would happen, then do not increase any octaves and instead return False.
        >>> happy_birthday = Melody("birthday.txt")
        >>> happy_birthday.upper_octave()
        True
        
        >>> ms = Melody("mysong.txt")
        >>> ms.upper_octave()
        False
        
        >>> hotcrossbuns=Melody("hotcrossbuns.txt")
        >>> hotcrossbuns.upper_octave()
        True
        """    
        return self.change_octave(1)    
    
    def change_tempo(self,tempo):
        """
        (float)->None
        takes one positive float as explicit input and returns nothing. It should multiply the duration of each note by the given float.
        >>> happy_birthday = Melody("birthday.txt")
        >>> happy_birthday.change_tempo(0.5)
        >>> happy_birthday.get_total_duration()
        6.5
        
        >>> hotcrossbuns = Melody("hotcrossbuns.txt")
        >>> hotcrossbuns.change_tempo(20)
        >>> hotcrossbuns.get_total_duration()
        100.0
        
        >>> ms=Melody("mysong.txt")
        >>> ms.get_total_duration()
        30.0
        >>> ms.change_tempo(2)
        >>> ms.get_total_duration()
        60.0
        """
        for note in self.notes:
            note.duration*=tempo















