from tkinter import *
import random
from pygame import mixer
import time
mixer.init()

background_music = mixer.Sound('song.wav')
sm=mixer.Sound('song1.wav')
#100 means sound play 101 times and after that it will close sound file
win=Tk()
win.title("Cross Squard")
#win.geometry("600x600+200+150")
win.resizable(width=False,height=False)
name1=StringVar()
name2=StringVar()
name3=StringVar()
name4=StringVar()
name1.set("")
name2.set("")
name3.set("")
name4.set("")
win.config(bg="white")
def valueset():
    global x,y,phase,temp1,temp2,winval,status,score,army,totalarmy,chance,kill,bx,by,gx,gy,rx,ry,yx,yy,rndmno1,box1,boy1,box2,boy2,se,name1,name2,name3,name4
    x=0
    y=0
    phase=1
    temp1=1
    temp2=1
    winval=0
    status=["Active","Active","Active","Active"]
    score=[0,0,0,0]
    army=[4,4,4,4]
    totalarmy=army[0]+army[1]+army[2]+army[3]
    chance=1
    kill=0
    bx=[20,20,20,20]
    by=[20,20,20,20]
    gx=[560,560,560,560]
    gy=[20,20,20,20]
    rx=[560,560,560,560]
    ry=[560,560,560,560]
    yx=[20,20,20,20]
    yy=[560,560,560,560]
    rndmno1=0
    box1=0
    boy1=0
    box2=600
    boy2=600
    se=0
    if name1.get()=="":
        army[0]=0
        status[0]="Inactive"
    if name2.get()=="":
        army[1]=0
        status[1]="Inactive"
    if name3.get()=="":
        army[2]=0
        status[2]="Inactive"
    if name4.get()=="":
        army[3]=0
        status[3]="Inactive"
    totalarmy=army[0]+army[1]+army[2]+army[3]
def exita():
    win.destroy()
    mixer.stop()
def firstpage():
    for child in win.winfo_children():
        child.destroy()
    win.geometry("450x400+200+50")
    def start():
        valueset()
        background_music.stop()
        win.geometry("800x680+100+0")
        ex= Example()
    mixer.stop()
    mixer.Channel(0).play(background_music,100)
    Button(win,text="CROSS  SQUAD          ",font=('arial',31,'bold'),bg="blue",fg="white",height=1).place(x=0,y=0)
    canvast=Canvas(win,bg="white",height=60,width=60)
    canvast.place(x=360,y=10)
    t=3
    for i in range(10):
        canvast.create_line(0,2+t,70,2+t)
        t=t+7
    t=2
    for i in range(11):
        canvast.create_line(t,0,t,60)
        t=t+7
    Label(win,text="Player 1 : ",bg="white",fg="blue").place(x=40,y=150)
    Label(win,text="Player 2 : ",bg="white",fg="blue").place(x=40,y=190)
    Label(win,text="Player 3 : ",bg="white",fg="blue").place(x=40,y=230)
    Label(win,text="Player 4 : ",bg="white",fg="blue").place(x=40,y=270)
    Entry(win,text=name1).place(x=100,y=150)
    Entry(win,text=name2).place(x=100,y=190)
    Entry(win,text=name3).place(x=100,y=230)
    Entry(win,text=name4).place(x=100,y=270)
    Button(win,text="Start",bg="blue",fg="white",width=15,font=('arial',10,'bold'),command=start).place(x=280,y=250)
    Button(win,text="Exit",bg="blue",fg="white",width=15,font=('arial',10,'bold'),command=exita).place(x=280,y=290)
    
class Example(Frame):
    
    def __init__(self):
        super().__init__()   
         
        self.initUI()
    def initUI(f1):
        
        fu=Frame(win,width=800,height=80,bg="deepskyblue",highlightthickness=3,highlightcolor="BURLYWOOD2",highlightbackground="BURLYWOOD3")
        fu.pack(side=TOP)
        fu.pack_propagate(False)
        fd=Frame(win,width=800,height=600)
        fd.pack(side=BOTTOM)
        f0=Frame(fd,width=100,height=600,bg="black")
        f0.pack(side=LEFT)
        f0.pack_propagate(False)
        f1=Frame(fd,width=600,height=600,bg="black")
        f1.pack(side=LEFT)
        
        f1.pack(fill=BOTH, expand=1)
        f1.pack_propagate(False)
        f2=Frame(fd,width=100,bg="black",height=600)
        f2.pack(side=RIGHT)
        f2.pack_propagate(False)
        canvas = Canvas(f1)
