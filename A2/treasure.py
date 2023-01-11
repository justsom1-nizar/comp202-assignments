#mcgill id : 261104927#
import treasure_utils as tu
import random



def generate_treasure_map_row(width,tof):
    """
    (int,bool)-> str
    takes a positive integer width and a boolean indicating if a 3D map is being generated as inputs. Creates and returns a single
    row of the given width (as a string) of a treasure map. Each character of the string should have a 5/6 chance to be one of the
    four basicmovement symbols and a 1/6 chance to be an empty symbol. If the boolean input is True, then thereshould be a 50% chance
    that one character in the row (only one, not more) is replaced by a 3Dmovement symbol (the hole or the ladder).
    >>> random.seed(120)
    >>> generate_treasure_map_row(5,True)
    'vvv>>'
    >>> generate_treasure_map_row(10,False)
    '.<>vv><.v>'
    >>> generate_treasure_map_row(1,True)
    '*'
    """
    map_string=""
    for i in range(width):
        if random.randint(1,6)==1:
            map_string=map_string+tu.EMPTY_SYMBOL
        else:
            map_string=map_string+tu.random_mvt_symbol()
    if tof and random.randint(1,2)==1:
        map_string=tu.change_char_in_map(map_string,0,random.randint(0,width-1),tu.random_3D_symbol(),width,1)
    return map_string

       
def generate_treasure_map(width,height,tof):
    """
    (int,int,bool)-> str
    takes an integer width and height and a boolean indicating if a 3D map is being generated as inputs. Creates and returns a
    treasure map of the given width and height (as a string). The occurrence probabilities of the characters in each row should
    be as is written above. The first character (row 0, col 0) of the map must be a right-pointing movement symbol.
    >>> random.seed(120)
    >>> generate_treasure_map(9,9,True)
    '>v<>^>>.vv<v<<>v.^^>|>>>>^.^>..^|>>..>*..>.v^>^.vv<<<v<><v>|v.>.^<<<><>v<<*v>v^<>'
    
    >>> generate_treasure_map(2,1,False)
    '>.'
    
    >>> generate_treasure_map(0,1,True)
    ''

    """
    map_generated=""
    for i in range(height):
        map_generated=map_generated+generate_treasure_map_row(width,tof)
    map_generated=tu.change_char_in_map(map_generated,0,0,tu.MOVEMENT_SYMBOLS[0],height,width)
    return map_generated

def generate_3D_treasure_map(width,height,depth):
    """
    (int,int,int)-> str
    takes a positive integer width, height and depth as inputs. Creates and returns a 3D treasure map of the given width, height and
    depth (as a string). The occurrence probabilities of the characters in each row of each map should be as is written above. The
    first character (row 0, col 0) of the first map (map 0) must be a right-pointing movement symbol.
    >>> generate_3D_treasure_map(3,3,3)
    '>v|^.><>^>.^.>|..^<|..^<vvv'
    >>> generate_3D_treasure_map(1,1,1)
    '>'
    >>> generate_3D_treasure_map(0,0,0)
    ''
    """
    map_generated=''
    for i in range(height*depth):
        map_generated=map_generated+generate_treasure_map_row(width,True)
    map_generated=tu.change_char_in_3D_map(map_generated,0,0,0,tu.MOVEMENT_SYMBOLS[0],height,width,depth)
    return map_generated
    
