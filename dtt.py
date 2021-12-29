# -*- coding: utf-8 -*-
try:
    import socket
    from tkinter import *
    from tkinter import ttk
    from ttkthemes import ThemedTk
    import sys
    from PIL import Image
    from PIL import ImageGrab
    import pytesseract
    import cv2
    import tkinter.scrolledtext as scrolledtext
    from random import randrange
    from deep_translator import GoogleTranslator
    errorC = False
except:
    errorC = True
try:
    sys.stdout.encoding
    
    cropping = False
    newWindowText = None
    aboutM = None
    settingsF = None
    openedMiniMod = False
    openedNewText = False
    rndmColor = ["green", "purple", "red", "brown", "orange"]
except:
    errorC = True
try:
    from googletrans import Translator
    translate = Translator()
except:
    pass

def EncrypText(text):
    t = str(text)
    clearText = t[33:]
    tEncryption = clearText.replace("'", "£#$.*-3123")
    tClean = tEncryption.replace(
        'pronunciation=None, extra_data="{£#$.*-3123confiden...")', '')
    tDecryption = tClean.replace("£#$.*-3123", "'")
    return(tDecryption)


def ifOpen(wind):
    global openedMiniMod
    global openedNewText
    if(openedNewText == True and newWindowText == wind):
        openedNewText = False
        wind.destroy()
    if(openedMiniMod == True and miniM == wind):
        openedMiniMod = False
        wind.destroy()


def selectTextBox(translatedTextChk, orgtext):
    if(openedMiniMod == True):
        miniMod(translatedTextChk)
    else:
        traText(translatedTextChk, orgtext)


def miniModWind():
    global miniM
    global openedMiniMod
    miniM = Toplevel(mainW)
    miniM.geometry("260x90")
    miniBtnTra = ttk.Button(miniM, text="Translate", command=lambda: imgRead())
    miniBtnTra.grid(sticky=W, row=0, column=0, ipadx=1, ipady=1)
    miniM.lift
    miniM.resizable(False, True)
    openedMiniMod = True
    miniM.protocol('WM_DELETE_WINDOW', lambda: ifOpen(miniM))
    return miniM


def miniMod(traTextminiOrg):
    traTextminiNoExt = EncrypText(traTextminiOrg)
    if(settingsExtraB.get() == 0):
        miniTranslateTR = scrolledtext.ScrolledText(
            miniM, undo=True, height=1, width=31)
        miniTranslateTR.grid(row=1, column=0)
        miniTranslateTR.insert(INSERT, traTextminiOrg)
    else:
        miniTranslateTR = scrolledtext.ScrolledText(
            miniM, undo=True, height=1, width=31)
        miniTranslateTR.grid(row=1, column=0)
        miniTranslateTR.insert(INSERT, traTextminiNoExt)


def windowsSetCenter(windowX, windowY):
    X_parent = mainW.winfo_height()
    Y_parent = mainW.winfo_width()
    x = (Y_parent - windowY)
    y = (X_parent - windowX)
    return x, y


def settingsWind():
    global settingsF
    settingsF = Toplevel(mainW)
    ayarFX = 410
    ayarFY = 250
    tpl = windowsSetCenter(ayarFX, ayarFY)
    x = tpl[0]
    y = tpl[1]
    settingsF.geometry("%dx%d+%d+%d" %
                       (ayarFX, ayarFY, x+ayarFX*2, y+ayarFY*2))
    settingsF.resizable(False, False)
    settingsF.lift


