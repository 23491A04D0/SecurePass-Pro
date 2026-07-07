"""
====================================================
 SecurePass Pro
 Theme Manager

 Controls application colors
====================================================
"""


class ThemeManager:


    def __init__(self):

        self.dark = True



    def get_theme(self):

        """
        Returns current theme colors.
        """


        if self.dark:


            return {


                "bg":"#0B1120",

                "card":"#111827",

                "input":"#020617",

                "text":"#F8FAFC",

                "subtext":"#94A3B8",

                "accent":"#3B82F6",

                "success":"#22C55E",

                "danger":"#EF4444"


            }



        else:


            return {


                "bg":"#F8FAFC",

                "card":"#FFFFFF",

                "input":"#E2E8F0",

                "text":"#0F172A",

                "subtext":"#475569",

                "accent":"#2563EB",

                "success":"#16A34A",

                "danger":"#DC2626"


            }



    def toggle(self):

        """
        Switch theme.
        """

        self.dark = not self.dark

        return self.get_theme()