from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.SelectMgr import *
from OCC.Core.Prs3d import *
from OCC.Core.TopoDS import *
from OCC.Core.PrsMgr import *
from OCC.Core.TopLoc import *
from OCC.Core.V3d import *
from OCC.Core.Select3D import *
from OCC.Core.TopAbs import *


class StdSelect_TypeOfEdge(IntEnum):
    StdSelect_AnyEdge: int = ...
    StdSelect_Line: int = ...
    StdSelect_Circle: int = ...

StdSelect_AnyEdge = StdSelect_TypeOfEdge.StdSelect_AnyEdge
StdSelect_Line = StdSelect_TypeOfEdge.StdSelect_Line
StdSelect_Circle = StdSelect_TypeOfEdge.StdSelect_Circle

class StdSelect_TypeOfFace(IntEnum):
    StdSelect_AnyFace: int = ...
    StdSelect_Plane: int = ...
    StdSelect_Cylinder: int = ...
    StdSelect_Sphere: int = ...
    StdSelect_Torus: int = ...
    StdSelect_Revol: int = ...
    StdSelect_Cone: int = ...

StdSelect_AnyFace = StdSelect_TypeOfFace.StdSelect_AnyFace
StdSelect_Plane = StdSelect_TypeOfFace.StdSelect_Plane
StdSelect_Cylinder = StdSelect_TypeOfFace.StdSelect_Cylinder
StdSelect_Sphere = StdSelect_TypeOfFace.StdSelect_Sphere
StdSelect_Torus = StdSelect_TypeOfFace.StdSelect_Torus
StdSelect_Revol = StdSelect_TypeOfFace.StdSelect_Revol
StdSelect_Cone = StdSelect_TypeOfFace.StdSelect_Cone

class StdSelect_TypeOfSelectionImage(IntEnum):
    StdSelect_TypeOfSelectionImage_NormalizedDepth: int = ...
    StdSelect_TypeOfSelectionImage_NormalizedDepthInverted: int = ...
    StdSelect_TypeOfSelectionImage_UnnormalizedDepth: int = ...
    StdSelect_TypeOfSelectionImage_ColoredDetectedObject: int = ...
    StdSelect_TypeOfSelectionImage_ColoredEntity: int = ...
    StdSelect_TypeOfSelectionImage_ColoredEntityType: int = ...
    StdSelect_TypeOfSelectionImage_ColoredOwner: int = ...
    StdSelect_TypeOfSelectionImage_ColoredSelectionMode: int = ...
    StdSelect_TypeOfSelectionImage_SurfaceNormal: int = ...

StdSelect_TypeOfSelectionImage_NormalizedDepth = StdSelect_TypeOfSelectionImage.StdSelect_TypeOfSelectionImage_NormalizedDepth
StdSelect_TypeOfSelectionImage_NormalizedDepthInverted = StdSelect_TypeOfSelectionImage.StdSelect_TypeOfSelectionImage_NormalizedDepthInverted
StdSelect_TypeOfSelectionImage_UnnormalizedDepth = StdSelect_TypeOfSelectionImage.StdSelect_TypeOfSelectionImage_UnnormalizedDepth
StdSelect_TypeOfSelectionImage_ColoredDetectedObject = StdSelect_TypeOfSelectionImage.StdSelect_TypeOfSelectionImage_ColoredDetectedObject
StdSelect_TypeOfSelectionImage_ColoredEntity = StdSelect_TypeOfSelectionImage.StdSelect_TypeOfSelectionImage_ColoredEntity
StdSelect_TypeOfSelectionImage_ColoredEntityType = StdSelect_TypeOfSelectionImage.StdSelect_TypeOfSelectionImage_ColoredEntityType
StdSelect_TypeOfSelectionImage_ColoredOwner = StdSelect_TypeOfSelectionImage.StdSelect_TypeOfSelectionImage_ColoredOwner
StdSelect_TypeOfSelectionImage_ColoredSelectionMode = StdSelect_TypeOfSelectionImage.StdSelect_TypeOfSelectionImage_ColoredSelectionMode
StdSelect_TypeOfSelectionImage_SurfaceNormal = StdSelect_TypeOfSelectionImage.StdSelect_TypeOfSelectionImage_SurfaceNormal

class stdselect:
    @staticmethod
    def SetDrawerForBRepOwner(aSelection: SelectMgr_Selection, aDrawer: Prs3d_Drawer) -> None: ...

class StdSelect_BRepOwner(SelectMgr_EntityOwner):
    @overload
    def __init__(self, aPriority: int) -> None: ...
    @overload
    def __init__(self, aShape: TopoDS_Shape, aPriority: Optional[int] = 0, ComesFromDecomposition: Optional[bool] = False) -> None: ...
    @overload
    def __init__(self, aShape: TopoDS_Shape, theOrigin: SelectMgr_SelectableObject, aPriority: Optional[int] = 0, FromDecomposition: Optional[bool] = False) -> None: ...
    def Clear(self, aPM: PrsMgr_PresentationManager, aMode: Optional[int] = 0) -> None: ...
    def HasHilightMode(self) -> bool: ...
    def HasShape(self) -> bool: ...
    def HilightMode(self) -> int: ...
    def HilightWithColor(self, thePM: PrsMgr_PresentationManager, theStyle: Prs3d_Drawer, theMode: int) -> None: ...
    def IsHilighted(self, aPM: PrsMgr_PresentationManager, aMode: Optional[int] = 0) -> bool: ...
    def ResetHilightMode(self) -> None: ...
    def SetHilightMode(self, theMode: int) -> None: ...
    def SetLocation(self, aLoc: TopLoc_Location) -> None: ...
    def Shape(self) -> TopoDS_Shape: ...
    def Unhilight(self, aPM: PrsMgr_PresentationManager, aMode: Optional[int] = 0) -> None: ...
    def UpdateHighlightTrsf(self, theViewer: V3d_Viewer, theManager: PrsMgr_PresentationManager, theDispMode: int) -> None: ...

