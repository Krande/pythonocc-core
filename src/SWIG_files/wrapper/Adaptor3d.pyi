from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.Geom import *
from OCC.Core.gp import *
from OCC.Core.GeomAbs import *
from OCC.Core.TColStd import *
from OCC.Core.TopAbs import *
from OCC.Core.Adaptor2d import *
from OCC.Core.math import *


class Adaptor3d_Curve(Standard_Transient):
    def BSpline(self) -> Geom_BSplineCurve: ...
    def Bezier(self) -> Geom_BezierCurve: ...
    def Circle(self) -> gp_Circ: ...
    def Continuity(self) -> GeomAbs_Shape: ...
    def D0(self, U: float, P: gp_Pnt) -> None: ...
    def D1(self, U: float, P: gp_Pnt, V: gp_Vec) -> None: ...
    def D2(self, U: float, P: gp_Pnt, V1: gp_Vec, V2: gp_Vec) -> None: ...
    def D3(self, U: float, P: gp_Pnt, V1: gp_Vec, V2: gp_Vec, V3: gp_Vec) -> None: ...
    def DN(self, U: float, N: int) -> gp_Vec: ...
    def Degree(self) -> int: ...
    def Ellipse(self) -> gp_Elips: ...
    def FirstParameter(self) -> float: ...
    def GetType(self) -> GeomAbs_CurveType: ...
    def Hyperbola(self) -> gp_Hypr: ...
    def Intervals(self, T: TColStd_Array1OfReal, S: GeomAbs_Shape) -> None: ...
    def IsClosed(self) -> bool: ...
    def IsPeriodic(self) -> bool: ...
    def IsRational(self) -> bool: ...
    def LastParameter(self) -> float: ...
    def Line(self) -> gp_Lin: ...
    def NbIntervals(self, S: GeomAbs_Shape) -> int: ...
    def NbKnots(self) -> int: ...
    def NbPoles(self) -> int: ...
    def OffsetCurve(self) -> Geom_OffsetCurve: ...
    def Parabola(self) -> gp_Parab: ...
    def Period(self) -> float: ...
    def Resolution(self, R3d: float) -> float: ...
    def Trim(self, First: float, Last: float, Tol: float) -> Adaptor3d_Curve: ...
    def Value(self, U: float) -> gp_Pnt: ...