def follow_trail(map_3d,row,colomn,depth_index,width,height,depth,n):
    """
    (str,int,int,int,int,int,int,int)->str
    
    takes a 3D treasure map string, starting row, column and depth index (all integers),integer width, height and depth of the map, and
    number of tiles to travel (integer) as inputs. Follows the trail in the map, starting at the given row, column and depth index. Stops
    when encountering a tile that has been previously encountered, or when the specified number of tiles has been travelled (whichever comes
    first), prints the number of treasures collected in the format Treasures collected: n (where n is the number collected) and the number
    of symbols visited in the format Symbols visited: n and returns the travelled map (i.e., where all movement symbols which were followed
    are replaced by breadcrumb symbols). If the number of tiles to travel is -1, then do not stop following the trail until encountering a
    tile that has been previously encountered.
    
    >>> follow_trail('>>v..v', 0, 0, 0, 3, 2, 1, 100)
    Treasures collected: 0
    Symbols visited: 4
    'XXX..X'
    
     >>> follow_trail(">+vv+<>+*..|.>^.^<",0,0,0,3,3,2,-1)
    Treasures collected: 3
    Symbols visited: 14
    'X+XX+XX+X..X.XX.XX'
    
    >>> follow_trail(">+vv+<>+*..|.>^.^<",0,2,1,3,3,2,-1)
    Treasures collected: 2
    Symbols visited: 12
    '>+XX+XX+X..X.XX.XX'
    
    >>>  follow_trail(">+...<>+*^^|.>^.^<",0,2,3,3,3,2,1)
    '>+vv+<>+*..|.>^.^<'
    """
    if row>=height or colomn>=width or depth_index>=depth or row<0 or colomn<0 or depth_index<0:
        return map_3d
    tiles_traveled=0
    same_mouvement=-1
    treasure=0
    
    while 0<=tiles_traveled<n or n==-1:
        map_2d=tu.get_nth_map_from_3D_map(map_3d,depth_index,width,height,depth)
        row_1d=tu.get_nth_row_from_map(map_2d,row,width,height)
        char_position=row_1d[colomn]
        initial_character=''
        if char_position==tu.BREADCRUMB_SYMBOL:
            break
        elif char_position==tu.EMPTY_SYMBOL or char_position==tu.TREASURE_SYMBOL:
            initial_character=char_position
            char_position=tu.ALL_MOUVEMENT[same_mouvement]
            
        if char_position==tu.MOVEMENT_SYMBOLS[0]:
            if initial_character==tu.MOVEMENT_SYMBOLS[0] or initial_character=='':
                map_3d=tu.change_char_in_3D_map(map_3d,row,colomn,depth_index,tu.BREADCRUMB_SYMBOL,width,height,depth)
            if colomn==width-1:
                colomn=0
            else:
                colomn+=1
            same_mouvement=0
            tiles_traveled+=1
            
        elif char_position==tu.MOVEMENT_SYMBOLS[1]:
            if initial_character==tu.MOVEMENT_SYMBOLS[1] or initial_character=='':
                map_3d=tu.change_char_in_3D_map(map_3d,row,colomn,depth_index,tu.BREADCRUMB_SYMBOL,width,height,depth)
                
            if colomn==0:
                colomn=width-1
            else:
                colomn-=1
            same_mouvement=1
            tiles_traveled+=1
            
        elif char_position==tu.MOVEMENT_SYMBOLS[2]:
            if initial_character==tu.MOVEMENT_SYMBOLS[2] or initial_character=='':
                map_3d=tu.change_char_in_3D_map(map_3d,row,colomn,depth_index,tu.BREADCRUMB_SYMBOL,width,height,depth)
                
            if row==height-1:
                row=0
            else:
                row+=1
            same_mouvement=2
            tiles_traveled+=1
            
        elif char_position==tu.MOVEMENT_SYMBOLS[3]:
            if initial_character==tu.MOVEMENT_SYMBOLS[3] or initial_character=='':
                map_3d=tu.change_char_in_3D_map(map_3d,row,colomn,depth_index,tu.BREADCRUMB_SYMBOL,width,height,depth)
                
            if row==0:
                row=height-1
            else:
                row-=1
            same_mouvement=3
            tiles_traveled+=1
            
        elif char_position==tu.MOVEMENT_SYMBOLS_3D[0]:
            if initial_character==tu.MOVEMENT_SYMBOLS_3D[0] or initial_character=='':
                map_3d=tu.change_char_in_3D_map(map_3d,row,colomn,depth_index,tu.BREADCRUMB_SYMBOL,width,height,depth)
                
            if depth_index==depth-1:
                depth_index=0
            else:
                depth_index+=1
            same_mouvement=4
            tiles_traveled+=1
        elif char_position==tu.MOVEMENT_SYMBOLS_3D[1]:
            if initial_character==tu.MOVEMENT_SYMBOLS_3D[1] or initial_character=='':
                map_3d=tu.change_char_in_3D_map(map_3d,row,colomn,depth_index,tu.BREADCRUMB_SYMBOL,width,height,depth)
                
            if depth_index==0:
                depth_index=depth-1
            else:
                depth_index-=1
            same_mouvement=5
            tiles_traveled+=1
        if initial_character==tu.TREASURE_SYMBOL:
            treasure+=1
        
    print("Treasures collected:",treasure)
    print('Symbols visited:',tiles_traveled)
    return map_3d




   

          



        
        
        
        
        
        
    