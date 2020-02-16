
'''
x + y + z + w = 13 
2x + 3y − w = −1 
−3x + 4y + z + 2w = 10 
x + 2y − z + w = 1

'''

eqleft=[[1,1,1,1],[2,3,0,-1],[-3,4,1,2],[1,2,-1,1]]
eqright=[13,-1,10,1]

class linear():
    def __init__(self,eqleft):
        self.linierslut=[]
        self.minmatrix=eqleft
        self.nvar=len(self.minmatrix)
        
        for j in range(self.nvar):
            pivotlinie=self.findpivot(j)
            print("pivotlinie",pivotlinie)
            self.linierslut.append(pivotlinie)
            for i in range(self.nvar):
                #if i!=pivotlinie:
                if i not in self.linierslut:
                    self.beregnlinie(i,pivotlinie,j)
        for line in self.minmatrix:
            print('{:6.3f},{:6.3f},{:6.3f},{:6.3f}'.format(*line))
       
        
    def findpivot(self,col):
        maxtal=abs(self.minmatrix[0][col])
        linie=0
        for i in range(1,self.nvar):
            if i not in self.linierslut:
                if abs(self.minmatrix[i][col])>maxtal:
                    maxtal=abs(self.minmatrix[i][col])
                    linie=i           
        print("linie",linie,maxtal)
        return linie
    
    def beregnlinie(self,linie,pivotlinie,col):
        faktor=self.minmatrix[linie][col]/self.minmatrix[pivotlinie][col]
        korrektion=[self.minmatrix[pivotlinie][j]*faktor for j in range(self.nvar)]
        nylinie=[self.minmatrix[linie][j]-korrektion[j] for j in range(self.nvar)]
        for j in range(self.nvar): self.minmatrix[linie][j]=nylinie[j]

    
linear(eqleft)
