from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.BRepAdaptor import *
from OCC.Core.TopoDS import *
from OCC.Core.TopAbs import *
from OCC.Core.ChFiDS import *
from OCC.Core.GeomAbs import *
from OCC.Core.TopOpeBRepBuild import *
from OCC.Core.Geom import *
from OCC.Core.TopTools import *
from OCC.Core.Adaptor3d import *
from OCC.Core.math import *
from OCC.Core.Law import *
from OCC.Core.gp import *
from OCC.Core.GeomAdaptor import *
from OCC.Core.TopOpeBRepDS import *
from OCC.Core.Geom2d import *
from OCC.Core.TColStd import *
from OCC.Core.Bnd import *
from OCC.Core.BRepBlend import *
from OCC.Core.IntSurf import *
from OCC.Core.GeomFill import *


class ChFi3d_FilletShape(IntEnum):
    ChFi3d_Rational: int = ...
    ChFi3d_QuasiAngular: int = ...
    ChFi3d_Polynomial: int = ...

ChFi3d_Rational = ChFi3d_FilletShape.ChFi3d_Rational
ChFi3d_QuasiAngular = ChFi3d_FilletShape.ChFi3d_QuasiAngular
ChFi3d_Polynomial = ChFi3d_FilletShape.ChFi3d_Polynomial

class chfi3d:
    @staticmethod
    def ConcaveSide(S1: BRepAdaptor_Surface, S2: BRepAdaptor_Surface, E: TopoDS_Edge, Or1: TopAbs_Orientation, Or2: TopAbs_Orientation) -> int: ...
    @staticmethod
    def DefineConnectType(E: TopoDS_Edge, F1: TopoDS_Face, F2: TopoDS_Face, SinTol: float, CorrectPoint: bool) -> ChFiDS_TypeOfConcavity: ...
    @staticmethod
    def IsTangentFaces(theEdge: TopoDS_Edge, theFace1: TopoDS_Face, theFace2: TopoDS_Face, Order: Optional[GeomAbs_Shape] = GeomAbs_G1) -> bool: ...
    @overload
    @staticmethod
    def NextSide(Or1: TopAbs_Orientation, Or2: TopAbs_Orientation, OrSave1: TopAbs_Orientation, OrSave2: TopAbs_Orientation, ChoixSauv: int) -> int: ...
    @overload
    @staticmethod
    def NextSide(Or: TopAbs_Orientation, OrSave: TopAbs_Orientation, OrFace: TopAbs_Orientation) -> None: ...
    @staticmethod
    def SameSide(Or: TopAbs_Orientation, OrSave1: TopAbs_Orientation, OrSave2: TopAbs_Orientation, OrFace1: TopAbs_Orientation, OrFace2: TopAbs_Orientation) -> bool: ...

class ChFi3d_Builder:
    def Abscissa(self, IC: int, V: TopoDS_Vertex) -> float: ...
    def BadShape(self) -> TopoDS_Shape: ...
    def Builder(self) -> TopOpeBRepBuild_HBuilder: ...
    def Closed(self, IC: int) -> bool: ...
    def ClosedAndTangent(self, IC: int) -> bool: ...
    def Compute(self) -> None: ...
    def ComputedSurface(self, IC: int, IS: int) -> Geom_Surface: ...
    @overload
    def Contains(self, E: TopoDS_Edge) -> int: ...
    @overload
    def Contains(self, E: TopoDS_Edge) -> Tuple[int, int]: ...
    def FaultyContour(self, I: int) -> int: ...
    def FaultyVertex(self, IV: int) -> TopoDS_Vertex: ...
    def FirstVertex(self, IC: int) -> TopoDS_Vertex: ...
    def Generated(self, EouV: TopoDS_Shape) -> TopTools_ListOfShape: ...
    def HasResult(self) -> bool: ...
    def IsDone(self) -> bool: ...
    def LastVertex(self, IC: int) -> TopoDS_Vertex: ...
    def Length(self, IC: int) -> float: ...
    def NbComputedSurfaces(self, IC: int) -> int: ...
    def NbElements(self) -> int: ...
    def NbFaultyContours(self) -> int: ...
    def NbFaultyVertices(self) -> int: ...
    def PerformTwoCornerbyInter(self, Index: int) -> bool: ...
    def RelativeAbscissa(self, IC: int, V: TopoDS_Vertex) -> float: ...
    def Remove(self, E: TopoDS_Edge) -> None: ...
    def Reset(self) -> None: ...
    def SetContinuity(self, InternalContinuity: GeomAbs_Shape, AngularTolerance: float) -> None: ...
    def SetParams(self, Tang: float, Tesp: float, T2d: float, TApp3d: float, TolApp2d: float, Fleche: float) -> None: ...
    def Shape(self) -> TopoDS_Shape: ...
    def SplitKPart(self, Data: ChFiDS_SurfData, SetData: ChFiDS_SequenceOfSurfData, Spine: ChFiDS_Spine, Iedge: int, S1: Adaptor3d_Surface, I1: Adaptor3d_TopolTool, S2: Adaptor3d_Surface, I2: Adaptor3d_TopolTool) -> Tuple[bool, bool, bool]: ...
    def StripeStatus(self, IC: int) -> ChFiDS_ErrorStatus: ...
    def Value(self, I: int) -> ChFiDS_Spine: ...

