from pathlib import Path
from typing import List, NamedTuple, Optional, Tuple

try:
    import _mecab
except ImportError:
    # ImportError: dlopen(...): Symbol not found: _iconv
    # Strange workaround: https://github.com/pymssql/pymssql/issues/705
    # This only happens on macOS
    import _mecab
    import _scproxy

mecabrc_path = Path(__file__).parent / "mecabrc"


class Feature(NamedTuple):
    pos: str
    semantic: str
    has_jongseong: bool
    reading: str
    type: str
    start_pos: str
    end_pos: str
    exprssion: str


def _create_lattice(sentence: str) -> _mecab.Lattice:
    lattice = _mecab.Lattice()
    lattice.add_request_type(_mecab.MECAB_ALLOCATE_SENTENCE)  # Required
    lattice.set_sentence(sentence)

    return lattice


def _extract_feature(node: _mecab.Node) -> Feature:
    # Reference:
    # - http://taku910.github.io/mecab/learn.html
    # - https://docs.google.com/spreadsheets/d/1-9blXKjtjeKZqsf4NzHeYJCrr49-nXeRF6D80udfcwY
    # - https://bitbucket.org/eunjeon/mecab-ko-dic/src/master/utils/dictionary/lexicon.py

    # feature = <pos>,<semantic>,<has_jongseong>,<reading>,<type>,<start_pos>,<end_pos>,<expression>
    values = node.feature.split(",")
    assert len(values) == 8

    values = [value if value != "*" else None for value in values]
    feature = dict(zip(Feature._fields, values))
    feature["has_jongseong"] = {"T": True, "F": False}.get(
        feature["has_jongseong"])

    return Feature(**feature)


class MeCabError(Exception):
    pass


class MeCab:  # APIs are inspried by KoNLPy
    def __init__(self, dictionary_directory: Optional[str] = None):
        if dictionary_directory is None:
            try:
                import mecab_ko_dic
                dictionary_directory = mecab_ko_dic.DICDIR
            except ImportError:
                raise RuntimeError(
                    "`mecab_ko_dic` not found. Please run `pip install mecab_ko_dic`")

        arguments = [
            "--rcfile", str(mecabrc_path),
            "--dicdir", dictionary_directory,
        ]

        self.tagger = _mecab.Tagger(arguments)

    def parse(self, sentence: str) -> List[Tuple[str, Feature]]:
        lattice = _create_lattice(sentence)
        if not self.tagger.parse(lattice):
            raise MeCabError(self.tagger.what())

        return [(node.surface, _extract_feature(node)) for node in lattice]

    def pos(self, sentence: str) -> List[Tuple[str, str]]:
        return [(surface, feature.pos) for surface, feature in self.parse(sentence)]

    def morphs(self, sentence: str) -> List[str]:
        return [surface for surface, _ in self.parse(sentence)]

    def nouns(self, sentence: str) -> List[str]:
        return [
            surface
            for surface, feature in self.parse(sentence)
            if feature.pos.startswith("N")
        ]
