from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.MAT import *
from OCC.Core.TopTools import *
from OCC.Core.TopoDS import *
from OCC.Core.gp import *
from OCC.Core.TColStd import *
from OCC.Core.Geom import *
from OCC.Core.Geom2d import *
from OCC.Core.AppParCurves import *
from OCC.Core.GeomPlate import *
from OCC.Core.Adaptor3d import *
from OCC.Core.GeomAbs import *
from OCC.Core.GeomFill import *
from OCC.Core.AppCont import *
from OCC.Core.BRepMAT2d import *
from OCC.Core.Law import *
from OCC.Core.Bisector import *
from OCC.Core.TColgp import *

#the following typedef cannot be wrapped as is
BRepFill_IndexedDataMapOfOrientedShapeListOfShape = NewType('BRepFill_IndexedDataMapOfOrientedShapeListOfShape', Any)

class BRepFill_ListOfOffsetWire:
    def __init__(self) -> None: ...
    def __len__(self) -> int: ...
    def Size(self) -> int: ...
    def Clear(self) -> None: ...
    def First(self) -> BRepFill_OffsetWire: ...
    def Last(self) -> BRepFill_OffsetWire: ...
    def Append(self, theItem: BRepFill_OffsetWire) -> BRepFill_OffsetWire: ...
    def Prepend(self, theItem: BRepFill_OffsetWire) -> BRepFill_OffsetWire: ...
    def RemoveFirst(self) -> None: ...
    def Reverse(self) -> None: ...
    def Value(self, theIndex: int) -> BRepFill_OffsetWire: ...
    def SetValue(self, theIndex: int, theValue: BRepFill_OffsetWire) -> None: ...

class BRepFill_SequenceOfEdgeFaceAndOrder:
    def __init__(self) -> None: ...
    def __len__(self) -> int: ...
    def Size(self) -> int: ...
    def Clear(self) -> None: ...
    def First(self) -> BRepFill_EdgeFaceAndOrder: ...
    def Last(self) -> BRepFill_EdgeFaceAndOrder: ...
    def Length(self) -> int: ...
    def Append(self, theItem: BRepFill_EdgeFaceAndOrder) -> BRepFill_EdgeFaceAndOrder: ...
    def Prepend(self, theItem: BRepFill_EdgeFaceAndOrder) -> BRepFill_EdgeFaceAndOrder: ...
    def RemoveFirst(self) -> None: ...
    def Reverse(self) -> None: ...
    def Value(self, theIndex: int) -> BRepFill_EdgeFaceAndOrder: ...
    def SetValue(self, theIndex: int, theValue: BRepFill_EdgeFaceAndOrder) -> None: ...

class BRepFill_SequenceOfFaceAndOrder:
    def __init__(self) -> None: ...
    def __len__(self) -> int: ...
    def Size(self) -> int: ...
    def Clear(self) -> None: ...
    def First(self) -> BRepFill_FaceAndOrder: ...
    def Last(self) -> BRepFill_FaceAndOrder: ...
    def Length(self) -> int: ...
    def Append(self, theItem: BRepFill_FaceAndOrder) -> BRepFill_FaceAndOrder: ...
    def Prepend(self, theItem: BRepFill_FaceAndOrder) -> BRepFill_FaceAndOrder: ...
    def RemoveFirst(self) -> None: ...
    def Reverse(self) -> None: ...
    def Value(self, theIndex: int) -> BRepFill_FaceAndOrder: ...
    def SetValue(self, theIndex: int, theValue: BRepFill_FaceAndOrder) -> None: ...

class BRepFill_SequenceOfSection:
    def __init__(self) -> None: ...
    def __len__(self) -> int: ...
    def Size(self) -> int: ...
    def Clear(self) -> None: ...
    def First(self) -> BRepFill_Section: ...
    def Last(self) -> BRepFill_Section: ...
    def Length(self) -> int: ...
    def Append(self, theItem: BRepFill_Section) -> BRepFill_Section: ...
    def Prepend(self, theItem: BRepFill_Section) -> BRepFill_Section: ...
    def RemoveFirst(self) -> None: ...
    def Reverse(self) -> None: ...
    def Value(self, theIndex: int) -> BRepFill_Section: ...
    def SetValue(self, theIndex: int, theValue: BRepFill_Section) -> None: ...

