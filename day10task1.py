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
class Song:
    def __init__(self, title="", author="", lyrics=tuple()):
        self.title = title
        self.author = author
        self.lyrics = lyrics
        print(f"New Song made - {self.title} by {self.author}")
    
    def sing(self):
        print(f"{self.author} - {self.title}: ") 
        line1, line2, line3, line4 = self.lyrics      
        print(line1)
        print(line2)
        print(line3)
        print(line4)
        return self

    def yell(self):
        print(f"{self.author} - {self.title}: ") 
        line1, line2, line3, line4 = self.lyrics      
        print(line1.upper())
        print(line2.upper())
        print(line3.upper())
        print(line4.upper())
        return self

song1 = Song(title="Neverending Story", author="Limahl", lyrics = ("Reach the stars", "Fly a fantasy", "Dream a dream", "And what you see will be"))
song1.sing()
print("\n")
song1.yell()

# Minimum:
# Write a method sing that prints the song line by line on the screen, first printing the author and title, if any.
# Write a method yell that prints the song in capital letters line by line on the screen, first printing the author and title, if any.
# Bonus: make the above sing and chain methods chainable, so we can call them several times (chained)
# Bonus: create an additional parameter max_lines to yell and sing methods that prints only a certain number of lines for both sing and yell. Better do with some default value e.g. -1, at which all rows are then printed.
# Create multiple songs with lyrics
# Example:
# ziemelmeita = Song("Ziemeļmeita", "Jumprava", ["Gāju meklēt ziemeļmeitu","
# Garu, tālu ceļu veicu"])
# ziemelmeita.sing(1).yell()
# Outputs:
# Ziemeļmeita - Jumprava
# Gāju meklēt ziemeļmeitu
# Ziemeļmeita - Jumprava
# GĀJU MEKLĒT ZIEMEĻMEITU
# GARU, TĀLU CEĻU VEICU


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