#        canvas.create_rectangle(0,0,500,50,outline="BURLYWOOD2",fill="BURLYWOOD2")
        canvas.configure(bg=canvasbg)
        canvas.create_line(0,2,600,2)
        t=0
        for i in range(10):
            t=t+60
            canvas.create_line(0,y+t,600,y+t)
        canvas.create_line(0,597,600,597)
        canvas.pack(fill=BOTH, expand=1)
        canvas.create_line(2,0,2,600)
        t=0
        for i in range(10):
            t=t+60
            canvas.create_line(x+t,0,x+t,600)
        canvas.create_line(597,0,597,600)
        def chanceini():
            global chance
            if army[0]==0:
                b1.destroy()
                b2.destroy()
                b3.destroy()
                b4.destroy()
                for i in range(4):
                    bx[i]=0
                    by[i]=0
            if army[1]==0:
                g1.destroy()
                g2.destroy()
                g3.destroy()
                g4.destroy()
                for i in range(4):
                    gx[i]=0
                    gy[i]=0
            if army[2]==0:
                r1.destroy()
                r2.destroy()
                r3.destroy()
                r4.destroy()
                for i in range(4):
                    rx[i]=0
                    ry[i]=0
            if army[3]==0:
                y1.destroy()
                y2.destroy()
                y3.destroy()
                y4.destroy()
                for i in range(4):
                    yx[i]=0
                    yy[i]=0
            if army[0]!=0:
                chance=1
                return
            if army[1]!=0:
                chance=2
                return
            if army[2]!=0:
                chance=3
                return
            if army[3]!=0:
                chance=4
                return
        def change(x,y,r):
            global se,kill,box1,boy1,box2,boy2
            kill=0
            if r==0:
                se=1
            else:
                se=0
            for i in range(r):
                if box1<x<box2-60 and y<boy1+60:
                    x=x+60
                    continue
                if box2-60<x<box2 and boy1<y<boy2-60:
                    y=y+60
                    continue
                if boy2-60<y<boy2 and box1+60<x<box2:
                    x=x-60
                    continue
                if box1<x<box1+60 and boy1+60<y<boy2:
                    y=y-60
                    continue
                print(box1,boy1,box2,boy2)
            return x,y
        def scorecount(var):
            global score,kill,totalarmy
            totalarmy=totalarmy-1
            if var==b1 or var==b2 or var==b3 or var==b4:
                score[0]=score[0]+1
            if var==g1 or var==g2 or var==g3 or var==g4:
                score[1]=score[1]+1
            if var==r1 or var==r2 or var==r3 or var==r4:
                score[2]=score[2]+1
            if var==y1 or var==y2 or var==y3 or var==y4:
                score[3]=score[3]+1
            scor1.configure(text="SCORE :  "+str(score[0]))
            scor2.configure(text="SCORE :  "+str(score[3]))
            scor3.configure(text="SCORE :  "+str(score[1]))
            scor4.configure(text="SCORE :  "+str(score[2]))
            army1.configure(text="ARMY :  "+str(army[0]))
            army2.configure(text="ARMY :  "+str(army[1]))
            army3.configure(text="ARMY :  "+str(army[2]))
            army4.configure(text="ARMY :  "+str(army[3]))
            if army[0]==0:
                statu1.configure(text="STATUS :  Inactive")
            if army[1]==0:
                statu2.configure(text="STATUS :  Inactive")
            if army[2]==0:
                statu3.configure(text="STATUS :  Inactive")
            if army[3]==0:
                statu4.configure(text="STATUS :  Inactive")
            kill=1
        def save(var,x,y):
            global bx,by,gx,gy,rx,ry,yx,yy
            s=int(0)
            p=int(0)
            if var!=b1 and var!=b2 and var!=b3 and var!=b4:
                if x==bx[0] and y==by[0]:
                    s=s+1
                if x==bx[1] and y==by[1]:
                    s=s+1
                if x==bx[2] and y==by[2]:
                    s=s+1
                if x==bx[3] and y==by[3]:
                    s=s+1
                if x==bx[0] and y==by[0] and s==1:
                    b1.destroy()
                    bx[0]=by[0]=0
                    army[0]=army[0]-1
                    scorecount(var)
                    
                if x==bx[1] and y==by[1] and s==1:
                    b2.destroy()
                    bx[1]=by[1]=0
                    army[0]=army[0]-1
                    scorecount(var)
                    
                if x==bx[2] and y==by[2] and s==1:
                    b3.destroy()
                    bx[2]=by[2]=0
                    army[0]=army[0]-1
                    scorecount(var)
                    
                if x==bx[3] and y==by[3] and s==1:
                    b4.destroy()
                    bx[3]=by[3]=0
                    army[0]=army[0]-1
                    scorecount(var)
                    
            if s>1:
                p=1
            s=int(0)
            if var!=g1 and var!=g2 and var!=g3 and var!=g4:
                if x==gx[0] and y==gy[0]:
                    s=s+1
                if x==gx[1] and y==gy[1]:
                    s=s+1
                if x==gx[2] and y==gy[2]:
                    s=s+1
                if x==gx[3] and y==gy[3]:
                    s=s+1
                if x==gx[0] and y==gy[0] and s==1:
                    g1.destroy()
                    gx[0]=gy[0]=0
                    army[1]=army[1]-1
                    scorecount(var)
                    
                if x==gx[1] and y==gy[1] and s==1:
                    g2.destroy()
                    gx[1]=gy[1]=0
                    army[1]=army[1]-1
                    scorecount(var)
                    
                if x==gx[2] and y==gy[2] and s==1:
                    g3.destroy()
                    gx[2]=gy[2]=0
                    army[1]=army[1]-1
                    scorecount(var)
                    
                if x==gx[3] and y==gy[3] and s==1:
                    g4.destroy()
                    gx[3]=gy[3]=0
                    army[1]=army[1]-1
                    scorecount(var)
                    
            if s>1:
                p=1
            s=int(0)
            if var!=r1 and var!=r2 and var!=r3 and var!=r4:
                if x==rx[0] and y==ry[0]:
                    s=s+1
                if x==rx[1] and y==ry[1]:
                    s=s+1
                if x==rx[2] and y==ry[2]:
                    s=s+1
                if x==rx[3] and y==ry[3]:
                    s=s+1
                if x==rx[0] and y==ry[0] and s==1:
                    r1.destroy()
                    rx[0]=ry[0]=0
                    army[2]=army[2]-1
                    scorecount(var)
                    
                if x==rx[1] and y==ry[1] and s==1:
                    r2.destroy()
                    rx[1]=ry[1]=0
                    army[2]=army[2]-1
                    scorecount(var)
                   
                if x==rx[2] and y==ry[2] and s==1:
                    r3.destroy()
                    rx[2]=ry[2]=0
                    army[2]=army[2]-1
                    scorecount(var)
                    
                if x==rx[3] and y==ry[3] and s==1:
                    r4.destroy()
                    rx[3]=ry[3]=0
                    army[2]=army[2]-1
                    scorecount(var)
                    
            if s>1:
                p=1
            s=int(0)
            if var!=y1 and var!=y2 and var!=y3 and var!=y4:
                if x==yx[0] and y==yy[0]:
                    s=s+1
                if x==yx[1] and y==yy[1]:
                    s=s+1
                if x==yx[2] and y==yy[2]:
                    s=s+1
                if x==yx[3] and y==yy[3]:
                    s=s+1
                if x==yx[0] and y==yy[0] and s==1:
                    y1.destroy()
                    yx[0]=yy[0]=0
                    army[3]=army[3]-1
                    scorecount(var)
                if x==yx[1] and y==yy[1] and s==1:
                    y2.destroy()
                    yx[1]=yy[1]=0
                    army[3]=army[3]-1
                    scorecount(var)
                if x==yx[2] and y==yy[2] and s==1:
                    y3.destroy()
                    yx[2]=yy[2]=0
                    army[3]=army[3]-1
                    scorecount(var)
                if x==yx[3] and y==yy[3] and s==1:
                    y4.destroy()
                    yx[3]=yy[3]=0
                    army[3]=army[3]-1
                    scorecount(var)
            if s>1:
                p=1
            return p
        def rndm():
            global chance,rndmno1
            rndmno1=random.randint(1,6)
            print(rndmno1)
            if chance==1:
                lrndm=Label(f0,text=" :  "+str(rndmno1),bg="black",fg="white")
                lrndm.place(x=40,y=160)
            else:
                lrndm=Label(f0,text=" :  "+str(0),bg="black",fg="white")
                lrndm.place(x=40,y=160)
            if chance==2:
                lrndm=Label(f2,text=" :  "+str(rndmno1),bg="black",fg="white")
                lrndm.place(x=40,y=160)
            else:
                lrndm=Label(f2,text=" :  "+str(0),bg="black",fg="white")
                lrndm.place(x=40,y=160)
            if chance==3:
                lrndm=Label(f2,text=" :  "+str(rndmno1),bg="black",fg="white")
                lrndm.place(x=40,y=450)
            else:
                lrndm=Label(f2,text=" :  "+str(0),bg="black",fg="white")
                lrndm.place(x=40,y=450)
            if chance==4:
                lrndm=Label(f0,text=" :  "+str(rndmno1),bg="black",fg="white")
                lrndm.place(x=40,y=450)
            else:
                lrndm=Label(f0,text=" :  "+str(0),bg="black",fg="white")
                lrndm.place(x=40,y=450)
        def chanced():
            global chance
            if chance==1 and army[0]==0:
                chance=2
            if chance==2 and army[1]==0:
                chance=3
            if chance==3 and army[2]==0:
                chance=4
            if chance==4 and army[3]==0:
                chance=1
        def chancec():
            global chance,rndmno1,se
            if chance==1 and rndmno1!=6 and se==0 and kill!=1:
                chance=2
                chanced()
                rndmno1=0
                return
            if chance==2 and rndmno1!=6 and se==0 and kill!=1:
                chance=3
                chanced()
                rndmno1=0
                return
            if chance==3 and rndmno1!=6 and se==0 and kill!=1:
                chance=4
                chanced()
                rndmno1=0
                return
            if chance==4 and rndmno1!=6 and se==0 and kill!=1:
                chance=1
                chanced()
                rndmno1=0
                return
        def phaseset():
            global bx,by,gx,gy,rx,ry,yx,yy
            if bx[0]!=0:
                b1.place(x=bx[0],y=by[0])
            if bx[1]!=0:
                b2.place(x=bx[1],y=by[1])
            if bx[2]!=0:
                b3.place(x=bx[2],y=by[2])
            if bx[3]!=0:
                b4.place(x=bx[3],y=by[3])
            if gx[0]!=0:
                g1.place(x=gx[0],y=gy[0])
            if gx[1]!=0:
                g2.place(x=gx[1],y=gy[1])
            if gx[2]!=0:
                g3.place(x=gx[2],y=gy[2])
            if gx[3]!=0:
                g4.place(x=gx[3],y=gy[3])
            if rx[0]!=0:
                r1.place(x=rx[0],y=ry[0])
            if rx[1]!=0:
                r2.place(x=rx[1],y=ry[1])
            if rx[2]!=0:
                r3.place(x=rx[2],y=ry[2])
            if rx[3]!=0:
                r4.place(x=rx[3],y=ry[3])
            if yx[0]!=0:
                y1.place(x=yx[0],y=yy[0])
            if yx[1]!=0:
                y2.place(x=yx[1],y=yy[1])
            if yx[2]!=0:
                y3.place(x=yx[2],y=yy[2])
            if yx[3]!=0:
                y4.place(x=yx[3],y=yy[3])
        def phasec():
            global totalarmy,bx,by,gx,gy,rx,ry,yx,yy,phase,box1,boy1,box2,boy2,temp1,temp2
            if (totalarmy==10 or totalarmy==8) and temp1==1:
                for i in range(4):
                    if bx[i]!=0:
                        bx[i]=80
                    if by[i]!=0:
                        by[i]=80
                    if gx[i]!=0:
                        gx[i]=500
                    if gy[i]!=0:
                        gy[i]=80
                    if rx[i]!=0:
                        rx[i]=500
                    if ry[i]!=0:
                        ry[i]=500
                    if yx[i]!=0:
                        yx[i]=80
                    if yy[i]!=0:
                        yy[i]=500
                temp1=2
                box1=60
                boy1=60
                box2=540
                boy2=540
                phase=2
                phas1.configure(text="PHASE :  "+str(phase))
                phas2.configure(text="PHASE :  "+str(phase))
                phas3.configure(text="PHASE :  "+str(phase))
                phas4.configure(text="PHASE :  "+str(phase))
                phaseset()
                return
            if totalarmy==4 and temp2==1:
                for i in range(4):
                    if bx[i]!=0:
                        bx[i]=200
                    if by[i]!=0:
                        by[i]=200
                    if gx[i]!=0:
                        gx[i]=380
                    if gy[i]!=0:
                        gy[i]=200
                    if rx[i]!=0:
                        rx[i]=380
                    if ry[i]!=0:
                        ry[i]=380
                    if yx[i]!=0:
                        yx[i]=200
                    if yy[i]!=0:
                        yy[i]=380
                temp2=2
                box1=180
                boy1=180
                box2=420
                boy2=420
                phase=3
                phas1.configure(text="PHASE :  "+str(phase))
                phas2.configure(text="PHASE :  "+str(phase))
                phas3.configure(text="PHASE :  "+str(phase))
                phas4.configure(text="PHASE :  "+str(phase))
                phaseset()
                return
        def winnername(name,s,army):
            fw=Frame(f1,width=600,height=600,bg="white")
            fw.pack()
            fw.pack_propagate(False)
            canvas=Canvas(fw,bg="white",width=600,height=600)
            r=canvas.create_rectangle([150,180,450,390],outline='BURLYWOOD2', fill='white')
            canvas.pack()
            Label(canvas,text="Congratulation...",font=('arial',30,'bold'),bg="white",fg="BURLYWOOD2").place(x=80,y=100)
            l=Label(canvas,text="WINNER :  "+name.get(),bg="white",fg="BURLYWOOD2",font=('arial',16,'bold'))
            l.place(x=200,y=220)
            Label(canvas,text="SCORE :  "+str(s),bg="white",fg="BURLYWOOD2").place(x=200,y=290)
            Label(canvas,text="ARMY REMAIN :  "+str(army),bg="white",fg="BURLYWOOD2").place(x=200,y=340)
            
        def winneran():
            if bx[0]!=0 or bx[1]!=0 or bx[2]!=0 or bx[3]!=0:
                canvas.destroy()
                winnername(name1,score[0],army[0])
            if gx[0]!=0 or gx[1]!=0 or gx[2]!=0 or gx[3]!=0:
                canvas.destroy()
                winnername(name2,score[1],army[1])
            if rx[0]!=0 or rx[1]!=0 or rx[2]!=0 or rx[3]!=0:
                canvas.destroy()
                winnername(name3,score[2],army[2])
            if yx[0]!=0 or yx[1]!=0 or yx[2]!=0 or yx[3]!=0:
                canvas.destroy()
                winnername(name4,score[3],army[3])
        def winner():
            global winval
            n1=0
            n2=0
            n3=0
            n4=0
            if bx[0]==0 and bx[1]==0 and bx[2]==0 and bx[3]==0:
                n1=1
            if gx[0]==0 and gx[1]==0 and gx[2]==0 and gx[3]==0:
                n2=1
            if rx[0]==0 and rx[1]==0 and rx[2]==0 and rx[3]==0:
                n3=1
            if yx[0]==0 and yx[1]==0 and yx[2]==0 and yx[3]==0:
                n4=1
            winval=n1+n2+n3+n4
            if winval==3:
                winneran()
        def blue1():
            global bx,by,chance
