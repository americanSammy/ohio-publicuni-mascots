# dictionaries for each member
dave = {
    "role": "Singer",
    "age": "52"
    }
carter = {
    "role": "Drummer",
    "age": "61"
    }
stefan = {
    "role": "Bassist",
    "age": "44"
    }
tim = {
    "role": "Guitarist",
    "age": "61"
    }
rashawn = {
    "role": "Trumpet",
    "age": "39"
    }
buddy = {
    "role": "Keyboard",
    "age": "unk"
    }
jeff = {
    "role": "Saxophonist",
    "age": "53"
    }
# each album track list
crash = {
    "year": "1996",
    "track1": "So Much to Say",
    "track2": "Two Step",
    "track3": "Crash into Me",
    "track4": "Too Much",
    "track5": "#41",
    "track6": "Say Goodbye",
    "track7": "Drive In, Drive Out",
    "track8": "Let You Down",
    "track9": "Lie In Our Graves",
    "track10": "Cry Freedom",
    "track11": "Tripping Billies",
    "track12": "Proudest Monkey",
    }
bustedStuff = {
    "year" : "2002",
    "track1" :"Busted Stuff",
    "track2" : "Grey Street",
    "track3" : "Where Are You Going",
    "track4" : "You NeverKnow",
    "track5" : "Captain",
    "track6" : "Raven",
    "track7" : "Grace is Gone",
    "track8" : "Kit Kat Jam",
    "track9" : "Digging a Ditch",
    "track10" : "Big Eyed Fish",
    "track11" : "Bartender",
    }
uttad = {
    "year" : "1994",
    "track1" : "The Best of What's Around",
    "track2" : "What Would You Say",
    "track3" : "Satellite",
    "track4" : "Rhyme & Reason",
    "track5" : "Typical Situation",
    "track6" : "Dancing Nancies",
    "track7" : "Ants Marching",
    "track8" : "Lover Lay Down",
    "track9" : "Jimi Thing",
    "track10" : "Warehouse",
    "track11" : "Pay For What You Get",
    "track12" : "#34",
    "track13" : "Granny",
    "track14" : "Dancing Nancies (Acoustic)",
    "track15" : "The Song That Janes Likes (Acoustic)",
    }
standUp = {
    "year" : "2005",
    "track1" : "Dreamgirl",
    "track2" : "Old Dirt Hill (Bring That Beat Back)",
    "track3" : "Stand Up (For It)",
    "track4" : "American Baby Intro",
    "track5" : "American Baby",
    "track6" : "Smooth Rider",
    "track7" : "Everybody Wake Up (Our Finest Hour Arrives)",
    "track8" : "Out of My Hands",
    "track9" : "Hello Again",
    "track10" : "Louisiana Bayou",
    "track11" : "Stolen Away on 55th & 3rd",
    "track12" : "You Might Die Trying",
    "track13" : "Steady As We Go",
    "track14" : "Hunger for the Great Light",
    }
everyday = {
    "year" : "2001",
    "track1" : "I Did It",
    "track2" : "When the World Ends",
    "track3" : "The Space Between",
    "track4" : "Dreams of Our Fathers",
    "track5" : "So Right",
    "track6" : "If I Had it All",
    "track7" : "What You Are",
    "track8" : "Angel",
    "track9" : "Fool to Think",
    "track10" : "Sleep to Dream Her",
    "track11" : "Mother Father",
    "track12" : "Everyday",
    }
btcs = {
    "year" : "1998",
    "track1" : "Pantala Naga Pampa",
    "track2" : "Rapunzel",
    "track3" : "The Last Stop",
    "track4" : "Don't Drink the Water",
    "track5" : "Stay (Wasting Time)",
    "track6" : "Halloween",
    "track7" : "The Stone",
    "track8" : "Crush",
    "track9" : "The Dreaming Tree",
    "track10" : "Pig",
    "track11" : "Spoon",
    }
bigwhiskey = {
    "year" : "2009",
    "track 1" : "Grux",
    "track 2" : "Shake Me Like a Monkey",
    "track 3" : "Funny the Way It Is",
    "track 4" : "Lying in the Hands of God",
    "track 5" : "Why I Am",
    "track 6" : "Dive In",
    "track 7" : "Spaceman",
    "track 8" : "Squirm",
    "track 9" : "Alligator Pie",
    "track 10" : "Seven",
    "track 11" : "Time Bomb",
    "track 12" : "Baby Blue",
    "track 13" : "You & Me"
    }
AFTW = {
    "year" : "2012",
    "track 1" : "Broken Things",
    "track 2" : "Belly Belly Nice",
    "track 3" : "Mercy",
    "track 4" : "Gaucho",
    "track 5" : "Sweet",
    "track 6" : "The Riff",
    "track 7" : "Belly Full",
    "track 8" : "If Only",
    "track 9" : "Rooftop",
    "track 10" : "Snow Outside",
    "track 11" : "Drunken Soldier"
    }
comeTomorrow = {
    "year" : "2018",
    "track 1" : "Samurai Cop (Oh Joy Begin)",
    "track 2" : "Can't Stop",
    "track 3" : "Here On Out",
    "track 4" : "That Girl Is You",
    "track 5" : "She",
    "track 6" : "Idea of You",
    "track 7" : "Virginia in the Rain",
    "track 8" : "Again and Again",
    "track 9" : "bkdkdkdd",
    "track 10" : "Black and Blue Bird",
    "track 11" : "Come On Come On",
    "track 12" : "Do You Remember",
    "track 13" : "Come Tomorrow",
    "track 14" : "When I'm Weary"
    }


# NUMBER OF STUDIO ALBUMS
# print("The number of studio albums the band currently has released: " + str(numAlbums))
# numAlbums = len(albums)

# fn for printing the user created variable favAlbum
def showFavAlbum():
        print(favAlbum)
        return;


        
# STUDIO ALBUMS
albums = ["Crash", "Under the Table and Dreaming", "Before These Crowded Streets",
          "Busted Stuff", "Everyday", "Stand Up", "Big Whiskey and the GrooGrux King",
          "Away from the World", "Come Tomorrow"]        
# asking user for their favorite
favAlbum = input("What is your favorite album? ")
'''
if favAlbum in albums:
        print(favAlbum + " is good.") 
else:
        print("A favorite album is hard to pick. Here is the list: ")
        print(albums)
# CURRENT BAND MEMBERS                
members = ["Dave Matthews", "Carter Beauford", "Stefan Lessard", "Tim Reynolds",
                "Jeff Coffin", "Rashawn Ross", "Buddy Strong"]               

favMember = input("Who is your favorite musician?")
if favMember in members:
  print(favMember + " is a great musician!") 
else:
        print("Here are the members: ")
        print(members)

# print track listing
'''
answer = input("Do you want a track listing: ")
if answer == "yes":
        for key, value in favAlbum:
          print (key, value)
elif answer == "no":
    print("How many shows have you been to?")
else:
    print("Please enter yes or no.")


        
                 
