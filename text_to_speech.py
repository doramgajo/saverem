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

# Libraries imports
import pyttsx3

class TextToSpeech:

    MALE_VOICE_INDEX = 0
    FEMALE_VOICE_INDEX = 1

    def __init__(self):
        self._engine = pyttsx3.init()

    def play(self, text: str):
        """
        Converts received text to speech and plays it
        :param text: text to convert to speech
        """
        self._engine.say(text)
        self._engine.runAndWait()

    def set_rate(self, rate: int):
        """
        Set text to speech voice rate
        :param rate: int value between 0 and 250
        """
        self._engine.setProperty('rate', rate)

    def get_rate(self):
        return self._engine.getProperty('rate')

    def set_volume(self, volume: float):
        """
        Set text to speech audio volume
        :param volume: float value between 0 and 1
        :return:
        """
        self._engine.setProperty('volume', volume)

    def get_volume(self):
        return self._engine.getProperty('volume')

    def _set_voice(self, voice_id: str):
        self._engine.setProperty('voice', voice_id)

    def _get_voice(self):
        return self._engine.getProperty('voice')

    def _get_voices(self):
        return self._engine.getProperty('voices')

    def _get_voices_ids(self):
        return [voice.id for voice in self._get_voices()]

    def set_male_voice(self):
        return self._set_voice(
            self._get_voices_ids()[TextToSpeech.MALE_VOICE_INDEX])

    def set_female_voice(self):
        return self._set_voice(
            self._get_voices_ids()[TextToSpeech.FEMALE_VOICE_INDEX])