class BRepFill_TransitionStyle(IntEnum):
    BRepFill_Modified: int = ...
    BRepFill_Right: int = ...
    BRepFill_Round: int = ...

BRepFill_Modified = BRepFill_TransitionStyle.BRepFill_Modified
BRepFill_Right = BRepFill_TransitionStyle.BRepFill_Right
BRepFill_Round = BRepFill_TransitionStyle.BRepFill_Round

class BRepFill_TypeOfContact(IntEnum):
    BRepFill_NoContact: int = ...
    BRepFill_Contact: int = ...
    BRepFill_ContactOnBorder: int = ...

BRepFill_NoContact = BRepFill_TypeOfContact.BRepFill_NoContact
BRepFill_Contact = BRepFill_TypeOfContact.BRepFill_Contact
BRepFill_ContactOnBorder = BRepFill_TypeOfContact.BRepFill_ContactOnBorder

class brepfill:
    @staticmethod
    def Axe(Spine: TopoDS_Shape, Profile: TopoDS_Wire, AxeProf: gp_Ax3, Tol: float) -> bool: ...
    @staticmethod
    def ComputeACR(wire: TopoDS_Wire, ACR: TColStd_Array1OfReal) -> None: ...
    @staticmethod
    def Face(Edge1: TopoDS_Edge, Edge2: TopoDS_Edge) -> TopoDS_Face: ...
    @staticmethod
    def InsertACR(wire: TopoDS_Wire, ACRcuts: TColStd_Array1OfReal, prec: float) -> TopoDS_Wire: ...
    @staticmethod
    def Shell(Wire1: TopoDS_Wire, Wire2: TopoDS_Wire) -> TopoDS_Shell: ...

class BRepFill_AdvancedEvolved:
    def __init__(self) -> None: ...
    def IsDone(self, theErrorCode: Optional[int] = 0) -> bool: ...
    def Perform(self, theSpine: TopoDS_Wire, theProfile: TopoDS_Wire, theTolerance: float, theSolidReq: Optional[bool] = True) -> None: ...
    def SetParallelMode(self, theVal: bool) -> None: ...
    def SetTemporaryDirectory(self, thePath: str) -> None: ...
    def Shape(self) -> TopoDS_Shape: ...

class BRepFill_ApproxSeewing:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, ML: BRepFill_MultiLine) -> None: ...
    def Curve(self) -> Geom_Curve: ...
    def CurveOnF1(self) -> Geom2d_Curve: ...
    def CurveOnF2(self) -> Geom2d_Curve: ...
    def IsDone(self) -> bool: ...
    def Perform(self, ML: BRepFill_MultiLine) -> None: ...

class BRepFill_CompatibleWires:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, Sections: TopTools_SequenceOfShape) -> None: ...
    def Generated(self) -> TopTools_DataMapOfShapeListOfShape: ...
    def GeneratedShapes(self, SubSection: TopoDS_Edge) -> TopTools_ListOfShape: ...
    def Init(self, Sections: TopTools_SequenceOfShape) -> None: ...
    def IsDegeneratedFirstSection(self) -> bool: ...
    def IsDegeneratedLastSection(self) -> bool: ...
    def IsDone(self) -> bool: ...
    def Perform(self, WithRotation: Optional[bool] = True) -> None: ...
    def SetPercent(self, percent: Optional[float] = 0.01) -> None: ...
    def Shape(self) -> TopTools_SequenceOfShape: ...

