def open_songs(filee):
    new_list = []
    with open(filee, 'r') as file:
        print("Songs sorted")
        for line in file.readlines():
            print(line)
            new_list.append(line.strip())
    return new_list


def list_to_sort(song_list):
    sorted_list = sorted(song_list)
    return sorted_list


def save_new(sorted_songs, fileee):
    with open(fileee, 'w') as file:
        print("Songs sorted" + '\n')
        for i in sorted_songs:
            file.write(i + '\n')
            print(i)


songs_list = open_songs('my songs.txt')
sorted_songs = list_to_sort(songs_list)
save_new(sorted_songs, 'new songs.txt')