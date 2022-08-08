from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.gp import *
from OCC.Core.TopoDS import *
from OCC.Core.GeomAbs import *
from OCC.Core.Geom2d import *
from OCC.Core.TopTools import *
from OCC.Core.Adaptor3d import *
from OCC.Core.Geom import *
from OCC.Core.BRepTools import *
from OCC.Core.TopLoc import *


class BRepLib_EdgeError(IntEnum):
    BRepLib_EdgeDone: int = ...
    BRepLib_PointProjectionFailed: int = ...
    BRepLib_ParameterOutOfRange: int = ...
    BRepLib_DifferentPointsOnClosedCurve: int = ...
    BRepLib_PointWithInfiniteParameter: int = ...
    BRepLib_DifferentsPointAndParameter: int = ...
    BRepLib_LineThroughIdenticPoints: int = ...

BRepLib_EdgeDone = BRepLib_EdgeError.BRepLib_EdgeDone
BRepLib_PointProjectionFailed = BRepLib_EdgeError.BRepLib_PointProjectionFailed
BRepLib_ParameterOutOfRange = BRepLib_EdgeError.BRepLib_ParameterOutOfRange
BRepLib_DifferentPointsOnClosedCurve = BRepLib_EdgeError.BRepLib_DifferentPointsOnClosedCurve
BRepLib_PointWithInfiniteParameter = BRepLib_EdgeError.BRepLib_PointWithInfiniteParameter
BRepLib_DifferentsPointAndParameter = BRepLib_EdgeError.BRepLib_DifferentsPointAndParameter
BRepLib_LineThroughIdenticPoints = BRepLib_EdgeError.BRepLib_LineThroughIdenticPoints

class BRepLib_FaceError(IntEnum):
    BRepLib_FaceDone: int = ...
    BRepLib_NoFace: int = ...
    BRepLib_NotPlanar: int = ...
    BRepLib_CurveProjectionFailed: int = ...
    BRepLib_ParametersOutOfRange: int = ...

BRepLib_FaceDone = BRepLib_FaceError.BRepLib_FaceDone
BRepLib_NoFace = BRepLib_FaceError.BRepLib_NoFace
BRepLib_NotPlanar = BRepLib_FaceError.BRepLib_NotPlanar
BRepLib_CurveProjectionFailed = BRepLib_FaceError.BRepLib_CurveProjectionFailed
BRepLib_ParametersOutOfRange = BRepLib_FaceError.BRepLib_ParametersOutOfRange

class BRepLib_ShapeModification(IntEnum):
    BRepLib_Preserved: int = ...
    BRepLib_Deleted: int = ...
    BRepLib_Trimmed: int = ...
    BRepLib_Merged: int = ...
    BRepLib_BoundaryModified: int = ...

BRepLib_Preserved = BRepLib_ShapeModification.BRepLib_Preserved
BRepLib_Deleted = BRepLib_ShapeModification.BRepLib_Deleted
BRepLib_Trimmed = BRepLib_ShapeModification.BRepLib_Trimmed
BRepLib_Merged = BRepLib_ShapeModification.BRepLib_Merged
BRepLib_BoundaryModified = BRepLib_ShapeModification.BRepLib_BoundaryModified

class BRepLib_ShellError(IntEnum):
    BRepLib_ShellDone: int = ...
    BRepLib_EmptyShell: int = ...
    BRepLib_DisconnectedShell: int = ...
    BRepLib_ShellParametersOutOfRange: int = ...

BRepLib_ShellDone = BRepLib_ShellError.BRepLib_ShellDone
BRepLib_EmptyShell = BRepLib_ShellError.BRepLib_EmptyShell
BRepLib_DisconnectedShell = BRepLib_ShellError.BRepLib_DisconnectedShell
BRepLib_ShellParametersOutOfRange = BRepLib_ShellError.BRepLib_ShellParametersOutOfRange

class BRepLib_WireError(IntEnum):
    BRepLib_WireDone: int = ...
    BRepLib_EmptyWire: int = ...
    BRepLib_DisconnectedWire: int = ...
    BRepLib_NonManifoldWire: int = ...