class StdSelect_BRepSelectionTool:
    @staticmethod
    def ComputeSensitive(theShape: TopoDS_Shape, theOwner: SelectMgr_EntityOwner, theSelection: SelectMgr_Selection, theDeflection: float, theDeflAngle: float, theNbPOnEdge: int, theMaxiParam: float, theAutoTriang: Optional[bool] = True) -> None: ...
    @staticmethod
    def GetEdgeSensitive(theShape: TopoDS_Shape, theOwner: SelectMgr_EntityOwner, theSelection: SelectMgr_Selection, theDeflection: float, theDeviationAngle: float, theNbPOnEdge: int, theMaxiParam: float, theSensitive: Select3D_SensitiveEntity) -> None: ...
    @staticmethod
    def GetSensitiveForFace(theFace: TopoDS_Face, theOwner: SelectMgr_EntityOwner, theOutList: Select3D_EntitySequence, theAutoTriang: Optional[bool] = True, theNbPOnEdge: Optional[int] = 9, theMaxiParam: Optional[float] = 500, theInteriorFlag: Optional[bool] = True) -> bool: ...
    @staticmethod
    def GetStandardPriority(theShape: TopoDS_Shape, theType: TopAbs_ShapeEnum) -> int: ...
    @overload
    @staticmethod
    def Load(aSelection: SelectMgr_Selection, aShape: TopoDS_Shape, aType: TopAbs_ShapeEnum, theDeflection: float, theDeviationAngle: float, AutoTriangulation: Optional[bool] = True, aPriority: Optional[int] = -1, NbPOnEdge: Optional[int] = 9, MaximalParameter: Optional[float] = 500) -> None: ...
    @overload
    @staticmethod
    def Load(aSelection: SelectMgr_Selection, Origin: SelectMgr_SelectableObject, aShape: TopoDS_Shape, aType: TopAbs_ShapeEnum, theDeflection: float, theDeviationAngle: float, AutoTriangulation: Optional[bool] = True, aPriority: Optional[int] = -1, NbPOnEdge: Optional[int] = 9, MaximalParameter: Optional[float] = 500) -> None: ...
    @staticmethod
    def PreBuildBVH(theSelection: SelectMgr_Selection) -> None: ...

class StdSelect_EdgeFilter(SelectMgr_Filter):
    def __init__(self, Edge: StdSelect_TypeOfEdge) -> None: ...
    def ActsOn(self, aStandardMode: TopAbs_ShapeEnum) -> bool: ...
    def IsOk(self, anobj: SelectMgr_EntityOwner) -> bool: ...
    def SetType(self, aNewType: StdSelect_TypeOfEdge) -> None: ...
    def Type(self) -> StdSelect_TypeOfEdge: ...

class StdSelect_FaceFilter(SelectMgr_Filter):
    def __init__(self, aTypeOfFace: StdSelect_TypeOfFace) -> None: ...
    def ActsOn(self, aStandardMode: TopAbs_ShapeEnum) -> bool: ...
    def IsOk(self, anobj: SelectMgr_EntityOwner) -> bool: ...
    def SetType(self, aNewType: StdSelect_TypeOfFace) -> None: ...
    def Type(self) -> StdSelect_TypeOfFace: ...

class StdSelect_Shape(PrsMgr_PresentableObject):
    def __init__(self, theShape: TopoDS_Shape, theDrawer: Optional[Prs3d_Drawer] = Prs3d_Drawer()) -> None: ...
    def Compute(self, thePrsMgr: PrsMgr_PresentationManager, thePrs: Prs3d_Presentation, theMode: int) -> None: ...
    @overload
    def Shape(self) -> TopoDS_Shape: ...
    @overload
    def Shape(self, theShape: TopoDS_Shape) -> None: ...

class StdSelect_ShapeTypeFilter(SelectMgr_Filter):
    def __init__(self, aType: TopAbs_ShapeEnum) -> None: ...
    def ActsOn(self, aStandardMode: TopAbs_ShapeEnum) -> bool: ...
    def IsOk(self, anobj: SelectMgr_EntityOwner) -> bool: ...
    def Type(self) -> TopAbs_ShapeEnum: ...

# harray1 classes
# harray2 classes
# hsequence classes

stdselect_SetDrawerForBRepOwner = stdselect.SetDrawerForBRepOwner
StdSelect_BRepSelectionTool_ComputeSensitive = StdSelect_BRepSelectionTool.ComputeSensitive
StdSelect_BRepSelectionTool_GetEdgeSensitive = StdSelect_BRepSelectionTool.GetEdgeSensitive
StdSelect_BRepSelectionTool_GetSensitiveForFace = StdSelect_BRepSelectionTool.GetSensitiveForFace
StdSelect_BRepSelectionTool_GetStandardPriority = StdSelect_BRepSelectionTool.GetStandardPriority
StdSelect_BRepSelectionTool_Load = StdSelect_BRepSelectionTool.Load
StdSelect_BRepSelectionTool_Load = StdSelect_BRepSelectionTool.Load
StdSelect_BRepSelectionTool_PreBuildBVH = StdSelect_BRepSelectionTool.PreBuildBVH
