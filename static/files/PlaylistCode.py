## ------------------------------------------------------
##        Name: Lauren Forando
##    Filename: Playlist Code
##        Date: March 20, 2019
## ------------------------------------------------------

import webbrowser

#Define command which has the defined input function (user_command) within it
def command():
    user_command = input("please select an option (ADD, REMOVE, PLAY, PRINT, or QUIT): ").upper()

    #brings answer back down to main
    return user_command 

#Define Add_Song function to add a song. Add_Song calls upon the list 'songs' which is defined in main
def Add_Song(songs):
    
    #Create an empty dictionary called my_playlist
    my_playlist = { }
    
    #Ask for song information from the user
    my_playlist["title"] = input("Enter the name of a song: ")
    my_playlist["artist"] = input("Artist: ")
    my_playlist["album"] = input("Album: ")
    my_playlist["url"] = input("Spotify URL: ")

    #Add song information from the dictionary 'my_playlist' to the list 'songs'
    songs.append(my_playlist)
    
#Define Remove_Song function to remove a song from my_playlist
def Remove_Song(songs):
    
    #If the list 'songs' is empty, tell the user to add a song first
    if songs == [ ]:
        print("Please add a song first")
        
    #Make 'i' into a string to create a counter starting from 1.
    #Here we are pulling out specific information from the 'songs' list
    else:
        for i in range(len(songs)):
            print(str(i+1) + ".", "'",str(songs[i]["title"]),"'", "by", songs[i]["artist"], "(",str(songs[i]["album"]),")")

        #remove song according to its position in 'songs' list
        print()
        remove_song = eval(input("Enter the number (ie. 1, 2, 3, etc) of the song you would like to remove: "))
        del songs[remove_song - 1]
        print("...DONE...song has been removed")
                           
#Define Print_Song to print 'songs' list
def Print_Song(songs):
    #If the list 'songs' is empty, tell the user to add a song first
    if songs == [ ]:
        print("Please add a song first")
    
    else:
        for i in range(len(songs)):
            print(str(i+1) + ".", "'",str(songs[i]["title"]),"'", "by", songs[i]["artist"], "(",str(songs[i]["album"]),")")

#Define Play_Song to select a linked song using webbrowser.open()
def Play_Song(songs):
    
    #If the list 'songs' is empty, tell the user to add a song first
    if songs == [ ]:
        print("Please add a song first")
        
    else:
        for i in range(len(songs)):        
            print(str(i+1) + ".", "'",str(songs[i]["title"]),"'", "by", songs[i]["artist"], "(",str(songs[i]["album"]),")")

        print()
        play_song = eval(input("Enter the number (ie. 1, 2, 3, etc) of the song you would like to play: "))
        webbrowser.open(songs[play_song - 1]["url"]) #select song by position while specifying url 

#Define main() to store the beginning interface and all of the commands
def main():
    songs = [ ]
    print("Welcome to your music library! ¯\_(ツ)_/¯ ")
    print( "           ~Main Menu~")
    user_command = command()

    while user_command != "QUIT":

        if user_command == "ADD":
            print()
            Add_Song(songs)
            print()
            user_command = command()

        elif user_command == "REMOVE":
            print()
            Remove_Song(songs)
            print()
            user_command = command()

        elif user_command == "PRINT":
            print()
            Print_Song(songs)
            print()
            user_command = command()

        elif user_command == "PLAY":
            print()
            Play_Song(songs)
            print()
            user_command = command()

                    
    print("Thanks for listening!")


if __name__ == "__main__":
    main()


    