def settingsWindFill():
    global currentcmbx_var

    labelframe1 = ttk.LabelFrame(settingsF, text="Translation font size:")
    labelframe1.grid(sticky="W", row=3, column=1)

    srb1 = ttk.Radiobutton(settingsF, text="Activate 'Cut Window'",
                           value=1, variable=settingsrb1)
    srb1.grid(sticky=W, row=2, column=0, ipadx=1, ipady=5)

    srb2 = ttk.Radiobutton(
        settingsF, text="Deactivate 'Cut Window'", value=2, variable=settingsrb1,)
    srb2.grid(sticky=W, row=3, column=0, ipadx=1, ipady=5)

    scb1 = ttk.Checkbutton(settingsF, text="Ajax API Extra information is active",
                           variable=settingsExtraB, onvalue=1, offvalue=0)
    scb1.grid(sticky=W, row=4, column=0, ipadx=1, ipady=5)

    scb2 = ttk.Checkbutton(settingsF, text="Use last cut area",
                           variable=settingsExtraB2, onvalue=1, offvalue=0)
    scb2.grid(sticky=W, row=2, column=1, ipadx=1, ipady=5)

    slbl1 = ttk.Label(settingsF, text="Program Settings----",
                      foreground="grey")
    slbl1.grid(sticky="W", row=1, column=0)
    slbl1 = ttk.Label(
        settingsF, text="Translate Engine Settings----", foreground="grey")
    slbl1.grid(sticky="W", row=5, column=0)

    srb3 = ttk.Radiobutton(settingsF, text="Google Translator API [recommended]",
                           value=1, variable=settingsrb2)
    srb3.grid(sticky=W, row=6, column=0, ipadx=1, ipady=5)

    srb4 = ttk.Radiobutton(settingsF, text="Google Translator Ajax API ['old version'\nusing: Tesseract Open Source OCR]",
                           value=2, variable=settingsrb2)
    srb4.grid(sticky=W, row=7, column=0, ipadx=1, ipady=5)

    fontSCmb = ttk.Combobox(labelframe1, textvariable=currentcmbx_var)
    fontSCmb.grid(sticky=W, row=3, column=1, ipadx=5, ipady=1)
    fontSCmb['values'] = ('10', '15', '20', '25', '30', '33')
    fontSCmb['state'] = 'readonly'


def Settings():
    if(settingsF == None):
        settingsWind()
        settingsWindFill()
    else:
        settingsF.destroy()
        settingsWind()
        settingsWindFill()


def abmMeWind():
    global aboutM
    aboutM = Toplevel(mainW)
    aboutM.geometry("300x100")
    aboutM.resizable(False, False)


def abmMeTextFill(rndInt):
    abmLabel = ttk.Label(aboutM, text="DESKTOP TRANSLATOR", foreground=rndInt)
    abmLabel1 = ttk.Label(
        aboutM, text="Developed by: OSMAN KOÇAK", foreground=rndInt)
    abmLabel2 = ttk.Label(aboutM, text="Version : 1.0", foreground=rndInt)
    abmLabel3 = ttk.Label(
        aboutM, text="E mail : osmankocakank@gmail.com", foreground=rndInt)

    abmLabel.grid(sticky=W, row=0, column=0)
    abmLabel1.grid(sticky=W, row=1, column=0)
    abmLabel2.grid(sticky=W, row=2, column=0)
    abmLabel3.grid(sticky=W, row=3, column=0)


def abmMe():
    ranInt = randrange(0, 5)

    if(aboutM == None):
        abmMeWind()
        abmMeTextFill(rndmColor[ranInt])
    else:
        aboutM.destroy()
        abmMeWind()
        abmMeTextFill(rndmColor[ranInt])


def NewWindowText():
    global newWindowText
    global openedNewText
    newWindowText = Toplevel(mainW)
    newWindowX = 1000
    newWindowY = 500
    tpl = windowsSetCenter(newWindowX, newWindowY)
    x = tpl[0]
    y = tpl[1]
    newWindowText.geometry(
        "%dx%d+%d+%d" % (newWindowX, newWindowY, x+(newWindowX/2), y+(newWindowY*3)))
    minibtnTra = ttk.Button(
        newWindowText, text="Translate", command=lambda: imgRead())
    minibtnTra.grid(sticky=W, row=0, column=0, ipadx=1, ipady=1)
    newWindowText.protocol('WM_DELETE_WINDOW', lambda: ifOpen(newWindowText))
    openedNewText = True
    return newWindowText


def originalText(orgTxt):
    if(openedMiniMod == False and openedNewText == True and orgTxt != ""):
        origiText = scrolledtext.ScrolledText(newWindowText, undo=True, width=25)
        origiText.grid(row=1, column=2)
        origiText.insert(INSERT, "[ORIGINAL:]"+orgTxt)

def traText(tratext, orgtext):
    global openedMiniMod
    global openedNewText
    if(newWindowText == None):
        NewWindowText()
        originalText(orgtext)
        transTR = scrolledtext.ScrolledText(
            newWindowText, undo=True, font=("", currentcmbx_var.get()))
        transTR.grid(row=1, column=0)
    else:
        if(openedMiniMod == True or openedNewText == True):
            originalText(orgtext)
            transTR = scrolledtext.ScrolledText(
                newWindowText, undo=True, font=("", currentcmbx_var.get()))
            transTR.grid(row=1, column=0)
            transTR.update()
        else:
            NewWindowText()
            originalText(orgtext)
            transTR = scrolledtext.ScrolledText(
                newWindowText, undo=True, font=("", currentcmbx_var.get()))
            transTR.grid(row=1, column=0)

    if(settingsExtraB.get() == 1 or settingsrb2.get() == 1):
        transTR.insert(INSERT, tratext)

    else:
        t = EncrypText(tratext)
        transTR.insert(INSERT, t)


