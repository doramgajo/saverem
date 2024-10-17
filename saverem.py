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

# Python imports
from time import sleep

# Saverem imports
from text_to_speech import TextToSpeech


class Saverem:

    def __init__(self, message, wait_time=300, rate=100, volume=1):
        self.tts = TextToSpeech()
        self.message = message
        self.wait_time = wait_time
        self.tts.set_rate(rate)
        self.tts.set_volume(volume)

    def start_reminder(self):
        self.tts.play("Reminder started correctly "
                      f"with a wait time of {self.wait_time} seconds")
        while True:
            sleep(self.wait_time)
            self.tts.play(self.message)
