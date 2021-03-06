# -*- coding: utf-8 -*-

from random import randrange
from Tkinter import Canvas,Tk
from tkFont import Font

class Cubo:
    moves={
        'F1': ( ( 16,24,47,0),    (19,27,44,3),   (21,29,42,5),    (10,15,13,8),    (12,14,11,9)    ), #F1 é giro de 90º horário da face F (Front)
        'F2': ( (16,47),(24,0),  (19,44),(27,3), (21,42),(29,5),  (10,13),(15,8),  (12,11),(14,19)  ), #F2 é giro de 180º da face F ou F1 aplicado 2 vezes
        'F3': (  (0,47,24,16),    (3,44,27,19),   (5,42,29,21),    (8,13,15,10),    (9,11,14,12)    ),  #F3 é giro de 90º anti-horário de F ou F3 aplicado 3 vezes ou inverso de F1

        'R1':  ( (45,13,21,37),   (46,14,22,38),   (47,15,23,39),   (26,31,29,24),   (30,27,25,28)),
        'R2':  ((45,21),(13,37), (46,22),(14,38), (47,23),(15,39), (26,29),(31,24), (30,25),(27,28)), 
        'R3':   ((37,21,13,45),   (38, 22,14,46),  (39,23,15,47),   (24,29,31,26),   (28,25,27,30)),

        'L1':  ((42,34,18,10), (41,33,17,9),   (40,32,16,8),  (5,0,2,7) ,  (4,6,3,1)),
        'L2': ((42,18),(34,10),(41,17),(33,9),(40,16),(32,8),(5,2),(0,7), (4,3),(6,1)),
        'L3':  ( (10,18,34,42), (9,17,33,41),   (8,16,32,40),  (7,2,0,5),   (1,3,6,4)),

        'U1': ( (32,26,15,5),  (35,25,12,6),   (37,24,10,7),   (23,21,16,18),    (22,19,17,20)),
        'U2': ((32,15),(26,5), (35,12),(25,6),( 37,10),(24,7), (23,16),(21,18), (22,17),(19,20)),      
        'U3': ((5,15,26,32) , (6,12,25,35), (7,10,24,37), (18,16,21,23), (20,17,19,22)),

        'B1': ( (23,7,40,31),  (20,4,43,28), (18,2,45,26),   (37,32,34,39),  (35,33,36,38)),
        'B2': ((23,40),(7,31),(20,43),(4,28),(18,45),(2,26),(37,34),(32,39),(35,36),(33,38)),  
        'B3': ( (31,40,7,23),  (28,43,4,20), (26,45,2,18),   (39,34,32,37), (38,36,33,35) ),

        'D1':  ((8,29,39,2),    (11,30,36,1),  (13,31,34,0),   (42,47,45,40),   (44,46,43,41)),
        'D2': ((8,39),(29,2), (11,36),(30,1), (13,34),(31,0), (42,45),(47,40), (44,43),(46,41)),      
        'D3':  ((2,39,29,8),    (1,36,30,11),  (0,34,31,13),   (40,45,47,42),   (41,43,46,44))
    }    

    def __init__(self,config=[]):
        if config==[]: self.config = range(48)
        elif type(config)==list and len(config)==48: self.config=config
        elif type(config)==tuple: self.permute(config)
        elif type(config)==str: pass
        else: pass
        
    def __str__(self):
        #posição de cada célula no grid do canvas para montar a representaça do cubo
        cels_canvas=(3,4,5,15,17,27,28,29,36,37,38,48,50,60,61,62,39,40,41,51,53,63,64,65,75,76,77,87,89,99,100,101,42,43,44,54,56,66,67,68,45,46,47,57,59,69,70,71)
        master = Tk()
        w = Canvas(master, width=280, height=220)
        for pos,id_quadrado in enumerate(self.config):
            w.create_rectangle(20+(cels_canvas[pos]%12)*20, 20+(cels_canvas[pos]/12)*20, 40+(cels_canvas[pos]%12)*20, 40+(cels_canvas[pos]/12)*20, fill=['green','red','white','blue','orange','yellow'][id_quadrado/8])
            w.create_text(30+(cels_canvas[pos]%12)*20, 30+(cels_canvas[pos]/12)*20, text=str(id_quadrado))

        for fixo in [{'pos':16, 't':'L', 'c':'green'},{'pos':49, 't':'F', 'c':'red'},{'pos':52, 't':'U', 'c':'white'},{'pos':55, 't':'B', 'c':'orange'},{'pos':88, 't':'R', 'c':'blue'},{'pos':58, 't':'D', 'c':'yellow'} ]:
            w.create_rectangle(20+(fixo['pos']%12)*20, 20+(fixo['pos']/12)*20, 40+(fixo['pos']%12)*20, 40+(fixo['pos']/12)*20, fill=fixo['c'])
            w.create_text(30+(fixo['pos']%12)*20, 30+(fixo['pos']/12)*20, text=fixo['t'], font=Font(weight='bold', size=11))
        w.pack()
        master.mainloop()
        return str(self.config)

    def permute(self, seq):
        if type(seq)==str:
            for move in [self.moves[seq[i*2:i*2+2]] for i in range(len(seq)/2)]:
                self.permute(move)
        elif type(seq)==tuple:                 
            if type(seq[0])==int: seq=seq,
            for s in seq:
                z=self.config[s[-1]]       
                for i in range(1,len(s)): self.config[s[-i]]=self.config[s[-(i+1)]]
                self.config[s[0]]=z
            
    def shuffle(self, n=20):
        for i in range(n):
            self.permute(self.moves.keys()[randrange(18)] )

    def isG1(self):
        res=[
            (9,(1,3,4,6)),
            (11,(1,3,4,6)),
            (12,(1,3,4,6)),
            (14,(1,3,4,6)),
            
            (17,(1,3,4,6)),
            (19,(9,11,12,14,17)),
            (20,(9,11,12,14,17)),
            (22,(1,3,4,6,19,20)),
            
            (25,(9,11,12,14,22)),
            (27,(9,11,12,14,22)),
            (28,(9,11,12,14,22)),
            (30,(9,11,12,14,22)),            
            
            (33,(1,3,4,6,19,20,25,27,28,30)),
            (35,(1,3,4,6,19,20,25,27,28,30)),
            (36,(1,3,4,6,19,20,25,27,28,30)),
            (38,(1,3,4,6,19,20,25,27,28,30)),
            
            (41,(1,3,4,6,19,20,25,27,28,30)),
            (43,(9,11,12,14,22,33,35,36,38,41)),
            (44,(9,11,12,14,22,33,35,36,38,41)),
            (46,(1,3,4,6,19,20,25,37,28,43,44))            
            ]
        for r in res:
            for pos in r[1]:
                if self.config[pos]==r[0]:
                    print [r[0],pos]
                    self.notIsG1=[r[0],pos]
                    return False
        return True

    

    def isG2(self):
        res=[
            (9,(1,3,4,6)),
            (11,(1,3,4,6,9)),
            (12,(1,3,4,6,9)),
            
            (14,(1,3,4,6,11,12)),            
            (17,(1,3,4,6,11,12)),
            (19,(1,3,4,6,11,12)),
            (20,(1,3,4,6,11,12)),
            (22,(1,3,4,6,11,12)),
            
            (25,(9,11,12,14,17,19,20,22)),
            (27,(9,11,12,14,17,19,20,22)),
            (28,(9,11,12,14,17,19,20,22)),
            (30,(9,11,12,14,17,19,20,22)),           
            
            (33,(1,3,4,6,11,12,25,27,28,30)),
            
            
            (36,(1,3,4,6,9,14,17,19,20,25,27,28,30,33)),
            
            (38,(1,3,4,6,11,12,25,27,28,30,35,36)),
            
            (41,(1,3,4,6,11,12,25,27,28,30,35,36)),
            (43,(1,3,4,6,11,12,25,27,28,30,35,36)),
            (44,(1,3,4,6,11,12,25,27,28,30,35,36)),
            (46,(1,3,4,6,11,12,25,27,28,30,35,36)),        
            ]
        for r in res:
            for pos in r[1]:
                if self.config[pos]==r[0]:
                    print [r[0],pos]
                    self.notIsG2=[r[0],pos]
                    return False
        return True


