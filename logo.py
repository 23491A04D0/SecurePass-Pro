"""
====================================================
 SecurePass Pro
 Logo Component
====================================================
"""


import tkinter as tk



class SecureLogo:


    def __init__(self,parent):


        self.canvas=tk.Canvas(

            parent,

            width=120,

            height=120,

            bg="#0B1120",

            highlightthickness=0

        )


        self.draw()



    def draw(self):


        # Shield

        self.canvas.create_polygon(

            60,10,

            100,30,

            95,75,

            60,105,

            25,75,

            20,30,

            fill="#3B82F6"

        )


        # Lock

        self.canvas.create_rectangle(

            45,

            50,

            75,

            85,

            fill="#FFFFFF"

        )


        self.canvas.create_arc(

            45,

            30,

            75,

            65,

            start=0,

            extent=180,

            style="arc",

            width=5,

            outline="#FFFFFF"

        )



    def pack(self,**kwargs):

        self.canvas.pack(**kwargs)