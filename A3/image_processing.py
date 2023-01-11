#mcgill id: 261104927
import doctest

def is_valid_image(image):
    """
    list<list> ->  bool
    takes a nested list as input, and returns True if the nested list represents a valid (non-compressed) PGM image matrix and False
    otherwise.
    >>> is_valid_image([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    True
    >>> is_valid_image([['kkkkk', 2, 3], [4, 'hyhy', 6]])
    False
    >>> is_valid_image([[1,2],[ 3]])
    False
    """
    valid_len=len(image[0])
    for my_list in image:
        if len(my_list)!=valid_len:
            return False
        for my_int in my_list:
            if type(my_int)!= int or not 0<=my_int<=255 :
                return False
    return True


def is_valid_compressed_image(image):
    """
    list<list> ->  bool
    takes a nested list as input, and returns True if the nested list represents a valid compressed PGM image matrix and False otherwise.
    >>> is_valid_compressed_image([["0x5", "200x2"], ["111x7"]])
    True
    >>> is_valid_compressed_image([["0x5", "200x2"], ["85x10"]])
    False
    >>> is_valid_compressed_image([["x5", "200x2"], ["85x7"]])
    False
    
    """
    valid_summ=0
    for my_list in image:
        summ=0
        for my_int in my_list:
            if type(my_int)!= str or not 'x' in my_int:
                return False
            A_B_list=my_int.split('x')
            if  not A_B_list[0].isdecimal() or not A_B_list[1].isdecimal() or not 0<=int(A_B_list[0])<=255 or int(A_B_list[1])<0:
                return False
            summ+=int(A_B_list[1])
        if valid_summ!=0 and valid_summ!=summ:
            return False
        valid_summ=summ
            
    return True

def raise_error_RI():
    raise AssertionError('The file you submitted is not a valid regular image file, check the requirments of a valid file and see what mistake you made.')


def load_regular_image(file_image):
    """
    str-> list<list<int>>
    takes a filename (string) of a PGM image file as input, and loads in the image contained in the file and returns it as an image matrix.
    
    >>> load_regular_image("comp.pgm")
    [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 51, 51, 51, 51, 51, 0, 119, 119, 119, 119, 119, 0, 187, 187, 187, 187, 187, 0, 255, 255, 255, 255, 0], [0, 51, 0, 0, 0, 0, 0, 119, 0, 0, 0, 119, 0, 187, 0, 187, 0, 187, 0, 255, 0, 0, 255, 0], [0, 51, 0, 0, 0, 0, 0, 119, 0, 0, 0, 119, 0, 187, 0, 187, 0, 187, 0, 255, 255, 255, 255,0], [0, 51, 0, 0, 0, 0, 0, 119, 0, 0, 0, 119, 0, 187, 0, 187, 0, 187, 0, 255, 0, 0, 0, 0], [0, 51, 51, 51, 51, 51, 0, 119, 119, 119, 119, 119, 0, 187, 0, 187, 0, 187, 0, 255, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    

    """
    image_matrix=[]
    file=open(file_image,'r')
    i=0
    for line in file:
        if (i==0 and line!='P2\n') or (i==2 and line!='255\n'):
            raise_error_RI()
        if i==1:
            width=int(line.split()[0])
            height=int(line.split()[1])
        if i>=3:
            row=[]
            for num in line.split():
                if num.isdecimal():
                    num=int(num)
                row.append(num)
            if len(row)!=width:
                raise_error_RI()
            
            image_matrix.append(row)
        i+=1
    
    file.close()
    if not is_valid_image(image_matrix) or len(image_matrix)!=height:
        raise_error_RI()
    return image_matrix
    
   
def raise_error_CI():
    raise AssertionError('The file you submitted is not a valid compressed image file, check the requirments of a valid file and see what mistake you made.')
    
    
