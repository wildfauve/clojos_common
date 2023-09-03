from typing import List
import re

from . import fn

special_char_set = [("-", "_"), (" ", "_"), ("'", ""), (".", "_")]
dot_splitter = re.compile(r'\.\s*')
sp_splitter = re.compile(r'\s')

def string_tokeniser(in_str: str, str_splitter: re.Pattern, char_replacers: List) -> str:
    return fn.multi_replace(str_splitter.split(in_str)[-1], char_replacers)



def titleiser_tokeniser(in_str: str, str_splitter: re.Pattern, char_replacers: List) -> str:
    return "".join(list(map(lambda token: fn.multi_replace(token, char_replacers).title(), str_splitter.split(in_str))))