class ChFi3d_SearchSing(math_FunctionWithDerivative):
    def __init__(self, C1: Geom_Curve, C2: Geom_Curve) -> None: ...
    def Derivative(self, X: float) -> Tuple[bool, float]: ...
    def Value(self, X: float) -> Tuple[bool, float]: ...
    def Values(self, X: float) -> Tuple[bool, float, float]: ...

class ChFi3d_ChBuilder(ChFi3d_Builder):
    def __init__(self, S: TopoDS_Shape, Ta: Optional[float] = 1.0e-2) -> None: ...
    @overload
    def Add(self, E: TopoDS_Edge) -> None: ...
    @overload
    def Add(self, Dis: float, E: TopoDS_Edge) -> None: ...
    @overload
    def Add(self, Dis1: float, Dis2: float, E: TopoDS_Edge, F: TopoDS_Face) -> None: ...
    def AddDA(self, Dis: float, Angle: float, E: TopoDS_Edge, F: TopoDS_Face) -> None: ...
    def Dists(self, IC: int) -> Tuple[float, float]: ...
    def GetDist(self, IC: int) -> float: ...
    def GetDistAngle(self, IC: int) -> Tuple[float, float]: ...
    def IsChamfer(self, IC: int) -> ChFiDS_ChamfMethod: ...
    def Mode(self) -> ChFiDS_ChamfMode: ...
    def NbSurf(self, IC: int) -> int: ...
    @overload
    def PerformSurf(self, Data: ChFiDS_SequenceOfSurfData, Guide: ChFiDS_ElSpine, Spine: ChFiDS_Spine, Choix: int, S1: BRepAdaptor_Surface, I1: Adaptor3d_TopolTool, S2: BRepAdaptor_Surface, I2: Adaptor3d_TopolTool, MaxStep: float, Fleche: float, TolGuide: float, Inside: bool, Appro: bool, Forward: bool, RecOnS1: bool, RecOnS2: bool, Soldep: math_Vector) -> Tuple[bool, float, float, int, int]: ...
    @overload
    def PerformSurf(self, Data: ChFiDS_SequenceOfSurfData, Guide: ChFiDS_ElSpine, Spine: ChFiDS_Spine, Choix: int, S1: BRepAdaptor_Surface, I1: Adaptor3d_TopolTool, PC1: BRepAdaptor_Curve2d, Sref1: BRepAdaptor_Surface, PCref1: BRepAdaptor_Curve2d, S2: BRepAdaptor_Surface, I2: Adaptor3d_TopolTool, Or2: TopAbs_Orientation, MaxStep: float, Fleche: float, TolGuide: float, Inside: bool, Appro: bool, Forward: bool, RecP: bool, RecS: bool, RecRst: bool, Soldep: math_Vector) -> Tuple[bool, float, float]: ...
    @overload
    def PerformSurf(self, Data: ChFiDS_SequenceOfSurfData, Guide: ChFiDS_ElSpine, Spine: ChFiDS_Spine, Choix: int, S1: BRepAdaptor_Surface, I1: Adaptor3d_TopolTool, Or1: TopAbs_Orientation, S2: BRepAdaptor_Surface, I2: Adaptor3d_TopolTool, PC2: BRepAdaptor_Curve2d, Sref2: BRepAdaptor_Surface, PCref2: BRepAdaptor_Curve2d, MaxStep: float, Fleche: float, TolGuide: float, Inside: bool, Appro: bool, Forward: bool, RecP: bool, RecS: bool, RecRst: bool, Soldep: math_Vector) -> Tuple[bool, float, float]: ...
    @overload
    def PerformSurf(self, Data: ChFiDS_SequenceOfSurfData, Guide: ChFiDS_ElSpine, Spine: ChFiDS_Spine, Choix: int, S1: BRepAdaptor_Surface, I1: Adaptor3d_TopolTool, PC1: BRepAdaptor_Curve2d, Sref1: BRepAdaptor_Surface, PCref1: BRepAdaptor_Curve2d, Or1: TopAbs_Orientation, S2: BRepAdaptor_Surface, I2: Adaptor3d_TopolTool, PC2: BRepAdaptor_Curve2d, Sref2: BRepAdaptor_Surface, PCref2: BRepAdaptor_Curve2d, Or2: TopAbs_Orientation, MaxStep: float, Fleche: float, TolGuide: float, Inside: bool, Appro: bool, Forward: bool, RecP1: bool, RecRst1: bool, RecP2: bool, RecRst2: bool, Soldep: math_Vector) -> Tuple[bool, bool, float, float]: ...
    def ResetContour(self, IC: int) -> None: ...
    def Sect(self, IC: int, IS: int) -> ChFiDS_SecHArray1: ...
    def SetDist(self, Dis: float, IC: int, F: TopoDS_Face) -> None: ...
    def SetDistAngle(self, Dis: float, Angle: float, IC: int, F: TopoDS_Face) -> None: ...
    def SetDists(self, Dis1: float, Dis2: float, IC: int, F: TopoDS_Face) -> None: ...
    def SetMode(self, theMode: ChFiDS_ChamfMode) -> None: ...
    @overload
    def SimulSurf(self, Data: ChFiDS_SurfData, Guide: ChFiDS_ElSpine, Spine: ChFiDS_Spine, Choix: int, S1: BRepAdaptor_Surface, I1: Adaptor3d_TopolTool, PC1: BRepAdaptor_Curve2d, Sref1: BRepAdaptor_Surface, PCref1: BRepAdaptor_Curve2d, S2: BRepAdaptor_Surface, I2: Adaptor3d_TopolTool, Or2: TopAbs_Orientation, Fleche: float, TolGuide: float, Inside: bool, Appro: bool, Forward: bool, RecP: bool, RecS: bool, RecRst: bool, Soldep: math_Vector) -> Tuple[bool, float, float]: ...
    @overload
    def SimulSurf(self, Data: ChFiDS_SurfData, Guide: ChFiDS_ElSpine, Spine: ChFiDS_Spine, Choix: int, S1: BRepAdaptor_Surface, I1: Adaptor3d_TopolTool, Or1: TopAbs_Orientation, S2: BRepAdaptor_Surface, I2: Adaptor3d_TopolTool, PC2: BRepAdaptor_Curve2d, Sref2: BRepAdaptor_Surface, PCref2: BRepAdaptor_Curve2d, Fleche: float, TolGuide: float, Inside: bool, Appro: bool, Forward: bool, RecP: bool, RecS: bool, RecRst: bool, Soldep: math_Vector) -> Tuple[bool, float, float]: ...
    @overload
    def SimulSurf(self, Data: ChFiDS_SurfData, Guide: ChFiDS_ElSpine, Spine: ChFiDS_Spine, Choix: int, S1: BRepAdaptor_Surface, I1: Adaptor3d_TopolTool, PC1: BRepAdaptor_Curve2d, Sref1: BRepAdaptor_Surface, PCref1: BRepAdaptor_Curve2d, Or1: TopAbs_Orientation, S2: BRepAdaptor_Surface, I2: Adaptor3d_TopolTool, PC2: BRepAdaptor_Curve2d, Sref2: BRepAdaptor_Surface, PCref2: BRepAdaptor_Curve2d, Or2: TopAbs_Orientation, Fleche: float, TolGuide: float, Inside: bool, Appro: bool, Forward: bool, RecP1: bool, RecRst1: bool, RecP2: bool, RecRst2: bool, Soldep: math_Vector) -> Tuple[bool, bool, float, float]: ...
    def Simulate(self, IC: int) -> None: ...

