"""
====================================================
 SecurePass Pro
 History Search Engine

 Filters password history data
====================================================
"""


class HistorySearch:


    def filter(self, history, keyword):

        """
        Returns matching history records.
        """

        if keyword == "":

            return history


        results=[]


        keyword=keyword.lower()


        for item in history:


            password=item["password"].lower()


            if keyword in password:

                results.append(item)


        return results