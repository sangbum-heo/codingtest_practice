numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = "right"

#행과 열을 하나씩 비교해보는거지 행에서 몇이 차이나고 열에서 몇이 차이나고 그 차이를 기반으로 누가 더 가까운지(적은 움직임으로 누를 수 있는지 확인 )
# 1,1을 누르는데 왼손은 3,0 오른손 3,1 / 왼손은 행 2차이 + 열 1차이 (총 3차이), 오른손은 행 2차이// 오른손이 차이가 적으므로 오른손이 더 가까움

def solution(numbers, hand):
    answer = ''
    go_pos=[]
    l_pos=[[3,0]]
    r_pos=[[3,2]]
    keypad = [[1,2,3],
              [4,5,6],
              [7,8,9],
              ['*',0,'#']]

    for i in numbers:
        
        go_pos=[[j,k] for j in range(4) for k in range(3) if keypad[j][k]==i]

        if i == 1 or i == 4 or i == 7:
            answer+="L"
        elif i == 3 or i == 6 or i == 9:
            answer+="R"
        
        elif (abs(l_pos[0][0] - go_pos[0][0]) + abs(l_pos[0][1] - go_pos[0][1])) < (abs(r_pos[0][0] - go_pos[0][0]) + abs(r_pos[0][1] - go_pos[0][1])):
            answer+="L"
        elif (abs(l_pos[0][0] - go_pos[0][0]) + abs(l_pos[0][1] - go_pos[0][1])) > (abs(r_pos[0][0] - go_pos[0][0]) + abs(r_pos[0][1] - go_pos[0][1])):
            answer+="R"
        
        elif hand == "left":
            answer+="L"
        else:
            answer+="R"

        if answer[-1] == "L":
            l_pos = go_pos
        else:
            r_pos = go_pos

    print(answer)
    return answer

solution(numbers,hand)