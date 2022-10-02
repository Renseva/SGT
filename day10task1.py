# # Day 10 - Work in Class - Classes and Objects
# 1. Song class
# define a class Song
# The class constructor needs to have three additional 3 parameters (self and 3 more!)
# title defaults to empty string
# author defaults to empty string
# lyrics by default empty tuple
# inside constructor method:
# set/store these three parameters inside objects variables of the same name (remember to use self!)
#  print on the screen "New Song made" - (try also printing here author and title!)
# Minimum:
# Write a method sing that prints the song line by line on the screen, first printing the author and title, if any.
# Write a method yell that prints the song in capital letters line by line on the screen, first printing the author and title, if any.
# Bonus: make the above sing and chain methods chainable, so we can call them several times (chained)
# Bonus: create an additional parameter max_lines to yell and sing methods that prints only a certain number of lines for both sing and yell. Better do with some default value e.g. -1, at which all rows are then printed.
# Create multiple songs with lyrics

class Song:
    def __init__(self, title="", author="", lyrics=tuple()):
        self.title = title
        self.author = author
        self.lyrics = lyrics
        print(f"New Song made - {self.title} by {self.author}")
    
    def sing(self, max_lines):
        print(f"{self.author} - {self.title}: ")    # print author/title header
        if max_lines > 0:                           # check max lines positive integer
            lines = list(self.lyrics)               # lyrics from tuple to list
            it = 0                                  # iterations start value
            for i in lines:                         # loop through lyrics lines
                print(i)                            # print current line
                it += 1                             # note iteration
                if it == max_lines:                 # break the loop once max lines reached
                    break
        return self

    def yell(self, max_lines):
        print(f"{self.author} - {self.title}: ")    # similar to def sing above
        if max_lines > 0:
            lines = list(self.lyrics)
            it = 0
            for i in lines:
                print(i.upper())                    # print lines in uppercase
                it += 1
                if it == max_lines:
                    break
        return self

song1 = Song(title="Neverending Story", author="Limahl", lyrics = ("Reach the stars", "Fly a fantasy", 
"Dream a dream", "And what you see will be", "Rhymes that keep their secrets", "Will unfold behind the clouds", 
"And there upon a rainbow", "Is the answer to a never-ending story", "Show no fear", "For she may fade away", "In your hand", 
"The birth of a new day"))

song2 = Song(title="Stay on these roads", author="A-ha", lyrics = ("The cold has a voice", "It talks to me", 
"Stillborn, by choice", "And it airs no need to hold", "Old man, feels the cold", "Oh baby don't", "'Cause I've been told", 
"Stay on these roads", "We shall meet, I know", "Stay on, my love", "We shall meet, I know", "I know", 
"Where joy should reign", "These skies restrain", "Shadow of your love", "The voice trails off again", "The voice trails off again", 
"Stay on these roads", "We shall meet, I know", "Stay on, my love", "You feel so weak, be strong"))

song3 = Song(title="Long time sun", author="Snatam Kaur", lyrics=("May the long-time sun", "Shine upon you", 
"All love surround you", "And the pure light", "Within you", "Guide your way on", "Guide your way on"))

# song3.yell(3)
# song3.sing(0)


# 2. Rap class
# For those feeling comfortable with class syntax, create a Rap class that inherits from Song
# # no new constructor method is necessary (you can if you want)
#  add a new method break_it with two default parameters max_lines=-1 and drop equal to "yeah", which is similar to sing, but adds a drop after each word .
# Example: 
# zrap = Rap("Ziemeļmeita", "Jumprava", ["Gāju meklēt ziemeļmeitu","
# Garu, tālu ceļu veicu"])
# zrap.break_it(1, "yah")
# Ziemeļmeita - Jumprava
# Gāju YAH meklēt YAH ziemeļmeitu YAH

class Rap(Song):                                        # inherited class
    def break_it(self, max_lines=-1, drop = "Yeah"):
        print(f"{self.author} - {self.title}: ")        # print author, song title header
        if max_lines > 0:                               # check max lines positive int
            lines = list(self.lyrics)                   # lyrics tuple to list  
            it = 0                                      # iteration start
            for i in lines:                             # loop through lines (which are str)
                i = i.replace(" ", " " + drop + " ")    # replace spaces with drop value
                print(i, end = " " + drop + "\n")       # print modified line
                it += 1                                 # note iteration
                if it == max_lines:                     # stop loop once max lines reached
                    break
        return self

song4 = Rap(title="Long time sun", author="Snatam Kaur", lyrics=("May the long-time sun", "Shine upon you", 
"All love surround you", "And the pure light", "Within you", "Guide your way on", "Guide your way on"))

# song4.break_it(2, "LA")