def getImg():
    imgget = ImageGrab.grab()
    imgget.save("images/1.jpg")


def languageArray(x, y):
    lngArrayX = ['', 'auto', 'en', 'tr', 'it']
    lngArrayY = ['', 'tr', 'en', 'ru', 'de', 'fr', 'it']
    try:
        pict = Image.open("images/1.jpg")
        imgToStrText = pytesseract.image_to_string(pict)
        if(imgToStrText != ""):
            if(settingsrb2.get() == 1):
                if(lngArrayX[x] != lngArrayY[y] ):
                    translatedText = GoogleTranslator(
                        source=lngArrayX[x], target=lngArrayY[y]).translate(imgToStrText)
                    selectTextBox(translatedText, imgToStrText)
                else:
                    translatedText = GoogleTranslator(
                        source=lngArrayX[1], target=lngArrayY[y]).translate(imgToStrText)
                    selectTextBox(translatedText, imgToStrText)
            else:
                try:
                    translatedText = translate.translate(
                        imgToStrText, src=lngArrayX[x], dest=lngArrayY[y])
                    selectTextBox(translatedText, imgToStrText)
                except:
                    NewWindowText()
                    traText(
                        "*********************************ERROR:Google Ajax API not accesible! >> Try: CMD -> pip install translator, pip install googletrans==4.0.0-rc1", "")
        else:
            NewWindowText()
            traText(
                "*********************************ERROR:Text could not be detected!", "")
    except:
        NewWindowText()
        traText(
            "*********************************ERROR:The directory cannot be accessed or the 'dtt/images/1.jpg' folder is empty.", "")


def imgRead():
    fromLng = i.get()
    toLng = z.get()
    if(settingsExtraB2.get() == 1):
        cutSameArea()
        languageArray(fromLng, toLng)
    else:
        languageArray(fromLng, toLng)


def getScreenCapture():
    getImg()
    cropping = False
    x_start, y_start, x_end, y_end = 0, 0, 0, 0
    image = cv2.imread('images/1.jpg')
    oriImage = image

    def mouse_crop(event, x, y, flags, param):

        global x_start, y_start, x_end, y_end, cropping

        cv2.imshow("image", image)
        if (event == cv2.EVENT_LBUTTONDOWN):
            x_start, y_start, x_end, y_end = x, y, x, y
            cropping = True
            cutinfox = x
            cutinfoy = y
            cutinfoxend = x
            cutinfoyend = y

        elif (event == cv2.EVENT_MOUSEMOVE):
            if cropping == True:
                x_end, y_end = x, y
                cutinfoxend = x
                cutinfoyend = y

        elif (event == cv2.EVENT_LBUTTONUP):
            #x_start, y_start = x,y
            x_end, y_end = x, y
            cropping = False
            cutinfoxend = x
            cutinfoyend = y
            refPoint = [(x_start, y_start), (x_end, y_end)]
            if (len(refPoint) == 2):
                roi = oriImage[refPoint[0][1]:refPoint[1]
                               [1], refPoint[0][0]:refPoint[1][0]]
                kesdeg = roi
                if(settingsrb1.get() == 1):
                    cv2.imshow("Cut Window", roi)
                    cv2.imwrite("images/1.jpg", roi)
                else:
                    cv2.imwrite("images/1.jpg", roi)

    cv2.namedWindow("image")
    cv2.setMouseCallback("image", mouse_crop)


def cutSameArea():
    try:
        if(x_start is None or y_start is None or x_end is None or y_end is None):
            NewWindowText()
            traText(
                "*********************************ERROR:Please select the area you want to translate.", "")
        else:
            getImg()
            refPoint = [(x_start, y_start), (x_end, y_end)]
            image = cv2.imread('images/1.jpg')
            oriImage = image

            roi = oriImage[refPoint[0][1]:refPoint[1]
                           [1], refPoint[0][0]:refPoint[1][0]]
            cv2.imwrite("images/1.jpg", roi)
    except NameError:
        NewWindowText()
        traText(
            "*********************************ERROR:Please select the area you want to translate.", "")
    except:
        NewWindowText()
        traText("ERROR:Something else went wrong", "")


