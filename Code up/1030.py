# [기초-데이터형] 정수 1개 입력받아 그대로 출력하기2(설명)
# long long int 는 파이썬에 없다.
# 하지만 파이썬의 자료형은 자유도가 높다가 장점. 대신 자료형이 따로 쓰이지 않기 때문에 메모리 누수가 심함 것이 단점.
a = input()
a = int(a)
print(a)