#            rndm()
            if chance==1:
                bx[0],by[0]=change(bx[0],by[0],rndmno1)
                

            print(bx[0],by[0])
            s=save(b1,bx[0],by[0])
            chancec()
            if s==1:
                b1.place(x=bx[0]+10,y=by[0]+10)
            else:
                b1.place(x=bx[0],y=by[0])
            if totalarmy==10 or totalarmy==4:
                phasec()
            if totalarmy<=4:
                winner()
        def blue2():
            global bx,by,chance
#            rndm()
            if chance==1:
                bx[1],by[1]=change(bx[1],by[1],rndmno1)
                
            print(bx[1],by[1])
            s=save(b2,bx[1],by[1])
            chancec()
            if s==1:
                b2.place(x=bx[1]+10,y=by[1]+10)
            else:
                b2.place(x=bx[1],y=by[1])
            if totalarmy==10 or totalarmy==4:
                phasec()
            if totalarmy<=4:
                winner()
        def blue3():
            global bx,by,chance
#            rndm()
            if chance==1:
                bx[2],by[2]=change(bx[2],by[2],rndmno1)
                
            print(bx[2],by[2])
            s=save(b3,bx[2],by[2])
            chancec()
            if s==1:
                b3.place(x=bx[2]+10,y=by[2]+10)
            else:
                b3.place(x=bx[2],y=by[2])
            if totalarmy==10 or totalarmy==4:
                phasec()
            if totalarmy<=4:
                winner()
        def blue4():
            global bx,by,chance
