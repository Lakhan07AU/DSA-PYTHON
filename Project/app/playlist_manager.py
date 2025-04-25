# Playlist storage
songs = []

# Function to add a song to the playlist
def add_song(title, artist, duration):
    songs.append([title, artist, duration, 0])

# Function to delete a song by title
def delete_song(title):
    for i in range(len(songs)):
        if songs[i][0] == title:
            songs.pop(i)
            break

# Function to simulate playing a song
def play_song(title):
    for song in songs:
        if song[0] == title:
            song[3] += 1
            print(f"Now Playing: {song[0]} by {song[1]}")
            return
    print("Song not found!")

# Function to display the current playlist
def display_playlist():
    if not songs:
        print("\nPlaylist is empty.\n")
        return
    print("\n🎵 Playlist:")
    for song in songs:
        print(f"{song[0]} by {song[1]} - {song[2]}s - Played: {song[3]} times")
    print()

# Merge Sort based on popularity (number of plays)
def merge_sort_by_popularity(song_list):
    if len(song_list) <= 1:
        return song_list
    mid = len(song_list) // 2
    left = merge_sort_by_popularity(song_list[:mid])
    right = merge_sort_by_popularity(song_list[mid:])
    return merge(left, right)

def merge(left, right):
    sorted_list = []
    while left and right:
        if left[0][3] > right[0][3]:
            sorted_list.append(left.pop(0))
        else:
            sorted_list.append(right.pop(0))
    sorted_list.extend(left + right)
    return sorted_list

# Bubble Sort based on song title
def bubble_sort_by_title(song_list):
    n = len(song_list)
    for i in range(n):
        for j in range(0, n - i - 1):
            if song_list[j][0] > song_list[j + 1][0]:
                song_list[j], song_list[j + 1] = song_list[j + 1], song_list[j]

# Initial Songs (you can modify or remove these if needed)
add_song("Believer", "Imagine Dragons", 204)
add_song("Perfect", "Ed Sheeran", 263)
add_song("Blinding Lights", "The Weeknd", 200)
play_song("Perfect")
play_song("Believer")
play_song("Believer")

# Menu-driven interface
def menu():
    while True:
        print("\n===== Playlist Manager =====")
        print("1. Display Playlist")
        print("2. Add Song")
        print("3. Delete Song")
        print("4. Play Song")
        print("5. Sort by Title (Bubble Sort)")
        print("6. Sort by Popularity (Merge Sort)")
        print("7. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            display_playlist()
        elif choice == "2":
            title = input("Enter title: ")
            artist = input("Enter artist: ")
            try:
                duration = int(input("Enter duration (in seconds): "))
                add_song(title, artist, duration)
            except ValueError:
                print("Duration must be a number!")
        elif choice == "3":
            title = input("Enter title to delete: ")
            delete_song(title)
        elif choice == "4":
            title = input("Enter title to play: ")
            play_song(title)
        elif choice == "5":
            bubble_sort_by_title(songs)
            print("Sorted by title!")
        elif choice == "6":
            sorted_songs = merge_sort_by_popularity(songs)
            songs.clear()
            songs.extend(sorted_songs)
            print("Sorted by popularity!")
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

# Run the menu
if __name__ == "__main__":
    menu()

