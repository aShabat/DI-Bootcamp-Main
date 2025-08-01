# 3
# Step 1: Create the Song Class
#
#     Create a class called Song.
#     In the __init__ method, take lyrics (a list) as a parameter and create a corresponding attribute.
#     Create a sing_me_a_song() method that prints each element of the lyrics list on a new line.


class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)
