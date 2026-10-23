def solution(video_len, pos, op_start, op_end, commands):
    # 모든 시각을 초로 바꿔 계산하고, 각 명령을 실행하기 전과 모든 명령이 끝난 뒤에 현재 위치가 오프닝 구간 안이면 오프닝 끝으로 옮긴다
    # 시간 복잡도: O(len(commands))
    def to_seconds(time):
        minutes, seconds = map(int, time.split(":"))
        return minutes * 60 + seconds

    length, cur, start, end = map(to_seconds, (video_len, pos, op_start, op_end))
    for command in commands:
        if start <= cur <= end:
            cur = end
        cur = max(cur - 10, 0) if command == "prev" else min(cur + 10, length)  # 처음(0초)과 끝(영상 길이)을 넘지 않게 자른다
    if start <= cur <= end:  # 마지막 명령으로 오프닝에 들어갔을 때도 건너뛴다
        cur = end
    return f"{cur // 60:02d}:{cur % 60:02d}"
