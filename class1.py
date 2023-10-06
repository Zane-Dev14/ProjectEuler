class Cat:
    def __init__(s, color, legs):
        s.color = color
        s.legs = legs
    def yo(s,num):
        s.legs+=num
    def addtwo(self,s1,s2):
        self.legs=s1.legs+s2.legs
    def __add__(s1,s2):
        return Cat(s1.color+s2.color,s1.legs+s2.legs)
      
      

felix = Cat("ginger", 4)
yooy=Cat("Red",5)
#result=Cat("hh",2)
#result.addtwo(felix,yooy)
result=felix+yooy
print(result.legs)
print(result.color) 