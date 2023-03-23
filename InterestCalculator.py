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
    window = tk.Tk()
    window.title("Interest Calculator")
    window.geometry("960x540")
    window.mainloop()


#Equations courtesy of Investopedia.com

def simpleInterest(p, i, n):
    result = p * i * n
    result = round(result, 2)
    return result
    
def compoundInterest(p, i, n):
    result = p * (pow((1 + i), n) - 1)
    result = round(result, 2)
    return result

    
if __name__ == "__main__":
    main()
