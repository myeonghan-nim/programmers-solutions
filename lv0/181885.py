def solution(todo_list, finished):
    # zip으로 일과 완료 여부를 짝지어 아직 마치지 못한(false) 일만 순서대로 담는다
    return [todo for todo, done in zip(todo_list, finished) if not done]