class Adaptor3d_HSurfaceTool:
    @staticmethod
    def AxeOfRevolution(theSurf: Adaptor3d_Surface) -> gp_Ax1: ...
    @staticmethod
    def BSpline(theSurf: Adaptor3d_Surface) -> Geom_BSplineSurface: ...
    @staticmethod
    def BasisCurve(theSurf: Adaptor3d_Surface) -> Adaptor3d_Curve: ...
    @staticmethod
    def BasisSurface(theSurf: Adaptor3d_Surface) -> Adaptor3d_Surface: ...
    @staticmethod
    def Bezier(theSurf: Adaptor3d_Surface) -> Geom_BezierSurface: ...
    @staticmethod
    def Cone(theSurf: Adaptor3d_Surface) -> gp_Cone: ...
    @staticmethod
    def Cylinder(theSurf: Adaptor3d_Surface) -> gp_Cylinder: ...
    @staticmethod
    def D0(theSurf: Adaptor3d_Surface, theU: float, theV: float, thePnt: gp_Pnt) -> None: ...
    @staticmethod
    def D1(theSurf: Adaptor3d_Surface, theU: float, theV: float, thePnt: gp_Pnt, theD1U: gp_Vec, theD1V: gp_Vec) -> None: ...
    @staticmethod
    def D2(theSurf: Adaptor3d_Surface, theU: float, theV: float, thePnt: gp_Pnt, theD1U: gp_Vec, theD1V: gp_Vec, theD2U: gp_Vec, theD2V: gp_Vec, theD2UV: gp_Vec) -> None: ...
    @staticmethod
    def D3(theSurf: Adaptor3d_Surface, theU: float, theV: float, thePnt: gp_Pnt, theD1U: gp_Vec, theD1V: gp_Vec, theD2U: gp_Vec, theD2V: gp_Vec, theD2UV: gp_Vec, theD3U: gp_Vec, theD3V: gp_Vec, theD3UUV: gp_Vec, theD3UVV: gp_Vec) -> None: ...
    @staticmethod
    def DN(theSurf: Adaptor3d_Surface, theU: float, theV: float, theNU: int, theNV: int) -> gp_Vec: ...
    @staticmethod
    def Direction(theSurf: Adaptor3d_Surface) -> gp_Dir: ...
    @staticmethod
    def FirstUParameter(theSurf: Adaptor3d_Surface) -> float: ...
    @staticmethod
    def FirstVParameter(theSurf: Adaptor3d_Surface) -> float: ...
    @staticmethod
    def GetType(theSurf: Adaptor3d_Surface) -> GeomAbs_SurfaceType: ...
    @staticmethod
    def IsSurfG1(theSurf: Adaptor3d_Surface, theAlongU: bool, theAngTol: Optional[float] = Precision.Angular()) -> bool: ...
    @staticmethod
    def IsUClosed(theSurf: Adaptor3d_Surface) -> bool: ...
    @staticmethod
    def IsUPeriodic(theSurf: Adaptor3d_Surface) -> bool: ...
    @staticmethod
    def IsVClosed(theSurf: Adaptor3d_Surface) -> bool: ...
    @staticmethod
    def IsVPeriodic(theSurf: Adaptor3d_Surface) -> bool: ...
    @staticmethod
    def LastUParameter(theSurf: Adaptor3d_Surface) -> float: ...
    @staticmethod
    def LastVParameter(theSurf: Adaptor3d_Surface) -> float: ...
    @overload
    @staticmethod
    def NbSamplesU(S: Adaptor3d_Surface) -> int: ...
    @overload
    @staticmethod
    def NbSamplesU(S: Adaptor3d_Surface, u1: float, u2: float) -> int: ...
    @overload
    @staticmethod
    def NbSamplesV(S: Adaptor3d_Surface) -> int: ...
    @staticmethod
    def NbUIntervals(theSurf: Adaptor3d_Surface, theSh: GeomAbs_Shape) -> int: ...
    @staticmethod
    def NbVIntervals(theSurf: Adaptor3d_Surface, theSh: GeomAbs_Shape) -> int: ...
    @staticmethod
    def OffsetValue(theSurf: Adaptor3d_Surface) -> float: ...
    @staticmethod
    def Plane(theSurf: Adaptor3d_Surface) -> gp_Pln: ...
    @staticmethod
    def Sphere(theSurf: Adaptor3d_Surface) -> gp_Sphere: ...
    @staticmethod
    def Torus(theSurf: Adaptor3d_Surface) -> gp_Torus: ...
    @staticmethod
    def UIntervals(theSurf: Adaptor3d_Surface, theTab: TColStd_Array1OfReal, theSh: GeomAbs_Shape) -> None: ...
    @staticmethod
    def UPeriod(theSurf: Adaptor3d_Surface) -> float: ...
    @staticmethod
    def UResolution(theSurf: Adaptor3d_Surface, theR3d: float) -> float: ...
    @staticmethod
    def UTrim(theSurf: Adaptor3d_Surface, theFirst: float, theLast: float, theTol: float) -> Adaptor3d_Surface: ...
    @staticmethod
    def VIntervals(theSurf: Adaptor3d_Surface, theTab: TColStd_Array1OfReal, theSh: GeomAbs_Shape) -> None: ...
    @staticmethod
    def VPeriod(theSurf: Adaptor3d_Surface) -> float: ...
    @staticmethod
    def VResolution(theSurf: Adaptor3d_Surface, theR3d: float) -> float: ...
    @staticmethod
    def VTrim(theSurf: Adaptor3d_Surface, theFirst: float, theLast: float, theTol: float) -> Adaptor3d_Surface: ...
    @staticmethod
    def Value(theSurf: Adaptor3d_Surface, theU: float, theV: float) -> gp_Pnt: ...

