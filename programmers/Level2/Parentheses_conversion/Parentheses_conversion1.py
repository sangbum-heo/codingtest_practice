p="())())(("

# 이번 문제 key point - 재귀 함수 이용!!

def fix(u):# ??????????????
    global res
    res+="("+u[1:-1]+")"
    u=u[1:-1]
    if u != "":
        fix(u)


    return res

def divide(w):
    open=0
    close=0
    u=""
    v=""
    for i in w:
        # print("i :",i)
        # 최소 길이의 균형잡힌 문자열로 나누기
        if open==close and open != 0:
            v+=i
        else:
            u+=i
            if i == "(":
                open+=1
            else:
                close+=1
    print("u :",u)
    print("v :",v)
    global answer
    answer+=fix(u)

    if v != "":
        divide(v)
        
def solution(text):
    global answer
    answer=""
    global res
    res=""
    divide(text)
    print("answer :",answer)

    return answer;

solution(p)