def load_compressed_image(file_image):
    """
    str->str-> list<list<str>>
    takes a filename (string) of a compressed PGM image file as input, and loads in the image contained in the file and returns it as a
    compressed image matrix.
    >>> load_compressed_image("compcompressed.pgm")
    [['0x24'], ['0x1', '51x5', '0x1', '119x5', '0x1', '187x5', '0x1', '255x4', '0x1'], ['0x1', '51x1', '0x5', '119x1', '0x3', '119x1', '0x1', '187x1', '0x1', '187x1', '0x1','187x1', '0x1', '255x1', '0x2', '255x1', '0x1'], ['0x1', '51x1', '0x5', '119x1', '0x3', '119x1', '0x1', '187x1', '0x1', '187x1', '0x1', '187x1', '0x1', '255x4', '0x1'], ['0x1', '51x1', '0x5', '119x1', '0x3', '119x1', '0x1', '187x1', '0x1', '187x1', '0x1', '187x1', '0x1', '255x1', '0x4'], ['0x1', '51x5', '0x1', '119x5', '0x1', '187x1', '0x1', '187x1', '0x1', '187x1', '0x1', '255x1', '0x4'], ['0x24']]
    """
    image_matrix=[]
    file=open(file_image,'r')
    i=0
    for line in file:
        if (i==0 and line!='P2C\n') or (i==2 and line!='255\n'):
            raise_error_CI()
            
        if i>2:
            row=[]
            for string in line.split():
                row.append(string)
            image_matrix.append(row)
        i+=1
    file.close()
    if not is_valid_compressed_image(image_matrix):
        raise_error_RI()
    return image_matrix

    

def load_image(file_image):
    """
    (str)->list<list<int/str>>
    takes a filename (string) of a file as input. Checks the first line of the file. If it is 'P2',then loads in the file as a regular PGM image and
    returns the image matrix. If it is 'P2C', thenloads in the file as a compressed PGM image and returns the compressed image matrix. If it isanything
    else, then a AssertionError with an appropriate error message should be raised instead.
    >>> load_image('compcompressed.pgm')
    [['0x24'], ['0x1', '51x5', '0x1', '119x5', '0x1', '187x5', '0x1', '255x4', '0x1'], ['0x1', '51x1', '0x5', '119x1', '0x3', '119x1', '0x1', '187x1', '0x1', '187x1', '0x1', '187x1', '0x1', '255x1', '0x2', '255x1', '0x1'], ['0x1', '51x1', '0x5', '119x1', '0x3', '119x1', '0x1', '187x1', '0x1', '187x1', '0x1', '187x1', '0x1', '255x4', '0x1'], ['0x1', '51x1', '0x5', '119x1', '0x3', '119x1', '0x1', '187x1', '0x1', '187x1', '0x1', '187x1', '0x1', '255x1', '0x4'], ['0x1', '51x5', '0x1', '119x5', '0x1', '187x1', '0x1', '187x1', '0x1', '187x1', '0x1', '255x1', '0x4'], ['0x24']]


    """
    f=open(file_image,'r')
    for line in f:
        if line=='P2\n' :
            f.close()
            return load_regular_image(file_image)
        elif line=='P2C\n' :
            f.close()
            return load_compressed_image(file_image)
        else:
            f.close() 
            raise AssertionError("The file you used is neither a valid regular image file nor a valid compressed image file.")
               

def save_regular_image(image_list,file_name):
    """
    (list<list<int>>,str)-> None
    takes a nested list and a filename (string) as input, and saves it in the PGM format to a file with the given filename. If the image matrix given
    as input is not a valid PGM image matrix, instead raise a AssertionError with an appropriate error message.
    >>> save_regular_image([[0]*10, [255]*10, [0]*10], "test.pgm")
    
    >>> save_regular_image([[3550]*10, [255]*10, [0]*10], "test.pgm")
    AssertionError("The list you submited is not a valid regular image list, try again!")
    
    >>> save_regular_image([['abcd1']*10], "test.pgm")
    AssertionError("The list you submited is not a valid regular image list, try again!")
    """
    if is_valid_image(image_list):
        width=len(image_list[0])
        height=len(image_list)
        f=open(file_name,'a')
        f.write("P2\n")
        f.write(str(width)+' '+str(height)+'\n')
        f.write("255\n")
        for i in range(height):
            for j in range(width):
                f.write(str(image_list[i][j]))
                if j!=width-1:
                    f.write(' ')
            f.write("\n")
        f.close()
    else:
        raise AssertionError("The list you submited is not a valid regular image list, try again!")