class Adaptor3d_HVertex(Standard_Transient):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, P: gp_Pnt2d, Ori: TopAbs_Orientation, Resolution: float) -> None: ...
    def IsSame(self, Other: Adaptor3d_HVertex) -> bool: ...
    def Orientation(self) -> TopAbs_Orientation: ...
    def Parameter(self, C: Adaptor2d_Curve2d) -> float: ...
    def Resolution(self, C: Adaptor2d_Curve2d) -> float: ...
    def Value(self) -> gp_Pnt2d: ...

class Adaptor3d_InterFunc(math_FunctionWithDerivative):
    def __init__(self, C: Adaptor2d_Curve2d, FixVal: float, Fix: int) -> None: ...
    def Derivative(self, X: float) -> Tuple[bool, float]: ...
    def Value(self, X: float) -> Tuple[bool, float]: ...
    def Values(self, X: float) -> Tuple[bool, float, float]: ...

class Adaptor3d_Surface(Standard_Transient):
    def AxeOfRevolution(self) -> gp_Ax1: ...
    def BSpline(self) -> Geom_BSplineSurface: ...
    def BasisCurve(self) -> Adaptor3d_Curve: ...
    def BasisSurface(self) -> Adaptor3d_Surface: ...
    def Bezier(self) -> Geom_BezierSurface: ...
    def Cone(self) -> gp_Cone: ...
    def Cylinder(self) -> gp_Cylinder: ...
    def D0(self, U: float, V: float, P: gp_Pnt) -> None: ...
    def D1(self, U: float, V: float, P: gp_Pnt, D1U: gp_Vec, D1V: gp_Vec) -> None: ...
    def D2(self, U: float, V: float, P: gp_Pnt, D1U: gp_Vec, D1V: gp_Vec, D2U: gp_Vec, D2V: gp_Vec, D2UV: gp_Vec) -> None: ...
    def D3(self, U: float, V: float, P: gp_Pnt, D1U: gp_Vec, D1V: gp_Vec, D2U: gp_Vec, D2V: gp_Vec, D2UV: gp_Vec, D3U: gp_Vec, D3V: gp_Vec, D3UUV: gp_Vec, D3UVV: gp_Vec) -> None: ...
    def DN(self, U: float, V: float, Nu: int, Nv: int) -> gp_Vec: ...
    def Direction(self) -> gp_Dir: ...
    def FirstUParameter(self) -> float: ...
    def FirstVParameter(self) -> float: ...
    def GetType(self) -> GeomAbs_SurfaceType: ...
    def IsUClosed(self) -> bool: ...
    def IsUPeriodic(self) -> bool: ...
    def IsURational(self) -> bool: ...
    def IsVClosed(self) -> bool: ...
    def IsVPeriodic(self) -> bool: ...
    def IsVRational(self) -> bool: ...
    def LastUParameter(self) -> float: ...
    def LastVParameter(self) -> float: ...
    def NbUIntervals(self, S: GeomAbs_Shape) -> int: ...
    def NbUKnots(self) -> int: ...
    def NbUPoles(self) -> int: ...
    def NbVIntervals(self, S: GeomAbs_Shape) -> int: ...
    def NbVKnots(self) -> int: ...
    def NbVPoles(self) -> int: ...
    def OffsetValue(self) -> float: ...
    def Plane(self) -> gp_Pln: ...
    def Sphere(self) -> gp_Sphere: ...
    def Torus(self) -> gp_Torus: ...
    def UContinuity(self) -> GeomAbs_Shape: ...
    def UDegree(self) -> int: ...
    def UIntervals(self, T: TColStd_Array1OfReal, S: GeomAbs_Shape) -> None: ...
    def UPeriod(self) -> float: ...
    def UResolution(self, R3d: float) -> float: ...
    def UTrim(self, First: float, Last: float, Tol: float) -> Adaptor3d_Surface: ...
    def VContinuity(self) -> GeomAbs_Shape: ...
    def VDegree(self) -> int: ...
    def VIntervals(self, T: TColStd_Array1OfReal, S: GeomAbs_Shape) -> None: ...
    def VPeriod(self) -> float: ...
    def VResolution(self, R3d: float) -> float: ...
    def VTrim(self, First: float, Last: float, Tol: float) -> Adaptor3d_Surface: ...
    def Value(self, U: float, V: float) -> gp_Pnt: ...

