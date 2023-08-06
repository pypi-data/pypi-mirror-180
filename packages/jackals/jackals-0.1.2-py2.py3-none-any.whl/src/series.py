#!/usr/bin/env python3
# Copyright (c) 
# All rights reserved.
#
# This source code is licensed under the MIT-style license found in the
# LICENSE file in the root directory of this source tree.

from typing import Union

# A Series class should be initialized with a class type .
# There are different types of Series:
# - StrSeries containing string elements(and None)
# - BoolSeries (with values True, False and None) 
# - FloatSeries different numeric for floating point values 
# - IntSeries for integer.


class Series():

    def __init__(self, elements: list, stype: type) -> None:
        assert type(elements) == list , "Series are initialized with a list of elements"
        if not all((type(i) == stype or type(i) == None)for i in elements):
            raise ValueError("Wrong type found")

        self.elements = elements
        self.stype = stype
    
    def __len__(self):
        return len(self.elements)

    def __getitem__(self, index: Union[int, "BoolSeries"]):

        if isinstance(index, BoolSeries):
            assert index.__len__() == self.__len__() , "Series lenghts don't match"
            elements = [self.elements[i] for(i, v) in enumerate(index.elements) if v]
            return collection[self.stype](elements=elements)

        elif isinstance(index, int):
            return self.elements[index]
        else:
            raise IndexError(index)

    def __eq__(self, other) -> "BoolSeries" :
        if type(other) is int:
            assert self.stype == int , "Invalid type"
            elements = [self.elements[i]==other for(i) in range(self.__len__())]
        elif isinstance(other, bool):
            assert self.stype == bool , "Invalid type"
            elements = [self.elements[i]==other for(i) in range(self.__len__())]
        elif isinstance(other, float):
            assert self.stype == float , "Invalid type"
            elements = [self.elements[i]==other for(i) in range(self.__len__())]
        elif isinstance(other, str):
            assert self.stype == str , "Invalid type"
            elements = [self.elements[i]==other for(i) in range(self.__len__())]
        elif type(other).__bases__[0] == Series:
            assert other.__len__() == self.__len__() , "Lenghts don't match"
            assert other.stype == self.stype , "Types don't match"
            elements = [self.elements[i]==other[i] for(i) in range(self.__len__())]
        else:
            raise ValueError 
        
        return BoolSeries(elements)

    def __ne__(self, other) -> "BoolSeries" :
        if type(other) is int:
            assert self.stype == int , "Invalid type"
            elements = [self.elements[i]!=other for(i) in range(self.__len__())]
        elif isinstance(other, bool):
            assert self.stype == bool , "Invalid type"
            elements = [self.elements[i]==other for(i) in range(self.__len__())]
        elif isinstance(other, float):
            assert self.stype == float , "Invalid type"
            elements = [self.elements[i]!=other for(i) in range(self.__len__())]
        elif isinstance(other, str):
            assert self.stype == str , "Invalid type"
            elements = [self.elements[i]==other for(i) in range(self.__len__())]
        elif type(other).__bases__[0] == Series:
            assert other.__len__() == self.__len__() , "Lenghts don't match"
            assert other.stype == self.stype , "Types don't match"
            elements = [self.elements[i]!=other[i] for(i) in range(self.__len__())]
        else:
            raise ValueError 
        
        return BoolSeries(elements)


"""
Numeric Series

"""


