from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.gp import *


class Hatch_SequenceOfLine:
    def __init__(self) -> None: ...
    def __len__(self) -> int: ...
    def Size(self) -> int: ...
    def Clear(self) -> None: ...
    def First(self) -> Hatch_Line: ...
    def Last(self) -> Hatch_Line: ...
    def Length(self) -> int: ...
    def Append(self, theItem: Hatch_Line) -> Hatch_Line: ...
    def Prepend(self, theItem: Hatch_Line) -> Hatch_Line: ...
    def RemoveFirst(self) -> None: ...
    def Reverse(self) -> None: ...
    def Value(self, theIndex: int) -> Hatch_Line: ...
    def SetValue(self, theIndex: int, theValue: Hatch_Line) -> None: ...

class Hatch_SequenceOfParameter:
    def __init__(self) -> None: ...
    def __len__(self) -> int: ...
    def Size(self) -> int: ...
    def Clear(self) -> None: ...
    def First(self) -> Hatch_Parameter: ...
    def Last(self) -> Hatch_Parameter: ...
    def Length(self) -> int: ...
    def Append(self, theItem: Hatch_Parameter) -> Hatch_Parameter: ...
    def Prepend(self, theItem: Hatch_Parameter) -> Hatch_Parameter: ...
    def RemoveFirst(self) -> None: ...
    def Reverse(self) -> None: ...
    def Value(self, theIndex: int) -> Hatch_Parameter: ...
    def SetValue(self, theIndex: int, theValue: Hatch_Parameter) -> None: ...

class Hatch_LineForm(IntEnum):
    Hatch_XLINE: int = ...
    Hatch_YLINE: int = ...
    Hatch_ANYLINE: int = ...

Hatch_XLINE = Hatch_LineForm.Hatch_XLINE
Hatch_YLINE = Hatch_LineForm.Hatch_YLINE
Hatch_ANYLINE = Hatch_LineForm.Hatch_ANYLINE

class Hatch_Hatcher:
    def __init__(self, Tol: float, Oriented: Optional[bool] = True) -> None: ...
    @overload
    def AddLine(self, L: gp_Lin2d, T: Optional[Hatch_LineForm] = Hatch_ANYLINE) -> None: ...
    @overload
    def AddLine(self, D: gp_Dir2d, Dist: float) -> None: ...
    def AddXLine(self, X: float) -> None: ...
    def AddYLine(self, Y: float) -> None: ...
    def Coordinate(self, I: int) -> float: ...
    def End(self, I: int, J: int) -> float: ...
    def EndIndex(self, I: int, J: int) -> Tuple[int, float]: ...
    def IsXLine(self, I: int) -> bool: ...
    def IsYLine(self, I: int) -> bool: ...
    def Line(self, I: int) -> gp_Lin2d: ...
    def LineForm(self, I: int) -> Hatch_LineForm: ...
    @overload
    def NbIntervals(self) -> int: ...
    @overload
    def NbIntervals(self, I: int) -> int: ...
    def NbLines(self) -> int: ...
    def Start(self, I: int, J: int) -> float: ...
    def StartIndex(self, I: int, J: int) -> Tuple[int, float]: ...
    @overload
    def Tolerance(self, Tol: float) -> None: ...
    @overload
    def Tolerance(self) -> float: ...
    @overload
    def Trim(self, L: gp_Lin2d, Index: Optional[int] = 0) -> None: ...
    @overload
    def Trim(self, L: gp_Lin2d, Start: float, End: float, Index: Optional[int] = 0) -> None: ...
    @overload
    def Trim(self, P1: gp_Pnt2d, P2: gp_Pnt2d, Index: Optional[int] = 0) -> None: ...

class Hatch_Line:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, L: gp_Lin2d, T: Hatch_LineForm) -> None: ...
    def AddIntersection(self, Par1: float, Start: bool, Index: int, Par2: float, theToler: float) -> None: ...

class Hatch_Parameter:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, Par1: float, Start: bool, Index: Optional[int] = 0, Par2: Optional[float] = 0) -> None: ...

# harray1 classes
# harray2 classes
# hsequence classes