class BRepFill_ComputeCLine:
    @overload
    def __init__(self, Line: BRepFill_MultiLine, degreemin: Optional[int] = 3, degreemax: Optional[int] = 8, Tolerance3d: Optional[float] = 1.0e-5, Tolerance2d: Optional[float] = 1.0e-5, cutting: Optional[bool] = False, FirstC: Optional[AppParCurves_Constraint] = AppParCurves_TangencyPoint, LastC: Optional[AppParCurves_Constraint] = AppParCurves_TangencyPoint) -> None: ...
    @overload
    def __init__(self, degreemin: Optional[int] = 3, degreemax: Optional[int] = 8, Tolerance3d: Optional[float] = 1.0e-05, Tolerance2d: Optional[float] = 1.0e-05, cutting: Optional[bool] = False, FirstC: Optional[AppParCurves_Constraint] = AppParCurves_TangencyPoint, LastC: Optional[AppParCurves_Constraint] = AppParCurves_TangencyPoint) -> None: ...
    def Error(self, Index: int) -> Tuple[float, float]: ...
    def IsAllApproximated(self) -> bool: ...
    def IsToleranceReached(self) -> bool: ...
    def NbMultiCurves(self) -> int: ...
    def Parameters(self, Index: int) -> Tuple[float, float]: ...
    def Perform(self, Line: BRepFill_MultiLine) -> None: ...
    def SetConstraints(self, FirstC: AppParCurves_Constraint, LastC: AppParCurves_Constraint) -> None: ...
    def SetDegrees(self, degreemin: int, degreemax: int) -> None: ...
    def SetHangChecking(self, theHangChecking: bool) -> None: ...
    def SetInvOrder(self, theInvOrder: bool) -> None: ...
    def SetMaxSegments(self, theMaxSegments: int) -> None: ...
    def SetTolerances(self, Tolerance3d: float, Tolerance2d: float) -> None: ...
    def Value(self, Index: Optional[int] = 1) -> AppParCurves_MultiCurve: ...

class BRepFill_CurveConstraint(GeomPlate_CurveConstraint):
    @overload
    def __init__(self, Boundary: Adaptor3d_CurveOnSurface, Order: int, NPt: Optional[int] = 10, TolDist: Optional[float] = 0.0001, TolAng: Optional[float] = 0.01, TolCurv: Optional[float] = 0.1) -> None: ...
    @overload
    def __init__(self, Boundary: Adaptor3d_Curve, Tang: int, NPt: Optional[int] = 10, TolDist: Optional[float] = 0.0001) -> None: ...

class BRepFill_Draft:
    def __init__(self, Shape: TopoDS_Shape, Dir: gp_Dir, Angle: float) -> None: ...
    def Generated(self, S: TopoDS_Shape) -> TopTools_ListOfShape: ...
    def IsDone(self) -> bool: ...
    @overload
    def Perform(self, LengthMax: float) -> None: ...
    @overload
    def Perform(self, Surface: Geom_Surface, KeepInsideSurface: Optional[bool] = True) -> None: ...
    @overload
    def Perform(self, StopShape: TopoDS_Shape, KeepOutSide: Optional[bool] = True) -> None: ...
    def SetDraft(self, IsInternal: Optional[bool] = False) -> None: ...
    def SetOptions(self, Style: Optional[BRepFill_TransitionStyle] = BRepFill_Right, AngleMin: Optional[float] = 0.01, AngleMax: Optional[float] = 3.0) -> None: ...
    def Shape(self) -> TopoDS_Shape: ...
    def Shell(self) -> TopoDS_Shell: ...

class BRepFill_EdgeFaceAndOrder:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, anEdge: TopoDS_Edge, aFace: TopoDS_Face, anOrder: GeomAbs_Shape) -> None: ...

class BRepFill_Evolved:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, Spine: TopoDS_Wire, Profile: TopoDS_Wire, AxeProf: gp_Ax3, Join: Optional[GeomAbs_JoinType] = GeomAbs_Arc, Solid: Optional[bool] = False) -> None: ...
    @overload
    def __init__(self, Spine: TopoDS_Face, Profile: TopoDS_Wire, AxeProf: gp_Ax3, Join: Optional[GeomAbs_JoinType] = GeomAbs_Arc, Solid: Optional[bool] = False) -> None: ...
    def Bottom(self) -> TopoDS_Shape: ...
    def GeneratedShapes(self, SpineShape: TopoDS_Shape, ProfShape: TopoDS_Shape) -> TopTools_ListOfShape: ...
    def IsDone(self) -> bool: ...
    def JoinType(self) -> GeomAbs_JoinType: ...
    @overload
    def Perform(self, Spine: TopoDS_Wire, Profile: TopoDS_Wire, AxeProf: gp_Ax3, Join: Optional[GeomAbs_JoinType] = GeomAbs_Arc, Solid: Optional[bool] = False) -> None: ...
    @overload
    def Perform(self, Spine: TopoDS_Face, Profile: TopoDS_Wire, AxeProf: gp_Ax3, Join: Optional[GeomAbs_JoinType] = GeomAbs_Arc, Solid: Optional[bool] = False) -> None: ...
    def Shape(self) -> TopoDS_Shape: ...
    def Top(self) -> TopoDS_Shape: ...