class NumericSeries(Series):

    def __init__(self, elements: list, stype : type) -> None:
        assert stype in [int, float], "Invalid type"
        super().__init__(elements=elements, stype=stype)
        self.stype = stype

    def __lt__(self, other) -> "BoolSeries" :
        if type(other) is int:
            assert self.stype == int , "Invalid type"
            elements = [self.elements[i]<other for(i) in range(self.__len__())]
        elif isinstance(other, float):
            assert self.stype == float , "Invalid type"
            elements = [self.elements[i]<other for(i) in range(self.__len__())]
        elif type(other).__bases__[0] == NumericSeries:
            assert other.__len__() == self.__len__() , "Lenghts don't match"
            assert other.stype == self.stype , "Types don't match"
            elements = [self.elements[i]<other[i] for(i) in range(self.__len__())]
        else:
            raise ValueError 
        
        return BoolSeries(elements)
    def __le__(self, other) -> "BoolSeries" :
        if type(other) is int:
            assert self.stype == int , "Invalid type"
            elements = [self.elements[i]<=other for(i) in range(self.__len__())]
        elif isinstance(other, float):
            assert self.stype == float , "Invalid type"
            elements = [self.elements[i]<=other for(i) in range(self.__len__())]
        elif type(other).__bases__[0] == NumericSeries:
            assert other.__len__() == self.__len__() , "Lenghts don't match"
            assert other.stype == self.stype , "Types don't match"
            elements = [self.elements[i]<=other[i] for(i) in range(self.__len__())]
        else:
            raise ValueError 
        
        return BoolSeries(elements)
 
    def __gt__(self, other) -> "BoolSeries" :
        if type(other) is int:
            assert self.stype == int , "Invalid type"
            elements = [self.elements[i]>other for(i) in range(self.__len__())]
        elif isinstance(other, float):
            assert self.stype == float , "Invalid type"
            elements = [self.elements[i]>other for(i) in range(self.__len__())]
        elif type(other).__bases__[0] == NumericSeries:
            assert other.__len__() == self.__len__() , "Lenghts don't match"
            assert other.stype == self.stype , "Types don't match"
            elements = [self.elements[i]>other[i] for(i) in range(self.__len__())]
        else:
            raise ValueError 
        
        return BoolSeries(elements)

    def __ge__(self, other) -> "BoolSeries" :
        if type(other) is int:
            assert self.stype == int , "Invalid type"
            elements = [self.elements[i]>=other for(i) in range(self.__len__())]
        elif isinstance(other, float):
            assert self.stype == float , "Invalid type"
            elements = [self.elements[i]>=other for(i) in range(self.__len__())]
        elif type(other).__bases__[0] == NumericSeries:
            assert other.__len__() == self.__len__() , "Lenghts don't match"
            assert other.stype == self.stype , "Types don't match"
            elements = [self.elements[i]>=other[i] for(i) in range(self.__len__())]
        else:
            raise ValueError 
        
        return BoolSeries(elements)

    def __add__(self, other):
        if type(other) is int:
            assert self.stype == int , "Invalid type"
            elements = [self.elements[i] + other for(i) in range(self.__len__())]
        elif isinstance(other, float):
            assert self.stype == float , "Invalid type"
            elements = [self.elements[i] + other for(i) in range(self.__len__())]
        elif type(other).__bases__[0] == NumericSeries:
            assert other.__len__() == self.__len__() , "Lenghts don't match"
            assert other.stype == self.stype , "Types don't match"
            elements = [self.elements[i] + other[i] for(i) in range(self.__len__())]
        else:
            raise ValueError 
        
        return collection[self.stype](elements)

    def __sub__(self, other):
        if type(other) is int:
            assert self.stype == int , "Invalid type"
            elements = [self.elements[i] - other for(i) in range(self.__len__())]
        elif isinstance(other, float):
            assert self.stype == float , "Invalid type"
            elements = [self.elements[i] - other for(i) in range(self.__len__())]
        elif type(other).__bases__[0] == NumericSeries:
            assert other.__len__() == self.__len__() , "Lenghts don't match"
            assert other.stype == self.stype , "Types don't match"
            elements = [self.elements[i] - other[i] for(i) in range(self.__len__())]
        else:
            raise ValueError 
        
        return collection[self.stype](elements)

    def __mul__(self, other):
        if type(other) is int:
            assert self.stype == int , "Invalid type"
            elements = [self.elements[i] * other for(i) in range(self.__len__())]
        elif isinstance(other, float):
            assert self.stype == float , "Invalid type"
            elements = [self.elements[i] * other for(i) in range(self.__len__())]
        elif type(other).__bases__[0] == NumericSeries:
            assert other.__len__() == self.__len__() , "Lenghts don't match"
            assert other.stype == self.stype , "Types don't match"
            elements = [self.elements[i] * other[i] for(i) in range(self.__len__())]
        else:
            raise ValueError 
        
        return collection[self.stype](elements)


    def __div__(self, other):
        # ZeroDivisionError is already handled by Python
        if type(other) is int:
            assert self.stype == int , "Invalid type"
            elements = [self.elements[i] / other for(i) in range(self.__len__())]
        elif isinstance(other, float):
            assert other > 0 , "Divison by Zero" 
            assert self.stype == float , "Invalid type"
            elements = [self.elements[i] / other for(i) in range(self.__len__())]
        elif type(other).__bases__[0] == NumericSeries:
            assert other.__len__() == self.__len__() , "Lenghts don't match"
            assert other.stype == self.stype , "Types don't match"
            elements = [self.elements[i] / other[i] for(i) in range(self.__len__())]
        else:
            raise ValueError 
        
        return collection[self.stype](elements)


class FloatSeries(NumericSeries):
    def __init__(self, elements: list) -> None:
        super().__init__(elements=elements, stype=float)

class IntSeries(NumericSeries):
    def __init__(self, elements: list) -> None:
        super().__init__(elements=elements, stype=int)


"""
String Series
"""


class StrSeries(Series):

    def __init__(self, elements: list) -> None:
        super().__init__(elements=elements, stype=str)


"""
Bool Series

"""

class BoolSeries(Series):

    def __init__(self, elements: list) -> None:
        super().__init__(elements=elements, stype=bool)

    def __and__(self, other) -> "BoolSeries" :
        return self.__eq__(other)

    def __or__(self, other) -> "BoolSeries" :
        if type(other) is bool:
            elements = [self.elements[i] or other for(i) in range(self.__len__())]
        elif isinstance(other, BoolSeries):
            assert other.__len__() == self.__len__() , "Lenghts don't match"
            elements = [self.elements[i] or other[i] for(i) in range(self.__len__())]
        else:
            raise ValueError 
        return BoolSeries(elements)

    def __xor__(self, other) -> "BoolSeries" :
        if type(other) is bool:
            elements = [self.elements[i] != other for(i) in range(self.__len__())]
        elif isinstance(other, BoolSeries):
            assert other.__len__() == self.__len__() , "Lenghts don't match"
            elements = [self.elements[i] != other[i] for(i) in range(self.__len__())]
        else:
            raise ValueError 
        return BoolSeries(elements)

    def __not__(self) -> "BoolSeries" :
        elements = [(not self.elements[i]) for(i) in range(self.__len__())]
        return BoolSeries(elements)



"""
Summary Object
"""


collection = {
    float : FloatSeries,
    bool : BoolSeries,
    str : StrSeries, 
    int : IntSeries
}