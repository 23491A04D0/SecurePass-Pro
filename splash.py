"""
====================================================
 SecurePass Pro
 Animated Splash Screen

====================================================
"""


import tkinter as tk


from src.logo import SecureLogo




class SplashScreen:



    def __init__(self):


        self.window=tk.Tk()


        self.window.geometry(

            "520x420"

        )


        self.window.configure(

            bg="#0B1120"

        )


        self.window.overrideredirect(

            True

        )



        self.alpha=0




    def fade_in(self):


        if self.alpha < 1:


            self.alpha += 0.05


            self.window.attributes(

                "-alpha",

                self.alpha

            )


            self.window.after(

                40,

                self.fade_in

            )




    def show(self):


        self.window.attributes(

            "-alpha",

            0

        )



        logo=SecureLogo(

            self.window

        )


        logo.pack(

            pady=40

        )




        tk.Label(

            self.window,

            text="SecurePass Pro",

            font=(

                "Segoe UI",

                32,

                "bold"

            ),

            bg="#0B1120",

            fg="white"

        ).pack()




        tk.Label(

            self.window,

            text="Next Generation Password Security",

            font=(

                "Segoe UI",

                12

            ),

            bg="#0B1120",

            fg="#94A3B8"

        ).pack(

            pady=10

        )



        loading=tk.Label(

            self.window,

            text="Initializing Security Engine...",

            bg="#0B1120",

            fg="#3B82F6"

        )


        loading.pack(

            pady=20

        )




        self.fade_in()



        self.window.after(

            2500,

            self.window.destroy

        )



        self.window.mainloop()