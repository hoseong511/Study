# [기초-데이터형] 실수 1개 입력받아 그대로 출력하기2(설명)
# 자료형의 크기 float의 경우 +- 3.4*10-38 ~ +- 3.4*1038의 범위를 갖고 이 이상 벗어나면 오버플로우
# long float(double) 를 이용하면 +- 1.7*10-308 ~ +- 1.7*10308 를 이용하는 것이 가능해짐
# 하지만 파이썬의 자료형은 자유도가 높다가 장점. 대신 자료형이 따로 쓰이지 않기 때문에 메모리 누수가 심함 것이 단점.
a = input()
a = float(a)
print("%.11f" %a)