BRepLib_WireDone = BRepLib_WireError.BRepLib_WireDone
BRepLib_EmptyWire = BRepLib_WireError.BRepLib_EmptyWire
BRepLib_DisconnectedWire = BRepLib_WireError.BRepLib_DisconnectedWire
BRepLib_NonManifoldWire = BRepLib_WireError.BRepLib_NonManifoldWire

class breplib:
    @staticmethod
    def BuildCurve3d(E: TopoDS_Edge, Tolerance: Optional[float] = 1.0e-5, Continuity: Optional[GeomAbs_Shape] = GeomAbs_C1, MaxDegree: Optional[int] = 14, MaxSegment: Optional[int] = 0) -> bool: ...
    @overload
    @staticmethod
    def BuildCurves3d(S: TopoDS_Shape, Tolerance: float, Continuity: Optional[GeomAbs_Shape] = GeomAbs_C1, MaxDegree: Optional[int] = 14, MaxSegment: Optional[int] = 0) -> bool: ...
    @overload
    @staticmethod
    def BuildCurves3d(S: TopoDS_Shape) -> bool: ...
    @overload
    @staticmethod
    def BuildPCurveForEdgeOnPlane(theE: TopoDS_Edge, theF: TopoDS_Face) -> None: ...
    @overload
    @staticmethod
    def BuildPCurveForEdgeOnPlane(theE: TopoDS_Edge, theF: TopoDS_Face, aC2D: Geom2d_Curve) -> bool: ...
    @staticmethod
    def CheckSameRange(E: TopoDS_Edge, Confusion: Optional[float] = 1.0e-12) -> bool: ...
    @staticmethod
    def ContinuityOfFaces(theEdge: TopoDS_Edge, theFace1: TopoDS_Face, theFace2: TopoDS_Face, theAngleTol: float) -> GeomAbs_Shape: ...
    @overload
    @staticmethod
    def EncodeRegularity(S: TopoDS_Shape, TolAng: Optional[float] = 1.0e-10) -> None: ...
    @overload
    @staticmethod
    def EncodeRegularity(S: TopoDS_Shape, LE: TopTools_ListOfShape, TolAng: Optional[float] = 1.0e-10) -> None: ...
    @overload
    @staticmethod
    def EncodeRegularity(E: TopoDS_Edge, F1: TopoDS_Face, F2: TopoDS_Face, TolAng: Optional[float] = 1.0e-10) -> None: ...
    @staticmethod
    def EnsureNormalConsistency(S: TopoDS_Shape, theAngTol: Optional[float] = 0.001, ForceComputeNormals: Optional[bool] = False) -> bool: ...
    @staticmethod
    def ExtendFace(theF: TopoDS_Face, theExtVal: float, theExtUMin: bool, theExtUMax: bool, theExtVMin: bool, theExtVMax: bool, theFExtended: TopoDS_Face) -> None: ...
    @overload
    @staticmethod
    def FindValidRange(theCurve: Adaptor3d_Curve, theTolE: float, theParV1: float, thePntV1: gp_Pnt, theTolV1: float, theParV2: float, thePntV2: gp_Pnt, theTolV2: float) -> Tuple[bool, float, float]: ...
    @overload
    @staticmethod
    def FindValidRange(theEdge: TopoDS_Edge) -> Tuple[bool, float, float]: ...
    @staticmethod
    def OrientClosedSolid(solid: TopoDS_Solid) -> bool: ...
    @overload
    @staticmethod
    def Plane(P: Geom_Plane) -> None: ...
    @overload
    @staticmethod
    def Plane() -> Geom_Plane: ...
    @overload
    @staticmethod
    def Precision(P: float) -> None: ...
    @overload
    @staticmethod
    def Precision() -> float: ...
    @staticmethod
    def ReverseSortFaces(S: TopoDS_Shape, LF: TopTools_ListOfShape) -> None: ...
    @overload
    @staticmethod
    def SameParameter(theEdge: TopoDS_Edge, Tolerance: Optional[float] = 1.0e-5) -> None: ...
    @overload
    @staticmethod
    def SameParameter(theEdge: TopoDS_Edge, theTolerance: float, IsUseOldEdge: bool) -> Tuple[TopoDS_Edge, float]: ...
    @overload
    @staticmethod
    def SameParameter(S: TopoDS_Shape, Tolerance: Optional[float] = 1.0e-5, forced: Optional[bool] = False) -> None: ...
    @overload
    @staticmethod
    def SameParameter(S: TopoDS_Shape, theReshaper: BRepTools_ReShape, Tolerance: Optional[float] = 1.0e-5, forced: Optional[bool] = False) -> None: ...
    @staticmethod
    def SameRange(E: TopoDS_Edge, Tolerance: Optional[float] = 1.0e-5) -> None: ...
    @staticmethod
    def SortFaces(S: TopoDS_Shape, LF: TopTools_ListOfShape) -> None: ...
    @staticmethod
    def UpdateDeflection(S: TopoDS_Shape) -> None: ...
    @staticmethod
    def UpdateEdgeTol(E: TopoDS_Edge, MinToleranceRequest: float, MaxToleranceToCheck: float) -> bool: ...
    @staticmethod
    def UpdateEdgeTolerance(S: TopoDS_Shape, MinToleranceRequest: float, MaxToleranceToCheck: float) -> bool: ...
    @staticmethod
    def UpdateInnerTolerances(S: TopoDS_Shape) -> None: ...
    @overload
    @staticmethod
    def UpdateTolerances(S: TopoDS_Shape, verifyFaceTolerance: Optional[bool] = False) -> None: ...
    @overload
    @staticmethod
    def UpdateTolerances(S: TopoDS_Shape, theReshaper: BRepTools_ReShape, verifyFaceTolerance: Optional[bool] = False) -> None: ...