class BRepFill_FaceAndOrder:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, aFace: TopoDS_Face, anOrder: GeomAbs_Shape) -> None: ...

class BRepFill_Filling:
    def __init__(self, Degree: Optional[int] = 3, NbPtsOnCur: Optional[int] = 15, NbIter: Optional[int] = 2, Anisotropie: Optional[bool] = False, Tol2d: Optional[float] = 0.00001, Tol3d: Optional[float] = 0.0001, TolAng: Optional[float] = 0.01, TolCurv: Optional[float] = 0.1, MaxDeg: Optional[int] = 8, MaxSegments: Optional[int] = 9) -> None: ...
    @overload
    def Add(self, anEdge: TopoDS_Edge, Order: GeomAbs_Shape, IsBound: Optional[bool] = True) -> int: ...
    @overload
    def Add(self, anEdge: TopoDS_Edge, Support: TopoDS_Face, Order: GeomAbs_Shape, IsBound: Optional[bool] = True) -> int: ...
    @overload
    def Add(self, Support: TopoDS_Face, Order: GeomAbs_Shape) -> int: ...
    @overload
    def Add(self, Point: gp_Pnt) -> int: ...
    @overload
    def Add(self, U: float, V: float, Support: TopoDS_Face, Order: GeomAbs_Shape) -> int: ...
    def Build(self) -> None: ...
    def Face(self) -> TopoDS_Face: ...
    @overload
    def G0Error(self) -> float: ...
    @overload
    def G0Error(self, Index: int) -> float: ...
    @overload
    def G1Error(self) -> float: ...
    @overload
    def G1Error(self, Index: int) -> float: ...
    @overload
    def G2Error(self) -> float: ...
    @overload
    def G2Error(self, Index: int) -> float: ...
    def Generated(self, S: TopoDS_Shape) -> TopTools_ListOfShape: ...
    def IsDone(self) -> bool: ...
    def LoadInitSurface(self, aFace: TopoDS_Face) -> None: ...
    def SetApproxParam(self, MaxDeg: Optional[int] = 8, MaxSegments: Optional[int] = 9) -> None: ...
    def SetConstrParam(self, Tol2d: Optional[float] = 0.00001, Tol3d: Optional[float] = 0.0001, TolAng: Optional[float] = 0.01, TolCurv: Optional[float] = 0.1) -> None: ...
    def SetResolParam(self, Degree: Optional[int] = 3, NbPtsOnCur: Optional[int] = 15, NbIter: Optional[int] = 2, Anisotropie: Optional[bool] = False) -> None: ...

class BRepFill_Generator:
    def __init__(self) -> None: ...
    def AddWire(self, Wire: TopoDS_Wire) -> None: ...
    def Generated(self) -> TopTools_DataMapOfShapeListOfShape: ...
    def GeneratedShapes(self, SSection: TopoDS_Shape) -> TopTools_ListOfShape: ...
    def Perform(self) -> None: ...
    def Shell(self) -> TopoDS_Shell: ...

class BRepFill_LocationLaw(Standard_Transient):
    def Abscissa(self, Index: int, Param: float) -> float: ...
    def CurvilinearBounds(self, Index: int) -> Tuple[float, float]: ...
    def D0(self, Abscissa: float, Section: TopoDS_Shape) -> None: ...
    def DeleteTransform(self) -> None: ...
    def Edge(self, Index: int) -> TopoDS_Edge: ...
    def GetStatus(self) -> GeomFill_PipeError: ...
    def Holes(self, Interval: TColStd_Array1OfInteger) -> None: ...
    def IsClosed(self) -> bool: ...
    def IsG1(self, Index: int, SpatialTolerance: Optional[float] = 1.0e-7, AngularTolerance: Optional[float] = 1.0e-4) -> int: ...
    def Law(self, Index: int) -> GeomFill_LocationLaw: ...
    def NbHoles(self, Tol: Optional[float] = 1.0e-7) -> int: ...
    def NbLaw(self) -> int: ...
    def Parameter(self, Abscissa: float) -> Tuple[int, float]: ...
    def PerformVertex(self, Index: int, InputVertex: TopoDS_Vertex, TolMin: float, OutputVertex: TopoDS_Vertex, Location: Optional[int] = 0) -> None: ...
    def TransformInCompatibleLaw(self, AngularTolerance: float) -> None: ...
    def TransformInG0Law(self) -> None: ...
    def Vertex(self, Index: int) -> TopoDS_Vertex: ...
    def Wire(self) -> TopoDS_Wire: ...

