class calc:
    #class to read input file and perform +-/* operations  
    def __init__(self,operation,file):
        #initilizes the classes 
        self.operation=operation
        self.file=file
        if (self.operation=="plus"):
            calc(self.plus(),self.fileN())
        elif (self.operation=="minus"):
            calc(self.minus(),self.fileN())
        elif (self.operation=="divide"):
            calc(self.division(),self.fileN())
        elif (self.operation=="multiply"):
            calc(self.multi(),self.fileN())
        
        self.line=None

    def set_line(self,line):
        #setter to set line of a file
        self.line=line

    def get_line(self):
        #getter of a line from file
        return self.line
    def fileN(self):
        #method to read input file and put numbers in list of lists format
        eachline=[]
        b=open(self.file,"r")
        for i in b:
            eachline.append(i.split())
        for i in range(len(eachline)):
            eachline[i]=[int(j) for j in eachline[i]]
        return eachline

    def plus(self):
        #method to add numbers
        newFile=open("resultP_plus+","w+")
        newNegFile=open("resultN_plus-","w+")
        for i in range(len(self.fileN())):
            if (sum(self.fileN()[i])>0):
                newFile.write(str(sum(self.fileN()[i]))+" строчка #"+str(i+1)+"\n")
            else:
                newNegFile.write(str(sum(self.fileN()[i]))+" строчка #"+str(i+1)+"\n")

    def minus(self):
        #method to subtract first number from second
        newFile=open("resultP_Minus+","w+")
        newNegFile=open("resultNMinus-","w+")
        for i in range(len(self.fileN())):
            dif=self.fileN()[i][0]-self.fileN()[i][1]
            if (dif>0):
                newFile.write(str(dif)+" строчка #"+str(i+1)+"\n")
            else:
                newNegFile.write(str(dif)+" строчка #"+str(i+1)+"\n")

    def multi(self):
        #method to multiply numbers
        newFile=open("resultP_multi+","w+")
        newNegFile=open("resultN_multi-","w+")
        for i in range(len(self.fileN())):
            multiply=self.fileN()[i][0]*self.fileN()[i][1]
            if (multiply>0):
                newFile.write(str(multiply)+" строчка #"+str(i+1)+"\n")
            else:
                newNegFile.write(str(multiply)+" строчка #"+str(i+1)+"\n")

    def division(self):
        #method to divide first number by second
        newFile=open("resultP_division+","w+")
        newNegFile=open("resultN_division-","w+")
        for i in range(len(self.fileN())):
            try:
                div=self.fileN()[i][0]/self.fileN()[i][1]
                if (div>0):
                    newFile.write(str(div)+" строчка #"+str(i+1)+"\n")
                else:
                    newNegFile.write(str(div)+" строчка #"+str(i+1)+"\n")
            except:
                print("На ноль делить нельзя\nYou cannot divide by 0")
                
            

##calc("plus","numbers.txt")
##calc("minus","numbers.txt")
##calc("divide","numbers.txt")
##calc("multiply","numbers.txt")
        
            
