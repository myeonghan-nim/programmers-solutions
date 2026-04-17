def solution(genres, plays):
    def is_better(song_a, song_b):
        return song_a[1] > song_b[1] or (song_a[1] == song_b[1] and song_a[0] < song_b[0])

    genre_total = {}
    genre_top_songs = {}
    for idx, (genre, play) in enumerate(zip(genres, plays)):
        genre_total[genre] = genre_total.get(genre, 0) + play
        
        top_songs = genre_top_songs.setdefault(genre, [])
        current_song = (idx, play)
        if not top_songs:
            top_songs.append(current_song)
            continue

        if len(top_songs) == 1:
            if is_better(current_song, top_songs[0]):
                top_songs.insert(0, current_song)
            else:
                top_songs.append(current_song)
            continue

        if is_better(current_song, top_songs[0]):
            top_songs[1] = top_songs[0]
            top_songs[0] = current_song
        elif is_better(current_song, top_songs[1]):
            top_songs[1] = current_song

    answer = []
    for genre, _ in sorted(genre_total.items(), key=lambda item: item[1], reverse=True):
        answer.extend(idx for idx, _ in genre_top_songs[genre])

    return answer