class ChFi3d_FilBuilder(ChFi3d_Builder):
    def __init__(self, S: TopoDS_Shape, FShape: Optional[ChFi3d_FilletShape] = ChFi3d_Rational, Ta: Optional[float] = 1.0e-2) -> None: ...
    @overload
    def Add(self, E: TopoDS_Edge) -> None: ...
    @overload
    def Add(self, Radius: float, E: TopoDS_Edge) -> None: ...
    def GetBounds(self, IC: int, E: TopoDS_Edge) -> Tuple[bool, float, float]: ...
    def GetFilletShape(self) -> ChFi3d_FilletShape: ...
    def GetLaw(self, IC: int, E: TopoDS_Edge) -> Law_Function: ...
    @overload
    def IsConstant(self, IC: int) -> bool: ...
    @overload
    def IsConstant(self, IC: int, E: TopoDS_Edge) -> bool: ...
    def NbSurf(self, IC: int) -> int: ...
    @overload
    def Radius(self, IC: int) -> float: ...
    @overload
    def Radius(self, IC: int, E: TopoDS_Edge) -> float: ...
    def ResetContour(self, IC: int) -> None: ...
    def Sect(self, IC: int, IS: int) -> ChFiDS_SecHArray1: ...
    def SetFilletShape(self, FShape: ChFi3d_FilletShape) -> None: ...
    def SetLaw(self, IC: int, E: TopoDS_Edge, L: Law_Function) -> None: ...
    @overload
    def SetRadius(self, C: Law_Function, IC: int, IinC: int) -> None: ...
    @overload
    def SetRadius(self, Radius: float, IC: int, E: TopoDS_Edge) -> None: ...
    @overload
    def SetRadius(self, Radius: float, IC: int, V: TopoDS_Vertex) -> None: ...
    @overload
    def SetRadius(self, UandR: gp_XY, IC: int, IinC: int) -> None: ...
    def Simulate(self, IC: int) -> None: ...
    @overload
    def UnSet(self, IC: int, E: TopoDS_Edge) -> None: ...
    @overload
    def UnSet(self, IC: int, V: TopoDS_Vertex) -> None: ...

# harray1 classes
# harray2 classes
# hsequence classes

