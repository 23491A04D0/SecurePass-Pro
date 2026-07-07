"""
====================================================
 SecurePass Pro
 Password Strength Analyzer

 Calculates:
 - Strength score
 - Entropy
 - Security level
 - Estimated crack time
====================================================
"""

import math


class PasswordStrength:

    def __init__(self, password):

        self.password = password


    def calculate_entropy(self):

        """
        Calculates password entropy in bits.
        Higher entropy = stronger password.
        """

        if not self.password:
            return 0


        pool = 0

        if any(char.islower() for char in self.password):
            pool += 26

        if any(char.isupper() for char in self.password):
            pool += 26

        if any(char.isdigit() for char in self.password):
            pool += 10

        if any(not char.isalnum() for char in self.password):
            pool += 32


        entropy = len(self.password) * math.log2(pool)

        return round(entropy, 2)



    def strength_score(self):

        """
        Returns security score from 0-100.
        """

        score = 0


        length = len(self.password)


        # Length points

        if length >= 8:
            score += 20

        if length >= 12:
            score += 20

        if length >= 16:
            score += 20


        # Character diversity

        if any(char.islower() for char in self.password):
            score += 10

        if any(char.isupper() for char in self.password):
            score += 10

        if any(char.isdigit() for char in self.password):
            score += 10

        if any(not char.isalnum() for char in self.password):
            score += 10


        return min(score, 100)



    def security_level(self):

        """
        Converts score into readable level.
        """

        score = self.strength_score()


        if score < 30:
            return "Very Weak"


        elif score < 50:
            return "Weak"


        elif score < 70:
            return "Medium"


        elif score < 90:
            return "Strong"


        else:
            return "Very Strong"



    def crack_time(self):

        """
        Rough estimation of brute force crack time.
        """

        entropy = self.calculate_entropy()


        guesses = 2 ** entropy


        seconds = guesses / 1_000_000_000


        if seconds < 60:
            return "Seconds"


        elif seconds < 3600:
            return "Minutes"


        elif seconds < 86400:
            return "Hours"


        elif seconds < 31536000:
            return "Days"


        elif seconds < 31536000 * 1000:
            return "Years"



        else:
            return "Millions of Years"



def analyze_password(password):

    """
    Simple function interface.
    """

    analyzer = PasswordStrength(password)


    return {

        "score": analyzer.strength_score(),

        "entropy": analyzer.calculate_entropy(),

        "level": analyzer.security_level(),

        "crack_time": analyzer.crack_time()

    }
