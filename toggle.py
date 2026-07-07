"""
====================================================
 SecurePass Pro
 Password Visibility Controller

 Handles hide/show password feature
====================================================
"""


class PasswordToggle:


    def __init__(self, entry):

        self.entry = entry

        self.visible = False



    def toggle(self):

        """
        Switch between hidden and visible mode.
        """

        if self.visible:

            self.entry.config(
                show="•"
            )

            self.visible = False


        else:

            self.entry.config(
                show=""
            )

            self.visible = True