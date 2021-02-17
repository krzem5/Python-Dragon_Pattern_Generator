from PIL import Image,ImageDraw



def alg(i):
	def rec(d,n=""):
		if (d==0):
			return n
		ns="0"
		i=0
		for i in range(0,len(n)):
			ns+=n[i]+("1" if i%2==0 else "0")
		return rec(d-1,ns)
	rot={(1,1):[[-1,1],[1,-1]],(-1,1):[[-1,-1],[1,1]],(-1,-1):[[1,-1],[-1,1]],(1,-1):[[1,1],[-1,-1]]}
	d,_=i.split("\n")[0].split(" ")
	pl=[[int(n.split(" ")[0]),int(n.split(" ")[1])] for n in i.split("\n")[1:]]
	o=[]
	for k in pl:
		o+=["0"]
	if (int(d)==0):
		return "\n".join(o)
	c="0"+rec(int(d))
	x,y=0,0
	dx,dy=1,-1
	t=1
	mx=0
	my=0
	m_x=0
	m_y=0
	ptl=[(0,0)]
	for i in c:
		dx,dy=rot[(dx,dy)][int(i)]
		x+=dx
		y+=dy
		ptl+=[(x*100,y*100)]
		mx=min(x-1,mx)
		my=min(y-1,my)
		m_x=max(x+1,m_x)
		m_y=max(y+1,m_y)
		if ([x,y] in pl):
			o[pl.index([x,y])]=str(int(o[pl.index([x,y])].split(" ")[0])+1)+" "+" ".join(o[pl.index([x,y])].split(" ")[1:]+[str(t)])
		t+=1
	i=0
	for k in ptl:
		ptl[i]=(k[0]+abs(mx)*100,k[1]+abs(my)*100)
		i+=1
	i=Image.new("RGB",((m_x-mx)*100,(m_y-my)*100),color="black")
	d=ImageDraw.Draw(i)
	d.line(ptl,fill="white")
	i.save("out.png")
	return "\n".join(o)



print(alg("10 3\n-3 -1\n1 1\n-1 0"))
