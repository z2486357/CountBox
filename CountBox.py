import numpy
BoxHave=[[10,10,20],[20,20,30],[30,30,40],[40,40,50],[50,50,60]] 
"""BoxHave from small volume to big volume"""
BoxVolume=[]
for i in range(0,len(BoxHave)):
    BoxVolume.append(BoxHave[i][0]*BoxHave[i][1]*BoxHave[i][2])
ThingBuy=[[3,6,7],[7,3,2],[9,7,8],[2,2,2]]
BuyNum=[3,2,1,4]
AllVolume=0
for i in range(0,len(BuyNum)):
    AllVolume+=BuyNum[i]*ThingBuy[i][0]*ThingBuy[i][1]*ThingBuy[i][2]
BoxChoose=0;
while (AllVolume>BoxVolume[BoxChoose]):
    BoxChoose+=1
    if (BoxChoose>=len(BuyNum)):
        print ("You need more than one box")
        break
"""Assume it won't need more than one box"""
"""find the bigest area of each ThingBuy. 
   Sort ThingBuy and BuyNum by ThingArea"""
ThingArea=[]
for i in range(0,len(ThingBuy)):
    BiggestArea=max(ThingBuy[i][0]*ThingBuy[i][1],ThingBuy[i][0]*ThingBuy[i][2],ThingBuy[i][1]*ThingBuy[i][2])
    ThingArea.append(BiggestArea)
BuyNum=[BuyNum for _,BuyNum in sorted(zip(ThingArea,BuyNum),reverse=True)]
ThingBuy=[ThingBuy for _,ThingBuy in sorted(zip(ThingArea,ThingBuy),reverse=True)]
ThingIn=0
"""
Box=numpy.zeros((BoxHave[BoxChoose][0],BoxHave[BoxChoose][1],BoxHave[BoxChoose][2]))
"""
while (ThingIn<len(BuyNum)):
    """put product to the box"""
    
    """next product"""
    BuyNum[ThingIn]-=1
    if BuyNum[ThingIn]==0:
        ThingIn+=1