if(errorC == False):
    mainW = ThemedTk(theme="equilux", themebg=True, toplevel=True)
    mainW.title("DTTranslator V 1.0")
    mainWFX = 425
    mainWFY = 250
    sc_width = mainW.winfo_screenwidth()
    sc_height = mainW.winfo_screenheight()
    xp = ((sc_width/2) - (mainWFX/2))
    yp = ((sc_height/2) - (mainWFY/2))
    mainW.geometry("%dx%d+%d+%d" % (mainWFX, mainWFY, xp, yp))
    mainW.resizable(False, False)
    # vars
    i = IntVar()
    z = IntVar()
    settingsrb1 = IntVar()
    settingsrb1.set(1)
    settingsrb2 = IntVar()
    settingsrb2.set(1)
    settingsExtraB = IntVar()
    settingsExtraB2 = IntVar()
    currentcmbx_var = StringVar()
    currentcmbx_var.set(0)
    ##
    r1 = ttk.Radiobutton(
        mainW, text="Detect language", value=1, variable=i)
    r1.grid(sticky=W, row=2, column=1, ipadx=1, ipady=5)
    r2 = ttk.Radiobutton(
        mainW, text="English[from En]", value=2, variable=i)
    r2.grid(sticky=W, row=3, column=1, ipadx=2, ipady=5)
    r3 = ttk.Radiobutton(mainW, text="Turkish[from Tr] ", value=3, variable=i)
    r3.grid(sticky=W, row=4, column=1, ipadx=6, ipady=5)
    r9 = ttk.Radiobutton(
        mainW, text="Italian[from It]", value=4, variable=i)
    r9.grid(sticky=W, row=5, column=1, ipadx=1, ipady=5)
    r10 = ttk.Radiobutton(mainW, text="Italian[to It]", value=6, variable=z)
    r10.grid(sticky=EW, row=7, column=2, ipadx=1, ipady=5)
    r4 = ttk.Radiobutton(mainW, text="Turkish[to Tr]", value=1, variable=z)
    r4.grid(sticky=EW, row=2, column=2, ipadx=0, ipady=5)
    r5 = ttk.Radiobutton(mainW, text="English[to En]", value=2, variable=z)
    r5.grid(sticky=EW, row=3, column=2, ipadx=0, ipady=5)
    r6 = ttk.Radiobutton(mainW, text="Russian[to Ru]", value=3, variable=z)
    r6.grid(sticky=EW, row=4, column=2, ipadx=0, ipady=5)
    r7 = ttk.Radiobutton(mainW, text="German[to De]", value=4, variable=z)
    r7.grid(sticky=EW, row=5, column=2, ipadx=0, ipady=5)
    r8 = ttk.Radiobutton(mainW, text="French[to Fr]", value=5, variable=z)
    r8.grid(sticky=EW, row=6, column=2, ipadx=0, ipady=5)
    btntra = ttk.Button(text="Translate", command=lambda: imgRead())
    btntra.grid(sticky=W, row=3, column=0, ipadx=37, ipady=5)
    btnmintra = ttk.Button(text="Mini Mod", command=lambda: miniModWind())
    btnmintra.grid(sticky=W, row=4, column=0, ipadx=37, ipady=5)
    btnscptr = ttk.Button(text="Screen Capture",
                          command=lambda: getScreenCapture())
    btnscptr.grid(sticky=W, row=2, column=0, ipadx=28, ipady=5)
    btnabm = ttk. Button(
        mainW, text="!", command=lambda: abmMe())
    btnabm.grid(sticky=W, row=6, column=0, ipadx=37, ipady=5)
    btnexit = ttk.Button(mainW, text="Exit", command=mainW.destroy)
    btnexit.grid(sticky=W, row=7, column=0, ipadx=37, ipady=5)
    btnsett = ttk.Button(mainW, text="Settings", command=lambda: Settings())
    btnsett.grid(sticky=W, row=5, column=0, ipadx=37, ipady=5)
else:
    mainW = Tk()
    mainW.title("Report any issue to: osmankocakank@gmail.com")
    mainW.geometry("450x25")
    mainW.resizable(False, False)
    chkConn = BooleanVar()
    try:
        sock = socket.create_connection(("www.google.com", 80))
        if sock is not None:
            chkConn = True
            sock.close
    except:
        chkConn = False
    if(chkConn == False):
        text = "Please Check Your Internet Connection :)"
    else:
        text = "Something went wrong!"
    lbl = Label(
        mainW, text=text, fg="Red")
    lbl.grid(sticky="W", row=0, column=0)
mainloop()
