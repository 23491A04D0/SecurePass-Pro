"""
====================================================
 SecurePass Pro
 Strength Meter UI Component

 Creates animated security visualization
====================================================
"""


import tkinter as tk



class StrengthMeter:


    def __init__(self, parent):

        self.parent = parent


        self.canvas = tk.Canvas(

            parent,

            width=500,

            height=25,

            bg="#020617",

            highlightthickness=0

        )


        self.canvas.pack(
            pady=15
        )


        self.progress = self.canvas.create_rectangle(

            0,

            0,

            0,

            25,

            fill="#EF4444",

            width=0

        )



        self.text = tk.Label(

            parent,

            text="Strength: --",

            font=("Segoe UI",12,"bold"),

            bg="#111827",

            fg="#F8FAFC"

        )


        self.text.pack()



    def update(self, score):


        width = int(score * 5)


        self.canvas.coords(

            self.progress,

            0,

            0,

            width,

            25

        )


        if score < 30:

            color="#EF4444"

            level="Very Weak"


        elif score < 50:

            color="#FACC15"

            level="Weak"


        elif score < 70:

            color="#3B82F6"

            level="Medium"


        elif score < 90:

            color="#22C55E"

            level="Strong"


        else:

            color="#10B981"

            level="Very Strong"



        self.canvas.itemconfig(

            self.progress,

            fill=color

        )


        self.text.config(

            text=f"Strength: {level} ({score}%)"

        )