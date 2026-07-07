"""
====================================================
 SecurePass Pro

 Glassmorphism UI Components

====================================================
"""


import tkinter as tk



class GlassCard:


    def __init__(self,parent):


        self.frame=tk.Frame(

            parent,

            bg="#162033",

            bd=0,

            highlightthickness=1,

            highlightbackground="#334155"

        )



    def pack(self,**kwargs):

        self.frame.pack(**kwargs)



    def grid(self,**kwargs):

        self.frame.grid(**kwargs)



    def widget(self):

        return self.frame