def save_compressed_image(image_list,file_name):
    """
    (list<list<str>>,str)-> None
    takes a nested list and a filename (string) as input, and saves it in the compressed PGM format to a file with the given filename. If the image
    matrix given as input is not a valid compressed PGM image matrix, instead raise a AssertionError with an appropriate errormessage.
    >>> save_compressed_image([["0x5", "200x2"], ["111x7"]], "test2.pgm.compressed")
    >>> fobj = open("test2.pgm.compressed", 'r')
    >>> fobj.read()
    'P2C\\n7 2\\n255\\n0x5 200x2\\n111x7\\n'
    >>> fobj.close()
    
    >>> save_compressed_image([["0x5"], ["111x7"]], "test211.pgm")
    >>> fobj = open("test211.pgm.compressed", 'r')
    >>> fobj.read()
    'P2C\\n7 2\\n255\\n0x5 200x2\\n'
    >>> fobj.close()
    
    >>> save_compressed_image([["0aa5"], ["111x7"]], "failure.pgm")
    AssertionError("The list you submited is not a valid compressed image list, try again!")
    """
    if is_valid_compressed_image(image_list):
        height=len(image_list)
        width=0
        for axb in image_list[0]:
            width+=int(axb.split('x')[-1])
        f=open(file_name,'a')
        f.write("P2C\n")
        f.write(str(width)+' '+str(height)+'\n')
        f.write("255\n")
        for i in range(height):
            for j in range(len(image_list[i])):
                f.write(image_list[i][j])
                if j!=len(image_list[i])-1:
                    f.write(' ')
            f.write("\n")
        f.close()
    else:
        raise AssertionError("The list you submited is not a valid compressed image list, try again!")

    
def save_image(image_list,file_name):
    """
    (list<list<str/int>>)-> None
    takes a nested list and a filename (string) as input. Checks the type of elements in the list. If they are integers, then saves the nested
    list as a PGM image matrix into a file with the given filename. If they are strings, then saves the nested list as a compressed PGM image matrix
    into a file with the given filename. If they are anything else, then a AssertionError with an appropriate error message should be raised instead.
    >>> save_image([["0x5", "200x2"], ["111x7"]], "test1.pgm.compressed")
    >>> fobj = open("test1.pgm.compressed", 'r')
    >>> fobj.read()
    'P2C\\n7 2\\n255\\n0x5 200x2\\n111x7\\n'
    >>> fobj.close()
    
    >>> save_image([[0]*10, [255]*10, [0]*10], "test.pgm")
    
    >>> save_image([[3550]*10, [255]*10, [0]*10], "test.pgm")
    AssertionError("The list you submited is not a valid regular image list, try again!")
    """
    if type(image_list[0][0])==int:
        save_regular_image(image_list,file_name)
    elif type(image_list[0][0])==str:
        save_compressed_image(image_list,file_name)
    else:
        raise AssertionError("The list you submited is neither a valid compressed image list nor a valid regular image list, try again!")


def invert(image_matrix):
    """
    (list<list<int>>)->list<list<int>>
    takes a (non-compressed) PGM image matrix as input, and returns the inverted image. Should not modify the input matrix. If the input matrix is
    not a valid PGM image matrix, then a AssertionError with an appropriate error message should be raised instead.
    >>> image = [[0, 100, 150], [200, 200, 200], [255, 255, 255]]
    >>> invert(image)
    [[255, 155, 105], [55, 55, 55], [0, 0, 0]]
    
    >>> image = [[ 200, 200], [255, 255, 255]]
    >>> invert(image)
    AssertionError: The file you submitted is not a valid regular image file, check the requirments of a valid file and see what mistake you made.
    
    >>> image = [[ 300,200, 200], [255, 255, 255]]
    >>> invert(image)
    AssertionError: The file you submitted is not a valid regular image file, check the requirments of a valid file and see what mistake you made.
    """
    if not is_valid_image(image_matrix):
        raise_error_RI()
    inverted_matrix=[]
    for row in image_matrix:
        inverted_row=[]
        for integer in row:
            inverted_row.append(255-integer)
        inverted_matrix.append(inverted_row)
    return inverted_matrix
    
    
    
def flip_horizontal(image_matrix):
    """
    (list<list<int>>)->list<list<int>>
    takes a (non-compressed) PGM image matrix as input, and returns the image matrix flipped horizontally. Should not modify the input matrix. If
    the input matrix is not a valid PGM image matrix, then a AssertionError with an appropriate error message should be raised instead.
    >>> image = [[1, 2, 3, 4, 5], [0, 0, 5, 10, 10], [5, 5, 5, 5, 5]]
    >>> flip_horizontal(image)
    [[5, 4, 3, 2, 1], [10, 10, 5, 0, 0], [5, 5, 5, 5, 5]]
    
    >>> image = [[1, '2', 3, 4, 5], [0, 0, 5, 10, 10], [5, 5, 5, 5, 5]]
    >>> flip_horizontal(image)
    AssertionError: The file you submitted is not a valid regular image file, check the requirments of a valid file and see what mistake you made.
    
    >>> image = [[1, 2, 3, 4, 5], [0, 0, 5, 10]]
    >>> flip_horizontal(image)
    AssertionError: The file you submitted is not a valid regular image file, check the requirments of a valid file and see what mistake you made.
    """
    if not is_valid_image(image_matrix):
        raise_error_RI()
    flipped_matrix=[]
    for row in image_matrix:
        flipped_row=[]
        for i in range(len(row)-1,-1,-1):
            flipped_row.append(row[i])
        flipped_matrix.append(flipped_row)
    return flipped_matrix

    

