# 상수 입력받음 n은 1~15 arr의 값 개수는 n과 동일 /20201211 first practice
n=6
arr1=[46,33,33,22,31,50]
arr2=[27,56,19,14,14,10]

def solution(n, arr1, arr2):
    answer=[]

    #0으로 채우는 자리수를 변수로 받기 위해 
    zero_num="{}:0>{}{}".format("{",n,"}")

    # 10진수를 2진수로 바꾸고 앞 두자리 지움
    for i in range(n):
        arr1[i] = zero_num.format(bin(arr1[i])[2:])
        arr2[i] = zero_num.format(bin(arr2[i])[2:])

    for i in range(n):
        imsi=""

        #arr1과 arr2를 or 비교하여 #을 넣는다. 그게 아니면 공백을 넣는다
        for j in range(n):
            if arr1[i][j] == '1' or arr2[i][j] == '1':
                imsi+="#"
            else:
                imsi+=" "
        # answer에 한줄씩 답안을 한줄씩 append
        answer.append(imsi)

    return answer