from __future__ import annotations
import os
import csv
from srutil import util
from typing import AnyStr, Dict, List

from ._file import _File


class Csv(_File):

    def write(self, data: List[List, List[Dict | List]], path: AnyStr | os.PathLike[AnyStr], mode: str = 'w') -> bool:
        fields = data.__getitem__(0)
        rows = data.__getitem__(1)
        with self._get_stream(path, mode) as csvfile:
            if isinstance(rows.__getitem__(0), list):
                csvwriter = csv.writer(csvfile)
                csvwriter.writerow(fields)
                csvwriter.writerows(rows)
            elif isinstance(rows.__getitem__(0), dict):
                csvwriter = csv.DictWriter(csvfile, fieldnames=fields)
                csvwriter.writeheader()
                csvwriter.writerows(rows)
        return os.path.exists(path)

    def read(self, path: AnyStr | os.PathLike[AnyStr], mode: str = 'r', _rfv: bool = False) -> List[List] | str:
        """
        :param path: path to target file
        :param mode: reading mode
        :param _rfv: True will return formatted string
        :return: list of values or formatted string
        """
        to_return = list()
        with self._get_stream(path, mode) as csvfile:
            for line in csv.reader(csvfile):
                to_return.append(line)
        return util.tabulate(to_return) if _rfv else to_return
