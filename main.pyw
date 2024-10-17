# -*- coding: utf-8 -*-

"""
------------------------------------------------------------
> SEVEREM

- AUTHOR:	Doramas García Jorge
- EMAIL:	doramgajo@gmail.com
- GITHUB:	https://github.com/doramgajo
- REPOSITORY:	https://github.com/doramgajo/saverem
- LINKEDIN:	https://www.linkedin.com/in/doramgajo
------------------------------------------------------------
"""

# Saverem imports
from saverem import Saverem


if __name__ == '__main__':
    saverem = Saverem(
        "Remember to save the game", 300, 150, 0.5)
    saverem.start_reminder()
