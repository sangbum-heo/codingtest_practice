s="aabbaccc"

def solution(text):
    # text가 1글자면 1 반환
    if len(text) == 1:
        return 1

    # result의 길이 경우의 수들을 배열로 저장
    result2=[]

    # i글자씩 잘랐을 때의 경우의 수를 알아보기 위한 반복
    for i in range(1,int(len(text)/2)+1):

        # 같은 요소가 몇 번 반복되었는지 확인하기 위한 변수
        num=1

        # i글자씩 잘랐을 때 앞의(이전) 요소가 무엇인지 확인하기 위한 변수
        front=""

        # i글자씩 잘랐을 때 어떤 요소가 몇 번씩 반복되는지 result 배열에 저장
        result=[]

        # i글자씩 잘랐을 때의 각 요소들을 알아보기 위한 반복
        for j in range(0,len(text)+i,i):    # len(text) 에 + i를 해주어야 마지막 요소의 자리수가 맞아 떨어지지 않아도 유동적으로 마지막까지 입력받을 수 있다.

            # 요소를 나누는 기준 text[j:j+i]    j : 현재 몇 번째 요소(반복)인지,  i: 몇 개를 기준으로 자르는지.
            # 따라서 text[j:j+i]로 나누게되면 현재 몇번째 요소부터 몇개씩 기준으로 자르는지(slicing) 구할 수 있다.
            
            # (front에 값이 없다면:)
            # print("i :",i,"/ j :",j,text[j:j+i])
            # text의 첫 번째 슬라이스면 front에 저장 (j가 0이면 첫번째 요소이기 때문에, 이전 요소라고 정의한 front에 값을 넣어준다.)
            if j == 0:
                front = text[j:j+i]

            # 첫번째 요소가 아니라면 (front에 값이 있다면)
            else:

                # 이전 요소와 현재 요소가 같다면 num 1 증가
                if front == text[j:j+i]:
                    num+=1
                
                # 이전 요소와 현재 요소가 다르다면
                else:

                    # 그 이전에 반복된 요소가 없었다면 result에 현재 요소 append
                    if num == 1:
                        result.append(front)
                        # front = text[j:j+i] 왜 여기에 이게 들어가지 않아도 정상 작동할까????????????????????????????????????????????????
                        # else문 아래 (Line 54)에서 똑같은걸 해주니까 그러지 바보야!!!!!!!!!!!!  <<<<<<<<

                    # 그 이전에 반복된 요소가 있었다면 몇 번 반복되었는지와 함께 result에 현재 요소 append,  num은 1로 초기화,  front에 현재 요소를 저장(다음 요소를 위해)
                    else:
                        result.append(str(num)+front)
                    front = text[j:j+i]
                    num=1
                        
        print("result :",result)
        result2.append(sum(len(k) for k in result))
        print("len :",result2)
    answer = min(result2)
    print("answer :",answer)
    return answer
solution(s)