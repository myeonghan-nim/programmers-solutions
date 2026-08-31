def solution(genres, plays):
    # 장르별 총 재생 수와 장르별 곡 목록을 만든 뒤, 총 재생 수가 많은 장르부터 곡을 (재생 수 내림차순, 고유 번호 오름차순)으로 정렬해 최대 2곡씩 담는다.
    # 시간 복잡도: O(n log n)
    genre_total = {}
    genre_songs = {}
    for idx, (genre, play) in enumerate(zip(genres, plays)):
        genre_total[genre] = genre_total.get(genre, 0) + play
        genre_songs.setdefault(genre, []).append((idx, play))

    answer = []
    for genre in sorted(genre_total, key=lambda g: genre_total[g], reverse=True):
        songs = sorted(genre_songs[genre], key=lambda song: (-song[1], song[0]))
        answer.extend(idx for idx, _ in songs[:2])

    return answer
