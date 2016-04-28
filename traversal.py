import tree

class backEnd:
  def __init__(self):
    self.data = tree.Tree()
    self.data.set_filename("tree.txt")
    self.firstQuestion = self.readFromDB(); #IMPLEMENT THIS
    self.question = ""
    self.hadCharacter = 0
    self.mainRoute = ""

  def doubleCheck(self):
    self.data.print_tree()

  def reset(self):
    self.data.restart_game()
    self.hadCharacter = 0

  def getOut(self):
    self.data.store_tree()

  def getYes(self):
    self.question,q = self.data.go_yes();
    if( not self.hadCharacter and not q):
      self.hadCharacter = 1;
      self.mainRoute = self.data.direction;
      #print self.mainRoute + ": 1"
    return self.question,q
  
  def getNo(self):
    self.question,q = self.data.go_no();
    if( not self.hadCharacter and not q):
      self.hadCharacter = 1;
      self.mainRoute = self.data.direction;
      #print self.mainRoute + ": 1"
    return self.question,q

  def getProbably(self):
    self.question,q = self.data.go_maybe_yes();
    if( not self.hadCharacter and not q):
      self.hadCharacter = 1;
      self.mainRoute = self.data.direction;
      #print self.mainRoute + ": 1"
    return self.question,q

  def getProbablyNot(self):
    self.question,q = self.data.go_maybe_no();
    if( not self.hadCharacter and not q):
      self.hadCharacter = 1;
      self.mainRoute = self.data.direction;
      #print self.mainRoute + ": 1"
    return self.question,q
    

  def getDNA(self):
    self.question,q = self.data.go_dna()
    if( not self.hadCharacter and not q):
      self.hadCharacter = 1;
      self.mainRoute = self.data.direction;
      #print self.mainRoute + ": 1"
    return self.question,q

  def recheckStuff(self):
    """Returns nextQuestion, gaveUp
       if gaveUp, nextQuestion is the previous character"""
    question, q = self.data.pop_maybe()
    if(q == None):
      thing = self.data.return_data(self.mainRoute)
      return thing.value , 0, 1 #NO STACK, GIVE UP
    elif(q == 2):
      return self.recheckStuff()
    else:
      self.question = question
      return self.question, q, 0
    
  def addCharacter(self,newChar):
    self.data.add_person(newChar,self.data.direction)
    
  def addQuestion(self,question, newChar,oldCharPos, newCharPos):
    if(oldCharPos == newCharPos):
        return 1;
    
    currentPath = self.mainRoute;
    self.data.direction = currentPath;
    oldChar = self.data.return_data(currentPath);
    #SET CURRENT NODE DATA TO QUESTION
    temp = oldChar.value
    oldChar.value = question;
    #SET CURRENT NODE TYPE TO Q
    oldChar.question = 1;

    #ALTERNATIVELY WE CAN STORE THE DATA, DELETE CURRENT NODE, CREATE NEW ONES
    #print oldCharPos
    #print newCharPos
    if(newCharPos == 'y'):
         self.data.add_person_yes(newChar);
    elif(newCharPos == 'n'):
         self.data.add_person_no(newChar);
    elif(newCharPos == 'd'):
         self.data.add_person_dna(newChar);

    self.data.go_parent();

    if(oldCharPos == 'y'):
         self.data.add_person_yes(temp);
    elif(oldCharPos == 'n'):
         self.data.add_person_no(temp);
    elif(oldCharPos == 'd'):
         self.data.add_person_dna(temp);

    return 0;


#CHANGE THIS to actually read from DB
  def readFromDB(self):
    self.data.make_tree_from_file()
    #self.data.add_question("Is your character a boy?", "")
    #self.data.add_question("Does she wear a blue dress?", "n")
    #self.data.add_question("Is you character's father alive?","y")
    #self.data.add_question("Does she have magical Ice Powers?", "ny")
    #self.data.add_question("Does she have a horse?","nn")
    #self.data.add_question("Is your character a demi-god","yy")
    #self.data.add_question("Is your character responsible for his father's death?","yn")
    #self.data.add_person("Elsa", "nyy")
    #self.data.add_person("Cinderella", "nyn")
    #self.data.add_person("Mulan","nny")
    #self.data.add_person("Ariel","nnn")
    #self.data.add_person("Hercules","yyy")
    #self.data.add_person("Pinochio","yyn")
    #self.data.add_person("Li Shang","ynn")
    #self.data.add_person("Kylo Ren","yny")
    #self.data.print_tree()
    return self.data.root.value