class BRepLib_CheckCurveOnSurface:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, theEdge: TopoDS_Edge, theFace: TopoDS_Face) -> None: ...
    def ErrorStatus(self) -> int: ...
    def Init(self, theEdge: TopoDS_Edge, theFace: TopoDS_Face) -> None: ...
    def IsDone(self) -> bool: ...
    def MaxDistance(self) -> float: ...
    def MaxParameter(self) -> float: ...
    def Perform(self, isMultiThread: Optional[bool] = False) -> None: ...

class BRepLib_Command:
    def Check(self) -> None: ...
    def IsDone(self) -> bool: ...

class BRepLib_FindSurface:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, S: TopoDS_Shape, Tol: Optional[float] = -1, OnlyPlane: Optional[bool] = False, OnlyClosed: Optional[bool] = False) -> None: ...
    def Existed(self) -> bool: ...
    def Found(self) -> bool: ...
    def Init(self, S: TopoDS_Shape, Tol: Optional[float] = -1, OnlyPlane: Optional[bool] = False, OnlyClosed: Optional[bool] = False) -> None: ...
    def Location(self) -> TopLoc_Location: ...
    def Surface(self) -> Geom_Surface: ...
    def Tolerance(self) -> float: ...
    def ToleranceReached(self) -> float: ...

class BRepLib_FuseEdges:
    def __init__(self, theShape: TopoDS_Shape, PerformNow: Optional[bool] = False) -> None: ...
    def AvoidEdges(self, theMapEdg: TopTools_IndexedMapOfShape) -> None: ...
    def Edges(self, theMapLstEdg: TopTools_DataMapOfIntegerListOfShape) -> None: ...
    def Faces(self, theMapFac: TopTools_DataMapOfShapeShape) -> None: ...
    def NbVertices(self) -> int: ...
    def Perform(self) -> None: ...
    def ResultEdges(self, theMapEdg: TopTools_DataMapOfIntegerShape) -> None: ...
    def SetConcatBSpl(self, theConcatBSpl: Optional[bool] = True) -> None: ...
    def Shape(self) -> TopoDS_Shape: ...

class BRepLib_ValidateEdge:
    def __init__(self, theReferenceCurve: Adaptor3d_Curve, theOtherCurve: Adaptor3d_CurveOnSurface, theSameParameter: bool) -> None: ...
    def CheckTolerance(self, theToleranceToCheck: float) -> bool: ...
    def GetMaxDistance(self) -> float: ...
    def IsDone(self) -> bool: ...
    def Process(self) -> None: ...
    def SetControlPointsNumber(self, theControlPointsNumber: int) -> None: ...
    def SetExitIfToleranceExceeded(self, theToleranceForChecking: float) -> None: ...
    def UpdateTolerance(self) -> float: ...

