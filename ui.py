"""
====================================================
 SecurePass Pro

 Main UI Controller

 Version:
 v8

 Integrated:
 - Dashboard Views
 - Glass Cards
 - Theme System
 - Password Engine

====================================================
"""


import tkinter as tk
from tkinter import messagebox


from src.generator import generate_password
from src.history import PasswordHistory
from src.clipboard import ClipboardManager
from src.toggle import PasswordToggle
from src.strength import analyze_password
from src.security_panel import SecurityPanel
from src.search import HistorySearch
from src.export import ExportManager
from src.theme import ThemeManager
from src.views import DashboardView
from src.components import ModernButton





class SecurePassUI:


    def __init__(self):


        self.root=tk.Tk()


        self.root.title(
            "SecurePass Pro"
        )


        self.root.geometry(
            "1250x900"
        )


        self.root.resizable(
            False,
            False
        )



        self.theme=ThemeManager()


        self.colors=self.theme.get_theme()



        self.history=PasswordHistory()


        self.clipboard=ClipboardManager(

            self.root

        )


        self.search_engine=HistorySearch()


        self.exporter=ExportManager()



        self.root.configure(

            bg=self.colors["bg"]

        )






    def build(self):


        # HEADER


        tk.Label(

            self.root,

            text="SecurePass Pro",

            font=(

                "Segoe UI",

                36,

                "bold"

            ),

            bg=self.colors["bg"],

            fg=self.colors["text"]

        ).pack(

            pady=25

        )



        tk.Label(

            self.root,

            text="Next Generation Password Security Platform",

            font=(

                "Segoe UI",

                14

            ),

            bg=self.colors["bg"],

            fg=self.colors["subtext"]

        ).pack()



        # DASHBOARD


        dashboard=DashboardView(

            self.root,

            self.colors

        )


        generator_area,history_area=dashboard.create_layout()



        # ==========================
        # GENERATOR AREA
        # ==========================


        tk.Label(

            generator_area,

            text="Password Generator",

            font=(

                "Segoe UI",

                20,

                "bold"

            ),

            bg=self.colors["card"],

            fg=self.colors["text"]

        ).pack(

            pady=20

        )



        self.length=tk.IntVar(

            value=16

        )



        tk.Scale(

            generator_area,

            from_=8,

            to=64,

            variable=self.length,

            orient="horizontal"

        ).pack()



        self.upper = tk.BooleanVar(
        value=True
        )

        self.lower = tk.BooleanVar(
        value=True
        )

        self.number = tk.BooleanVar(
        value=True
        )

        self.symbol = tk.BooleanVar(
        value=True
        )


        for text,var in [

            ("Uppercase",self.upper),

            ("Lowercase",self.lower),

            ("Numbers",self.number),

            ("Symbols",self.symbol)

        ]:


            tk.Checkbutton(

                generator_area,

                text=text,

                variable=var

            ).pack()




        self.password=tk.Entry(

            generator_area,

            font=(

                "Consolas",

                20

            ),

            justify="center",

            show="•"

        )


        self.password.pack(

            fill="x",

            padx=30,

            pady=20,

            ipady=10

        )




        self.toggle=PasswordToggle(

            self.password

        )



        self.security=SecurityPanel(

            generator_area

        )




        ModernButton(

            generator_area,

            "Generate Password",

            self.generate

        ).pack(

            pady=5

        )



        ModernButton(

            generator_area,

            "Copy Password",

            self.copy,

            "#334155"

        ).pack(

            pady=5

        )



        ModernButton(

            generator_area,

            "Show / Hide",

            self.toggle.toggle,

            "#475569"

        ).pack(

            pady=5

        )





        # ==========================
        # HISTORY AREA
        # ==========================


        tk.Label(

            history_area,

            text="Password History",

            font=(

                "Segoe UI",

                20,

                "bold"

            )

        ).pack(

            pady=20

        )



        self.search=tk.StringVar()



        tk.Entry(

            history_area,

            textvariable=self.search

        ).pack()



        self.history_box=tk.Listbox(

            history_area,

            width=35,

            height=25

        )


        self.history_box.pack(

            pady=20

        )


        self.search.trace(

            "w",

            lambda *x:self.refresh_history()

        )





    def generate(self):


        try:


            pwd=generate_password(

                self.length.get(),

                self.upper.get(),

                self.lower.get(),

                self.number.get(),

                self.symbol.get()

            )



            self.password.delete(

                0,

                tk.END

            )


            self.password.insert(

                0,

                pwd

            )



            self.history.add_password(

                pwd

            )


            self.security.update(

                analyze_password(pwd)

            )



            self.refresh_history()



        except Exception as e:


            messagebox.showerror(

                "SecurePass Pro",

                str(e)

            )





    def copy(self):


        self.clipboard.copy(

            self.password.get()

        )





    def refresh_history(self):


        self.history_box.delete(

            0,

            tk.END

        )


        data=self.search_engine.filter(

            self.history.load_history(),

            self.search.get()

        )



        for item in data:


            self.history_box.insert(

                tk.END,

                item["password"]

            )





    def run(self):


        self.build()


        self.refresh_history()


        self.root.mainloop()