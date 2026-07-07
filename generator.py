"""
=========================================================
 SecurePass Pro
 Password Generation Engine

 Uses Python's cryptographically secure `secrets` module
 instead of the normal `random` module.

 Author : Your Name
=========================================================
"""

import secrets
import string


def generate_password(
    length: int,
    uppercase: bool = True,
    lowercase: bool = True,
    numbers: bool = True,
    symbols: bool = True,
):
    """
    Generate a cryptographically secure password.

    Parameters
    ----------
    length : int
        Desired password length.

    uppercase : bool
    lowercase : bool
    numbers : bool
    symbols : bool

    Returns
    -------
    str
        Generated password.
    """

    character_pool = ""

    mandatory = []

    if uppercase:
        character_pool += string.ascii_uppercase
        mandatory.append(secrets.choice(string.ascii_uppercase))

    if lowercase:
        character_pool += string.ascii_lowercase
        mandatory.append(secrets.choice(string.ascii_lowercase))

    if numbers:
        character_pool += string.digits
        mandatory.append(secrets.choice(string.digits))

    if symbols:
        character_pool += "!@#$%^&*()-_=+[]{}<>?"
        mandatory.append(secrets.choice("!@#$%^&*()-_=+[]{}<>?"))

    if character_pool == "":
        raise ValueError("Select at least one character type.")

    if length < len(mandatory):
        raise ValueError(
            "Password length is too short for the selected options."
        )

    password = mandatory.copy()

    remaining = length - len(password)

    for _ in range(remaining):
        password.append(secrets.choice(character_pool))

    secrets.SystemRandom().shuffle(password)

    return "".join(password)
