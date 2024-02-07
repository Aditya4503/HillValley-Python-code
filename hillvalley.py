def hillvalley(l):
    count = 0
    
    for i in range(0,len(l)-2):
        if (l[i]<l[i+1] and l[i+1]>l[i+2]) or (l[i]>l[i+1] and l[i+1]<l[i+2]):
                count = count+1
    if count == 1:
        print(True)
    else:
        print(False)

hillvalley([1,2,3,5,4,3,2,1])
#True
	
hillvalley([1,2,3,4,5,3,2,4,5,3,2,1])
#False

