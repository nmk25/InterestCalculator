# -*- coding: utf-8 -*-
"""
LaunchCode Demo Program
Interest Calculator
Nathan Kadlec
"""

import tkinter as tk

#list of lists 
#format: [type (simple/compound), input1 (p), input2 (i), input3 (n), result]
queries = []


def main():
    
    frontEnd()


#Equations courtesy of Investopedia.com

def simpleInterest(p, i, n):
    result = p * i * n
    result = round(result, 2)
    return result
    
def compoundInterest(p, i, n):
    result = p * (pow((1 + i), n) - 1)
    result = round(result, 2)
    return result

#Saves all completed calculations to text file in same directory as InterestCalculator.py
def writeResults():
    writeArr = queries
    with open("Interest_Results", "w") as x:
        for query in writeArr:
            x.write(query[0] + ":  ")
            x.write("principal: " + query[1] + "  ")
            x.write("interest rate: " + query[2] + "  ")
            if(query[0] == "Simple Interest"):
                x.write("loan term: " + query[3] + "  ")
            else:
                x.write("compounding periods: " + query[3] + "  ")
            x.write("RESULT: " + query[4])
            x.write('\n')


def frontEnd():
    window = tk.Tk()
    window.title("Interest Calculator")
    window.geometry("475x525")
    pageTitle = tk.Label(window, text = "Interest Calculator", font = ("myriad pro", 30))
    titleSpacer = tk.Label(window, text = "")
    simpleLabel = tk.Label(window, text = "Simple Interest", font = ("myriad pro", 15))
    pLabel1 = tk.Label(window, text = "Principal", font = ("myriad pro", 10))
    simpleP = tk.Entry(window, width = 10)
    iLabel1 = tk.Label(window, text = "Interest rate (%)", font = ("myriad pro", 10))
    simpleI = tk.Entry(window, width = 10)
    nLabel1 = tk.Label(window, text = "Loan term", font = ("myriad pro", 10))
    simpleN = tk.Entry(window, width = 10)
    simpleResultLabel = tk.Label(window, text = "RESULT", font = ("myriad pro", 10, "bold"))
    simpleResult = tk.Text(window, height = 1, width = 12, relief = "raised")
    
    def calculateSimple():
        simpleResult.delete("1.0", "end")
        principal = simpleP.get()
        interest = simpleI.get()
        loanTerm = simpleN.get()
        result = ""
        if(any(x.isalpha() for x in principal) 
        or any(y.isalpha() for y in interest) 
        or any(z.isalpha() for z in loanTerm)):
            result = "ERROR"
            simpleResult.insert("1.0", result)
        if(not principal or not interest or not loanTerm):
            result = ""
        else:
            p = float(principal)
            i = float(interest) / 100
            n = float(loanTerm)
            result = str(simpleInterest(p, i, n))
            calculationArr = ["Simple Interest", principal, interest, loanTerm, result]
            queries.append(calculationArr)
            simpleResult.insert("1.0", result)
    
    def clearSimple():
        simpleP.delete(first = 0, last = "end")
        simpleI.delete(first = 0, last = "end")
        simpleN.delete(first = 0, last = "end")
        simpleResult.delete("1.0", "end")
    
    tk.Button(window, text = "CALCULATE", command = calculateSimple).grid(row = 7, column = 1, pady = 10)
    tk.Button(window, text = "CLEAR", command = clearSimple).grid(row = 7, column = 0, pady = 10)
    
    operationSpacer = tk.Label(window, text = "")
    
    compoundLabel = tk.Label(window, text = "Compound Interest", font = ("myriad pro", 15))
    pLabel2 = tk.Label(window, text = "Principal", font = ("myriad pro", 10))
    compoundP = tk.Entry(window, width = 10)
    ilabel2 = tk.Label(window, text = "Interest rate (%)", font = ("myriad pro", 10))
    compoundI = tk.Entry(window, width = 10)
    nLabel2 = tk.Label(window, text = "Compounding periods per year", font = ("myriad pro", 10))
    compoundN = tk.Entry(window, width = 10)
    compoundResultLabel = tk.Label(window, text = "RESULT", font = ("myriad pro", 10, "bold"))
    compoundResult = tk.Text(window, height = 1, width = 12, relief = "raised")
    
    def calculateCompound():
        compoundResult.delete("1.0", "end")
        principal = compoundP.get()
        interest = compoundI.get()
        compoundingPeriods = compoundN.get()
        result = ""
        if(any(x.isalpha() for x in principal) 
        or any(y.isalpha() for y in interest) 
        or any(z.isalpha() for z in compoundingPeriods)):
            result = "ERROR"
            compoundResult.insert("1.0", result)
        if(not principal or not interest or not compoundingPeriods):
            result = ""
        else:
            p = float(principal)
            i = float(interest) / 100
            n = float(compoundingPeriods)
            result = str(compoundInterest(p, i, n))
            calculationArr = ["Compound Interest", principal, interest, compoundingPeriods, result]
            queries.append(calculationArr)
            compoundResult.insert("1.0", result)        
    
    def clearCompound():
        compoundP.delete(first = 0, last = "end")
        compoundI.delete(first = 0, last = "end")
        compoundN.delete(first = 0, last = "end")
        compoundResult.delete("1.0", "end")
    
    tk.Button(window, text = "CALCULATE", command = calculateCompound).grid(row = 14, column = 1, pady = 10)
    tk.Button(window, text = "CLEAR", command = clearCompound).grid(row = 14, column = 0, pady = 10)
    
    #Grid alignment
    pageTitle.grid(row = 0)
    titleSpacer.grid(row = 1, pady = 10)
    simpleLabel.grid(row = 2)
    pLabel1.grid(row = 3)
    simpleP.grid(row = 3, column = 1)
    iLabel1.grid(row = 4)
    simpleI.grid(row = 4, column = 1)
    nLabel1.grid(row = 5)
    simpleN.grid(row = 5, column = 1)
    simpleResultLabel.grid(row = 6)
    simpleResult.grid(row = 6, column = 1)
    operationSpacer.grid(row = 8)
    compoundLabel.grid(row = 9)
    pLabel2.grid(row = 10)
    compoundP.grid(row = 10, column = 1)
    ilabel2.grid(row = 11)
    compoundI.grid(row = 11, column = 1)
    nLabel2.grid(row = 12)
    compoundN.grid(row = 12, column = 1)
    compoundResultLabel.grid(row = 13)
    compoundResult.grid(row = 13, column = 1)
    
    tk.Label(window, text = "").grid(row = 15)
    tk.Button(window, text = "EXIT", width = 5, command = window.destroy).grid(row = 17, column = 2)
    
    def saveResults():
        writeResults()
        saveConfirm = tk.Toplevel()
        saveConfirm.wm_transient(window)
        winX = window.winfo_x()
        winY = window.winfo_y()
        saveConfirm.geometry("+%d+%d" %(winX + 135, winY + 265))
        saveConfirm.title("Success")
        saveConfirm.geometry("210x50")
        tk.Label(saveConfirm, text = "Calculation results were saved.", font = ("myriad pro", 11)).grid(row = 0, column = 0)
        tk.Button(saveConfirm, text = "OK", command = saveConfirm.destroy).grid(row = 1)
        
    tk.Button(window, text = "SAVE RESULTS", width = 11, command = saveResults).grid(row = 16, column = 1, pady = 5)
    
    def displayEquations():
        equationsBox = tk.Toplevel()
        equationsBox.wm_transient(window)
        winX = window.winfo_x()
        winY = window.winfo_y()
        equationsBox.geometry("+%d+%d" %(winX + 35, winY + 200))
        equationsBox.title("Equations")
        equationsBox.geometry("400x150")
        tk.Label(equationsBox, text = "Simple Interest = P x i x n\nWhere 'P' is the principal, 'i' is the interest rate percentage,\nand 'n' is the term of the loan in years.", font = ("myriad pro", 10)).grid(row = 0)
        tk.Label(equationsBox, text = "Compound Interest = P((1 + i)^n - 1)\nWhere 'P' is the principal, 'i' is the interest rate percentage,\nand 'n' is the amount of times the interest is compounded per year.", font = ("myriad pro", 10)).grid(row = 1)
        tk.Button(equationsBox, text = "OK", command = equationsBox.destroy).grid(row = 2, pady = 10)
        
    tk.Button(window, text = "EQUATIONS", width = 11, command = displayEquations).grid(row = 17, column = 1)
    
    def displayHelp():
        helpBox = tk.Toplevel()
        helpBox.wm_transient(window)
        winX = window.winfo_x()
        winY = window.winfo_y()
        helpBox.geometry("+%d+%d" %(winX + 35, winY + 200))
    
    tk.Button(window, text = "HELP", width = 5).grid(row = 16, column = 2)
    
    window.mainloop()

    
if __name__ == "__main__":
    main()