class BRepLib_MakeShape(BRepLib_Command):
    def Build(self) -> None: ...
    def DescendantFaces(self, F: TopoDS_Face) -> TopTools_ListOfShape: ...
    def FaceStatus(self, F: TopoDS_Face) -> BRepLib_ShapeModification: ...
    def FacesFromEdges(self, E: TopoDS_Edge) -> TopTools_ListOfShape: ...
    def HasDescendants(self, F: TopoDS_Face) -> bool: ...
    def NbSurfaces(self) -> int: ...
    def NewFaces(self, I: int) -> TopTools_ListOfShape: ...
    def Shape(self) -> TopoDS_Shape: ...

class BRepLib_MakeEdge(BRepLib_MakeShape):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, V1: TopoDS_Vertex, V2: TopoDS_Vertex) -> None: ...
    @overload
    def __init__(self, P1: gp_Pnt, P2: gp_Pnt) -> None: ...
    @overload
    def __init__(self, L: gp_Lin) -> None: ...
    @overload
    def __init__(self, L: gp_Lin, p1: float, p2: float) -> None: ...
    @overload
    def __init__(self, L: gp_Lin, P1: gp_Pnt, P2: gp_Pnt) -> None: ...
    @overload
    def __init__(self, L: gp_Lin, V1: TopoDS_Vertex, V2: TopoDS_Vertex) -> None: ...
    @overload
    def __init__(self, L: gp_Circ) -> None: ...
    @overload
    def __init__(self, L: gp_Circ, p1: float, p2: float) -> None: ...
    @overload
    def __init__(self, L: gp_Circ, P1: gp_Pnt, P2: gp_Pnt) -> None: ...
    @overload
    def __init__(self, L: gp_Circ, V1: TopoDS_Vertex, V2: TopoDS_Vertex) -> None: ...
    @overload
    def __init__(self, L: gp_Elips) -> None: ...
    @overload
    def __init__(self, L: gp_Elips, p1: float, p2: float) -> None: ...
    @overload
    def __init__(self, L: gp_Elips, P1: gp_Pnt, P2: gp_Pnt) -> None: ...
    @overload
    def __init__(self, L: gp_Elips, V1: TopoDS_Vertex, V2: TopoDS_Vertex) -> None: ...
    @overload
    def __init__(self, L: gp_Hypr) -> None: ...
    @overload
    def __init__(self, L: gp_Hypr, p1: float, p2: float) -> None: ...
    @overload
    def __init__(self, L: gp_Hypr, P1: gp_Pnt, P2: gp_Pnt) -> None: ...
    @overload
    def __init__(self, L: gp_Hypr, V1: TopoDS_Vertex, V2: TopoDS_Vertex) -> None: ...
    @overload
    def __init__(self, L: gp_Parab) -> None: ...
    @overload
    def __init__(self, L: gp_Parab, p1: float, p2: float) -> None: ...
    @overload
    def __init__(self, L: gp_Parab, P1: gp_Pnt, P2: gp_Pnt) -> None: ...
    @overload
    def __init__(self, L: gp_Parab, V1: TopoDS_Vertex, V2: TopoDS_Vertex) -> None: ...
    @overload
    def __init__(self, L: Geom_Curve) -> None: ...
    @overload
    def __init__(self, L: Geom_Curve, p1: float, p2: float) -> None: ...
    @overload
    def __init__(self, L: Geom_Curve, P1: gp_Pnt, P2: gp_Pnt) -> None: ...
    @overload
    def __init__(self, L: Geom_Curve, V1: TopoDS_Vertex, V2: TopoDS_Vertex) -> None: ...
    @overload
    def __init__(self, L: Geom_Curve, P1: gp_Pnt, P2: gp_Pnt, p1: float, p2: float) -> None: ...
    @overload
    def __init__(self, L: Geom_Curve, V1: TopoDS_Vertex, V2: TopoDS_Vertex, p1: float, p2: float) -> None: ...
    @overload
    def __init__(self, L: Geom2d_Curve, S: Geom_Surface) -> None: ...
    @overload
    def __init__(self, L: Geom2d_Curve, S: Geom_Surface, p1: float, p2: float) -> None: ...
    @overload
    def __init__(self, L: Geom2d_Curve, S: Geom_Surface, P1: gp_Pnt, P2: gp_Pnt) -> None: ...
    @overload
    def __init__(self, L: Geom2d_Curve, S: Geom_Surface, V1: TopoDS_Vertex, V2: TopoDS_Vertex) -> None: ...
    @overload
    def __init__(self, L: Geom2d_Curve, S: Geom_Surface, P1: gp_Pnt, P2: gp_Pnt, p1: float, p2: float) -> None: ...
    @overload
    def __init__(self, L: Geom2d_Curve, S: Geom_Surface, V1: TopoDS_Vertex, V2: TopoDS_Vertex, p1: float, p2: float) -> None: ...
    def Edge(self) -> TopoDS_Edge: ...
    def Error(self) -> BRepLib_EdgeError: ...
    @overload
    def Init(self, C: Geom_Curve) -> None: ...
    @overload
    def Init(self, C: Geom_Curve, p1: float, p2: float) -> None: ...
    @overload
    def Init(self, C: Geom_Curve, P1: gp_Pnt, P2: gp_Pnt) -> None: ...
    @overload
    def Init(self, C: Geom_Curve, V1: TopoDS_Vertex, V2: TopoDS_Vertex) -> None: ...
    @overload
    def Init(self, C: Geom_Curve, P1: gp_Pnt, P2: gp_Pnt, p1: float, p2: float) -> None: ...
    @overload
    def Init(self, C: Geom_Curve, V1: TopoDS_Vertex, V2: TopoDS_Vertex, p1: float, p2: float) -> None: ...
    @overload
    def Init(self, C: Geom2d_Curve, S: Geom_Surface) -> None: ...
    @overload
    def Init(self, C: Geom2d_Curve, S: Geom_Surface, p1: float, p2: float) -> None: ...
    @overload
    def Init(self, C: Geom2d_Curve, S: Geom_Surface, P1: gp_Pnt, P2: gp_Pnt) -> None: ...
    @overload
    def Init(self, C: Geom2d_Curve, S: Geom_Surface, V1: TopoDS_Vertex, V2: TopoDS_Vertex) -> None: ...
    @overload
    def Init(self, C: Geom2d_Curve, S: Geom_Surface, P1: gp_Pnt, P2: gp_Pnt, p1: float, p2: float) -> None: ...
    @overload
    def Init(self, C: Geom2d_Curve, S: Geom_Surface, V1: TopoDS_Vertex, V2: TopoDS_Vertex, p1: float, p2: float) -> None: ...
    def Vertex1(self) -> TopoDS_Vertex: ...
    def Vertex2(self) -> TopoDS_Vertex: ...

