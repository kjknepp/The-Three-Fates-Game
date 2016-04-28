import wx
import traversal as otherStuff

APP_SIZE_X = 400
APP_SIZE_Y = 600
BUTTON_SIZE_X = APP_SIZE_X*160/400
BUTTON_SIZE_Y = APP_SIZE_Y/10
RADIO_SIZE_X = APP_SIZE_X/4
RADIO_SIZE_Y = APP_SIZE_Y*2/30

class goldButton(wx.Button):
    def __init__(self, *a, **k):
        wx.Button.__init__(self, *a, **k)
        self.SetBackgroundColour('#f9f144')

    def myDisable(self):
        self.Disable()
        self.SetBackgroundColour('#f9f48e')

    def myEnable(self):
        self.Enable()
        self.SetBackgroundColour('#f9f144')

class myText(wx.StaticText):
    def __init__(self,*a, **k):
        wx.StaticText.__init__(self, *a, **k)
        self.SetBackgroundColour('#311f3f')
        self.SetForegroundColour('WHITE')

class myTextu(wx.StaticText):
    def __init__(self,*a, **k):
        wx.StaticText.__init__(self, *a, **k)
        self.SetBackgroundColour('#382449')
        self.SetForegroundColour('WHITE')

class myTextd(wx.StaticText):
    def __init__(self,*a, **k):
        wx.StaticText.__init__(self, *a, **k)
        self.SetBackgroundColour('#23162d')
        self.SetForegroundColour('WHITE')

class myTextdd(wx.StaticText):
    def __init__(self,*a, **k):
        wx.StaticText.__init__(self, *a, **k)
        self.SetBackgroundColour('#150e1c')
        self.SetForegroundColour('WHITE')    

class myRadioButton(wx.RadioButton):
    def __init__(self, *a, **k):
        wx.RadioButton.__init__(self, *a, **k)
        self.SetBackgroundColour('#563e68')
        self.SetForegroundColour('white')
  
class theGame(wx.Dialog):
    def __init__(self, parent, id, title):
        wx.Dialog.__init__(self, parent, id, title, size=(APP_SIZE_X,APP_SIZE_Y))
        self.window = wx.Window(self)
        self.Canvas = self.window

        wx.FutureCall(1,self.drawBackground)

        self.welcome = myText(self.Canvas,id,label="Welcome!",pos=(APP_SIZE_X/3,100),size=(APP_SIZE_X/3,APP_SIZE_Y/30),style=wx.ALIGN_CENTRE_HORIZONTAL)

        #WELCOME SCREEN
        #various images
        lostImage = wx.Image("userLost1.bmp",wx.BITMAP_TYPE_BMP).ConvertToBitmap()
        self.lostDisplay = wx.StaticBitmap(self.Canvas, id, lostImage, (0, APP_SIZE_Y/6), (lostImage.GetWidth(), lostImage.GetHeight()))
        self.lostDisplay.Hide()

        wonImage = wx.Image("userWon1.bmp",wx.BITMAP_TYPE_BMP).ConvertToBitmap()
        self.wonDisplay = wx.StaticBitmap(self.Canvas, id, wonImage, (0, APP_SIZE_Y/3), (lostImage.GetWidth(), lostImage.GetHeight()))
        self.wonDisplay.Hide()
        #Display Welcome Image'
        welcomeImage = wx.Image("welcomeImage1.bmp",wx.BITMAP_TYPE_BMP).ConvertToBitmap()
        self.welcomeDisplay = wx.StaticBitmap(self.Canvas, id, welcomeImage, (0, APP_SIZE_Y*7/30), (welcomeImage.GetWidth(), welcomeImage.GetHeight()))
        #Define Buttons
        self.exitButton = goldButton(self.Canvas,label="Exit",pos=((APP_SIZE_X/2)-(BUTTON_SIZE_X/2),APP_SIZE_Y-(BUTTON_SIZE_Y*6/3)),size=(BUTTON_SIZE_X,BUTTON_SIZE_Y),style=wx.BORDER_NONE)
        self.continueButton = goldButton(self.Canvas,label="Continue",pos=((APP_SIZE_X/2)-(BUTTON_SIZE_X/2),APP_SIZE_Y-(BUTTON_SIZE_Y*10/3)),size=(BUTTON_SIZE_X,BUTTON_SIZE_Y),style=wx.BORDER_NONE)
        self.restartButton = goldButton(self.Canvas,label="Restart Game",pos=((APP_SIZE_X/2)-(BUTTON_SIZE_X/2),APP_SIZE_Y-(BUTTON_SIZE_Y*10/3)),size=(BUTTON_SIZE_X,BUTTON_SIZE_Y),style=wx.BORDER_NONE)
        self.restartButton.Hide()
        self.exitButton.Show()
        self.continueButton.Show()
        #Bind Buttons
        self.Bind(wx.EVT_BUTTON, self.restartGame2, self.restartButton)
        self.Bind(wx.EVT_BUTTON, self.closebutton, self.exitButton)
        self.Bind(wx.EVT_CLOSE, self.closewindow)
        self.Bind(wx.EVT_BUTTON, self.continueToGame, self.continueButton)

        #Game Buttons
        self.noButton  = goldButton
        self.yesButton = goldButton
        self.dnaButton = goldButton
        self.probablyButton = goldButton
        self.probablyNotButton = goldButton

        #Other Stuff
        self.continueText = myText
        self.questionText = myText
        self.yesRadioOld = myRadioButton
        self.noRadioOld = myRadioButton
        self.dnaRadioOld = myRadioButton
        self.yesRadioNew = myRadioButton
        self.noRadioNew = myRadioButton
        self.dnaRadioNew = myRadioButton
        self.addOld = myText
        self.addNew = myText
        self.newQuestion = wx.TextCtrl
        self.submitButton = goldButton
        self.newCharacter = wx.TextCtrl
        self.charPrompt = myText
        self.quesPrompt = myText
        self.newTitle = myText
        self.newQuesValid = 0
        self.newCharValid = 0

        #Back End Stuff
        self.theHiddenStuff = otherStuff.backEnd()

        #Other Necessary Variables
        self.question = self.theHiddenStuff.firstQuestion
        #print self.question

    #def doThing(self):
        

    def drawBackground(self):
        dc = wx.ClientDC(self.Canvas)
        dc.GradientFillLinear((0,0, APP_SIZE_X, APP_SIZE_Y), '#4d4cbdb', '#3e274f', wx.NORTH)
