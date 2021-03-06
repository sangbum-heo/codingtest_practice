# n은 60000 이하의 자연수.
n = 2;

# 길이 2에 대해서는 2가지 경우의 수, 길이 1에 대해서는 1가지 경우의 수. <- 이게 가장 기본
# but, 길이 2에 대한 2가지 경우의 수 중 하나는, 길이 1에 대한 경우의 수와 중복될 수 있다. (규칙은?)
# 길이 1은 길이 2에 포함되는 개념으로 생각하야 하나?
# 길이가 3이면 2가 1번 들어갈 수 있고. 1은 2번 들어갈 수 있다. ( 1이 2번 들어갈 수 있게되는 규칙?)
# 길이가 4이면 2가 2번 들어갈 수 있고, 1은 


def solution(n):
    answer=1 # │││││ 모양 1개 미리 더해줌 (밑에서는 = 모양이 몇개 들어가나 경우의 수 계산)

    # 첫번째 칸부터 마지막 -1번째 칸까지 i를 통해 반복
    # i번째 칸부터 마지막 -1번째 칸까지 j를 통해 반복?
    # n의 값이 크다면 i 안에서 수많은 경우의 수가 생기는데.. 그걸 반복적으로 캐치해야해

    # 지금 이대로면 for 안에 for 안에 for 안에 계속 무한반복으로 만들어야되는건가?
    # 아니면 새로운 경우의 수에 대한 for문을 만들 수 있는걸까?

    for i in range(1,n):
        answer+=1 # 반복되지 않는 요소, i의 index값에 = 하나만 들어간 상황.
        print("i :",i)
        
        for j in range(i+2,n):
            answer+=1
            print("j :",j)
            
            for k in range(j+2,n,2):
                answer+=1
                print("k :",k)
        print("=====")        

    # for i in range(1,n):
    #     print(" i :",i)
    #     print("=======")
    #     for j in range(i,n,2):
    #         answer+=1
    #         print(" j :",j)
    #     print("=======")
    answer = answer % 1000000007
    print("answer : ",answer)
    # return answer

solution(7)