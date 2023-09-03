from clojos_common.util import tokeniser


def test_tokenise():
    assert tokeniser.string_tokeniser("Bronzie.Bear", tokeniser.sp_splitter,
                                      tokeniser.special_char_set) == "Bronzie_Bear"


def test_titleiser():
    assert tokeniser.titleiser_tokeniser("bronzie bear", tokeniser.sp_splitter,
                                         tokeniser.special_char_set) == "BronzieBear"
