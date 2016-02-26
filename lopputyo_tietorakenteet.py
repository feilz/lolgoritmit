from sys import argv
import copy
from operator import itemgetter
import time
def shortPath(towns,city,target,path,i):
	if(city==[]):
		return
	else:	
		global maxWeight,flag,paths
		city=sorted(city,key=itemgetter(1))[::-1]
		for p in city:			
			if(p[0]==target):
				prevMaxWeight=maxWeight		
				path[i]=p
				maxWeight=p[1]						
				for n in range(i,-1,-1):
					if(path[n][1]<maxWeight):
						maxWeight=path[n][1]
				if not flag:
					paths=copy.copy(path)
					flag=True				
					continue			
				elif(maxWeight>prevMaxWeight):
					paths=copy.copy(path)				
					continue			
				else:		
					maxWeight=prevMaxWeight	
					continue
			if p[1]<maxWeight and flag:		
				continue
			elif p[1]<9:
				continue
			
			path[i]=p
			shortPath(towns,towns[p[0]], target,path,i+1) 


aika = time.clock()

f = open(argv[1])				#avataan tiedosto, josta luetaan kaikki reitit towns muuttujaan
cities=f.readline().split()
towns=[[] for _ in range(0,int(cities[0]))]
for i in range(0,int(cities[1])):
	nums=f.readline().split()
	towns[int(nums[0])].append(tuple((int(nums[1]),int(nums[2]))))
target=int(f.readline())
global maxWeight
maxWeight=100000
global flag
flag = False
global paths
paths=[]
path=[[] for _ in range(0,int(cities[0]))]
i=0						#kutsutaan rekursiivista funktiota
shortPath(towns, towns[1],target, path,i)
if not paths:
	print("Mahdollista reittiä ei ole")
else:		
	weight=10000
	thispath="1"
	for n in paths:
		if not n:
			continue
		thispath+=" -> "+str(n[0])
		if(n[1]<weight):
			weight=n[1]
		if(n[0]==target):
			break
	print("Maximi kuorma jonka voi kuljettaa kaupunkiin "+str(target)+" on "+str(weight-8)+" tonnia, jolloin paras reitti on: "+thispath+". Reitillä saa kuljettaa max "+str(weight)+" ja auto painaa 8 tonnia")
print("Suoritusaika", time.clock()-aika)
