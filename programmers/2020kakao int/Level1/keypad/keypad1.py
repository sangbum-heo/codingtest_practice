numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = "right"

def solution(numbers, hand):
    answer = ''
    L_Position = 10
    R_Position = 10
    
    # 이 방식으로 하면 양 옆 비교는 되는데 위 아래 비교가 안 되는듯(넘버가 5일 경우 2와 8은 거리가 같은데 컴퓨터가 어떻게 알까....?)

    for i in numbers:
        k=0
        
        if i == 1 or i == 4 or i == 7:
            answer+="L"
        elif i == 3 or i == 6 or i == 9:
            answer+="R"

        # 첫 번째 번호가 2,5,8,0 일 경우도 생각해야해
        else:
            if (i-L_Position < i-R_Position):
                answer+="L"
            elif (i-L_Position > i-R_Position):
                answer+="R"
            elif (hand == "right"):
                answer+="R"
            else:
                answer+="L"
            
            if answer[-1] == "L":
                L_Position = i
                print("L :",L_Position)
            else:
                R_Position = i
                print("R :",R_Position)
            k=1


        # 손가락 위치 저장
        if k==0:
            if answer[-1] == "L":
                L_Position = i+1
                print("L :",L_Position)
            else:
                R_Position = i-1
                print("R :",R_Position)
        print(answer)
        

    
    return answer

solution(numbers,hand)