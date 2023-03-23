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
    pageTitle = tk.Label(window, text = "Interest Calculator", font = ("myriad pro", 30)).grid(row = 0)
    titleSpacer = tk.Label(window, text = "").grid(row = 1, pady = 10)
    
    simpleLabel = tk.Label(window, text = "Simple Interest", font = ("myriad pro", 15)).grid(row = 2)
    pLabel1 = tk.Label(window, text = "Principal", font = ("myriad pro", 10)).grid(row = 3)
    simpleP = tk.Entry(window, width = 10).grid(row = 3, column = 1)
    iLabel1 = tk.Label(window, text = "Interest rate", font = ("myriad pro", 10)).grid(row = 4)
    simpleI = tk.Entry(window, width = 10).grid(row = 4, column = 1)
    nLabel1 = tk.Label(window, text = "Loan term", font = ("myriad pro", 10)).grid(row = 5)
    simpleN = tk.Entry(window, width = 10).grid(row = 5, column = 1)
    tk.Button(window, text = "CALCULATE").grid(row = 6, column = 0, pady = 10)
    tk.Button(window, text = "CLEAR").grid(row = 6, column = 1, pady = 10)
    
    operationSpacer = tk.Label(window, text = "").grid(row = 7, pady = 10)
    
    compoundLabel = tk.Label(window, text = "Compound Interest", font = ("myriad pro", 15)).grid(row = 8)
    pLabel2 = tk.Label(window, text = "Principal", font = ("myriad pro", 10)).grid(row = 9)
    compoundP = tk.Entry(window, width = 10).grid(row = 9, column = 1)
    ilabel2 = tk.Label(window, text = "Interest rate", font = ("myriad pro", 10)).grid(row = 10)
    compoundI = tk.Entry(window, width = 10).grid(row = 10, column = 1)
    nLabel2 = tk.Label(window, text = "Compounding periods per year", font = ("myriad pro", 10)).grid(row = 11)
    compoundN = tk.Entry(window, width = 10).grid(row = 11, column = 1)
    tk.Button(window, text = "CALCULATE").grid(row = 12, column = 0, pady = 10)
    tk.Button(window, text = "CLEAR").grid(row = 12, column = 1, pady = 10)
    
    window.mainloop()

#Still need boxes for displaying results

"""
def calculateSimple():
    take user input from boxes and call simpleInterest, displays result
"""

"""
def calculateCompound():
    take user input from boxes and call compoundInterest, displays result
"""

"""
def clearSimple():
    clear input boxes and result box for simple interest
"""

"""
def clearCompound():
    clear input boxes and result box for compound interest
"""
    
#Adds user inputs and result to queries array
#def appendQuery(inputArr):

    
if __name__ == "__main__":
    main()