#            rndm()
            if chance==1:
                bx[3],by[3]=change(bx[3],by[3],rndmno1)
                
            print(bx[3],by[3])
            s=save(b4,bx[3],by[3])
            chancec()
            if s==1:
                b4.place(x=bx[3]+10,y=by[3]+10)
            else:
                b4.place(x=bx[3],y=by[3])
            if totalarmy==10 or totalarmy==4:
                phasec()
            if totalarmy<=4:
                winner()
        def green1():
            global gx,gy,chance
#            rndm()
            if chance==2:
                gx[0],gy[0]=change(gx[0],gy[0],rndmno1)
                
            print(gx[0],gy[0])
            s=save(g1,gx[0],gy[0])
            chancec()
            if s==1:
                g1.place(x=gx[0]-10,y=gy[0]-10)
            else:
                g1.place(x=gx[0],y=gy[0])
            if totalarmy==10 or totalarmy==4:
                phasec()
            if totalarmy<=4:
                winner()
        def green2():
            global g2x,g2y,chance
#            rndm()
            if chance==2:
                gx[1],gy[1]=change(gx[1],gy[1],rndmno1)
                
            print(gx[1],gy[1])
            s=save(g2,gx[1],gy[1])
            chancec()
            if s==1:
                g2.place(x=gx[1]-10,y=gy[1]-10)
            else:
                g2.place(x=gx[1],y=gy[1])
            if totalarmy==10 or totalarmy==4:
                phasec()
            if totalarmy<=4:
                winner()
        def green3():
            global gx,gy,chance
