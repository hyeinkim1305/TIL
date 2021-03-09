import requests
import random
from django.shortcuts import render

def lotto(request):
  url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=953'
  res = requests.get(url)   # 요청을 보내서 정보를 받아와
  res_dict = res.json()
  res_list = []   # 로또 당첨 번호
  for i in range(1, 7):
    # res_list.append(res_dict[f'drwtNO{i}'])  이렇게도 할 수 있음 
    res_list.append(res_dict.get("drwtNo"+str(i)))
  vonus = []    # 보너스 번호
  vonus.append(res_dict.get("bnusNo"))

  # 무작위 생성 로또 번호
  rank = [0] * 6     # 1등 ~ 꽝 개수
  for i in range(1000):
    cnt = 0
    v_cnt = 0
    pick = random.sample(range(1, 46), 6)
    for j in pick:
      if j in res_list:
        cnt += 1
      if j in vonus:
        v_cnt += 1
    if cnt == 6:    # 딕셔너리로도 할 수 있음 
      rank[0] += 1
    elif cnt == 5 and v_cnt == 1:
      rank[1] += 1
    elif cnt == 5:
      rank[2] += 1
    elif cnt == 4:
      rank[3] += 1
    elif cnt == 3:
      rank[4] += 1
    else:
      rank[5] += 1

  context = {
    "num" : res_list,
    "vonus_num" : vonus[0],
    "rank" : rank,
    # "first" : first,
  }
  return render(request, 'lotto.html', context)

  # 1등 당첨 하려면 몇 번 돌려야할까?
  # rank = [0] * 6     # 1등 ~ 꽝 개수
  # first = 0
  # while True:
  #   first += 1
  #   cnt = 0
  #   v_cnt = 0
  #   pick = random.sample(range(1, 46), 6)
  #   for j in pick:
  #     if j in res_list:
  #       cnt += 1
  #     if j in vonus:
  #       v_cnt += 1
  #   if cnt == 6:
  #     rank[0] += 1
  #     break
  #   elif cnt == 5 and v_cnt == 1:
  #     rank[1] += 1
  #   elif cnt == 5:
  #     rank[2] += 1
  #   elif cnt == 4:
  #     rank[3] += 1
  #   elif cnt == 3:
  #     rank[4] += 1
  #   else:
  #     rank[5] += 1

  

