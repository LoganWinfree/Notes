import tkinter
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
import seaborn as sb




def main():
    fWidth = 600
    fHeight = 300
    
    root = tkinter.Tk()
    root.title("Stats Pdf Constructor")
    root.config()
    root.geometry(str(str(fWidth) + "x" + str(fHeight))) 
    
    frame = tkinter.Frame(root)

    leftFrame = tkinter.Frame(frame, width=int(fWidth/2), height=fHeight)
    leftFrame.grid_propagate(0)
    leftFrame.columnconfigure(0, weight=1)
    rightFrame = tkinter.Frame(frame, width=int(fWidth/2), height=fHeight)
    rightFrame.grid_propagate(0)
    rightFrame.columnconfigure(0, weight=1)

    #For Distribution selection and main menu
    label1 = tkinter.Label(leftFrame, text="Menu1")
    label1.grid(row=0, sticky="nsew")

    menu1 = tkinter.Frame(leftFrame)
    
    menu1.grid(row=1)


    #For Distribution statistics
    label2 = tkinter.Label(rightFrame, text="Menu2")
    label2.grid(row=0, sticky="nsew")

    menu2 = tkinter.Frame(rightFrame)
    
    menu2.grid(row=1)

    leftFrame.grid(row=0, column=0)
    rightFrame.grid(row=0, column=1)

    frame.pack()
    root.mainloop()

if __name__ == "__main__":
  main()

