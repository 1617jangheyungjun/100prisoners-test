<<<<<<< HEAD
# 100prisoners-test
=======
# 100prisoners-test

#코딩 #입문 #수학 #취미 #첫 블로그 #베리타시움 #피드백 환영

먼저 베리타시움님의 영상을 보고 만들었음을 밝힙니다.

[출처](https://www.youtube.com/watch?v=PE4vLbyOgw0&t=479s)


위의 영상을 간략하게 요약해 보자면 어느 방에는 1부터 100까지의 번호가 새겨진 죄수들이 있으며 다른 방에는 1부터 100이 적힌 쪽지가 들어있는 상자가 있다. 죄수들은 한 명씩 들어가서 50개의 상자를 열 수 있고 자신의 번호가 적힌 쪽지를 발견했다면 성공, 아니라면 실패를 한다. 100명 모두가 성공할 확률이 가장 높은 방법은 무엇인가?입니다.

​

​

결론부터 말하자면 그 방법은 모든 상자에 위에서부터 순서대로 번호를 부여한 뒤 자신의 번호의 상자에 가 그 상자를 열어 나온 쪽지의 번호를 확인한 후 그 번호의 상자로 가서 같은 작업을 반복하는 것입니다. 그 원리에 대해서는 유튜브 링크에 자세하게 나와있으니 참고해 주세요!

​

이영상을 보고 정말 30%에 근접하게 나오는 것인가?라는 궁금증이 생겼고 코딩으로 확인할 수 있을 거 같아 만들어 보게 됐습니다.

​

가장 먼저 이제부터 이런 궁금증을 확인하는 데에 사용할 취미 코딩이란 파일을 만들어 줬습니다.


vscode를 사용하여 만들 것이기 때문에 vscode의 파일 열기로 취미 코딩 파일을 열어 (100 prisoners.py)파일을 만들어 주었습니다.


먼저 죄수는 번호를, 상자는 안의 쪽지의 숫자를 넣어줘야 하니 리스트로 작성해 주었습니다.

상자 속의 쪽지는 무작위로 들어가야 하니 random 라이브러리도 불러와 주었습니다.
``` python
import random
prisoners = []
box_index = []
```
죄수에게 번호를 부여하는 코드를 작성해 줍니다.
``` python
for i in range(1,101):
    prisoners.append(i)
```
상자 속의 쪽지의 숫자를 부여하는 코드를 작성해 줍니다.
``` python
for i in range(1, 101):
    index_box = random.randint(1, 100)
    if index_box in box_index:
        index_box = random.randint(1, 100)
    box_index.append(index_box)
```
위 코드를 작성하고 box_index를 출력해 보니 


이러한 결과가 나왔습니다. 저는 index_box가 box_index 안에 있으면 다시 뽑는 코드를 작성했지만 중복되는 숫자들이 보였습니다.

확인 결과 if 문으로 작성을  하여 중복이 나왔을 때 다시 뽑긴 하지만 다음 번호도 중복되는 경우가 나와 이러한 현상이 일어난 것이었습니다.

따라서 중복이 나오면 안 나올 때까지 다시 뽑을 수 있게 while 문으로 변경해 주었습니다.
``` python
for i in range(1, 101):
    index_box = random.randint(1, 100)
    while index_box in box_index:
        index_box = random.randint(1, 100)
    box_index.append(index_box)
```


이렇게 결과가 나왔지만 중복이 있는지 확인하기 어려워 sort 함수를 사용해 오름차순으로 정렬해 주었습니다.


set로 확인해도 되지만 sort를 사용한 이유는 1부터 100까지 잘 들어가 있는지 확인하기 위해 사용했습니다.

​

이제 박스 안에 랜덤하게 숫자가 잘 들어가는 것을 확인했으니 죄수들이 순서대로 나와 번호를 뽑을 차례입니다.

​

50번 안에 성공했는지 확인하기 위해 success 리스트를 추가해 줍니다.
``` python
from operator import index
import random
from re import I
win = []
lose = []
while True:
    prisoners = []
    box_index = []
    for i in range(100):
        prisoners.append(i)
    print(prisoners)

    for i in range(1, 101):
        index_box = random.randint(0,99)
        while index_box in box_index:
            index_box = random.randint(0,99)
        box_index.append(index_box)

    success = []
```
그 후 죄수들을 한 명씩 들여보내서 상자를 열고 그 상자의 번호에 따른 상자를 열고를 50번 반복하는 코드를 작성해 줍니다.
``` python
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
```
코드를 보면 박스의 번호가 죄수의 번호가 일치하면 성공을 추가하고 아니라면 한 번 더 반복하며 반복 횟수를 1추가 해줍니다.

반복 횟수가 50회가 넘어가면 F를 추가해 줍니다.

success 변수를 출력하면 다음과 같습니다.



원하는 결과는 나왔지만 궁극적으로 3분의 1확률 즉 33퍼센트의 확률로 나오는지 확인이 불가능합니다.

따라서 전체가 T가 나오는 확률을 계산하는 코드를 추가해 줍니다.
``` python
from operator import index
import random
from re import I
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
    print(len(win) / up * 100)
```
         
먼저 반복할 횟수를 입력받은 뒤  그 숫자를 repeater에 저장하고 전체 코드 반복 횟수를 up에 저장합니다.

그 후 while 문을 사용해 repeater가 up보다 크다면 무한 반복하게 만들어줍니다.

만약 죄수들이 성공했다면 success 변수 안에는 T만이 남아있을 것이므로 set를 사용하여 중복을 없애줬을 때 길이가 1이라면 win에 아니라면 lose에 저장하고 반복 횟수를 사용하여 성공 확률이 몇 %있지 알려줍니다.

​

결과는

34.48637316561845

34.45026178010471

34.51882845188285

34.48275862068966

34.44676409185804

34.51511991657977

34.479166666666664

34.443288241415196

34.407484407484404

34.3717549325026

34.33609958506224

34.30051813471503

34.368530020703936

34.4364012409514

34.40082644628099

34.46852425180599

34.43298969072165

34.5005149330587

34.465020576131685

34.42959917780062

34.496919917864474

34.56410256410257

34.52868852459016

34.5957011258956

34.56032719836401

34.52502553626149

34.48979591836735

34.454638124362894

34.521384928716905

34.58799593082401

34.552845528455286

34.619289340101524

34.5841784989858

34.549138804457954

34.51417004048583

34.580384226491404

34.64646464646465

34.61150353178608

34.57661290322581

34.64249748237664

34.70824949698189

34.67336683417086

34.63855421686747

34.60381143430291

34.569138276553105

34.53453453453454

34.5

​

이 나왔습니다.

​

결론적으로  영상에서처럼 같은 방식을 사용한다면 3분의 1인 33퍼센트에 근접한다는 것을 확인했습니다.. ㄷㄷ

​

하지만 아직 제대로 된 시각화가 안 되어있습니다. 이게 언제 끝날지도 모르겠고 어느 정도의 루트가 돈 것인지 보이지 않습니다. 따라서 시각화 작업을 해주겠습니다.

​
``` python
print("계산중 {0}%완료 예상 완료시간 {1}초".format(int(up / repeater * 100), int((repeater - up) / 360 + 1)))
```
아까 만들어둔 up 변수와 repeater 변수를 이용하여 전체의 몇 퍼센트의 루트가 돌았는지 몇 초 정도가 남았는지 계산하여 보여줍니다.
``` python
print("""성공횟수 {0}번
실패횟수 : {1}
성공확률 {2}%

""".format(len(win), len(lose), int(len(win) / up * 100)))
```
마지막으로 최종 성공 횟수와 실패 횟수 성공 확률을 len 함수를 사용해 보여주도록 하였습니다.


최종 결과입니다.

성공 횟수와 실패 횟수가 잘 나오고 계산 시간도 잘 나오고 있습니다.

​

이 작업을 무한 반복하게 하여 여러 번 실행할 수 있게 하였습니다. 

최종 코드입니다.
``` python
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

        print("계산중 {0}%완료 예상 완료시간 {1}초".format(int(up / repeater * 100), int((repeater - up) / 360 + 1)))
    print("""성공횟수 {0}번
실패횟수 : {1}
성공확률 {2}%

""".format(len(win), len(lose), int(len(win) / up * 100)))
```
제가 프로그래밍 초보라 피드백은 언제나 환영입니다!!

감사합니다
>>>>>>> cead179 (완성본)
