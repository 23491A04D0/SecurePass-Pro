"""
====================================================
 SecurePass Pro
 Clipboard Manager

 Handles copying passwords without external libraries.
 Uses built-in Tkinter clipboard functionality.
====================================================
"""


class ClipboardManager:

    def __init__(self, root):
        self.root = root


    def copy(self, text):

        """
        Copy text to system clipboard.

        Parameters:
        text (str): Password to copy
        """

        if not text:
            return False

        try:

            self.root.clipboard_clear()

            self.root.clipboard_append(text)

            self.root.update()

            return True

        except Exception:

            return False