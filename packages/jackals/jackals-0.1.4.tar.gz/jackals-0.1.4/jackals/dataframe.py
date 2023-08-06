#!/usr/bin/env python3
# Copyright (c) 
# All rights reserved.
#
# This source code is licensed under the MIT-style license found in the
# LICENSE file in the root directory of this source tree.

from typing import Union
from .series import Series, BoolSeries, NumericSeries
import pdb

# A TDataFrame class should be initialized with a dict of typed Series .


class TDataFrame():

    def __init__(self, series: dict) -> None:
        assert type(series) == dict and series != {} , "Dataframes are initialized with non empty dictionaries of Series"

        for i, v in enumerate(series.values()):
            if not type(v).__bases__[0] in [Series, NumericSeries] :
                raise ValueError("Invalid Object was found")
            if i == 0:
                self.lenght = v.__len__()
            elif self.lenght != v.__len__():
                raise ValueError("Different Lenghts are not Implemented")

        self.series = series

    def __len__(self):
        return self.lenght

    def __getitem__(self, index: Union[str, "BoolSeries"]):

        if isinstance(index, BoolSeries):
            assert index.__len__() == self.__len__() , "Boolean lenght doesn't match"
            new_dict = dict.fromkeys(list(self.series.keys()))
            for key in self.series.keys():
                new_dict[key] = self.series[key][index]
            return self.__class__(series=new_dict)

        elif isinstance(index, str):
            return self.series[index]
        else:
            raise IndexError(index)
    