class BRepFill_MultiLine(AppCont_Function):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, Face1: TopoDS_Face, Face2: TopoDS_Face, Edge1: TopoDS_Edge, Edge2: TopoDS_Edge, Inv1: bool, Inv2: bool, Bissec: Geom2d_Curve) -> None: ...
    def Continuity(self) -> GeomAbs_Shape: ...
    def Curves(self, Curve: Geom_Curve, PCurve1: Geom2d_Curve, PCurve2: Geom2d_Curve) -> None: ...
    def FirstParameter(self) -> float: ...
    def IsParticularCase(self) -> bool: ...
    def LastParameter(self) -> float: ...
    @overload
    def Value(self, U: float) -> gp_Pnt: ...
    def Value3dOnF1OnF2(self, U: float, P3d: gp_Pnt, PF1: gp_Pnt2d, PF2: gp_Pnt2d) -> None: ...
    def ValueOnF1(self, U: float) -> gp_Pnt2d: ...
    def ValueOnF2(self, U: float) -> gp_Pnt2d: ...

class BRepFill_OffsetAncestors:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, Paral: BRepFill_OffsetWire) -> None: ...
    def Ancestor(self, S1: TopoDS_Edge) -> TopoDS_Shape: ...
    def HasAncestor(self, S1: TopoDS_Edge) -> bool: ...
    def IsDone(self) -> bool: ...
    def Perform(self, Paral: BRepFill_OffsetWire) -> None: ...

class BRepFill_OffsetWire:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, Spine: TopoDS_Face, Join: Optional[GeomAbs_JoinType] = GeomAbs_Arc, IsOpenResult: Optional[bool] = False) -> None: ...
    def GeneratedShapes(self, SpineShape: TopoDS_Shape) -> TopTools_ListOfShape: ...
    def Init(self, Spine: TopoDS_Face, Join: Optional[GeomAbs_JoinType] = GeomAbs_Arc, IsOpenResult: Optional[bool] = False) -> None: ...
    def IsDone(self) -> bool: ...
    def JoinType(self) -> GeomAbs_JoinType: ...
    def Perform(self, Offset: float, Alt: Optional[float] = 0.0) -> None: ...
    def PerformWithBiLo(self, WSP: TopoDS_Face, Offset: float, Locus: BRepMAT2d_BisectingLocus, Link: BRepMAT2d_LinkTopoBilo, Join: Optional[GeomAbs_JoinType] = GeomAbs_Arc, Alt: Optional[float] = 0.0) -> None: ...
    def Shape(self) -> TopoDS_Shape: ...
    def Spine(self) -> TopoDS_Face: ...

class BRepFill_Pipe:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, Spine: TopoDS_Wire, Profile: TopoDS_Shape, aMode: Optional[GeomFill_Trihedron] = GeomFill_IsCorrectedFrenet, ForceApproxC1: Optional[bool] = False, GeneratePartCase: Optional[bool] = False) -> None: ...
    def Edge(self, ESpine: TopoDS_Edge, VProfile: TopoDS_Vertex) -> TopoDS_Edge: ...
    def ErrorOnSurface(self) -> float: ...
    def Face(self, ESpine: TopoDS_Edge, EProfile: TopoDS_Edge) -> TopoDS_Face: ...
    def FirstShape(self) -> TopoDS_Shape: ...
    def Generated(self, S: TopoDS_Shape, L: TopTools_ListOfShape) -> None: ...
    def LastShape(self) -> TopoDS_Shape: ...
    def Perform(self, Spine: TopoDS_Wire, Profile: TopoDS_Shape, GeneratePartCase: Optional[bool] = False) -> None: ...
    def PipeLine(self, Point: gp_Pnt) -> TopoDS_Wire: ...
    def Profile(self) -> TopoDS_Shape: ...
    def Section(self, VSpine: TopoDS_Vertex) -> TopoDS_Shape: ...
    def Shape(self) -> TopoDS_Shape: ...
    def Spine(self) -> TopoDS_Shape: ...

