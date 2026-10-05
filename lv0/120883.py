def solution(id_pw, db):
    # db를 아이디→비밀번호 딕셔너리로 만들어, 아이디가 없으면 "fail", 비밀번호까지 맞으면 "login", 아니면 "wrong pw"를 돌려준다
    user_id, pw = id_pw
    accounts = dict(db)
    if user_id not in accounts:
        return "fail"
    return "login" if accounts[user_id] == pw else "wrong pw"
