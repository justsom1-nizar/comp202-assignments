#mcgill id : 261104927#
MOVEMENT_SYMBOLS = '><v^'
EMPTY_SYMBOL = '.'
TREASURE_SYMBOL = '+'
BREADCRUMB_SYMBOL = 'X'
MOVEMENT_SYMBOLS_3D = '*|'
ALL_MOUVEMENT=MOVEMENT_SYMBOLS+MOVEMENT_SYMBOLS_3D
import random
def random_mvt_symbol():
    return(MOVEMENT_SYMBOLS[random.randint(0,3)])
def random_3D_symbol():
    return(MOVEMENT_SYMBOLS_3D[random.randint(0,1)])
def get_nth_row_from_map(map_string,n,width,height):
    """
    (str,int,int,int)-> Str
    takes a treasure map string, integer n and integer width and height as inputs. Returns the n’th row of the treasure map
    (remember that we start counting at zero, so n = 0 means the first row in the treasure map string). If n is not a valid row
    (i.e., outside thebounds of the number of rows), return an empty string.
    >>> get_nth_row_from_map('^..>>>..v', 1, 3, 3)
    '>>>'
    >>> get_nth_row_from_map('^>>>>>>><<<', 0, 3, 4)
    '^>>'
    >>>>>> get_nth_row_from_map('^^>>^^>>^^>>', 5, 2, 6)
    '>>'
    """
    if n>=height or n<0:
        return("")
    return(map_string[n*width:(n+1)*width])
def print_treasure_map(map_string,width,height):
    """
    (str,int,int)->None
    takes a treasure map string and integer width and height as inputs and returns nothing. Prints out the treasure map with each
    row on its own line.
    
    >>> print_treasure_map('<..vvv..^', 3, 3)
    <..
    vvv
    ..^
    
    >>> print_treasure_map('<^^vvv..^', 1, 9)
    <
    ^
    ^
    v
    v
    v
    .
    .
    >>> print_treasure_map('<^^vvv..^><><>', 7, 2)
    <^^vvv.
    .^><><>
    """
    for i in range(height):
        print(get_nth_row_from_map(map_string,i,width,height))
    
def change_char_in_map(map_string,row,colomn,char,width,height):
    """
    (str,int,int,str,int,int)->str
    takes a treasure map string, integer row and column index, character c, and integer width and height as inputs. Returns a copy
    of the given treasure map string but with the character at the given row and column index replaced by c. If either or both of
    the indices are outof bounds of the map, return the input string unchanged.
    >>> change_char_in_map('<..vvv..^',1,2,'A', 3, 3)
    '<..vvA..^'
    
    >>> change_char_in_map('<^^vvv..^',1,0,'X', 1, 9)
    '<X^vvv..^'
    
    >>> change_char_in_map('<^^vvv..^><><>',1,3,'7' ,7, 2)
    '<^^vvv..^>7><>'
    """
    if row>=height or colomn>=width or row<0 or colomn<0:
        return map_string
    new_map=""
    for i in range(len(map_string)):
        if i==row*width+colomn:
            new_map=new_map+char
            continue
        new_map=new_map+map_string[i]
    return new_map
def get_proportion_travelled(map_string):
    """
    (str)-> float
    takes a treasure map string as input, and returns as a float the percentage (between 0 and 1) of the map that was travelled (i.e., the number
    of breadcrumb symbols in the map), rounded to two decimal places.
    >>> get_proportion_travelled('<^^vvv..^><><>')
    0.0
    
    >>> get_proportion_travelled('<^^XXXX<><>')
    0.36
    
    >>>get_proportion_travelled('')
    0
    """
    summ_X=0
    if len(map_string)==0:
        return 0
    for i in range(len(map_string)):
        if map_string[i]== BREADCRUMB_SYMBOL:
            summ_X+=1
    return round(summ_X/len(map_string),2)
def get_nth_map_from_3D_map(map_string,n,width,height,depth):
    """
    (str,int,int,int,int)->str
    takes a 3D treasure map string, integer n and integer width, height and depth as inputs. Returns the n’th map of the 3D treasure map.
    (When n = 0, e.g., return the firstmap in the string.) If n is not a valid map index (i.e., outside the bounds of the number of maps),
    return an empty string.
    >>> get_nth_map_from_3D_map(''..........^.^X^.^.'', 5, 3, 3, 2)
    ''
    >>> get_nth_map_from_3D_map('.X.XXX.X..v.vXv.v.', 0, 3, 3, 2)
    '.X.XXX.X.'
    
    >>> get_nth_map_from_3D_map('<^^vvv..^><><>',0 ,7, 2,1)
    '<^^vvv..^><><>'
    >>>


    """
    if n>=depth or n<0:
        return("")
    return(map_string[n*width*height:(n+1)*width*height])


def print_3D_treasure_map(map_string,width,height,depth):
    """
    (str,int,int,int)-> None
    takes a 3D treasure map string and integer width, height and depth as inputs and returns nothing. Prints out the treasure map with each
    row on its own line, and each map separated by a blank line. Make sure that there is no blank line at the end of your output.
    >>> print_3D_treasure_map('..........^.^X^.^.', 3, 3, 2)
    ...
    ...
    ...
    
    .^.
    ^X^
    .^.
    
    >>> print_3D_treasure_map('.X.XXX.X..v.vXv.v.',  3, 3, 2)
    .X.
    XXX
    .X.
    
    .v.
    vXv
    .v.
    
    >>>  print_3D_treasure_map('<^^vvv..^><><>' ,7, 2,1)
    <^^vvv.
    .^><><>
    """
    for j in range(depth):
        for i in range(height):
            print( get_nth_row_from_map(map_string,i+j*(height),width,depth*height))
        if j!=depth-1:
            print ("")

def change_char_in_3D_map(map_string,row,colomn,depth_index,char,width,height,depth):
    """
    (str,,int,int,int,str,int,int,int)-> str
    takes a 3D treasure map string, integer row, column and depth index,character c, and integer width, height and depth as inputs.
    Returns a copy of the given 3D treasuremap string but with the character at the given row, column and depth index replaced by c.
    If anyof the indices are out of bounds of the map, return the input string unchanged.
    
    >>> change_char_in_3D_map('.X.XXX.X..v.vXv.v.', 0, 0, 0, '#', 3, 3, 2)
    '#X.XXX.X..v.vXv.v.'
    
    >>> change_char_in_3D_map('..........^.^X^.^.',0,1,5,'D', 3, 3, 2)
    '..........^.^X^.^.'
    
    >>> change_char_in_3D_map('<^^vvv..^><><>' ,1,5,0,'q',7, 2,1)
    '<^^vvv..^><>q>'
    """
    if row>=height or colomn>=width or depth_index>=depth or row<0 or colomn<0 or depth_index<0:
        return map_string
    new_3D_map=""
    for i in range(len(map_string)):
        if i==(row+depth_index*height)*width+colomn:
            new_3D_map=new_3D_map+char
            continue
        new_3D_map=new_3D_map+map_string[i]
    return new_3D_map
