class BRepFill_PipeShell(Standard_Transient):
    def __init__(self, Spine: TopoDS_Wire) -> None: ...
    @overload
    def Add(self, Profile: TopoDS_Shape, WithContact: Optional[bool] = False, WithCorrection: Optional[bool] = False) -> None: ...
    @overload
    def Add(self, Profile: TopoDS_Shape, Location: TopoDS_Vertex, WithContact: Optional[bool] = False, WithCorrection: Optional[bool] = False) -> None: ...
    def Build(self) -> bool: ...
    def DeleteProfile(self, Profile: TopoDS_Shape) -> None: ...
    def ErrorOnSurface(self) -> float: ...
    def FirstShape(self) -> TopoDS_Shape: ...
    def Generated(self, S: TopoDS_Shape, L: TopTools_ListOfShape) -> None: ...
    def GetStatus(self) -> GeomFill_PipeError: ...
    def IsReady(self) -> bool: ...
    def LastShape(self) -> TopoDS_Shape: ...
    def MakeSolid(self) -> bool: ...
    def Profiles(self, theProfiles: TopTools_ListOfShape) -> None: ...
    @overload
    def Set(self, Frenet: Optional[bool] = False) -> None: ...
    @overload
    def Set(self, Axe: gp_Ax2) -> None: ...
    @overload
    def Set(self, BiNormal: gp_Dir) -> None: ...
    @overload
    def Set(self, SpineSupport: TopoDS_Shape) -> bool: ...
    @overload
    def Set(self, AuxiliarySpine: TopoDS_Wire, CurvilinearEquivalence: Optional[bool] = True, KeepContact: Optional[BRepFill_TypeOfContact] = BRepFill_NoContact) -> None: ...
    def SetDiscrete(self) -> None: ...
    def SetForceApproxC1(self, ForceApproxC1: bool) -> None: ...
    @overload
    def SetLaw(self, Profile: TopoDS_Shape, L: Law_Function, WithContact: Optional[bool] = False, WithCorrection: Optional[bool] = False) -> None: ...
    @overload
    def SetLaw(self, Profile: TopoDS_Shape, L: Law_Function, Location: TopoDS_Vertex, WithContact: Optional[bool] = False, WithCorrection: Optional[bool] = False) -> None: ...
    def SetMaxDegree(self, NewMaxDegree: int) -> None: ...
    def SetMaxSegments(self, NewMaxSegments: int) -> None: ...
    def SetTolerance(self, Tol3d: Optional[float] = 1.0e-4, BoundTol: Optional[float] = 1.0e-4, TolAngular: Optional[float] = 1.0e-2) -> None: ...
    def SetTransition(self, Mode: Optional[BRepFill_TransitionStyle] = BRepFill_Modified, Angmin: Optional[float] = 1.0e-2, Angmax: Optional[float] = 6.0) -> None: ...
    def Shape(self) -> TopoDS_Shape: ...
    def Simulate(self, NumberOfSection: int, Sections: TopTools_ListOfShape) -> None: ...
    def Spine(self) -> TopoDS_Wire: ...

class BRepFill_Section:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, Profile: TopoDS_Shape, V: TopoDS_Vertex, WithContact: bool, WithCorrection: bool) -> None: ...
    def IsLaw(self) -> bool: ...
    def IsPunctual(self) -> bool: ...
    def ModifiedShape(self, theShape: TopoDS_Shape) -> TopoDS_Shape: ...
    def OriginalShape(self) -> TopoDS_Shape: ...
    def Set(self, IsLaw: bool) -> None: ...
    def Vertex(self) -> TopoDS_Vertex: ...
    def Wire(self) -> TopoDS_Wire: ...
    def WithContact(self) -> bool: ...
    def WithCorrection(self) -> bool: ...