#            rndm()
            if chance==2:
                gx[2],gy[2]=change(gx[2],gy[2],rndmno1)
                
            print(gx[2],gy[2])
            s=save(g3,gx[2],gy[2])
            chancec()
            if s==1:
                g3.place(x=gx[2]-10,y=gy[2]-10)
            else:
                g3.place(x=gx[2],y=gy[2])
            if totalarmy==10 or totalarmy==4:
                phasec()
            if totalarmy<=4:
                winner()
        def green4():
            global gx,gy,chance
#            rndm()
            if chance==2:
                gx[3],gy[3]=change(gx[3],gy[3],rndmno1)
                
            print(gx[3],gy[3])
            s=save(g4,gx[3],gy[3])
            chancec()
            if s==1:
                g4.place(x=gx[3]-10,y=gy[3]-10)
            else:
                g4.place(x=gx[3],y=gy[3])
            if totalarmy==10 or totalarmy==4:
                phasec()
            if totalarmy<=4:
                winner()
        def red1():
            global rx,ry,chance
#            rndm()
            if chance==3:
                rx[0],ry[0]=change(rx[0],ry[0],rndmno1)
                
            print(bx[0],by[0])
            s=save(r1,rx[0],ry[0])
            chancec()
            if s==1:
                r1.place(x=rx[0]+15,y=ry[0]+15)
            else:
                r1.place(x=rx[0],y=ry[0])
            if totalarmy==10 or totalarmy==4:
                phasec()
            if totalarmy<=4:
                winner()
        def red2():
            global rx,ry,chance
