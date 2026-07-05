### D: & cd D:\Desktop\Profile\Note\Game\遊戲王YGOPro & 起手測試.py
### D: & cd D:\Desktop & 起手測試.py
import random
from collections import Counter
cards = []
cards.extend(['砲手','砲手','砲手','槍手','槍手','槍手','山羊','山羊','響手','獅子'])
cards.extend(['蠍子','蠍子','蠍子','導化','導化','導化','阿不','赫聖','增殖','增殖'])
cards.extend(['灰流','灰流','灰流','開幕','開幕','開幕','金謙','抹指','墓指','墓指'])
cards.extend(['計都','計都','計都','羅睺','羅睺','羅睺','烙融','刺毒','裂角','吼炎'])
    
# 抽5張並觀察情況
def DrawFive():
    drawResult = random.sample(cards, 5)
    hasStartPoint = False
    
    supplyPointA = ['計都','羅睺','烙融','砲手','開幕','金謙']
    supplyPointB = ['沼地','融合']
    supplyPointC = ['計都','羅睺','烙融','開幕','金謙']
    supplyPointD = ['山羊','獅子','響手','砲手','槍手','蠍子']
    supplyPointE = ['羅睺','烙融','開幕']
    supplyPointF = ['計都','烙融','開幕']
    
    if '槍手' in drawResult and (set(drawResult) & set(supplyPointA)):
        hasStartPoint = True
        
    if '槍手' in drawResult and (set(drawResult) & set(supplyPointB)):
        hasStartPoint = True
        
    if '蠍子' in drawResult and (set(drawResult) & set(supplyPointA)):
        hasStartPoint = True
    
    if '蠍子' in drawResult and (set(drawResult) & set(supplyPointB)):
        hasStartPoint = True
        
    if '赫聖' in drawResult and (set(drawResult) & set(supplyPointC)) and (set(drawResult) & set(supplyPointD)):
        hasStartPoint = True
    
    if '計都' in drawResult and (set(drawResult) & set(supplyPointE)):
        hasStartPoint = True
    
    if '羅睺' in drawResult and (set(drawResult) & set(supplyPointF)):
        hasStartPoint = True
    
    # 累計有動點+補點的情況
    if hasStartPoint == True: 
        matchCheck[0] += 1
        
# 起手N次
N = 10000
matchCheck = [0]
for i in range(N):
    DrawFive()

# 打印統計結果
print('%s次起手，有動點+補點的機率 = %s'%(N, round(matchCheck[0]/N, 2)))
print('牌組張數: %d'%(len(cards)))