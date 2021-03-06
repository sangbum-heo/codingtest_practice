n=6
arr1=[46,33,33,22,31,50]
arr2=[27,56,19,14,14,10]

def solution(n, arr1, arr2):
    answer=[]
    for i,j in zip(arr1,arr2):
        tmp = bin(i|j)[2:]
        tmp = tmp.rjust(n,'0')
        tmp = tmp.replace('1','#')
        tmp = tmp.replace('0',' ')
        answer.append(tmp)

    print(answer)
    return answer
solution(n,arr1,arr2)