class Adaptor3d_TopolTool(Standard_Transient):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, Surface: Adaptor3d_Surface) -> None: ...
    def BSplSamplePnts(self, theDefl: float, theNUmin: int, theNVmin: int) -> None: ...
    def Classify(self, P: gp_Pnt2d, Tol: float, ReacdreOnPeriodic: Optional[bool] = True) -> TopAbs_State: ...
    def ComputeSamplePoints(self) -> None: ...
    def DomainIsInfinite(self) -> bool: ...
    def Edge(self) -> None: ...
    @staticmethod
    def GetConeApexParam(theC: gp_Cone) -> Tuple[float, float]: ...
    def Has3d(self) -> bool: ...
    def Identical(self, V1: Adaptor3d_HVertex, V2: Adaptor3d_HVertex) -> bool: ...
    def Init(self) -> None: ...
    def InitVertexIterator(self) -> None: ...
    @overload
    def Initialize(self) -> None: ...
    @overload
    def Initialize(self, S: Adaptor3d_Surface) -> None: ...
    @overload
    def Initialize(self, Curve: Adaptor2d_Curve2d) -> None: ...
    def IsThePointOn(self, P: gp_Pnt2d, Tol: float, ReacdreOnPeriodic: Optional[bool] = True) -> bool: ...
    def IsUniformSampling(self) -> bool: ...
    def More(self) -> bool: ...
    def MoreVertex(self) -> bool: ...
    def NbSamples(self) -> int: ...
    def NbSamplesU(self) -> int: ...
    def NbSamplesV(self) -> int: ...
    def Next(self) -> None: ...
    def NextVertex(self) -> None: ...
    @overload
    def Orientation(self, C: Adaptor2d_Curve2d) -> TopAbs_Orientation: ...
    @overload
    def Orientation(self, V: Adaptor3d_HVertex) -> TopAbs_Orientation: ...
    def Pnt(self, V: Adaptor3d_HVertex) -> gp_Pnt: ...
    def SamplePnts(self, theDefl: float, theNUmin: int, theNVmin: int) -> None: ...
    def SamplePoint(self, Index: int, P2d: gp_Pnt2d, P3d: gp_Pnt) -> None: ...
    @overload
    def Tol3d(self, C: Adaptor2d_Curve2d) -> float: ...
    @overload
    def Tol3d(self, V: Adaptor3d_HVertex) -> float: ...
    def UParameters(self, theArray: TColStd_Array1OfReal) -> None: ...
    def VParameters(self, theArray: TColStd_Array1OfReal) -> None: ...
    def Value(self) -> Adaptor2d_Curve2d: ...
    def Vertex(self) -> Adaptor3d_HVertex: ...

class Adaptor3d_CurveOnSurface(Adaptor3d_Curve):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, S: Adaptor3d_Surface) -> None: ...
    @overload
    def __init__(self, C: Adaptor2d_Curve2d, S: Adaptor3d_Surface) -> None: ...
    def BSpline(self) -> Geom_BSplineCurve: ...
    def Bezier(self) -> Geom_BezierCurve: ...
    def ChangeCurve(self) -> Adaptor2d_Curve2d: ...
    def ChangeSurface(self) -> Adaptor3d_Surface: ...
    def Circle(self) -> gp_Circ: ...
    def Continuity(self) -> GeomAbs_Shape: ...
    def D0(self, U: float, P: gp_Pnt) -> None: ...
    def D1(self, U: float, P: gp_Pnt, V: gp_Vec) -> None: ...
    def D2(self, U: float, P: gp_Pnt, V1: gp_Vec, V2: gp_Vec) -> None: ...
    def D3(self, U: float, P: gp_Pnt, V1: gp_Vec, V2: gp_Vec, V3: gp_Vec) -> None: ...
    def DN(self, U: float, N: int) -> gp_Vec: ...
    def Degree(self) -> int: ...
    def Ellipse(self) -> gp_Elips: ...
    def FirstParameter(self) -> float: ...
    def GetCurve(self) -> Adaptor2d_Curve2d: ...
    def GetSurface(self) -> Adaptor3d_Surface: ...
    def GetType(self) -> GeomAbs_CurveType: ...
    def Hyperbola(self) -> gp_Hypr: ...
    def Intervals(self, T: TColStd_Array1OfReal, S: GeomAbs_Shape) -> None: ...
    def IsClosed(self) -> bool: ...
    def IsPeriodic(self) -> bool: ...
    def IsRational(self) -> bool: ...
    def LastParameter(self) -> float: ...
    def Line(self) -> gp_Lin: ...
    @overload
    def Load(self, S: Adaptor3d_Surface) -> None: ...
    @overload
    def Load(self, C: Adaptor2d_Curve2d) -> None: ...
    @overload
    def Load(self, C: Adaptor2d_Curve2d, S: Adaptor3d_Surface) -> None: ...
    def NbIntervals(self, S: GeomAbs_Shape) -> int: ...
    def NbKnots(self) -> int: ...
    def NbPoles(self) -> int: ...
    def Parabola(self) -> gp_Parab: ...
    def Period(self) -> float: ...
    def Resolution(self, R3d: float) -> float: ...
    def Trim(self, First: float, Last: float, Tol: float) -> Adaptor3d_Curve: ...
    def Value(self, U: float) -> gp_Pnt: ...