class BRepLib_MakeEdge2d(BRepLib_MakeShape):
    @overload
    def __init__(self, V1: TopoDS_Vertex, V2: TopoDS_Vertex) -> None: ...
    @overload
    def __init__(self, P1: gp_Pnt2d, P2: gp_Pnt2d) -> None: ...
    @overload
    def __init__(self, L: gp_Lin2d) -> None: ...
    @overload
    def __init__(self, L: gp_Lin2d, p1: float, p2: float) -> None: ...
    @overload
    def __init__(self, L: gp_Lin2d, P1: gp_Pnt2d, P2: gp_Pnt2d) -> None: ...
    @overload
    def __init__(self, L: gp_Lin2d, V1: TopoDS_Vertex, V2: TopoDS_Vertex) -> None: ...
    @overload
    def __init__(self, L: gp_Circ2d) -> None: ...
    @overload
    def __init__(self, L: gp_Circ2d, p1: float, p2: float) -> None: ...
    @overload
    def __init__(self, L: gp_Circ2d, P1: gp_Pnt2d, P2: gp_Pnt2d) -> None: ...
    @overload
    def __init__(self, L: gp_Circ2d, V1: TopoDS_Vertex, V2: TopoDS_Vertex) -> None: ...
    @overload
    def __init__(self, L: gp_Elips2d) -> None: ...
    @overload
    def __init__(self, L: gp_Elips2d, p1: float, p2: float) -> None: ...
    @overload
    def __init__(self, L: gp_Elips2d, P1: gp_Pnt2d, P2: gp_Pnt2d) -> None: ...
    @overload
    def __init__(self, L: gp_Elips2d, V1: TopoDS_Vertex, V2: TopoDS_Vertex) -> None: ...
    @overload
    def __init__(self, L: gp_Hypr2d) -> None: ...
    @overload
    def __init__(self, L: gp_Hypr2d, p1: float, p2: float) -> None: ...
    @overload
    def __init__(self, L: gp_Hypr2d, P1: gp_Pnt2d, P2: gp_Pnt2d) -> None: ...
    @overload
    def __init__(self, L: gp_Hypr2d, V1: TopoDS_Vertex, V2: TopoDS_Vertex) -> None: ...
    @overload
    def __init__(self, L: gp_Parab2d) -> None: ...
    @overload
    def __init__(self, L: gp_Parab2d, p1: float, p2: float) -> None: ...
    @overload
    def __init__(self, L: gp_Parab2d, P1: gp_Pnt2d, P2: gp_Pnt2d) -> None: ...
    @overload
    def __init__(self, L: gp_Parab2d, V1: TopoDS_Vertex, V2: TopoDS_Vertex) -> None: ...
    @overload
    def __init__(self, L: Geom2d_Curve) -> None: ...
    @overload
    def __init__(self, L: Geom2d_Curve, p1: float, p2: float) -> None: ...
    @overload
    def __init__(self, L: Geom2d_Curve, P1: gp_Pnt2d, P2: gp_Pnt2d) -> None: ...
    @overload
    def __init__(self, L: Geom2d_Curve, V1: TopoDS_Vertex, V2: TopoDS_Vertex) -> None: ...
    @overload
    def __init__(self, L: Geom2d_Curve, P1: gp_Pnt2d, P2: gp_Pnt2d, p1: float, p2: float) -> None: ...
    @overload
    def __init__(self, L: Geom2d_Curve, V1: TopoDS_Vertex, V2: TopoDS_Vertex, p1: float, p2: float) -> None: ...
    def Edge(self) -> TopoDS_Edge: ...
    def Error(self) -> BRepLib_EdgeError: ...
    @overload
    def Init(self, C: Geom2d_Curve) -> None: ...
    @overload
    def Init(self, C: Geom2d_Curve, p1: float, p2: float) -> None: ...
    @overload
    def Init(self, C: Geom2d_Curve, P1: gp_Pnt2d, P2: gp_Pnt2d) -> None: ...
    @overload
    def Init(self, C: Geom2d_Curve, V1: TopoDS_Vertex, V2: TopoDS_Vertex) -> None: ...
    @overload
    def Init(self, C: Geom2d_Curve, P1: gp_Pnt2d, P2: gp_Pnt2d, p1: float, p2: float) -> None: ...
    @overload
    def Init(self, C: Geom2d_Curve, V1: TopoDS_Vertex, V2: TopoDS_Vertex, p1: float, p2: float) -> None: ...
    def Vertex1(self) -> TopoDS_Vertex: ...
    def Vertex2(self) -> TopoDS_Vertex: ...

