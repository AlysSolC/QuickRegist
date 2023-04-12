import tkinter as tk
import keyboard as k
import pyautogui as ag


class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("800x400+1000+100")
        self.root.title("QuikRegist Prototype")
        self.root.resizable(height=False, width=False)

        self.crnV1 = tk.StringVar()
        self.crnV2 = tk.StringVar()
        self.crnV3 = tk.StringVar()
        self.crnV4 = tk.StringVar()
        self.crnV5 = tk.StringVar()

        self.instructtext = '''Welcome to QuikRegist. To use:
        1) Enter each desired course's CRN into the text boxes below (1 course per box)
        2) Press "Save CRNs" in this program to store the CRNs for later use
        3) Enter your pin in the course registration site (MAKE SURE ITS IN FULLSCREEN!)
        4) Hit "Enter" in this program & pray!
        ***There is no internal CRN verification system in this program. Ensure your CRNs
        are valid or the program WILL break***'''

        self.attributiontext = '''  This program and all of its scripts were
        made by Alys Combs. Credit to Lawrence Hoerst for
        making the first version and giving me advice for
        the learning experience of making my own shitty
        copycat version.'''

        self.instructions = tk.Label(text=self.instructtext,justify="left").place(x=10,y=30)
        self.attribution = tk.Label(text=self.attributiontext,justify="left").place(x=370,y=200)

        self.box1 = tk.Entry(textvariable=self.crnV1).place(x=100,y=200)
        self.box2 = tk.Entry(textvariable=self.crnV2).place(x=100, y=230)
        self.box3 = tk.Entry(textvariable=self.crnV3).place(x=100, y=260)
        self.box4 = tk.Entry(textvariable=self.crnV4).place(x=100, y=290)
        self.box5 = tk.Entry(textvariable=self.crnV5).place(x=100, y=320)

        self.storeButt = tk.Button(text="Save CRNs", command=self.storeCRNS).place(x=300,y=260)
        self.enterButt = tk.Button(text="Enter", command=self.enterCRNs).place(x=300,y=300)

        self.root.mainloop()

    def storeCRNS(self):
        crn1 = self.crnV1.get()
        crn2 = self.crnV2.get()
        crn3 = self.crnV3.get()
        crn4 = self.crnV4.get()
        crn5 = self.crnV5.get()
        crnlist = [crn1, crn2, crn3, crn4, crn5]

        revlist = []
        failcount = 0
        for crn in crnlist:
            if len(crn) == 5 and type(crn) == str:
                revlist.append(crn)
            else:
                failcount = failcount + 1

        datawrite = ''
        for crn in revlist:
            datawrite = datawrite + crn + '\n'

        crnfile = open("CRNS.txt", "w")
        crnfile.write(datawrite)
        crnfile.close()
        self.failnotif = tk.Label(text="{} inputs were blank/invalid CRNs & were not applied.".format(failcount)).place(x=300, y=220)


    def enterCRNs(self):
        # Grabs the CRNs from CRNS.txt
        crnfile = open("CRNS.txt", "r")
        crns = crnfile.read()
        crnslist = crns.split("\n")
        crnslist.remove('')
        crnfile.close()

        # Switches to the enter crns tab
        ag.moveTo(200, 300)
        ag.click()

        # Creates a new CRN textbox for each CRN
        ag.moveTo(250, 440)
        ag.click()
        for i in range(len(crnslist) - 1):
            ag.press('tab')
            ag.press('enter')

        # Enters each CRN
        ag.moveTo(250, 430)
        ag.click()
        for crn in crnslist:
            k.write(crn)
            ag.press('tab')
        ag.press('tab')
        ag.press('enter')

        #uncomment in order for the program to fully function
        ag.moveTo(1800, 1000)
        ag.click()
        ag.click()


