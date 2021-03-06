# 다른 사람의 풀이 참고해서 만든 코드
board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

def solution(board, moves):
    answer = 0
    stacklist=[]

    for i in moves:
        for j in board:
            if (j[i-1]) != 0:
                stacklist.append(j[i-1])
                j[i-1] = 0
                
                if len(stacklist) > 1:
                    if stacklist[-1] == stacklist[-2]:
                        del stacklist[-1]
                        del stacklist[-1]
                        answer+=2
                break

    print(answer)
    return answer

solution(board,moves)