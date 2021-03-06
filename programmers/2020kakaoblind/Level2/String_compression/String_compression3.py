s="aabbacc"

def compress(text, tok_len):
    words = [text[i:i+tok_len] for i in range(0, len(text), tok_len)]
    print("words :",words)
    
    res = []
    cur_word = words[0]
    cur_cnt = 1
    for a, b in zip(words, words[1:] + ['']):
        if a == b:
            cur_cnt += 1
        else:
            res.append([cur_word, cur_cnt])
            cur_word = b
            cur_cnt = 1
            print("===res : ",res)
    return sum(len(word) + (len(str(cnt)) if cnt > 1 else 0) for word, cnt in res)


# 나는 tok_len 을 floor(내림)으로 만들어서 마지막에 떨어지지 않을 때 예외처리를 해주어야 했는데 이렇게(+1) 하니 그럴 필요가 없다!? ㄴㄴㄴㄴㄴ
# 아니네 range(1,4)면 1,2,3 이 리스트에 들어가니까 똑같네;

# list에 [len(text)] 를 더해주지 않으면 한글자가 입력되었을 때 오류 발생 !!
def solution(text):
    print( list(range(1, int(len(text)/2) + 1)) + [len(text)])
    return min(compress(text, tok_len) for tok_len in list(range(1, int(len(text)/2) + 1)) + [len(text)])

solution(s)
print("===============test===============")
print(list(range(1,10)))

for i in range(0,9,4):
    print(i)
