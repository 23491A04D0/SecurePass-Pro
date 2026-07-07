"""
====================================================
 SecurePass Pro

 Password History Manager

====================================================
"""


import json
import os
from datetime import datetime



class PasswordHistory:


    def __init__(self):


        self.file_path = "data/history.json"


        self.create_file()



    def create_file(self):


        folder="data"


        if not os.path.exists(folder):

            os.makedirs(folder)



        if not os.path.exists(self.file_path):

            with open(
                self.file_path,
                "w"
            ) as file:

                json.dump(
                    [],
                    file
                )




    def load_history(self):


        try:


            with open(
                self.file_path,
                "r"
            ) as file:


                return json.load(file)



        except:


            return []




    def add_password(self,password):


        history=self.load_history()



        data={

            "password":password,

            "date":datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )

        }



        history.append(data)



        with open(

            self.file_path,

            "w"

        ) as file:


            json.dump(

                history,

                file,

                indent=4

            )





    def clear_history(self):


        with open(

            self.file_path,

            "w"

        ) as file:


            json.dump(

                [],

                file

            )