class BRepLib_MakeFace(BRepLib_MakeShape):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, F: TopoDS_Face) -> None: ...
    @overload
    def __init__(self, P: gp_Pln) -> None: ...
    @overload
    def __init__(self, C: gp_Cylinder) -> None: ...
    @overload
    def __init__(self, C: gp_Cone) -> None: ...
    @overload
    def __init__(self, S: gp_Sphere) -> None: ...
    @overload
    def __init__(self, C: gp_Torus) -> None: ...
    @overload
    def __init__(self, S: Geom_Surface, TolDegen: float) -> None: ...
    @overload
    def __init__(self, P: gp_Pln, UMin: float, UMax: float, VMin: float, VMax: float) -> None: ...
    @overload
    def __init__(self, C: gp_Cylinder, UMin: float, UMax: float, VMin: float, VMax: float) -> None: ...
    @overload
    def __init__(self, C: gp_Cone, UMin: float, UMax: float, VMin: float, VMax: float) -> None: ...
    @overload
    def __init__(self, S: gp_Sphere, UMin: float, UMax: float, VMin: float, VMax: float) -> None: ...
    @overload
    def __init__(self, C: gp_Torus, UMin: float, UMax: float, VMin: float, VMax: float) -> None: ...
    @overload
    def __init__(self, S: Geom_Surface, UMin: float, UMax: float, VMin: float, VMax: float, TolDegen: float) -> None: ...
    @overload
    def __init__(self, W: TopoDS_Wire, OnlyPlane: Optional[bool] = False) -> None: ...
    @overload
    def __init__(self, P: gp_Pln, W: TopoDS_Wire, Inside: Optional[bool] = True) -> None: ...
    @overload
    def __init__(self, C: gp_Cylinder, W: TopoDS_Wire, Inside: Optional[bool] = True) -> None: ...
    @overload
    def __init__(self, C: gp_Cone, W: TopoDS_Wire, Inside: Optional[bool] = True) -> None: ...
    @overload
    def __init__(self, S: gp_Sphere, W: TopoDS_Wire, Inside: Optional[bool] = True) -> None: ...
    @overload
    def __init__(self, C: gp_Torus, W: TopoDS_Wire, Inside: Optional[bool] = True) -> None: ...
    @overload
    def __init__(self, S: Geom_Surface, W: TopoDS_Wire, Inside: Optional[bool] = True) -> None: ...
    @overload
    def __init__(self, F: TopoDS_Face, W: TopoDS_Wire) -> None: ...
    def Add(self, W: TopoDS_Wire) -> None: ...
    def Error(self) -> BRepLib_FaceError: ...
    def Face(self) -> TopoDS_Face: ...
    @overload
    def Init(self, F: TopoDS_Face) -> None: ...
    @overload
    def Init(self, S: Geom_Surface, Bound: bool, TolDegen: float) -> None: ...
    @overload
    def Init(self, S: Geom_Surface, UMin: float, UMax: float, VMin: float, VMax: float, TolDegen: float) -> None: ...
    @staticmethod
    def IsDegenerated(theCurve: Geom_Curve, theMaxTol: float) -> Tuple[bool, float]: ...

