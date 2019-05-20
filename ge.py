def ge_fw(M):
    re=M[:]
    a=0
    for i in range(0,len(re)):
        fi=firstNonZero(sub(re,i,a))
        
        if(fi!=-1 and fi!=0):
            if(fi!=[i,i] and fi[0]!=0):
                fi=[fi[0]+i,fi[1]+a]
                re[i],re[fi[0]]=re[fi[0]],re[i]
            
            for j in range(i+1,len(re)):
                if (re[j][i]!=0.0):
                    mult=-1.0*(re[j][i]/re[i][a])
                    re[j]=addRow(multRow(re[i],mult),re[j])
            a+=1
        elif(fi==0):
            a+=1
            for j in range(i+1,len(re)):
                if (re[j][a]!=0.0):
                    mult=-1.0*(re[j][a]/re[i][a])
                    re[j]=addRow(multRow(re[i],mult),re[j])
    
    return re

def sub(M,r,c):
    N=[]
    for i in range(r,len(M)):
        i=M[i][c:]
        N.append(i)
    return N

def firstNonZero(M):
    for i in range(0,len(M)):
        if(M[i][0]==0.0 and i==(len(M)-1)):
            return 0
    for i in range(0,len(M)):
        for j in range (0,len(M)):
            if (M[j][i]!=0.0):
                return [j,i]
    return -1
    
def ge_bw(M):
    re=M[:]
    n=len(re)
    nrow=[0.0 for i in range(0,len(re[n-1]))]
    st=n-1
    if (re[n-1]==nrow):
        for i in range (n-1,0,-1):
            if (re[i]!=nrow):
                st=i
                break
    re[st]=normRow(re[st])
    
    for i in range(st,0,-1):
        item=filter(lambda x: x!= 0, re[i])[0]
        pos=0
        for a in range(0,len(re[i])):
            if (re[i][a]==item):
                pos=a
                break
        fi=re[i][pos]
        for b in range(i,0,-1):
            if (fi!=0.0):
                mult=-1.0*(re[b-1][pos]/fi)
                re[b-1]=addRow(multRow(re[i],mult),re[b-1])
            else:
                break
        re[i]=normRow(re[i])
    re[0]=normRow(re[0])
    return re
    
def normRow(M):
    mult=1.0/(filter(lambda x: x!= 0, M)[0])
    return multRow(M,mult)
    
def multRow(M,num):
    ans=[]
    for k in M:
        ans.append(num*k)
    return ans

def addRow(M1,M2):
    ans=[]
    for i in range(0,len(M1)):
        ans.append(M1[i]+M2[i])
    return ans
    
def printArr(M):
    for i in M:
        print i
        
mat=[[0.0,-3.0,-6.0,4.0,9.0],[-1.0,-2.0,-1.0,3.0,1.0],[-2.0,-3.0,0.0,3.0,-1.0],[1.0,4.0,5.0,-9.0,-7.0]]
# mat=[[0.0,3.0,-6.0,6.0,4.0,-5.0],[3.0,-7.0,8.0,-5.0,8.0,9.0],[3.0,-9.0,12.0,-9.0,6.0,15.0]]
# mat=[[0.0,2.0,3.0,-4.0,1.0],[0.0,0.0,2.0,3.0,4.0],[2.0,2.0,-5.0,2.0,4.0],[2.0,0.0,-6.0,9.0,7.0]]
# mat=[[0.0,0.0,0.0,0.0,1.0],[0.0,1.0,0.0,0.0,0.0],[0.0,0.0,1.0,0.0,0.0],[0.0,0.0,0.0,1.0,0.0],[1.0,0.0,0.0,0.0,0.0]]

print("Original:")
printArr(mat)
print("")
print("Forward Step:")
fw=ge_fw(mat)
printArr(fw)

print("")
bw=ge_bw(fw)
print("Backward Step:")
printArr(bw)