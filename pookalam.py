from joy import *

c0=circle(r=15,fill="skyblue",stoke="white")
c1=ellipse(w=40,h=10,fill="white",stroke="black")|repeat(20,rotate(15))
c2=circle(r=25,fill="skyblue")
c3=ellipse(w=60,h=10,fill="black",stroke="black")|repeat(20,rotate(15))
#c=ellipse(w=70,h=10,fill="gold",stroke="black")|repeat(60,rotate(5))
c4=ellipse(w=80,h=10,fill="red",stroke="black")|repeat(40,rotate(7.5))
c5=circle(r=45,fill="#004970")
c6=circle(r=50,fill="skyblue")
c7=ellipse(w=110,h=10,fill="white",stroke="black")|repeat(40,rotate(5))
c8=ellipse(w=120,h=20,fill="#004970",stroke="black")|repeat(15,rotate(20))
c9=ellipse(w=120,h=20,fill="red",stroke="black")|repeat(15,rotate(30))|repeat(15,rotate(50))
c10=ellipse(w=130,h=25,fill="white",stroke="black")|repeat(15,rotate(20))
c11=circle(r=70,fill="skyblue",stroke="none")
c12=ellipse(w=150,h=40,fill="skyblue",stroke="none")|repeat(20,rotate(30))
c13=circle(r=80,fill="black")
c14=ellipse(w=210,h=40,fill="black",stroke="none")|repeat(20,rotate(30))
c15=ellipse(w=215,h=50,fill="white",stroke="none")|repeat(20,rotate(30))
c16=circle(r=90,fill="#e9b443",stroke="none")   #gold
c17=circle(r=97.5,fill="#004970",stroke="none")
e1=ellipse(w=210,h=30,fill="skyblue",stroke="none")|repeat(20,rotate(15))
e2=ellipse(w=215,h=40,fill="#e9b443",stroke="none")|repeat(20,rotate(15))
c18=circle(r=107.5,fill="#004013",stroke="none") #darkgreen
e3=ellipse(w=240,h=50,fill="#a81b2e",stroke="none")|repeat(20,rotate(30))
e4=ellipse(w=245,h=50,fill="white",stroke="none")|repeat(20,rotate(30))
e5=ellipse(w=255,h=50,fill="skyblue",stroke="none")|repeat(20,rotate(30))
c19=circle(r=120,fill="#a81b2e",stroke="none") #darkred
c20=circle(r=130,fill="#004970",stroke="none") #dartkblue
c21=ellipse(w=280,h=80,fill="black",stroke="black")|repeat(20,rotate(15))
c22=ellipse(w=290,h=80,fill="#e9b443",stroke="black")|repeat(20,rotate(15))
c23=circle(r=150,fill="#004970",stroke="none") #darkred

show(c23,c22,c21,c20,c19,e5,e4,e3,c18,e2,e1,c17,c16,c15,c14,c13,c12,c11,c10,c9,c8,c7,c6,c5,c4,c3,c2,c1,c0)