def verse(lyrics):
    for line in lyrics:
        print(line)

def chorus():
    print("Fill the bowl to overflowing. Raise the goblet high!")
    print("With a \"F\" and a \"R\" and an \"E\" and a \"D\"")
    print("And a \"F-R-E-D\" Fred! Yeah!")

def lala():
    lala = "la la la la, " * 3 + "\b" * 2 + "!"
    print(lala.capitalize())

def clap():
    clap = "Clap clap, clap clap, clap clap clap clap, clap, clap clap!"
    print(clap)

def love():
    love = "I'm in love with a girl named Fred."
    print(love)

def bravo():
    bravo = "Bravo! Bravo! Bravissimo bravo! Bravissimo!"
    print(bravo)
    
def strum():
    strum = "Strum strum, strum strum, strum strum strum strum strum, strum."
    print(strum)


def main():
    #==========================================================================#

   #1
    verse([
        "I like you, Fred, I like you!",
        "You're just saying those words to be kind.",
        "No, I mean it. I like... I mean I love you, Fred!",
        "He is out of his medieval mind!",
        "I'm perfectly sane and sound! I never felt better in my life!",
        "Everybody... everybody, everybody! Come on! And meet my incipient wife!"
        
    ])
    print("\n")
    #==========================================================================#


    #2
    love()
    verse([

        "My reasons must be clear.",
        "When she shows you all how strong she is you'll stand right up and cheer!",
        "With a \"F\" and a \"R\" and an \"E\" and a \"D\"",
        "And a \"F-R-E-D\" Fred! Yeah!"

    ])
    print("\n")
    #==========================================================================#


    #3
    love()
    verse([
        
        "She drinks just like a lord!",
        "So sing a merry drinking song and let the wine be poured!"

    ])
    chorus()
    print("\n")
    #==========================================================================#


    #4
    love()
    verse([

        "She sings just like a bird!",
        "You'll be left completely speechless when her gentle voice is heard!",
        
    ])
    lala()
    chorus()
    print("\n")
    #==========================================================================#


    #5
    love()
    verse([
        
        "She wrestles like a Greek!",
        "You will clap your hands in wonder at her fabulous technique!",
        
    ])
    clap()
    lala()
    chorus()
    print("\n")
    #==========================================================================#


    #6
    love()
    verse([
        
        "She dances with such grace!",
        "You are bound to sing her praises 'til you're purple in the face!",
    ])
    bravo()
    clap()
    lala()
    chorus()
    print("\n")
    #==========================================================================#

    
    #7
    love()
    verse([   
        "She's musical to boot!",
        "She will set your feet a-tapping when she plays upon her lute!",
    ])
    strum()
    bravo()
    clap()
    lala()
    chorus()
    print("\n")
    #==========================================================================#


    #8
    love()
    verse([
        "A clever, clownish wit!",
        "When she does her funny pantomime your sides are sure to split!",
        "Ha ha ha ha, ho ho ho ho, ha ha ha ha ho!",
    ])
    strum()
    bravo()
    clap()
    lala()
    chorus()
    print("\n")
    #==========================================================================#

    #9
    verse([
        "I'm in love with a girl.",
        "He's in love with a girl named \"F-R-E-D\" Fred!"
    ])
    #==========================================================================#



if __name__ == "__main__":
    main()
