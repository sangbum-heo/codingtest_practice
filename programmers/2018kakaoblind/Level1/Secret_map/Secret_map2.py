# 상수 입력받음 n은 1~15 arr의 값 개수는 n과 동일 // 이 코드를 처음 보았을 때 감탄을 금치 못했고 박수가 절로 나왔다.
# 함수 사용법을 몰라도 한 눈에 들어오고 깔끔하다는 느낌이 확 들어온다. 이게 코딩이지.
n=6
arr1=[46,33,33,22,31,50]
arr2=[27,56,19,14,14,10]

def solution(n, arr1, arr2):
    answer=[]

    # 압축 / 5번 반복
    for i,j in zip(arr1,arr2):

        # 2진수로 바꾸고 or 연산, 그리고 앞 두글자 지운 후 a12에 저장
        a12 = str((bin(i|j)[2:]))

        # 비어있는 자리수를 n 번째 자리수만큼 0으로 채움
        a12 = a12.rjust(n,'0')

        # 1을 #으로 바꿈
        a12 = a12.replace('1','#')

        # 0을 공백으로 바꿈
        a12 = a12.replace('0',' ')

        #답안에 a12 저장 (한줄씩)
        answer.append(a12)
    print(answer)
    
    return answer

solution(n,arr1,arr2)