#            rndm()
            if chance==3:
                rx[1],ry[1]=change(rx[1],ry[1],rndmno1)
                
            print(rx[1],ry[1])
            s=save(r2,rx[1],ry[1])
            chancec()
            if s==1:
                r2.place(x=rx[1]+15,y=ry[1]+15)
            else:
                r2.place(x=rx[1],y=ry[1])
            if totalarmy==10 or totalarmy==4:
                phasec()
            if totalarmy<=4:
                winner()
        def red3():
            global rx,ry,chance
#            rndm()
            if chance==3:
                rx[2],ry[2]=change(rx[2],ry[2],rndmno1)
            
            print(rx[2],ry[2])
            s=save(r3,rx[2],ry[2])
            chancec()
            if s==1:
                r3.place(x=rx[2]+15,y=ry[2]+15)
            else:
                r3.place(x=rx[2],y=ry[2])
            if totalarmy==10 or totalarmy==4:
                phasec()
            if totalarmy<=4:
                winner()
        def red4():
            global rx,ry,chance
#            rndm()
            if chance==3:
                rx[3],ry[3]=change(rx[3],ry[3],rndmno1)
                
            print(rx[3],ry[3])
            s=save(r4,rx[3],ry[3])
            chancec()
            if s==1:
                r4.place(x=rx[3]+15,y=ry[3]+15)
            else:
                r4.place(x=rx[3],y=ry[3])
            if totalarmy==10 or totalarmy==4:
                phasec()
            if totalarmy<=4:
                winner()
        def yellow1():
            global yx,yy,chance
#            rndm()
            if chance==4:
                yx[0],yy[0]=change(yx[0],yy[0],rndmno1)
                
            print(yx[0],yy[0])
            s=save(y1,yx[0],yy[0])
            chancec()
            if s==1:
                y1.place(x=yx[0]-15,y=yy[0]-15)
            else:
                y1.place(x=yx[0],y=yy[0])
            if totalarmy==10 or totalarmy==4:
                phasec()
            if totalarmy<=4:
                winner()
        def yellow2():
            global yx,yy,chance
#            rndm()
            if chance==4:
                yx[1],yy[1]=change(yx[1],yy[1],rndmno1)
                
            print(yx[1],yy[1])
            s=save(y2,yx[1],yy[1])
            chancec()
            if s==1:
                y2.place(x=yx[1]-15,y=yy[1]-15)
            else:
                y2.place(x=yx[1],y=yy[1])
            if totalarmy==10 or totalarmy==4:
                phasec()
            if totalarmy<=4:
                winner()
        def yellow3():
            global yx,yy,chance
