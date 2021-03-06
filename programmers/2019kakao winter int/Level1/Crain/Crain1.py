board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]



def solution(board, moves):
    answer = 0
    result=[]

# for i in moves: 로 했으면 훨씬 더 깔끔했을 것.
    for i in range(len(moves)):
        for k in board:
            if (k[moves[i]-1]) != 0:
                tmp = k[moves[i]-1]
                k[moves[i]-1] = 0
                result.append(tmp)
                # tmp에 넣을 값을 바로 append 했으면 더 좋았을 것.
                # 변수를 줄일 수 있으면 줄이자. 의미 없는 메모리 낭비.

                if len(result) > 1:
                    if result[-1] == result[-2]:
                        print(result)
                        del result[-1]
                        del result[-1]
                        print(result)
                        answer+=2
                break

            
    print(answer)
    return answer

solution(board,moves)