#
    def continueToGame(self,event):
        wx.FutureCall(1, self.drawBackground)
        self.welcomeDisplay.Hide()
        self.continueButton.Hide()
        self.welcome.Hide()
        self.exitButton.Hide()
        self.questionText = myText(self.Canvas,label=self.question,pos=(0,APP_SIZE_Y/6),size=(APP_SIZE_X,APP_SIZE_Y/30),style=wx.ALIGN_CENTRE_HORIZONTAL,name="questionText")
        #GAME SCREEN
        #Define Buttons
        self.noButton = goldButton(self.Canvas,label="No",pos=((APP_SIZE_X/2)-(BUTTON_SIZE_X*11/10),APP_SIZE_Y-(BUTTON_SIZE_Y*10/3)),size=(BUTTON_SIZE_X,BUTTON_SIZE_Y),style=wx.BORDER_NONE)
        self.yesButton = goldButton(self.Canvas,label="Yes",pos=((APP_SIZE_X/2)-(BUTTON_SIZE_X*11/10),APP_SIZE_Y-(BUTTON_SIZE_Y*14/3)),size=(BUTTON_SIZE_X,BUTTON_SIZE_Y),style=wx.BORDER_NONE)
        self.dnaButton = goldButton(self.Canvas,label="Does Not Apply",pos=((APP_SIZE_X/2)-(BUTTON_SIZE_X/2),APP_SIZE_Y-(BUTTON_SIZE_Y*6/3)),size=(BUTTON_SIZE_X,BUTTON_SIZE_Y),style=wx.BORDER_NONE)
        self.probablyButton = goldButton(self.Canvas,label="Probably",pos=((APP_SIZE_X/2)+(BUTTON_SIZE_X*1/10),APP_SIZE_Y-(BUTTON_SIZE_Y*14/3)),size=(BUTTON_SIZE_X,BUTTON_SIZE_Y),style=wx.BORDER_NONE)
        self.probablyNotButton = goldButton(self.Canvas,label="Probably Not",pos=((APP_SIZE_X/2)+(BUTTON_SIZE_X*1/10),APP_SIZE_Y-(BUTTON_SIZE_Y*10/3)),size=(BUTTON_SIZE_X,BUTTON_SIZE_Y),style=wx.BORDER_NONE)
        #Bind Events
        self.Bind(wx.EVT_BUTTON, self.isNo, self.noButton)
        self.Bind(wx.EVT_BUTTON, self.isYes, self.yesButton)
        self.Bind(wx.EVT_BUTTON, self.doesNotApply, self.dnaButton)
        self.Bind(wx.EVT_BUTTON, self.probably, self.probablyButton)
        self.Bind(wx.EVT_BUTTON, self.probablyNot, self.probablyNotButton)


    #---------Possible Screens' Logic-------------#
    def askCharacter(self):
        self.dnaButton.myDisable()
        self.probablyButton.myDisable()
        self.probablyNotButton.myDisable()
        self.questionText.SetLabel(self.question)
        self.Bind(wx.EVT_BUTTON,self.wrongCharacter,self.noButton)
        self.Bind(wx.EVT_BUTTON,self.correctCharacter,self.yesButton)

    def correctCharacter(self,event):
        self.yesButton.Hide()
        self.noButton.Hide()
        self.dnaButton.Hide()
        self.questionText.Hide()
        self.probablyButton.Hide()
        self.probablyNotButton.Hide()
        wx.FutureCall(1,self.drawBackground)
        self.exitButton.Show()
        self.restartButton.Show()
        #SHOW STUFF FOR CELEBRATION
        self.lostDisplay.Show()
        self.questionText.SetLabel("It would appear you lost")
        self.questionText.Show()
        
    def wrongCharacter(self,event):
        self.continueText = myText(self.Canvas,label="Continue?",pos=(0,APP_SIZE_Y/6),size=(APP_SIZE_X,APP_SIZE_Y/30),style=wx.ALIGN_CENTRE_HORIZONTAL,name="continueText")
        self.continueText.Show()
        self.questionText.Hide()
        self.Bind(wx.EVT_BUTTON,self.closewindow, self.noButton)
        self.Bind(wx.EVT_BUTTON,self.continueAfterWrong,self.yesButton)

    def continueAfterWrong(self,event):
        #Get new question from back end
        self.question, isQuestion, gaveUp = self.theHiddenStuff.recheckStuff()
        #Reset Screen and Rebind Buttons
        #print self.question
        if(gaveUp):
            self.addCharacterScreen()
        elif(isQuestion):
            self.questionText.SetLabel(self.question)
            self.questionText.Show()
            self.dnaButton.myEnable()
            self.probablyButton.myEnable()
            self.probablyNotButton.myEnable()
            self.continueText.Hide()
            self.Bind(wx.EVT_BUTTON, self.isNo, self.noButton)
            self.Bind(wx.EVT_BUTTON, self.isYes, self.yesButton)
            self.Bind(wx.EVT_BUTTON, self.doesNotApply, self.dnaButton)
        else:
            self.continueText.Hide()
            self.questionText.SetLabel(self.question)
            self.questionText.Show()
            self.Bind(wx.EVT_BUTTON,self.wrongCharacter,self.noButton)
            self.Bind(wx.EVT_BUTTON,self.correctCharacter,self.yesButton)

    def quickAddCharacter(self):
        wx.FutureCall(1, self.drawBackground)
        self.questionText.Hide()
        self.yesButton.Hide()
        self.noButton.Hide()
        self.dnaButton.Hide()
        self.probablyButton.Hide()
        self.probablyNotButton.Hide()

        self.wonDisplay.Show()

        self.submitButton = goldButton(self.Canvas,label="Submit",pos=((APP_SIZE_X/2)-(BUTTON_SIZE_X/2),APP_SIZE_Y-3*BUTTON_SIZE_Y/2),size=(BUTTON_SIZE_X,BUTTON_SIZE_Y),style=wx.BORDER_NONE)
        self.submitButton.myDisable()
        self.newCharacter = wx.TextCtrl(self.Canvas,pos=(APP_SIZE_X/20,APP_SIZE_Y*140/600),size=(APP_SIZE_X-APP_SIZE_X/10,APP_SIZE_Y/30))

        self.charPrompt = myText(self.Canvas,label="Character we did not guess:",pos=(0,APP_SIZE_Y*9/48),size=(APP_SIZE_X,APP_SIZE_Y/30),style=wx.ALIGN_CENTRE_HORIZONTAL)
        self.newTitle = myTextu(self.Canvas,label="Congratulations! You won!",pos=(0,APP_SIZE_Y*1/12),size=(APP_SIZE_X,APP_SIZE_Y/30),style=wx.ALIGN_CENTRE_HORIZONTAL)

        self.Bind(wx.EVT_BUTTON, self.submitDataQuick, self.submitButton)
        self.Bind(wx.EVT_TEXT, self.textCharQuick, self.newCharacter)


    def addCharacterScreen(self):
        wx.FutureCall(1, self.drawBackground)
        self.continueText.Hide()
        self.yesButton.Hide()
        self.noButton.Hide()
        self.dnaButton.Hide()
        self.probablyButton.Hide()
        self.probablyNotButton.Hide()

        self.yesRadioOld = myRadioButton(self.Canvas, label="Yes", pos=((APP_SIZE_X/2)-(RADIO_SIZE_X/2),APP_SIZE_Y-(RADIO_SIZE_Y*18/5) - APP_SIZE_Y/12),
            size=(RADIO_SIZE_X,RADIO_SIZE_Y), style=wx.RB_GROUP)
        self.noRadioOld = myRadioButton(self.Canvas, label="No", pos=((APP_SIZE_X/2)-(RADIO_SIZE_X/2),APP_SIZE_Y-(RADIO_SIZE_Y*14/5) - APP_SIZE_Y/12),
            size=(RADIO_SIZE_X,RADIO_SIZE_Y))
        self.dnaRadioOld = myRadioButton(self.Canvas, label="Does Not Apply", pos=((APP_SIZE_X/2)-(RADIO_SIZE_X/2),APP_SIZE_Y-(RADIO_SIZE_Y*10/5) - APP_SIZE_Y/12),
            size=(RADIO_SIZE_X,RADIO_SIZE_Y))
        self.yesRadioNew = myRadioButton(self.Canvas, label="Yes", pos=((APP_SIZE_X/2)-(RADIO_SIZE_X/2),APP_SIZE_Y-(RADIO_SIZE_Y*34/5) - APP_SIZE_Y/12),
            size=(RADIO_SIZE_X,RADIO_SIZE_Y), style=wx.RB_GROUP)
        self.noRadioNew = myRadioButton(self.Canvas, label="No", pos=((APP_SIZE_X/2)-(RADIO_SIZE_X/2),APP_SIZE_Y-(RADIO_SIZE_Y*30/5) - APP_SIZE_Y/12),
            size=(RADIO_SIZE_X,RADIO_SIZE_Y))
        self.dnaRadioNew = myRadioButton(self.Canvas, label="Does Not Apply", pos=((APP_SIZE_X/2)-(RADIO_SIZE_X/2),APP_SIZE_Y-(RADIO_SIZE_Y*26/5) - APP_SIZE_Y/12),
            size=(RADIO_SIZE_X,RADIO_SIZE_Y))

        old = "Answer for " + self.question + ":"
        new = "Answer for new character:"
        self.addOld = myTextdd(self.Canvas,label=old,pos=(APP_SIZE_X*1/6,APP_SIZE_Y*35/48 - APP_SIZE_Y/12),size=(APP_SIZE_X,APP_SIZE_Y*1/30))
        self.addNew = myTextd(self.Canvas,label=new,pos=(APP_SIZE_X*1/6,APP_SIZE_Y*12/24 - APP_SIZE_Y/12),size=(APP_SIZE_X,APP_SIZE_Y*1/30))
        self.newQuestion = wx.TextCtrl(self.Canvas,pos=(APP_SIZE_X/20,APP_SIZE_Y/3),size=(APP_SIZE_X-APP_SIZE_X/10,APP_SIZE_Y/30))
        self.submitButton = goldButton(self.Canvas,label="Submit",pos=((APP_SIZE_X/2)-(BUTTON_SIZE_X/2),APP_SIZE_Y-3*BUTTON_SIZE_Y/2),size=(BUTTON_SIZE_X,BUTTON_SIZE_Y),style=wx.BORDER_NONE)
        self.submitButton.myDisable()
        self.newCharacter = wx.TextCtrl(self.Canvas,pos=(APP_SIZE_X/20,APP_SIZE_Y*140/600),size=(APP_SIZE_X-APP_SIZE_X/10,APP_SIZE_Y/30))

        prompt = "Question to distinguish between " + self.question + " and the new Character:"
        self.charPrompt = myText(self.Canvas,label="Character we did not guess:",pos=(0,APP_SIZE_Y*9/48),size=(APP_SIZE_X,APP_SIZE_Y/30),style=wx.ALIGN_CENTRE_HORIZONTAL)
        self.quesPrompt = myText(self.Canvas,label=prompt,pos=(0,APP_SIZE_Y*7/24),size=(APP_SIZE_X,APP_SIZE_Y/30),style=wx.ALIGN_CENTRE_HORIZONTAL)

        self.newTitle = myTextu(self.Canvas,label="Congratulations! You won!",pos=(0,APP_SIZE_Y*1/12),size=(APP_SIZE_X,APP_SIZE_Y/30),style=wx.ALIGN_CENTRE_HORIZONTAL)

        self.yesRadioOld.SetValue(False)
        self.yesRadioOld.Disable()

        self.Bind(wx.EVT_RADIOBUTTON, self.fixYesOld, self.yesRadioNew)
        self.Bind(wx.EVT_RADIOBUTTON, self.fixNoOld, self.noRadioNew)
        self.Bind(wx.EVT_RADIOBUTTON, self.fixDNAOld, self.dnaRadioNew)
        self.Bind(wx.EVT_BUTTON, self.submitData, self.submitButton)
        self.Bind(wx.EVT_TEXT, self.textChar, self.newCharacter)
        self.Bind(wx.EVT_TEXT, self.textQues, self.newQuestion)
        self.Bind(wx.EVT_RADIOBUTTON, self.checkTotal2, self.yesRadioOld)
        self.Bind(wx.EVT_RADIOBUTTON, self.checkTotal2, self.noRadioOld)
        self.Bind(wx.EVT_RADIOBUTTON, self.checkTotal2, self.dnaRadioOld)
        
        
        
    #------------BUTTON LOGIC-------------#
    def checkTotal2(self,event):
        self.checkTotal()

    def checkTotal(self):
        if((self.yesRadioOld.GetValue() or self.noRadioOld.GetValue() or self.dnaRadioOld.GetValue()) &
           (self.yesRadioNew.GetValue() or self.noRadioNew.GetValue() or self.dnaRadioNew.GetValue()) &
           self.newCharValid & self.newQuesValid):
            self.submitButton.myEnable()
        else:
            self.submitButton.myDisable()

    def checkQuick(self):
        if(self.newCharValid):
            self.submitButton.myEnable()
        else:
            self.submitButton.myDisable()

    def textCharQuick(self,event):
        if(len(self.newCharacter.GetLineText(1))>2):
            self.newCharValid = 1
        else:
            self.newCharValid = 0
        self.checkQuick()
        
    def textChar(self,event):
        if(len(self.newCharacter.GetLineText(1))>2):
            self.newCharValid = 1
        else:
            self.newCharValid = 0
        self.checkTotal()
        
    def textQues(self,event):
        if(len(self.newQuestion.GetLineText(1))>2):
            self.newQuesValid = 1
        else:
            self.newQuesValid = 0
        self.checkTotal()

    def submitDataQuick(self,event):
        character = self.newCharacter.GetLineText(1)
        wx.FutureCall(1, self.drawBackground)
        self.theHiddenStuff.addCharacter(character)
