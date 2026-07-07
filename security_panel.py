"""
====================================================
 SecurePass Pro
 Security Intelligence Panel

 Displays:
 - Strength Score
 - Entropy
 - Crack Time

====================================================
"""


import tkinter as tk



class SecurityPanel:


    def __init__(self,parent):


        self.frame=tk.Frame(

            parent,

            bg="#111827"

        )


        self.frame.pack(

            pady=20,

            padx=20,

            fill="x"

        )



        self.title=tk.Label(

            self.frame,

            text="Security Analysis",

            font=(

                "Segoe UI",

                16,

                "bold"

            ),

            bg="#111827",

            fg="#F8FAFC"

        )


        self.title.pack(

            pady=10

        )




        self.status=tk.Label(

            self.frame,

            text="Strength : --",

            font=(

                "Segoe UI",

                12

            ),

            bg="#111827",

            fg="#94A3B8"

        )


        self.status.pack()




        self.entropy=tk.Label(

            self.frame,

            text="Entropy : --",

            font=(

                "Segoe UI",

                12

            ),

            bg="#111827",

            fg="#94A3B8"

        )


        self.entropy.pack()




        self.crack=tk.Label(

            self.frame,

            text="Crack Time : --",

            font=(

                "Segoe UI",

                12

            ),

            bg="#111827",

            fg="#94A3B8"

        )


        self.crack.pack()



    def update(self,data):


        self.status.config(

            text=

            f"Strength : {data['level']}"

        )


        self.entropy.config(

            text=

            f"Entropy : {data['entropy']} bits"

        )


        self.crack.config(

            text=

            f"Crack Time : {data['crack_time']}"

        )