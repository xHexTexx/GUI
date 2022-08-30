num1 = str(input())
count = int(0)
print("ความยาวทั้งหมด",len(num1))
for i in range(0, len(num1)) :
    if(num1[i]!='.') :
        if(num1[i]=='0') :
            if(i+1>=len(num1)) :
                count += 1
            elif(num1[i-1]=='0' or num1[i-1]=='.') :
                    for n in range(len(num1)-i ,i) :
                        if(num1[n]!='.') :
                            count += 1 
            elif(num1[i+1]=='.') :
                if(num1[i-1]!='0') : count += 1
            elif(num1[i+1]=='0') :
                temp = bool(False)
                for j in range(i ,len(num1)) :
                    if(num1[j]=='0') :
                        temp = True
                if(temp==True) :
                    count += 1
            else :
                count += 1
        else : 
            count += 1
    elif(num1[i]=='.') :
        count += 0
    print("ตำแหน่งที่",i+1,"(i=",i,")","เลข",num1[i]," นับได้",count)
print("นับได้ทั้งหมด",count)
"""elif(i-1<len(num1)) :
    count += 0"""