#            rndm()
            if chance==4:
                yx[2],yy[2]=change(yx[2],yy[2],rndmno1)
                
            print(yx[2],yy[2])
            s=save(y3,yx[2],yy[2])
            chancec()
            if s==1:
                y3.place(x=yx[2]-15,y=yy[2]-15)
            else:
                y3.place(x=yx[2],y=yy[2])
            if totalarmy==10 or totalarmy==4:
                phasec()
            if totalarmy<=4:
                winner()
        def yellow4():
            global yx,yy,chance
#            rndm()
            if chance==4:
                yx[3],yy[3]=change(yx[3],yy[3],rndmno1)
                
            print(yx[3],yy[3])
            s=save(y4,yx[3],yy[3])
            chancec()
            if s==1:
                y4.place(x=yx[3]-15,y=yy[3]-15)
            else:
                y4.place(x=yx[3],y=yy[3])
            if totalarmy==10 or totalarmy==4:
                phasec()
            if totalarmy<=4:
                winner()
        def restartf():
            for child in win.winfo_children():
                child.destroy()
            valueset()
            ex=Example()
        def soundn():
            mixer.Channel(1).play(sm,100)
            soundoff.configure(text="SOUND OFF",command=soundf)
        def soundf():
            sm.stop()
            soundoff.configure(text="SOUND ON",command=soundn)
        Button(fu,text="  CROSS  SQUAD    ",font=('arial',27,'bold'),bg="blue",fg="white").place(x=0,y=0)
        home=Button(fu,text="HOME",bg="white",fg="blue",bd=5,width=8,command=firstpage)
        home.place(x=400,y=30)
        restart=Button(fu,text="RESTART",bg="white",fg="blue",bd=5,width=8,command=restartf)
        restart.place(x=500,y=30)
        soundoff=Button(fu,text="SOUND OFF",bg="white",fg="blue",bd=5,width=9,command=soundf)
        soundoff.place(x=600,y=30)
        Exit=Button(fu,text="EXIT",bg="white",fg="blue",bd=5,width=8,command=exita)
        Exit.place(x=700,y=30)
        b1=Button(canvas,text=" ",bg="deepskyblue2",width=2,command=blue1)
        b1.place(x=bx[0],y=by[0])
        b2=Button(canvas,text=" ",bg="deepskyblue2",width=2,command=blue2)
        b2.place(x=bx[1],y=by[1])
        b3=Button(canvas,text=" ",bg="deepskyblue2",width=2,command=blue3)
        b3.place(x=bx[2],y=by[2])
        b4=Button(canvas,text=" ",bg="deepskyblue2",width=2,command=blue4)
        b4.place(x=bx[3],y=by[3])
        g1=Button(canvas,text=" ",bg="seagreen3",width=2,command=green1)
        g1.place(x=gx[0],y=gy[0])
        g2=Button(canvas,text=" ",bg="seagreen3",width=2,command=green2)
        g2.place(x=gx[1],y=gy[1])
        g3=Button(canvas,text=" ",bg="seagreen3",width=2,command=green3)
        g3.place(x=gx[2],y=gy[2])
        g4=Button(canvas,text=" ",bg="seagreen3",width=2,command=green4)
        g4.place(x=gx[3],y=gy[3])
        r1=Button(canvas,text=" ",bg="tomato",width=2,command=red1)
        r1.place(x=rx[0],y=ry[0])
        r2=Button(canvas,text=" ",bg="tomato",width=2,command=red2)
        r2.place(x=rx[1],y=ry[1])
        r3=Button(canvas,text=" ",bg="tomato",width=2,command=red3)
        r3.place(x=rx[2],y=ry[2])
        r4=Button(canvas,text=" ",bg="tomato",width=2,command=red4)
        r4.place(x=rx[3],y=ry[3])
        y1=Button(canvas,text=" ",bg="orange",width=2,command=yellow1)
        y1.place(x=yx[0],y=yy[0])
        y2=Button(canvas,text=" ",bg="orange",width=2,command=yellow2)
        y2.place(x=yx[1],y=yy[1])
        y3=Button(canvas,text=" ",bg="orange",width=2,command=yellow3)
        y3.place(x=yx[2],y=yy[2])
        y4=Button(canvas,text=" ",bg="orange",width=2,command=yellow4)
        y4.place(x=yx[3],y=yy[3])
        
