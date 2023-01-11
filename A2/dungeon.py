#mcgill id : 261104927#
ROOM_NAME="just_some1s_room"
AUTHOR= "JustSOM1_"
PUBLIC=True
def escape_room() :
    """
    ()->None
    Plays a fun escape room.
    """
    print('I am a very bad narrator so i will get straight to the point, you have to get of this room there are three main things in this room: a chess board on a table, a console and a textbook(Hey for a better experience go through the objects in the same order i gave plz, i was tooo lazy to make a code to force you go through all of them so be nice and do it)')
    out=False
    j=1
    i=0
    while not out:
        interaction=input()
        if interaction.lower()=="list commands":
            print("aproach the table")
            print("aproach console")
            print("examine textbook")
        elif interaction.lower()=="aproach the table" or interaction.lower()=="examine the table" or interaction.lower()=="come closeto the the table":
            print(" As you aproach it the chair suddenly pushs you and forces you to sit on it, a hand suddently appear from nowhere, it appears to be FLOATINGGGG IN THE AIIIRRRRR. By a simple mouvement, you understand that you are being challenged to a chess match, if you win you might get out of here, do you accept the challenge?")
            chess=input()
            if chess.lower()=="list commands":
                print('Accept the challenge')
                print('Refuse the challenge because i am too scared to lose against a hand..')
            chess2=input()
            if chess2.lower()=="accept the challenge" or chess2.lower()=="refuse the challenge because i am too scared to lose against a hand.." or chess2.lower()=="yes" or chess2.lower()=="no":
                print("As you can see you can't run from this(PS: i know you refused)")
                print(" You are black, the hand starts off with pawn to e4, what's  your move?")
            else:
                print("invalid input(come on dude copy paste if you are dyslexique..)")
                break
            chess1=input()
            if chess1=="list commands":
                print("Come on now, everyone knows how to play chess on an invisible board.. Shame on you.")
            else:
                print("HAHAHAHAHAHHA YOU REALLY THAUGHT YOU WERE GONNA PLAY A GAME AGAINST AN AI!!! WHO DO YOU THINK AM I TO CODE THAT, ELON MUSK??(btw couldn't find any other well known person to fit the profile for this situation more than him)")
                i+=1
        elif interaction.lower()=="aproach console" or  interaction.lower()=="play console" or interaction.lower()=="examine console":
            print("You are aproching the console when suddently, the controller jumps to your hand, it's stuck, you can't get rid of it. As you realise the situation you are in, you think you will have to finish playing the game in front of you if you want to get out of here.")
            print("What game you ask? Oh it's just a cool adventure game, it seems fun too")
            console=input()
            if console.lower()=="list commands":
                print("Play the game")
            else:
                print("invalid input.")
            console1=input()
            if console.lower()=="play the game" or console1.lower()=="play the game":
                print("400 days later, you finally finish the game..But you are still not out, you have to find another way.")
                i+=1
            else:
                print("invalid input.")
        elif interaction.lower()=="aproach textbook" or  interaction.lower()=="read textbook" or interaction.lower()=="examine textbook":
            print("It seems to be a math text book, calculus 2 to be more precise. A note is hidden between the pages, here's what it says:'Solve this integrale and you might get out..'")
            print("You smile in the face of your only hope to get out, but then you take a look at the integral and tell yourself'How bad can it be anyways'. ")
            print("Plot twist: It's bad..")
            math=input()
            if math.lower()=="list commands":
                print("Look at the integral")
            else:
                print("invalid input.")
            math1=input()
            if math1.lower()=="look at the integral":
                print("(-40e**x-180)/(e**(2x)+13e**x+36)")
                print(" Hint: Don't forget the C ,simplify to the maximum ad don't use spaces")
                answer=input("Answer: ")
                if answer=="5ln(1+4e**(-x))+4ln((e**x+9)/(e**x+4))+C" or answer=="4ln(e**x+9)+ln(e**x+4)-5x+C":
                    out=True
                else:
                    print("bruhh")
                    j+=1
        elif interaction=="":
            print("Come on sing with me, IF yOu HanDS USe thEM!!(Hint:type this guy i got u: list commands)")
        else:
            print("invalid input.")
    if j==1:
        print("")
        print("You are either a genius or you just cheated if you cheated tho, shame on you")
    else:
        print("Congratialtions on getting out!")
    if i==2:
        print("Thanks for respecting the order")
    else:
        print("You made sad for not visiting everything :(")