def flip_vertical(image_matrix):
    """
    (list<list<int>>)->list<list<int>>
    takes a (non-compressed) PGM image matrix as input, and returns the image matrix flipped vertically. Should not modify the input matrix. If the
    input matrix is not a valid PGM image matrix, then a AssertionError with an appropriate error message should be raised instead.

    >>> flip_vertical([[1, 2, 3, 4, 5], [0, 0, 5, 10, 10], [5, 5, 5, 5, 5]])
    [[5, 5, 5, 5, 5], [0, 0, 5, 10, 10], [1, 2, 3, 4, 5]]
    
    >>> flip_vertical([['1', 2, 3, 4, 5], [0, 0, 5, 10, 10]])
    AssertionError: The file you submitted is not a valid regular image file, check the requirments of a valid file and see what mistake you made.
    
    >>> flip_vertical([[2555, 2, 3, -515151, 5]])
    AssertionError: The file you submitted is not a valid regular image file, check the requirments of a valid file and see what mistake you made.
    """
    if not is_valid_image(image_matrix):
        raise_error_RI()
    inverted_matrix=[]
    for i in range(len(image_matrix)-1,-1,-1):
        inverted_row=[]
        for integer in image_matrix[i]:
            inverted_row.append(integer)
        inverted_matrix.append(inverted_row)
    return inverted_matrix

    
    
def crop(image_matrix,top_left_row,top_left_column,n_rows,n_columns):
    """
    (list<list<int>>,int,int,int,int)->list<list<int>>
    takes a (non-compressed) PGM image matrix, two non-negative integers and two positive integers as input. The two non-negative integers
    correspond to the top left row and top left columnof the target rectangle, and the two positive integers correspond to the number of
    rows and number of columns of the target rectangle. The function should return an image matrix corresponding tothe pixels contained in
    the target rectangle. Should not modify the input list. If the input matrix is not a valid PGM image matrix, then a AssertionError with
    an appropriate error message should be raised instead.
    >>> crop([[5, 5, 5], [5, 6, 6], [6, 6, 7]], 1, 1, 2, 2)
    [[6, 6], [6, 7]]
    
    >>> crop([[1, 2, 3, 4], [4, 5, 6, 7], [8, '9, 10, 11']], 1, 2, 2, 1) 
    AssertionError: The file you submitted is not a valid regular image file, check the requirments of a valid file and see what mistake you
    made.
    
    >>> crop([[1, 2, 3, 4], [4, 5, 6, 7]], 0, 0, 2, 4) 
    [[1, 2, 3, 4], [4, 5, 6, 7]]
    
    """
    if not is_valid_image(image_matrix):
        raise_error_RI()
    cropped_matrix=[]
    for i in range(top_left_row,top_left_row+n_rows):
        cropped_row=[]
        for j in range(top_left_column,top_left_column+n_columns):
            cropped_row.append(image_matrix[i][j])
        cropped_matrix.append(cropped_row)    
    return cropped_matrix
    
   
def find_end_of_repetition(my_list,index,number):
    """
    (list<int>,int,int)->int
    takes a list of integers and two non-negative integers (an index and atarget number) as input. You can assume that the list will contain
    the target number at the givenindex. Looks through the list starting after the given index, and returns the index of the lastconsecutive
    occurrence of the target number. That is, as soon as you come across a number that isnot the target, then return the previous index.
    >>> find_end_of_repetition([1, 2, 3, 4, 5, 6, 7], 6, 7)
    6
    >>> find_end_of_repetition([1,1,1,1,1,1], 3,1)
    5
    >>> find_end_of_repetition([4555, 4555, 4555, 6, 7], 0, 4555)
    2
    """
    for i in range(index,len(my_list)):
        if number!=my_list[i]:
            i-=1
            break
        
    return i