#        Label(f0,text="Player1 :  "+name1,fg="red",bg="black").place(x=0,y=0)
#        Button(f0,text="S\nu\nf\nf\nl\ne",command=rndm,bg="white",width=2,height=18).place(x=80,y=20)
        Button(f0,text=name1.get()+"           ",bg="white",width=13).place(x=0,y=2)
        Button(f0,text=name4.get()+"           ",bg="white",width=13).place(x=0,y=290)
        Button(f2,text=name2.get()+"           ",bg="white",width=13).place(x=0,y=2)
        Button(f2,text=name3.get()+"           ",bg="white",width=13).place(x=0,y=290)
        Button(f0,text="",bg="deepskyblue",width=1).place(x=70,y=2)
        Button(f0,text="",bg="yellow",width=1).place(x=70,y=290)
        Button(f2,text="",bg="green",width=1).place(x=70,y=2)
        Button(f2,text="",bg="RED",width=1).place(x=70,y=290)
        
        phas1=Label(f0,text="PHASE :  "+str(phase),bg="black",fg="white")
        phas1.place(x=0,y=40)
        phas2=Label(f0,text="PHASE :  "+str(phase),bg="black",fg="white")
        phas2.place(x=0,y=330)
        phas3=Label(f2,text="PHASE :  "+str(phase),bg="black",fg="white")
        phas3.place(x=0,y=40)
        phas4=Label(f2,text="PHASE :  "+str(phase),bg="black",fg="white")
        phas4.place(x=0,y=330)
        
        
        statu1=Label(f0,text="STATUS :  "+status[0],bg="black",fg="white")
        statu1.place(x=0,y=70)
        statu2=Label(f0,text="STATUS :  "+status[3],bg="black",fg="white")
        statu2.place(x=0,y=360)
        statu3=Label(f2,text="STATUS :  "+status[1],bg="black",fg="white")
        statu3.place(x=0,y=70)
        statu4=Label(f2,text="STATUS :  "+status[2],bg="black",fg="white")
        statu4.place(x=0,y=360)
        
        scor1=Label(f0,text="SCORE :  "+str(score[0]),bg="black",fg="white")
        scor1.place(x=0,y=100)
        scor2=Label(f0,text="SCORE :  "+str(score[1]),bg="black",fg="white")
        scor2.place(x=0,y=390)
        scor3=Label(f2,text="SCORE :  "+str(score[2]),bg="black",fg="white")
        scor3.place(x=0,y=100)
        scor4=Label(f2,text="SCORE :  "+str(score[3]),bg="black",fg="white")
        scor4.place(x=0,y=390)
        
        army1=Label(f0,text="ARMY :  "+str(army[0]),bg="black",fg="white")
        army1.place(x=0,y=130)
        army2=Label(f2,text="ARMY :  "+str(army[1]),bg="black",fg="white")
        army2.place(x=0,y=130)
        army3=Label(f2,text="ARMY :  "+str(army[2]),bg="black",fg="white")
        army3.place(x=0,y=420)
        army4=Label(f0,text="ARMY :  "+str(army[3]),bg="black",fg="white")
        army4.place(x=0,y=420)
        
        Button(f0,text="DICE",bg="black",fg="white",command=rndm).place(x=0,y=160)
        Button(f0,text="DICE",bg="black",fg="white",command=rndm).place(x=0,y=450)
        Button(f2,text="DICE",bg="black",fg="white",command=rndm).place(x=0,y=160)
        Button(f2,text="DICE",bg="black",fg="white",command=rndm).place(x=0,y=450)
        
        chanceini()
        phasec()
        
        canvas.pack(fill=BOTH, expand=1)    
        mixer.Channel(1).play(sm,100)
#x=0
#y=0
#phase=1
#temp1=1
#temp2=1
#winval=0
#status=["Active","Active","Active","Active"]
#score=[0,0,0,0]
#army=[0,0,0,4]
#totalarmy=army[0]+army[1]+army[2]+army[3]
#chance=1
#kill=0
#bx=[20,20,20,20]
#by=[20,20,20,20]
#gx=[560,560,560,560]
#gy=[20,20,20,20]
#rx=[560,560,560,560]
#ry=[560,560,560,560]
#yx=[20,20,20,20]
#yy=[560,560,560,560]
#rndmno1=0
#box1=0
#boy1=0
#box2=600
#boy2=600
#se=0
global x,y,phase,temp1,temp2,winval,status,score,army,totalarmy,chance,kill,bx,by,gx,gy,rx,ry,yx,yy,rndmno1,box1,boy1,box2,boy2,se
canvasbg="white"
firstpage()
win.mainloop()
background_music.stop()
sm.stop()