def shortener(move_list):    
    def short(move_list):        
        if len(move_list)<=1: return move_list
        if move_list[0][0]==move_list[1][0]:
            move_list[1]=move_list[1][0]+ str((int(move_list[0][1])+int(move_list[1][1]))%4)
            move_list=move_list[2:] if move_list[1][1]=='0' else move_list[1:]
        else:
            move_list=[move_list[0]]+short(move_list[1:])
        return  move_list

    string=False
    if type(move_list)==str:
        move_list=move_list.split(' ')
        string=True
    shorted_move_list=short(move_list)
    while shorted_move_list!=move_list:
        
        move_list=shorted_move_list
        shorted_move_list=short(move_list)
    return ' '.join(move_list) if string else move_list


print "Novo Cubo todo arrumadinho"
cubo=Cubo()

cubo.shuffle()
#print cubo.config
#cubo.config=[26, 41, 24, 25, 4, 2, 14, 7, 23, 22, 34, 38, 11, 31, 17, 10, 40, 27, 18, 44, 9, 5, 36, 42, 16, 43, 8, 6, 46, 39, 35, 29, 32, 33, 21, 3, 19, 0, 30, 47, 15, 1, 37, 12, 28, 13, 20, 45]
dictG1={1:('D1','L1'),
        3:('F1','L1'),
        4:('B1','L1'),
        6:('U1','L1'),
        9:('L1','F1'),
        11:('D1','F1'),
        12:('U1','F1'),
        14:('R1','F1'),
        17:('L1','U1'),
        19:('F1','U1'),
        20:('B1','U1'),
        22:('R1','U1'),
        25:('U1','R1'),
        27:('F1','R1'),
        28:('B1','R1'),
        30:('D1','R1'),
        33:('L1','B1'),
        35:('U1','B1'),
        36:('D1','B1'),
        38:('R1','B1'),
        41:('L1','D1'),
        43:('B1','D1'),
        44:('F1','D1')
        }