#        self.theHiddenStuff.doubleCheck()
        self.wonDisplay.Hide()
        self.restartGame(3)
        
    def submitData(self,event):
        question = self.newQuestion.GetLineText(1)
        character = self.newCharacter.GetLineText(1)
        #print question
        #print character
        newCharPos = ""
        oldCharPos = ""
        if(self.yesRadioOld.GetValue()):
            oldCharPos = "y"
        elif(self.noRadioOld.GetValue()):
            oldCharPos = "n"
        else:
            oldCharPos = "d"
        if(self.yesRadioNew.GetValue()):
            newCharPos = "y"
        elif(self.noRadioNew.GetValue()):
            newCharPos = "n"
        else:
            newCharPos = "d"

        wx.FutureCall(1, self.drawBackground)
        self.theHiddenStuff.addQuestion(question,character,oldCharPos,newCharPos)
#        self.theHiddenStuff.doubleCheck()
        self.restartGame(1)
    
    def fixYesOld(self,event):
        self.yesRadioOld.Disable()
        self.noRadioOld.Enable()
        self.dnaRadioOld.Enable()
        self.yesRadioOld.SetValue(False)
        self.checkTotal()

    def fixNoOld(self,event):
        self.yesRadioOld.Enable()
        self.noRadioOld.Disable()
        self.dnaRadioOld.Enable()
        self.noRadioOld.SetValue(False)
        self.checkTotal()

    def fixDNAOld(self,event):
        self.yesRadioOld.Enable()
        self.noRadioOld.Enable()
        self.dnaRadioOld.Disable()
        self.dnaRadioOld.SetValue(False)
        self.checkTotal()
    
    def closebutton(self,event):
        self.Close(True)

    def closewindow(self,event):
        self.theHiddenStuff.getOut()
        self.Destroy()

    def probably(self,event):
        self.question,isNotCharacter = self.theHiddenStuff.getProbably()
        if(isNotCharacter == None):
            self.quickAddCharacter()
        elif(isNotCharacter):
            self.questionText.SetLabel(self.question)
        else:
            self.askCharacter()

    def probablyNot(self,event):
        self.question,isNotCharacter = self.theHiddenStuff.getProbablyNot()
        if(isNotCharacter == None):
            self.quickAddCharacter()
        elif(isNotCharacter):
            self.questionText.SetLabel(self.question)
        else:
            self.askCharacter()

    def isNo(self,event):
        self.question,isNotCharacter = self.theHiddenStuff.getNo()
        if(isNotCharacter == None):
            self.quickAddCharacter()
        elif(isNotCharacter):
            self.questionText.SetLabel(self.question)
        else:
            self.askCharacter()

    def isYes(self,event):
        self.question,isNotCharacter = self.theHiddenStuff.getYes()
        if(isNotCharacter == None):
            self.quickAddCharacter()
        elif(isNotCharacter):
            self.questionText.SetLabel(self.question)
        else:
            self.askCharacter()

    def doesNotApply(self,event):
        self.question,isNotCharacter = self.theHiddenStuff.getDNA()
        if(isNotCharacter == None):
            self.quickAddCharacter()
        elif(isNotCharacter):
            self.questionText.SetLabel(self.question)
        else:
            self.askCharacter()

    def restartGame2(self,event):
        self.restartGame(2)

    def restartGame(self,val):
        if(val == 1):
            self.continueText.Hide()
            self.yesRadioOld.Hide()
            self.noRadioOld.Hide()
            self.dnaRadioOld.Hide()
            self.yesRadioNew.Hide()
            self.noRadioNew.Hide()
            self.dnaRadioNew.Hide()
            self.addOld.Hide()
            self.addNew.Hide()
            self.newQuestion.Hide()
            self.submitButton.Hide()
            self.newCharacter.Hide()
            self.charPrompt.Hide()
            self.quesPrompt.Hide()
            self.newTitle.Hide()
        if(val == 2):
            self.restartButton.Hide()
            self.lostDisplay.Hide()
            self.questionText.Hide()
        if(val == 3):
            self.newTitle.Hide()
            self.newCharacter.Hide()
            self.submitButton.Hide()
            self.charPrompt.Hide()
        self.questionText.Hide()
        self.noButton.Hide()
        self.yesButton.Hide()
        self.dnaButton.Hide()
        self.probablyButton.Hide()
        self.probablyNotButton.Hide()
        self.welcome.Show()
        self.exitButton.Show()
        self.continueButton.Show()
        self.welcomeDisplay.Show()
        self.theHiddenStuff.reset()
        self.question = self.theHiddenStuff.firstQuestion
        wx.FutureCall(1, self.drawBackground)

app = wx.App()
frame = theGame(None,99,'The Three Fates Game')
frame.Show()
app.MainLoop()