class BRepLib_MakePolygon(BRepLib_MakeShape):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, P1: gp_Pnt, P2: gp_Pnt) -> None: ...
    @overload
    def __init__(self, P1: gp_Pnt, P2: gp_Pnt, P3: gp_Pnt, Close: Optional[bool] = False) -> None: ...
    @overload
    def __init__(self, P1: gp_Pnt, P2: gp_Pnt, P3: gp_Pnt, P4: gp_Pnt, Close: Optional[bool] = False) -> None: ...
    @overload
    def __init__(self, V1: TopoDS_Vertex, V2: TopoDS_Vertex) -> None: ...
    @overload
    def __init__(self, V1: TopoDS_Vertex, V2: TopoDS_Vertex, V3: TopoDS_Vertex, Close: Optional[bool] = False) -> None: ...
    @overload
    def __init__(self, V1: TopoDS_Vertex, V2: TopoDS_Vertex, V3: TopoDS_Vertex, V4: TopoDS_Vertex, Close: Optional[bool] = False) -> None: ...
    @overload
    def Add(self, P: gp_Pnt) -> None: ...
    @overload
    def Add(self, V: TopoDS_Vertex) -> None: ...
    def Added(self) -> bool: ...
    def Close(self) -> None: ...
    def Edge(self) -> TopoDS_Edge: ...
    def FirstVertex(self) -> TopoDS_Vertex: ...
    def LastVertex(self) -> TopoDS_Vertex: ...
    def Wire(self) -> TopoDS_Wire: ...

class BRepLib_MakeShell(BRepLib_MakeShape):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, S: Geom_Surface, Segment: Optional[bool] = False) -> None: ...
    @overload
    def __init__(self, S: Geom_Surface, UMin: float, UMax: float, VMin: float, VMax: float, Segment: Optional[bool] = False) -> None: ...
    def Error(self) -> BRepLib_ShellError: ...
    def Init(self, S: Geom_Surface, UMin: float, UMax: float, VMin: float, VMax: float, Segment: Optional[bool] = False) -> None: ...
    def Shell(self) -> TopoDS_Shell: ...