class BRepFill_SectionLaw(Standard_Transient):
    def ConcatenedLaw(self) -> GeomFill_SectionLaw: ...
    def Continuity(self, Index: int, TolAngular: float) -> GeomAbs_Shape: ...
    def CurrentEdge(self) -> TopoDS_Edge: ...
    def D0(self, U: float, S: TopoDS_Shape) -> None: ...
    def IndexOfEdge(self, anEdge: TopoDS_Shape) -> int: ...
    def Init(self, W: TopoDS_Wire) -> None: ...
    def IsConstant(self) -> bool: ...
    def IsDone(self) -> bool: ...
    def IsUClosed(self) -> bool: ...
    def IsVClosed(self) -> bool: ...
    def IsVertex(self) -> bool: ...
    def Law(self, Index: int) -> GeomFill_SectionLaw: ...
    def NbLaw(self) -> int: ...
    def Vertex(self, Index: int, Param: float) -> TopoDS_Vertex: ...
    def VertexTol(self, Index: int, Param: float) -> float: ...

class BRepFill_SectionPlacement:
    @overload
    def __init__(self, Law: BRepFill_LocationLaw, Section: TopoDS_Shape, WithContact: Optional[bool] = False, WithCorrection: Optional[bool] = False) -> None: ...
    @overload
    def __init__(self, Law: BRepFill_LocationLaw, Section: TopoDS_Shape, Vertex: TopoDS_Shape, WithContact: Optional[bool] = False, WithCorrection: Optional[bool] = False) -> None: ...
    def AbscissaOnPath(self) -> float: ...
    def Transformation(self) -> gp_Trsf: ...

class BRepFill_Sweep:
    def __init__(self, Section: BRepFill_SectionLaw, Location: BRepFill_LocationLaw, WithKPart: bool) -> None: ...
    def Build(self, ReversedEdges: TopTools_MapOfShape, Tapes: BRepFill_DataMapOfShapeHArray2OfShape, Rails: BRepFill_DataMapOfShapeHArray2OfShape, Transition: Optional[BRepFill_TransitionStyle] = BRepFill_Modified, Continuity: Optional[GeomAbs_Shape] = GeomAbs_C2, Approx: Optional[GeomFill_ApproxStyle] = GeomFill_Location, Degmax: Optional[int] = 11, Segmax: Optional[int] = 30) -> None: ...
    def ErrorOnSurface(self) -> float: ...
    def InterFaces(self) -> TopTools_HArray2OfShape: ...
    def IsDone(self) -> bool: ...
    def Sections(self) -> TopTools_HArray2OfShape: ...
    def SetAngularControl(self, AngleMin: Optional[float] = 0.01, AngleMax: Optional[float] = 6.0) -> None: ...
    def SetBounds(self, FirstShape: TopoDS_Wire, LastShape: TopoDS_Wire) -> None: ...
    def SetForceApproxC1(self, ForceApproxC1: bool) -> None: ...
    def SetTolerance(self, Tol3d: float, BoundTol: Optional[float] = 1.0, Tol2d: Optional[float] = 1.0e-5, TolAngular: Optional[float] = 1.0e-2) -> None: ...
    def Shape(self) -> TopoDS_Shape: ...
    def SubShape(self) -> TopTools_HArray2OfShape: ...
    def Tape(self, Index: int) -> TopoDS_Shape: ...

class BRepFill_TrimEdgeTool:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, Bisec: Bisector_Bisec, S1: Geom2d_Geometry, S2: Geom2d_Geometry, Offset: float) -> None: ...
    def AddOrConfuse(self, Start: bool, Edge1: TopoDS_Edge, Edge2: TopoDS_Edge, Params: TColgp_SequenceOfPnt) -> None: ...
    def IntersectWith(self, Edge1: TopoDS_Edge, Edge2: TopoDS_Edge, InitShape1: TopoDS_Shape, InitShape2: TopoDS_Shape, End1: TopoDS_Vertex, End2: TopoDS_Vertex, theJoinType: GeomAbs_JoinType, IsOpenResult: bool, Params: TColgp_SequenceOfPnt) -> None: ...
    def IsInside(self, P: gp_Pnt2d) -> bool: ...

class BRepFill_TrimShellCorner:
    def __init__(self, theFaces: TopTools_HArray2OfShape, theTransition: BRepFill_TransitionStyle, theAxeOfBisPlane: gp_Ax2) -> None: ...
    def AddBounds(self, Bounds: TopTools_HArray2OfShape) -> None: ...
    def AddUEdges(self, theUEdges: TopTools_HArray2OfShape) -> None: ...
    def AddVEdges(self, theVEdges: TopTools_HArray2OfShape, theIndex: int) -> None: ...
    def HasSection(self) -> bool: ...
    def IsDone(self) -> bool: ...
    def Modified(self, S: TopoDS_Shape, theModified: TopTools_ListOfShape) -> None: ...
    def Perform(self) -> None: ...

