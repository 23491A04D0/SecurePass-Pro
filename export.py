"""
====================================================
 SecurePass Pro
 Export Manager

 Handles exporting password history
 into TXT and JSON formats.
====================================================
"""


import json
from datetime import datetime



class ExportManager:


    def __init__(self, history_file="data/history.json"):

        self.history_file = history_file



    def load_history(self):

        """
        Load password history.
        """

        try:

            with open(
                self.history_file,
                "r"
            ) as file:

                return json.load(file)


        except:

            return []



    def export_txt(self):

        """
        Export history into text file.
        """

        history = self.load_history()


        filename = (
            "SecurePass_History_"
            +
            datetime.now()
            .strftime("%Y%m%d_%H%M%S")
            +
            ".txt"
        )


        with open(
            filename,
            "w"
        ) as file:


            file.write(
                "SecurePass Pro - Password History\n"
            )


            file.write(
                "="*40+"\n\n"
            )


            for item in history:


                file.write(

                    f"Password : {item['password']}\n"

                )


                file.write(

                    f"Created  : {item['time']}\n\n"

                )


        return filename




    def export_json(self):

        """
        Export history into JSON file.
        """

        history=self.load_history()


        filename=(

            "SecurePass_History_"

            +

            datetime.now()
            .strftime("%Y%m%d_%H%M%S")

            +

            ".json"

        )


        with open(

            filename,

            "w"

        ) as file:


            json.dump(

                history,

                file,

                indent=4

            )


        return filename