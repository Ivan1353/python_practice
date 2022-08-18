def add_songs(*args):
    song_dict = {}
    for song in args:
        title = song[0]
        lyrics = song[1]

        if title not in song_dict:
            song_dict[title] = lyrics
        elif title in song_dict:
            song_dict[title].extend(lyrics)

    end_string = ""
    for title in song_dict:
        song_string = f"- {title}\n"
        if song_dict[title]:
            song_string += '\n'.join(song_dict[title])+'\n'
        else:
            song_string += '\n'.join(song_dict[title])
        end_string += f"{song_string}"

    return end_string