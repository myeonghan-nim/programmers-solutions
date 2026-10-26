def solution(data, ext, val_ext, sort_by):
    # 컬럼 이름을 인덱스로 바꿔 ext 값이 val_ext보다 작은 행만 남긴 뒤 sort_by 값 기준으로 오름차순 정렬한다
    # 시간 복잡도: O(N log N) (N: data의 길이)
    columns = ["code", "date", "maximum", "remain"]
    ext_index, sort_index = columns.index(ext), columns.index(sort_by)
    return sorted((row for row in data if row[ext_index] < val_ext), key=lambda row: row[sort_index])