class BRepLib_MakeSolid(BRepLib_MakeShape):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, S: TopoDS_CompSolid) -> None: ...
    @overload
    def __init__(self, S: TopoDS_Shell) -> None: ...
    @overload
    def __init__(self, S1: TopoDS_Shell, S2: TopoDS_Shell) -> None: ...
    @overload
    def __init__(self, S1: TopoDS_Shell, S2: TopoDS_Shell, S3: TopoDS_Shell) -> None: ...
    @overload
    def __init__(self, So: TopoDS_Solid) -> None: ...
    @overload
    def __init__(self, So: TopoDS_Solid, S: TopoDS_Shell) -> None: ...
    def Add(self, S: TopoDS_Shell) -> None: ...
    def FaceStatus(self, F: TopoDS_Face) -> BRepLib_ShapeModification: ...
    def Solid(self) -> TopoDS_Solid: ...

class BRepLib_MakeVertex(BRepLib_MakeShape):
    @overload
    def __init__(self, P: gp_Pnt) -> None: ...
    def Vertex(self) -> TopoDS_Vertex: ...

class BRepLib_MakeWire(BRepLib_MakeShape):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, E: TopoDS_Edge) -> None: ...
    @overload
    def __init__(self, E1: TopoDS_Edge, E2: TopoDS_Edge) -> None: ...
    @overload
    def __init__(self, E1: TopoDS_Edge, E2: TopoDS_Edge, E3: TopoDS_Edge) -> None: ...
    @overload
    def __init__(self, E1: TopoDS_Edge, E2: TopoDS_Edge, E3: TopoDS_Edge, E4: TopoDS_Edge) -> None: ...
    @overload
    def __init__(self, W: TopoDS_Wire) -> None: ...
    @overload
    def __init__(self, W: TopoDS_Wire, E: TopoDS_Edge) -> None: ...
    @overload
    def Add(self, E: TopoDS_Edge) -> None: ...
    @overload
    def Add(self, W: TopoDS_Wire) -> None: ...
    @overload
    def Add(self, L: TopTools_ListOfShape) -> None: ...
    def Edge(self) -> TopoDS_Edge: ...
    def Error(self) -> BRepLib_WireError: ...
    def Vertex(self) -> TopoDS_Vertex: ...
    def Wire(self) -> TopoDS_Wire: ...

# harray1 classes
# harray2 classes
# hsequence classes

breplib_BoundingVertex = breplib.BoundingVertex
breplib_BuildCurve3d = breplib.BuildCurve3d
breplib_BuildCurves3d = breplib.BuildCurves3d
breplib_BuildCurves3d = breplib.BuildCurves3d
breplib_BuildPCurveForEdgeOnPlane = breplib.BuildPCurveForEdgeOnPlane
breplib_BuildPCurveForEdgeOnPlane = breplib.BuildPCurveForEdgeOnPlane
breplib_CheckSameRange = breplib.CheckSameRange
breplib_ContinuityOfFaces = breplib.ContinuityOfFaces
breplib_EncodeRegularity = breplib.EncodeRegularity
breplib_EncodeRegularity = breplib.EncodeRegularity
breplib_EncodeRegularity = breplib.EncodeRegularity
breplib_EnsureNormalConsistency = breplib.EnsureNormalConsistency
breplib_ExtendFace = breplib.ExtendFace
breplib_FindValidRange = breplib.FindValidRange
breplib_FindValidRange = breplib.FindValidRange
breplib_OrientClosedSolid = breplib.OrientClosedSolid
breplib_Plane = breplib.Plane
breplib_Plane = breplib.Plane
breplib_Precision = breplib.Precision
breplib_Precision = breplib.Precision
breplib_ReverseSortFaces = breplib.ReverseSortFaces
breplib_SameParameter = breplib.SameParameter
breplib_SameParameter = breplib.SameParameter
breplib_SameParameter = breplib.SameParameter
breplib_SameParameter = breplib.SameParameter
breplib_SameRange = breplib.SameRange
breplib_SortFaces = breplib.SortFaces
breplib_UpdateDeflection = breplib.UpdateDeflection
breplib_UpdateEdgeTol = breplib.UpdateEdgeTol
breplib_UpdateEdgeTolerance = breplib.UpdateEdgeTolerance
breplib_UpdateInnerTolerances = breplib.UpdateInnerTolerances
breplib_UpdateTolerances = breplib.UpdateTolerances
breplib_UpdateTolerances = breplib.UpdateTolerances
BRepLib_MakeFace_IsDegenerated = BRepLib_MakeFace.IsDegenerated
