"""
====================================================
 SecurePass Pro

 UI Components

 Professional reusable widgets

====================================================
"""


import tkinter as tk



class ModernButton:


    def __init__(
        self,
        parent,
        text,
        command,
        color="#3B82F6"
    ):


        self.button=tk.Button(

            parent,

            text=text,

            command=command,

            bg=color,

            fg="white",

            activebackground=color,

            activeforeground="white",

            font=(

                "Segoe UI",

                11,

                "bold"

            ),

            relief="flat",

            cursor="hand2",

            padx=18,

            pady=8

        )


        self.normal=color


        self.hover="#2563EB"



        self.button.bind(

            "<Enter>",

            self.on_hover

        )


        self.button.bind(

            "<Leave>",

            self.on_leave

        )





    def on_hover(self,event):


        self.button.configure(

            bg=self.hover

        )





    def on_leave(self,event):


        self.button.configure(

            bg=self.normal

        )





    def pack(self,**kwargs):


        self.button.pack(**kwargs)





    def grid(self,**kwargs):


        self.button.grid(**kwargs)