def compress(image_matrix):
    """
    (list<list<int>>)->list<list<str>>
    takes a (non-compressed) PGM image matrix as input. Compresses the matrix according to the compression algorithm described earlier in
    this PDF and returns the compressed matrix. If the input matrix is not a valid PGM image matrix, then a AssertionError with an
    appropriate error message should be raised instead.
    >>> compress([[11, 11, 11, 11, 11], [1, 5, 5, 5, 7], [255, 255, 255, 0, 255]])
    [['11x5'], ['1x1', '5x3', '7x1'], ['255x3', '0x1', '255x1']]
    
    >>> compress([[11, 11, 11, 11, 11], [1,' 5, 5, 5', 7]])
    AssertionError: The file you submitted is not a valid regular image file, check the requirments of a valid file and see what mistake
    you made.
    
    >>> compress([[0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0]])
    [['0x14'], ['0x14']]
    """
    if not is_valid_image(image_matrix):
        raise_error_RI()
    compressed_matrix=[]
    for row in image_matrix:
        compressed_row=[]
        i=0
        while i<len(row):
            end_i=find_end_of_repetition(row,i,row[i])
            axb=str(row[i])+'x'+str(end_i-i+1)
            compressed_row.append(axb)
            i=end_i+1
        compressed_matrix.append(compressed_row)
    return compressed_matrix
        
    
def decompress(image_matrix):
    """
    (list<list<str>>)->list<list<int>>
    takes a compressed PGM image matrix as input. Decompresses the matrix by undoing the compression algorithm described earlier in this
    PDF and returns the decompressed matrix. If the input matrix is not a valid compressed PGM image matrix, then a AssertionError with an
    appropriate error message should be raised instead.
    >>> decompress([['11x5'], ['1x1', '5x3', '7x1'], ['255x3', '0x1', '255x1']])
    [[11, 11, 11, 11, 11], [1, 5, 5, 5, 7], [255, 255, 255, 0, 255]]
    
    >>> decompress([['11x5'],  ['25555555x3', '0x1', '255x1']])
    AssertionError: The file you submitted is not a valid compressed image file, check the requirments of a valid file and see what mistake
    you made.
    
    >>> decompress([ [288585, '5x3'], ['255x3', '255x1']])
    AssertionError: The file you submitted is not a valid compressed image file, check the requirments of a valid file and see what mistake
    you made.
    """
    if not is_valid_compressed_image(image_matrix):
        raise_error_CI()
    decompressed_image=[]
    for row in image_matrix:
        decompressed_row=[]
        for axb in row:
            a=int(axb.split('x')[0])
            b=int(axb.split('x')[-1])
            for i in range(b):
                decompressed_row.append(a)
        decompressed_image.append(decompressed_row)
    return decompressed_image


def process_command(string_command):
    """
    (str)->None
    takes a string as input corresponding to a series of space-separated image processing commands, and executes each command in turn.
    Does not return anything.
    >>> process_command("LOAD<comp.pgm> CP DC INV INV SAVE<comp2.pgm>")
    >>> image = load_image("comp.pgm")
    >>> image2 = load_image("comp2.pgm")
    >>> image == image2
    True
    
    >>> process_command("LOAD<comp.pgm> FV FH INV CP DC INV INV SAVE<comp42.pgm>")
    >>> image = load_image("comp.pgm")
    >>> image2 = load_image("comp42.pgm")
    >>> image == image2
    False
    
    >>> process_command("LOAD<comp.pgm> CR<1,1,5,5> SAVE<comp4442.pgm>")
    >>> image = load_image("comp4442.pgm")
    >>> image == [[51, 51, 51, 51, 51],[51,0,0,0,0],[51,0,0,0,0],[51,0,0,0,0],[51, 51, 51, 51, 51]]
    True
    """
    list_commands=string_command.split()
    for command in list_commands:
        if 'LOAD'in command:
            image_matrix=load_image(command[5:-1])
        elif command=='CP':
            image_matrix=compress(image_matrix)
        elif command=='DC':
            image_matrix=decompress(image_matrix)
        elif 'SAVE' in command:
            save_image(image_matrix,command[5:-1])
        elif command=='INV':
            image_matrix=invert(image_matrix)
        elif command=='FH':
            image_matrix=flip_horizontal(image_matrix)
        elif command=='FV':
            image_matrix=flip_vertical(image_matrix)
        elif 'CR' in command:
            crop_numbers=command[3:-1:1].split(',')
            image_matrix=crop(image_matrix,int(crop_numbers[0]),int(crop_numbers[1]),int(crop_numbers[2]),int(crop_numbers[3]))
        else:
            raise AssertionError('One of the commands you used is Unprocessable. ')
    
 
