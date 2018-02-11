# -*- coding: utf-8 -*-

from random import randrange
from Tkinter import Canvas,Tk
from tkFont import Font
'''
master = Tk()

w = Canvas(master, width=500, height=500)

w.create_rectangle(80, 20, 100, 40, fill="green")
w.create_rectangle(100, 20, 120, 40, fill="green")
w.create_rectangle(120, 20, 140, 40, fill="green")
w.create_rectangle(80, 40, 100, 60, fill="green")
w.create_rectangle(100, 40, 120, 60, fill="green")
w.create_rectangle(120, 40, 140, 60, fill="green")
w.create_rectangle(80, 60, 100, 80, fill="green")
w.create_rectangle(100, 60, 120, 80, fill="green")
w.create_rectangle(120, 60, 140, 80, fill="green")

w.create_rectangle(20, 80, 40, 100, fill="red")
w.create_rectangle(40, 80, 60, 100, fill="red")
w.create_rectangle(60, 80, 80, 100, fill="red")
id = w.create_text(90, 30, text="00")
id = w.create_text(110, 30, text="01")
id = w.create_text(130, 30, text="02")
id = w.create_text(90, 50, text="03")
id = w.create_text(110, 50, text="L", font=Font(weight='bold', size=11))
id = w.create_text(130, 50, text="04")
#w.create_rectangle(30, 30, 100, 100, fill="green", outline = 'blue') 
w.pack()
master.mainloop()
'''
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

        'B1': ((7,40,31,23),    (4,42,28,20),   (2,45,26,18),   (32,34,39,37), (33,36,38,35)),
        'B2': ((7,31),(40,23), (4,28),(42,30), (2,26),(45,18), (32,39),(34,37), (33,38),(36,35)),
        'B3': ((23,31,30,7),    (20,28,42,7),   (18,26,45,2),   (37,39,34,32), (35,38,36,33)),

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
        for i in range(n): self.permute(self.moves.keys()[randrange(18)] )

cubo=Cubo()


cubo.shuffle()

print cubo