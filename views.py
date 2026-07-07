"""
====================================================
 SecurePass Pro

 Dashboard Views

 Handles UI layouts

====================================================
"""


import tkinter as tk

from src.glass import GlassCard



class DashboardView:



    def __init__(self,parent,colors):


        self.parent=parent

        self.colors=colors



    def create_layout(self):


        container=tk.Frame(

            self.parent,

            bg=self.colors["bg"]

        )


        container.pack(

            padx=30,

            pady=30,

            fill="both",

            expand=True

        )



        generator_card=GlassCard(

            container

        )


        generator_card.pack(

            side="left",

            fill="both",

            expand=True,

            padx=15

        )



        history_card=GlassCard(

            container

        )


        history_card.pack(

            side="right",

            fill="both",

            padx=15

        )



        return (

            generator_card.widget(),

            history_card.widget()

        )