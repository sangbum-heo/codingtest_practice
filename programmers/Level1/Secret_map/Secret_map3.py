# 상수 입력받음 n은 1~15 arr의 값 개수는 n과 동일 /20201211 first practice
n=6
arr1=[46,33,33,22,31,50]
arr2=[27,56,19,14,14,10]

def solution(n, arr1, arr2):
    answer=[]

    for i, j in zip(arr1,arr2):
        line = bin(i | j)[2:]
        line = line.rjust(n,"0")
        line = line.replace("1","#")
        line = line.replace("0"," ")
        answer.append(line)
        
    print(answer)
    return answer

solution(n,arr1,arr2)