class BRepFill_TrimSurfaceTool:
    def __init__(self, Bis: Geom2d_Curve, Face1: TopoDS_Face, Face2: TopoDS_Face, Edge1: TopoDS_Edge, Edge2: TopoDS_Edge, Inv1: bool, Inv2: bool) -> None: ...
    def IntersectWith(self, EdgeOnF1: TopoDS_Edge, EdgeOnF2: TopoDS_Edge, Points: TColgp_SequenceOfPnt) -> None: ...
    def IsOnFace(self, Point: gp_Pnt2d) -> bool: ...
    def ProjOn(self, Point: gp_Pnt2d, Edge: TopoDS_Edge) -> float: ...
    def Project(self, U1: float, U2: float, Curve: Geom_Curve, PCurve1: Geom2d_Curve, PCurve2: Geom2d_Curve, myCont: GeomAbs_Shape) -> None: ...

class BRepFill_ACRLaw(BRepFill_LocationLaw):
    def __init__(self, Path: TopoDS_Wire, Law: GeomFill_LocationGuide) -> None: ...

class BRepFill_Edge3DLaw(BRepFill_LocationLaw):
    def __init__(self, Path: TopoDS_Wire, Law: GeomFill_LocationLaw) -> None: ...

class BRepFill_EdgeOnSurfLaw(BRepFill_LocationLaw):
    def __init__(self, Path: TopoDS_Wire, Surf: TopoDS_Shape) -> None: ...
    def HasResult(self) -> bool: ...

class BRepFill_NSections(BRepFill_SectionLaw):
    @overload
    def __init__(self, S: TopTools_SequenceOfShape, Build: Optional[bool] = True) -> None: ...
    @overload
    def __init__(self, S: TopTools_SequenceOfShape, Trsfs: GeomFill_SequenceOfTrsf, P: TColStd_SequenceOfReal, VF: float, VL: float, Build: Optional[bool] = True) -> None: ...
    def ConcatenedLaw(self) -> GeomFill_SectionLaw: ...
    def Continuity(self, Index: int, TolAngular: float) -> GeomAbs_Shape: ...
    def D0(self, Param: float, S: TopoDS_Shape) -> None: ...
    def IsConstant(self) -> bool: ...
    def IsVertex(self) -> bool: ...
    def Vertex(self, Index: int, Param: float) -> TopoDS_Vertex: ...
    def VertexTol(self, Index: int, Param: float) -> float: ...

class BRepFill_ShapeLaw(BRepFill_SectionLaw):
    @overload
    def __init__(self, V: TopoDS_Vertex, Build: Optional[bool] = True) -> None: ...
    @overload
    def __init__(self, W: TopoDS_Wire, Build: Optional[bool] = True) -> None: ...
    @overload
    def __init__(self, W: TopoDS_Wire, L: Law_Function, Build: Optional[bool] = True) -> None: ...
    def ConcatenedLaw(self) -> GeomFill_SectionLaw: ...
    def Continuity(self, Index: int, TolAngular: float) -> GeomAbs_Shape: ...
    def D0(self, Param: float, S: TopoDS_Shape) -> None: ...
    def Edge(self, Index: int) -> TopoDS_Edge: ...
    def IsConstant(self) -> bool: ...
    def IsVertex(self) -> bool: ...
    def Vertex(self, Index: int, Param: float) -> TopoDS_Vertex: ...
    def VertexTol(self, Index: int, Param: float) -> float: ...

class BRepFill_DraftLaw(BRepFill_Edge3DLaw):
    def __init__(self, Path: TopoDS_Wire, Law: GeomFill_LocationDraft) -> None: ...
    def CleanLaw(self, TolAngular: float) -> None: ...

# harray1 classes
# harray2 classes
# hsequence classes

brepfill_Axe = brepfill.Axe
brepfill_ComputeACR = brepfill.ComputeACR
brepfill_Face = brepfill.Face
brepfill_InsertACR = brepfill.InsertACR
brepfill_Shell = brepfill.Shell
