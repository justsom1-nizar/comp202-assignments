#name: Kheir Eddine Nizar
#mcgill id: 261104927
import musicalbeeps

class Note:
    """
    A class to represent a Note.
    
    instance attributes:
    * accidental_value: str
    * pitch: str
    * octave: int
    * duration: float
    
    class attributes:
    * OCTAVE_MIN: int
    * OCTAVE_MAX: int
    * list_values=list<str>
    
    
    """
    OCTAVE_MIN=1
    OCTAVE_MAX=7
    list_values=['sharp','flat','natural']
    def __init__(self,duration,pitch,octave=1,accidental='natural'):
        '''
        (float,str,int,str)->Nonetype
        creates an object of type Note.
        
        >>> note = Note(2.0, "B", 4, "natural")
        >>> note.pitch
        'B'
        
        >>> note1 = Note(-10, "B", 4, "flat")
        Traceback (most recent call last):
        AssertionError: One or more than one of the caracteristics of your note is not valid.
        
        >>> note2 = Note(2.0, "B", 4.5, "NATURAL")
        Traceback (most recent call last):
        AssertionError: One or more than one of the caracteristics of your note is not valid.
        
        '''
        if type(duration)!=float or duration<=0 or not pitch in 'ABCDEFGR' or  type(octave)!=int or not self.OCTAVE_MIN<=octave<=self.OCTAVE_MAX\
           or not accidental in self.list_values:
            raise AssertionError("One or more than one of the caracteristics of your note is not valid.")
        self.duration=float(duration)
        self.pitch=pitch
        self.octave=octave
        self.accidental=accidental
    
    
    def __str__(self):
        """
        ()->str
        returns a string of the format 'DURATION PITCH OCTAVE ACCIDENTAL' where each of the four words refer to the appropriate instance
        attributes.
        >>> note = Note(2.0, "B", 4, "natural")
        >>> print(note)
        2.0 B 4 natural
        
        >>>  print(Note(-10, "B", 4, "flat"))
        Traceback (most recent call last):
        AssertionError: One or more than one of the caracteristics of your note is not valid.
        
        >>> print(Note(2.0, "B", 4.5, "NATURAL"))
        Traceback (most recent call last):
        AssertionError: One or more than one of the caracteristics of your note is not valid.
        """
        return (str(self.duration)+' '+self.pitch+' '+str(self.octave)+' '+self.accidental)
    
    
    def play(self,player):
        """
        (player)->None
        takes one explicit input corresponding to a music player object(e.g., the player object given in the earlier example would be
        passed as argument to the method).The method should construct the note string that the play_note method accepts (again,
        describedabove), then pass the note string and duration to it so that the note can be played through thespeakers.If the note is a
        rest note (pitch R), then the note string should be the single word 'pause'.

        """
        note_string=self.pitch+str(self.octave)
        if self.pitch=='R':
            note_string='pause'
        elif self.accidental=='sharp':
            note_string+='#'
        elif self.accidental=='flat':
            note_string+='b'
        player.play_note(note_string,self.duration)
        


        
        
        
        
           
        
        
        