class Adaptor3d_IsoCurve(Adaptor3d_Curve):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, S: Adaptor3d_Surface) -> None: ...
    @overload
    def __init__(self, S: Adaptor3d_Surface, Iso: GeomAbs_IsoType, Param: float) -> None: ...
    @overload
    def __init__(self, S: Adaptor3d_Surface, Iso: GeomAbs_IsoType, Param: float, WFirst: float, WLast: float) -> None: ...
    def BSpline(self) -> Geom_BSplineCurve: ...
    def Bezier(self) -> Geom_BezierCurve: ...
    def Circle(self) -> gp_Circ: ...
    def Continuity(self) -> GeomAbs_Shape: ...
    def D0(self, U: float, P: gp_Pnt) -> None: ...
    def D1(self, U: float, P: gp_Pnt, V: gp_Vec) -> None: ...
    def D2(self, U: float, P: gp_Pnt, V1: gp_Vec, V2: gp_Vec) -> None: ...
    def D3(self, U: float, P: gp_Pnt, V1: gp_Vec, V2: gp_Vec, V3: gp_Vec) -> None: ...
    def DN(self, U: float, N: int) -> gp_Vec: ...
    def Degree(self) -> int: ...
    def Ellipse(self) -> gp_Elips: ...
    def FirstParameter(self) -> float: ...
    def GetType(self) -> GeomAbs_CurveType: ...
    def Hyperbola(self) -> gp_Hypr: ...
    def Intervals(self, T: TColStd_Array1OfReal, S: GeomAbs_Shape) -> None: ...
    def IsClosed(self) -> bool: ...
    def IsPeriodic(self) -> bool: ...
    def IsRational(self) -> bool: ...
    def Iso(self) -> GeomAbs_IsoType: ...
    def LastParameter(self) -> float: ...
    def Line(self) -> gp_Lin: ...
    @overload
    def Load(self, S: Adaptor3d_Surface) -> None: ...
    @overload
    def Load(self, Iso: GeomAbs_IsoType, Param: float) -> None: ...
    @overload
    def Load(self, Iso: GeomAbs_IsoType, Param: float, WFirst: float, WLast: float) -> None: ...
    def NbIntervals(self, S: GeomAbs_Shape) -> int: ...
    def NbKnots(self) -> int: ...
    def NbPoles(self) -> int: ...
    def Parabola(self) -> gp_Parab: ...
    def Parameter(self) -> float: ...
    def Period(self) -> float: ...
    def Resolution(self, R3d: float) -> float: ...
    def Surface(self) -> Adaptor3d_Surface: ...
    def Trim(self, First: float, Last: float, Tol: float) -> Adaptor3d_Curve: ...
    def Value(self, U: float) -> gp_Pnt: ...

# harray1 classes
# harray2 classes
# hsequence classes

