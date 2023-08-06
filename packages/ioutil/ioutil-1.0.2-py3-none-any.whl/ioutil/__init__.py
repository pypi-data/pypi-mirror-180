"""to read and write files"""

from typing import Literal

from ioutil._file import _File
from ioutil._csv import Csv
from ioutil._text import Text
from ioutil._toml import TOML
from ioutil._json import Json
from ioutil._parquet import Parquet


class File:
    @staticmethod
    def getinstance(_format: Literal["csv", "json", "parquet", "toml", "text"]) -> _File:
        _instance = {"csv": Csv, "json": Json, "parquet": Parquet, "toml": TOML, "text": Text}.get(_format)
        if not _instance:
            _instance = _File
        return _instance()


csv = Csv()
json = Json()
parquet = Parquet()
text = Text()
toml = TOML()

__author__ = 'srg'
__version__ = '1.0.2'

__all__ = [
    'File',
    'csv',
    'json',
    'parquet',
    'toml',
    'text'
]