dictG2={1:('D2','L1'),
        3:('F1','L1'),
        4:('B1','L1'),
        6:('U2','L1'),
        9:('L1','F1'),
        11:('D2','F1'),
        12:('U2','F1'),
        14:('R1','F1'),
        17:('L1','U2'),
        19:('F1','U2'),
        20:('B1','U2'),
        22:('R1','U2'),
        25:('U2','R1'),
        27:('F1','R1'),
        28:('B1','R1'),
        30:('D2','R1'),
        33:('L1','B1'),
        35:('U2','B1'),
        36:('D2','B1'),
        38:('R1','B1'),
        41:('L1','D2'),
        43:('B1','D2'),
        44:('F1','D2')
        }

c=0
repeat=0
last_move=''
saida=[]

while not cubo.isG1() and c<1000: 
    c+=1
    
    next_move=dictG1[cubo.notIsG1[1]][0]
    if next_move==last_move:
        repeat+=1
    else:
        repeat=0

    if repeat==3:
        next_move=dictG1[cubo.notIsG1[1]][1]
    
    print cubo.notIsG1, next_move, c
    saida+=[next_move]
    cubo.permute(next_move)
    
    last_move=next_move

print shortener(saida)
#print saida









c=0
repeat=0
last_move=''
saida=[]

while not cubo.isG2() and c<1000: 
    c+=1
    
    next_move=dictG2[cubo.notIsG2[1]][0]
    if next_move==last_move:
        repeat+=1
    else:
        repeat=0

    if repeat==3:
        next_move=dictG2[cubo.notIsG2[1]][1]
    
    print cubo.notIsG2, next_move, c
    saida+=[next_move]
    cubo.permute(next_move)
    
    last_move=next_move


print shortener(saida)
#print saida
'''



for j in range(1000):
    for i in range(20):
        cubo.permute(['L2','R2','F2','B2','U2','D2'][randrange(6)])

    #print cubo.isG2()

    print cubo.config

#print cubo.isG1()
#print cubo.config
#print cubo 
#print sum([ abs(cubo.config[i]-i) for i in range(48)] )/48 



#print "Cubo depois do movimento U2"
#cubo.permute('U1')
#print sum([ abs(cubo.config[i]-i) for i in range(48)] )/48 



#print "Cubo embaralhado"
'''
