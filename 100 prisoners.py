from operator import index
import random
from re import I
while True:
    win = []
    lose = []
    up = 0
    repeater = int(input("원하는 반복 횟수를 작성해 주세요 : "))
    while repeater > up:
        prisoners = []
        box_index = []
        for i in range(100):
            prisoners.append(i)

        for i in range(1, 101):
            index_box = random.randint(0,99)
            while index_box in box_index:
                index_box = random.randint(0,99)
            box_index.append(index_box)

        success = []

        for i in prisoners:
            repeat = 0
            box_indexer = box_index[i]
            box_index_text = box_index[i]
            while repeat <= 50:
                box_indexer = box_index[box_index_text]
                if i == box_indexer:
                    success.append("T")
                    repeat = 51
                else:
                    box_index_text = box_indexer
                    repeat += 1
                    if repeat == 50:
                        success.append("F")
        if len(set(success)) == 1:
            win.append(1)
            
        else:
            lose.append(1)
        
        up += 1

        print("계산중 {0}%완료 | 예상 완료시간 {1}초".format(int(up / repeater * 100), int((repeater - up) / 600 + 1)))
    print("""성공횟수 : {0}번
실패횟수 : {1}
성공확률 {2}%

""".format(len(win), len(lose), int(len(win) / up * 100)))