# -*- coding: utf-8 -*-
"""
LaunchCode Demo Program
Interest Calculator
Nathan Kadlec
"""

import tkinter as tk
import tkinter.ttk as ttk


#defs for interest calculations
#Option to display all previous entries/results
#Option to clear previous queries
#Option to save results to text file
#Help button that plays video tutorial
#Equations button that shows all equations
#Exit button



def main():
    #array of arrays (format: [input1, input2, input3, result])
    queries = []
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


def frontEnd():
    window = tk.Tk()
    window.title("Interest Calculator")
    window.geometry("500x500")
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
        else:
            p = float(principal)
            i = float(interest)
            n = float(loanTerm)
            result = str(simpleInterest(p, i, n))
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
        else:
            p = float(principal)
            i = float(interest)
            n = float(compoundingPeriods)
            result = str(compoundInterest(p, i, n))
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
    operationSpacer.grid(row = 8, pady = 10)
    compoundLabel.grid(row = 9)
    pLabel2.grid(row = 10)
    compoundP.grid(row = 10, column = 1)
    ilabel2.grid(row = 11)
    compoundI.grid(row = 11, column = 1)
    nLabel2.grid(row = 12)
    compoundN.grid(row = 12, column = 1)
    compoundResultLabel.grid(row = 13)
    compoundResult.grid(row = 13, column = 1)
    
    
    window.mainloop()
    

    
#Adds user inputs and result to queries array
#def appendQuery(inputArr):

    
if __name__ == "__main__":
    main()
