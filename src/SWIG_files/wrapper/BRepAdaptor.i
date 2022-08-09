/*
Copyright 2008-2020 Thomas Paviot (tpaviot@gmail.com)

This file is part of pythonOCC.
pythonOCC is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

pythonOCC is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License
along with pythonOCC.  If not, see <http://www.gnu.org/licenses/>.
*/
%define BREPADAPTORDOCSTRING
"BRepAdaptor, see official documentation at https://www.opencascade.com/doc/occt-7.6.0/refman/html/package_brepadaptor.html"
%enddef
%module (package="OCC.Core", docstring=BREPADAPTORDOCSTRING) BRepAdaptor


%{
#ifdef WNT
#pragma warning(disable : 4716)
#endif
%}

%include ../common/CommonIncludes.i
%include ../common/ExceptionCatcher.i
%include ../common/FunctionTransformers.i
%include ../common/EnumTemplates.i
%include ../common/Operators.i
%include ../common/OccHandle.i


%{
#include<BRepAdaptor_module.hxx>

//Dependencies
#include<Standard_module.hxx>
#include<NCollection_module.hxx>
#include<Adaptor3d_module.hxx>
#include<TopoDS_module.hxx>
#include<Geom_module.hxx>
#include<gp_module.hxx>
#include<GeomAbs_module.hxx>
#include<TColStd_module.hxx>
#include<GeomAdaptor_module.hxx>
#include<Geom2dAdaptor_module.hxx>
#include<TopLoc_module.hxx>
#include<Geom2d_module.hxx>
#include<Message_module.hxx>
#include<Adaptor2d_module.hxx>
#include<TColgp_module.hxx>
#include<TColStd_module.hxx>
#include<TCollection_module.hxx>
#include<Storage_module.hxx>
%};
%import Standard.i
%import NCollection.i
%import Adaptor3d.i
%import TopoDS.i
%import Geom.i
%import gp.i
%import GeomAbs.i
%import TColStd.i
%import GeomAdaptor.i
%import Geom2dAdaptor.i

%pythoncode {
from enum import IntEnum
from OCC.Core.Exception import *
};

/* public enums */
/* end public enums declaration */

/* python proy classes for enums */
%pythoncode {
};
/* end python proxy for enums */

/* handles */
%wrap_handle(BRepAdaptor_CompCurve)
%wrap_handle(BRepAdaptor_Curve)
%wrap_handle(BRepAdaptor_Curve2d)
%wrap_handle(BRepAdaptor_Surface)
%wrap_handle(BRepAdaptor_HArray1OfCurve)
/* end handles declaration */

/* templates */
%template(BRepAdaptor_Array1OfCurve) NCollection_Array1<BRepAdaptor_Curve>;

%extend NCollection_Array1<BRepAdaptor_Curve> {
    %pythoncode {
    def __getitem__(self, index):
        if index + self.Lower() > self.Upper():
            raise IndexError("index out of range")
        else:
            return self.Value(index + self.Lower())

    def __setitem__(self, index, value):
        if index + self.Lower() > self.Upper():
            raise IndexError("index out of range")
        else:
            self.SetValue(index + self.Lower(), value)

    def __len__(self):
        return self.Length()

    def __iter__(self):
        self.low = self.Lower()
        self.up = self.Upper()
        self.current = self.Lower() - 1
        return self

    def next(self):
        if self.current >= self.Upper():
            raise StopIteration
        else:
            self.current += 1
        return self.Value(self.current)

    __next__ = next
    }
};
/* end templates declaration */

/* typedefs */
typedef NCollection_Array1<BRepAdaptor_Curve> BRepAdaptor_Array1OfCurve;
/* end typedefs declaration */

/******************************
* class BRepAdaptor_CompCurve *
******************************/
class BRepAdaptor_CompCurve : public Adaptor3d_Curve {
	public:
		/****************** BRepAdaptor_CompCurve ******************/
		/**** md5 signature: c1152ba591cae8b160ace1ba10d270dc ****/
		%feature("compactdefaultargs") BRepAdaptor_CompCurve;
		%feature("autodoc", "Creates an undefined curve with no wire loaded.

Returns
-------
None
") BRepAdaptor_CompCurve;
		 BRepAdaptor_CompCurve();

		/****************** BRepAdaptor_CompCurve ******************/
		/**** md5 signature: 536f827323fa633aa2cdc2b24e992a20 ****/
		%feature("compactdefaultargs") BRepAdaptor_CompCurve;
		%feature("autodoc", "No available documentation.

Parameters
----------
W: TopoDS_Wire
KnotByCurvilinearAbcissa: bool,optional
	default value is Standard_False

Returns
-------
None
") BRepAdaptor_CompCurve;
		 BRepAdaptor_CompCurve(const TopoDS_Wire & W, const Standard_Boolean KnotByCurvilinearAbcissa = Standard_False);

		/****************** BRepAdaptor_CompCurve ******************/
		/**** md5 signature: d6d730d5ed59cc103614b39691bdbfd1 ****/
		%feature("compactdefaultargs") BRepAdaptor_CompCurve;
		%feature("autodoc", "Creates a curve to access the geometry of edge <w>.

Parameters
----------
W: TopoDS_Wire
KnotByCurvilinearAbcissa: bool
First: float
Last: float
Tol: float

Returns
-------
None
") BRepAdaptor_CompCurve;
		 BRepAdaptor_CompCurve(const TopoDS_Wire & W, const Standard_Boolean KnotByCurvilinearAbcissa, const Standard_Real First, const Standard_Real Last, const Standard_Real Tol);

		/****************** BSpline ******************/
		/**** md5 signature: 3ccc0d851302bffb5de6344e3eb3e58d ****/
		%feature("compactdefaultargs") BSpline;
		%feature("autodoc", "No available documentation.

Returns
-------
opencascade::handle<Geom_BSplineCurve>
") BSpline;
		opencascade::handle<Geom_BSplineCurve> BSpline();

		/****************** Bezier ******************/
		/**** md5 signature: 092280fc6ee0e7104fbbe3460d73e83c ****/
		%feature("compactdefaultargs") Bezier;
		%feature("autodoc", "No available documentation.

Returns
-------
opencascade::handle<Geom_BezierCurve>
") Bezier;
		opencascade::handle<Geom_BezierCurve> Bezier();

		/****************** Circle ******************/
		/**** md5 signature: 5f382e7a6af009845ea6e16d54814298 ****/
		%feature("compactdefaultargs") Circle;
		%feature("autodoc", "No available documentation.

Returns
-------
gp_Circ
") Circle;
		gp_Circ Circle();

		/****************** Continuity ******************/
		/**** md5 signature: 9381b370dfdd50af7f1b79ce202f0c6f ****/
		%feature("compactdefaultargs") Continuity;
		%feature("autodoc", "No available documentation.

Returns
-------
GeomAbs_Shape
") Continuity;
		GeomAbs_Shape Continuity();

		/****************** D0 ******************/
		/**** md5 signature: 5f7d08d8d17afc516aac9ef64bf9711f ****/
		%feature("compactdefaultargs") D0;
		%feature("autodoc", "Computes the point of parameter u.

Parameters
----------
U: float
P: gp_Pnt

Returns
-------
None
") D0;
		void D0(const Standard_Real U, gp_Pnt & P);

		/****************** D1 ******************/
		/**** md5 signature: 1dc830ec49a945a61cde5e5c027b78d7 ****/
		%feature("compactdefaultargs") D1;
		%feature("autodoc", "Computes the point of parameter u on the curve with its first derivative. raised if the continuity of the current interval is not c1.

Parameters
----------
U: float
P: gp_Pnt
V: gp_Vec

Returns
-------
None
") D1;
		void D1(const Standard_Real U, gp_Pnt & P, gp_Vec & V);

		/****************** D2 ******************/
		/**** md5 signature: a694b4ba68c0fd83fbac79f945cb5d8c ****/
		%feature("compactdefaultargs") D2;
		%feature("autodoc", "Returns the point p of parameter u, the first and second derivatives v1 and v2. raised if the continuity of the current interval is not c2.

Parameters
----------
U: float
P: gp_Pnt
V1: gp_Vec
V2: gp_Vec

Returns
-------
None
") D2;
		void D2(const Standard_Real U, gp_Pnt & P, gp_Vec & V1, gp_Vec & V2);

		/****************** D3 ******************/
		/**** md5 signature: cf1c3b5fe7af9d5c183c1b16b21c43f1 ****/
		%feature("compactdefaultargs") D3;
		%feature("autodoc", "Returns the point p of parameter u, the first, the second and the third derivative. raised if the continuity of the current interval is not c3.

Parameters
----------
U: float
P: gp_Pnt
V1: gp_Vec
V2: gp_Vec
V3: gp_Vec

Returns
-------
None
") D3;
		void D3(const Standard_Real U, gp_Pnt & P, gp_Vec & V1, gp_Vec & V2, gp_Vec & V3);

		/****************** DN ******************/
		/**** md5 signature: 0d4a3e2fc2b4b03d2a49e0796a487efb ****/
		%feature("compactdefaultargs") DN;
		%feature("autodoc", "The returned vector gives the value of the derivative for the order of derivation n. raised if the continuity of the current interval is not cn. raised if n < 1.

Parameters
----------
U: float
N: int

Returns
-------
gp_Vec
") DN;
		gp_Vec DN(const Standard_Real U, const Standard_Integer N);

		/****************** Degree ******************/
		/**** md5 signature: 5ce473e72cc7bb935a667f4c839dab09 ****/
		%feature("compactdefaultargs") Degree;
		%feature("autodoc", "No available documentation.

Returns
-------
int
") Degree;
		Standard_Integer Degree();

		/****************** Edge ******************/
		/**** md5 signature: f73dfc9c9040a29acf2262eb8cd9a8ea ****/
		%feature("compactdefaultargs") Edge;
		%feature("autodoc", "Returns an edge and one parameter on them corresponding to the parameter u.

Parameters
----------
U: float
E: TopoDS_Edge

Returns
-------
UonE: float
") Edge;
		void Edge(const Standard_Real U, TopoDS_Edge & E, Standard_Real &OutValue);

		/****************** Ellipse ******************/
		/**** md5 signature: e9a77f14e9bbca29370202de404ea9c1 ****/
		%feature("compactdefaultargs") Ellipse;
		%feature("autodoc", "No available documentation.

Returns
-------
gp_Elips
") Ellipse;
		gp_Elips Ellipse();

		/****************** FirstParameter ******************/
		/**** md5 signature: eb9ebe94572bd67588fe8811eac261fb ****/
		%feature("compactdefaultargs") FirstParameter;
		%feature("autodoc", "No available documentation.

Returns
-------
float
") FirstParameter;
		Standard_Real FirstParameter();

		/****************** GetType ******************/
		/**** md5 signature: 0ad61dcbb5497908c1b536e766f0fcb9 ****/
		%feature("compactdefaultargs") GetType;
		%feature("autodoc", "No available documentation.

Returns
-------
GeomAbs_CurveType
") GetType;
		GeomAbs_CurveType GetType();

		/****************** Hyperbola ******************/
		/**** md5 signature: a96ca49b2ad017b35bb09d0b86cb690d ****/
		%feature("compactdefaultargs") Hyperbola;
		%feature("autodoc", "No available documentation.

Returns
-------
gp_Hypr
") Hyperbola;
		gp_Hypr Hyperbola();

		/****************** Initialize ******************/
		/**** md5 signature: 084e04b2711058308ee9c6ffc8589f6f ****/
		%feature("compactdefaultargs") Initialize;
		%feature("autodoc", "Sets the wire <w>.

Parameters
----------
W: TopoDS_Wire
KnotByCurvilinearAbcissa: bool

Returns
-------
None
") Initialize;
		void Initialize(const TopoDS_Wire & W, const Standard_Boolean KnotByCurvilinearAbcissa);

		/****************** Initialize ******************/
		/**** md5 signature: 3f7ce5fd6aa0f7b3bdaf45694f156692 ****/
		%feature("compactdefaultargs") Initialize;
		%feature("autodoc", "Sets wire <w> and trimmed parameter.

Parameters
----------
W: TopoDS_Wire
KnotByCurvilinearAbcissa: bool
First: float
Last: float
Tol: float

Returns
-------
None
") Initialize;
		void Initialize(const TopoDS_Wire & W, const Standard_Boolean KnotByCurvilinearAbcissa, const Standard_Real First, const Standard_Real Last, const Standard_Real Tol);

		/****************** Intervals ******************/
		/**** md5 signature: fc573cb56cf1a9c05ee189fd913ff6f5 ****/
		%feature("compactdefaultargs") Intervals;
		%feature("autodoc", "Stores in <t> the parameters bounding the intervals of continuity <s>. //! the array must provide enough room to accommodate for the parameters. i.e. t.length() > nbintervals().

Parameters
----------
T: TColStd_Array1OfReal
S: GeomAbs_Shape

Returns
-------
None
") Intervals;
		void Intervals(TColStd_Array1OfReal & T, const GeomAbs_Shape S);

		/****************** IsClosed ******************/
		/**** md5 signature: 00978070ec4cb5f00d1d002a8d5d3763 ****/
		%feature("compactdefaultargs") IsClosed;
		%feature("autodoc", "No available documentation.

Returns
-------
bool
") IsClosed;
		Standard_Boolean IsClosed();

		/****************** IsPeriodic ******************/
		/**** md5 signature: 15e3ccfd3ad4ae42959489f7f64aa8ca ****/
		%feature("compactdefaultargs") IsPeriodic;
		%feature("autodoc", "No available documentation.

Returns
-------
bool
") IsPeriodic;
		Standard_Boolean IsPeriodic();

		/****************** IsRational ******************/
		/**** md5 signature: 82ca56fad113156125f40128b25c0d8e ****/
		%feature("compactdefaultargs") IsRational;
		%feature("autodoc", "No available documentation.

Returns
-------
bool
") IsRational;
		Standard_Boolean IsRational();

		/****************** LastParameter ******************/
		/**** md5 signature: cb4925a2d4a451ceec8f6ad486530f9c ****/
		%feature("compactdefaultargs") LastParameter;
		%feature("autodoc", "No available documentation.

Returns
-------
float
") LastParameter;
		Standard_Real LastParameter();

		/****************** Line ******************/
		/**** md5 signature: cf28f5541e4e744dd8038e2a9ac75a8f ****/
		%feature("compactdefaultargs") Line;
		%feature("autodoc", "No available documentation.

Returns
-------
gp_Lin
") Line;
		gp_Lin Line();

		/****************** NbIntervals ******************/
		/**** md5 signature: 8ce4f61bff96d1ce0784028b47edd8dc ****/
		%feature("compactdefaultargs") NbIntervals;
		%feature("autodoc", "Returns the number of intervals for continuity <s>. may be one if continuity(me) >= <s>.

Parameters
----------
S: GeomAbs_Shape

Returns
-------
int
") NbIntervals;
		Standard_Integer NbIntervals(const GeomAbs_Shape S);

		/****************** NbKnots ******************/
		/**** md5 signature: 841663cbf96bec3b939f307c52df6c7c ****/
		%feature("compactdefaultargs") NbKnots;
		%feature("autodoc", "No available documentation.

Returns
-------
int
") NbKnots;
		Standard_Integer NbKnots();

		/****************** NbPoles ******************/
		/**** md5 signature: 52e5fadf897540545847ef59cc0ba942 ****/
		%feature("compactdefaultargs") NbPoles;
		%feature("autodoc", "No available documentation.

Returns
-------
int
") NbPoles;
		Standard_Integer NbPoles();

		/****************** Parabola ******************/
		/**** md5 signature: 68860abab63fd184ea5c7eb97f0762c1 ****/
		%feature("compactdefaultargs") Parabola;
		%feature("autodoc", "No available documentation.

Returns
-------
gp_Parab
") Parabola;
		gp_Parab Parabola();

		/****************** Period ******************/
		/**** md5 signature: 88909a321398632744c0d6841580c626 ****/
		%feature("compactdefaultargs") Period;
		%feature("autodoc", "No available documentation.

Returns
-------
float
") Period;
		Standard_Real Period();

		/****************** Resolution ******************/
		/**** md5 signature: cc4a4d9111fadd20ad48e62bc4df1579 ****/
		%feature("compactdefaultargs") Resolution;
		%feature("autodoc", "Returns the parametric resolution.

Parameters
----------
R3d: float

Returns
-------
float
") Resolution;
		Standard_Real Resolution(const Standard_Real R3d);

		/****************** Trim ******************/
		/**** md5 signature: 40a46ffe7379c6d919968b501b8343a5 ****/
		%feature("compactdefaultargs") Trim;
		%feature("autodoc", "Returns a curve equivalent of <self> between parameters <first> and <last>. <tol> is used to test for 3d points confusion. if <first> >= <last>.

Parameters
----------
First: float
Last: float
Tol: float

Returns
-------
opencascade::handle<Adaptor3d_Curve>
") Trim;
		opencascade::handle<Adaptor3d_Curve> Trim(const Standard_Real First, const Standard_Real Last, const Standard_Real Tol);

		/****************** Value ******************/
		/**** md5 signature: d7f310c73762cbaa285ace0a141bc7bf ****/
		%feature("compactdefaultargs") Value;
		%feature("autodoc", "Computes the point of parameter u on the curve.

Parameters
----------
U: float

Returns
-------
gp_Pnt
") Value;
		gp_Pnt Value(const Standard_Real U);

		/****************** Wire ******************/
		/**** md5 signature: 066765b94f5225dad05ab95ae3f8b503 ****/
		%feature("compactdefaultargs") Wire;
		%feature("autodoc", "Returns the wire.

Returns
-------
TopoDS_Wire
") Wire;
		const TopoDS_Wire Wire();

};


%make_alias(BRepAdaptor_CompCurve)

%extend BRepAdaptor_CompCurve {
	%pythoncode {
	__repr__ = _dumps_object
	}
};

/**************************
* class BRepAdaptor_Curve *
**************************/
class BRepAdaptor_Curve : public Adaptor3d_Curve {
	public:
		/****************** BRepAdaptor_Curve ******************/
		/**** md5 signature: 36916a7ac88f4dc1e560c43c25da0671 ****/
		%feature("compactdefaultargs") BRepAdaptor_Curve;
		%feature("autodoc", "Creates an undefined curve with no edge loaded.

Returns
-------
None
") BRepAdaptor_Curve;
		 BRepAdaptor_Curve();

		/****************** BRepAdaptor_Curve ******************/
		/**** md5 signature: 740e451b59f60726263aab98ec1f1316 ****/
		%feature("compactdefaultargs") BRepAdaptor_Curve;
		%feature("autodoc", "Creates a curve to access the geometry of edge <e>.

Parameters
----------
E: TopoDS_Edge

Returns
-------
None
") BRepAdaptor_Curve;
		 BRepAdaptor_Curve(const TopoDS_Edge & E);

		/****************** BRepAdaptor_Curve ******************/
		/**** md5 signature: c4ad88c445ddb172d9a61b5a673cf024 ****/
		%feature("compactdefaultargs") BRepAdaptor_Curve;
		%feature("autodoc", "Creates a curve to access the geometry of edge <e>. the geometry will be computed using the parametric curve of <e> on the face <f>. an error is raised if the edge does not have a pcurve on the face.

Parameters
----------
E: TopoDS_Edge
F: TopoDS_Face

Returns
-------
None
") BRepAdaptor_Curve;
		 BRepAdaptor_Curve(const TopoDS_Edge & E, const TopoDS_Face & F);

		/****************** BSpline ******************/
		/**** md5 signature: 3ccc0d851302bffb5de6344e3eb3e58d ****/
		%feature("compactdefaultargs") BSpline;
		%feature("autodoc", "Warning: this will make a copy of the bspline curve since it applies to it mytsrf. be careful when using this method.

Returns
-------
opencascade::handle<Geom_BSplineCurve>
") BSpline;
		opencascade::handle<Geom_BSplineCurve> BSpline();

		/****************** Bezier ******************/
		/**** md5 signature: 092280fc6ee0e7104fbbe3460d73e83c ****/
		%feature("compactdefaultargs") Bezier;
		%feature("autodoc", "Warning: this will make a copy of the bezier curve since it applies to it mytsrf. be careful when using this method.

Returns
-------
opencascade::handle<Geom_BezierCurve>
") Bezier;
		opencascade::handle<Geom_BezierCurve> Bezier();

		/****************** Circle ******************/
		/**** md5 signature: 5f382e7a6af009845ea6e16d54814298 ****/
		%feature("compactdefaultargs") Circle;
		%feature("autodoc", "No available documentation.

Returns
-------
gp_Circ
") Circle;
		gp_Circ Circle();

		/****************** Continuity ******************/
		/**** md5 signature: 9381b370dfdd50af7f1b79ce202f0c6f ****/
		%feature("compactdefaultargs") Continuity;
		%feature("autodoc", "No available documentation.

Returns
-------
GeomAbs_Shape
") Continuity;
		GeomAbs_Shape Continuity();

		/****************** Curve ******************/
		/**** md5 signature: f572f2bd5ed01577163560ac880dd538 ****/
		%feature("compactdefaultargs") Curve;
		%feature("autodoc", "Returns the curve of the edge.

Returns
-------
GeomAdaptor_Curve
") Curve;
		const GeomAdaptor_Curve & Curve();

		/****************** CurveOnSurface ******************/
		/**** md5 signature: f06c54ea203f128f90114fb7bd684518 ****/
		%feature("compactdefaultargs") CurveOnSurface;
		%feature("autodoc", "Returns the curveonsurface of the edge.

Returns
-------
Adaptor3d_CurveOnSurface
") CurveOnSurface;
		const Adaptor3d_CurveOnSurface & CurveOnSurface();

		/****************** D0 ******************/
		/**** md5 signature: 5f7d08d8d17afc516aac9ef64bf9711f ****/
		%feature("compactdefaultargs") D0;
		%feature("autodoc", "Computes the point of parameter u.

Parameters
----------
U: float
P: gp_Pnt

Returns
-------
None
") D0;
		void D0(const Standard_Real U, gp_Pnt & P);

		/****************** D1 ******************/
		/**** md5 signature: 1dc830ec49a945a61cde5e5c027b78d7 ****/
		%feature("compactdefaultargs") D1;
		%feature("autodoc", "Computes the point of parameter u on the curve with its first derivative. raised if the continuity of the current interval is not c1.

Parameters
----------
U: float
P: gp_Pnt
V: gp_Vec

Returns
-------
None
") D1;
		void D1(const Standard_Real U, gp_Pnt & P, gp_Vec & V);

		/****************** D2 ******************/
		/**** md5 signature: a694b4ba68c0fd83fbac79f945cb5d8c ****/
		%feature("compactdefaultargs") D2;
		%feature("autodoc", "Returns the point p of parameter u, the first and second derivatives v1 and v2. raised if the continuity of the current interval is not c2.

Parameters
----------
U: float
P: gp_Pnt
V1: gp_Vec
V2: gp_Vec

Returns
-------
None
") D2;
		void D2(const Standard_Real U, gp_Pnt & P, gp_Vec & V1, gp_Vec & V2);

		/****************** D3 ******************/
		/**** md5 signature: cf1c3b5fe7af9d5c183c1b16b21c43f1 ****/
		%feature("compactdefaultargs") D3;
		%feature("autodoc", "Returns the point p of parameter u, the first, the second and the third derivative. raised if the continuity of the current interval is not c3.

Parameters
----------
U: float
P: gp_Pnt
V1: gp_Vec
V2: gp_Vec
V3: gp_Vec

Returns
-------
None
") D3;
		void D3(const Standard_Real U, gp_Pnt & P, gp_Vec & V1, gp_Vec & V2, gp_Vec & V3);

		/****************** DN ******************/
		/**** md5 signature: 0d4a3e2fc2b4b03d2a49e0796a487efb ****/
		%feature("compactdefaultargs") DN;
		%feature("autodoc", "The returned vector gives the value of the derivative for the order of derivation n. raised if the continuity of the current interval is not cn. raised if n < 1.

Parameters
----------
U: float
N: int

Returns
-------
gp_Vec
") DN;
		gp_Vec DN(const Standard_Real U, const Standard_Integer N);

		/****************** Degree ******************/
		/**** md5 signature: 5ce473e72cc7bb935a667f4c839dab09 ****/
		%feature("compactdefaultargs") Degree;
		%feature("autodoc", "No available documentation.

Returns
-------
int
") Degree;
		Standard_Integer Degree();

		/****************** Edge ******************/
		/**** md5 signature: be590cff987799d8b7c28083399d0e9f ****/
		%feature("compactdefaultargs") Edge;
		%feature("autodoc", "Returns the edge.

Returns
-------
TopoDS_Edge
") Edge;
		const TopoDS_Edge Edge();

		/****************** Ellipse ******************/
		/**** md5 signature: e9a77f14e9bbca29370202de404ea9c1 ****/
		%feature("compactdefaultargs") Ellipse;
		%feature("autodoc", "No available documentation.

Returns
-------
gp_Elips
") Ellipse;
		gp_Elips Ellipse();

		/****************** FirstParameter ******************/
		/**** md5 signature: eb9ebe94572bd67588fe8811eac261fb ****/
		%feature("compactdefaultargs") FirstParameter;
		%feature("autodoc", "No available documentation.

Returns
-------
float
") FirstParameter;
		Standard_Real FirstParameter();

		/****************** GetType ******************/
		/**** md5 signature: 0ad61dcbb5497908c1b536e766f0fcb9 ****/
		%feature("compactdefaultargs") GetType;
		%feature("autodoc", "No available documentation.

Returns
-------
GeomAbs_CurveType
") GetType;
		GeomAbs_CurveType GetType();

		/****************** Hyperbola ******************/
		/**** md5 signature: a96ca49b2ad017b35bb09d0b86cb690d ****/
		%feature("compactdefaultargs") Hyperbola;
		%feature("autodoc", "No available documentation.

Returns
-------
gp_Hypr
") Hyperbola;
		gp_Hypr Hyperbola();

		/****************** Initialize ******************/
		/**** md5 signature: b0b8cb0790e5e63c5a8b3b133b757731 ****/
		%feature("compactdefaultargs") Initialize;
		%feature("autodoc", "Sets the curve <self> to access the geometry of edge <e>.

Parameters
----------
E: TopoDS_Edge

Returns
-------
None
") Initialize;
		void Initialize(const TopoDS_Edge & E);

		/****************** Initialize ******************/
		/**** md5 signature: cf258179577adbc75b4efbc5847934f6 ****/
		%feature("compactdefaultargs") Initialize;
		%feature("autodoc", "Sets the curve <self> to access the geometry of edge <e>. the geometry will be computed using the parametric curve of <e> on the face <f>. an error is raised if the edge does not have a pcurve on the face.

Parameters
----------
E: TopoDS_Edge
F: TopoDS_Face

Returns
-------
None
") Initialize;
		void Initialize(const TopoDS_Edge & E, const TopoDS_Face & F);

		/****************** Intervals ******************/
		/**** md5 signature: fc573cb56cf1a9c05ee189fd913ff6f5 ****/
		%feature("compactdefaultargs") Intervals;
		%feature("autodoc", "Stores in <t> the parameters bounding the intervals of continuity <s>. //! the array must provide enough room to accommodate for the parameters. i.e. t.length() > nbintervals().

Parameters
----------
T: TColStd_Array1OfReal
S: GeomAbs_Shape

Returns
-------
None
") Intervals;
		void Intervals(TColStd_Array1OfReal & T, const GeomAbs_Shape S);

		/****************** Is3DCurve ******************/
		/**** md5 signature: f5d6aa26c69fccbb40636aa757b15284 ****/
		%feature("compactdefaultargs") Is3DCurve;
		%feature("autodoc", "Returns true if the edge geometry is computed from a 3d curve.

Returns
-------
bool
") Is3DCurve;
		Standard_Boolean Is3DCurve();

		/****************** IsClosed ******************/
		/**** md5 signature: 00978070ec4cb5f00d1d002a8d5d3763 ****/
		%feature("compactdefaultargs") IsClosed;
		%feature("autodoc", "No available documentation.

Returns
-------
bool
") IsClosed;
		Standard_Boolean IsClosed();

		/****************** IsCurveOnSurface ******************/
		/**** md5 signature: 3910efc6129939aa50e8be5bbd9c78d4 ****/
		%feature("compactdefaultargs") IsCurveOnSurface;
		%feature("autodoc", "Returns true if the edge geometry is computed from a pcurve on a surface.

Returns
-------
bool
") IsCurveOnSurface;
		Standard_Boolean IsCurveOnSurface();

		/****************** IsPeriodic ******************/
		/**** md5 signature: 15e3ccfd3ad4ae42959489f7f64aa8ca ****/
		%feature("compactdefaultargs") IsPeriodic;
		%feature("autodoc", "No available documentation.

Returns
-------
bool
") IsPeriodic;
		Standard_Boolean IsPeriodic();

		/****************** IsRational ******************/
		/**** md5 signature: 82ca56fad113156125f40128b25c0d8e ****/
		%feature("compactdefaultargs") IsRational;
		%feature("autodoc", "No available documentation.

Returns
-------
bool
") IsRational;
		Standard_Boolean IsRational();

		/****************** LastParameter ******************/
		/**** md5 signature: cb4925a2d4a451ceec8f6ad486530f9c ****/
		%feature("compactdefaultargs") LastParameter;
		%feature("autodoc", "No available documentation.

Returns
-------
float
") LastParameter;
		Standard_Real LastParameter();

		/****************** Line ******************/
		/**** md5 signature: cf28f5541e4e744dd8038e2a9ac75a8f ****/
		%feature("compactdefaultargs") Line;
		%feature("autodoc", "No available documentation.

Returns
-------
gp_Lin
") Line;
		gp_Lin Line();

		/****************** NbIntervals ******************/
		/**** md5 signature: 8ce4f61bff96d1ce0784028b47edd8dc ****/
		%feature("compactdefaultargs") NbIntervals;
		%feature("autodoc", "Returns the number of intervals for continuity <s>. may be one if continuity(me) >= <s>.

Parameters
----------
S: GeomAbs_Shape

Returns
-------
int
") NbIntervals;
		Standard_Integer NbIntervals(const GeomAbs_Shape S);

		/****************** NbKnots ******************/
		/**** md5 signature: 841663cbf96bec3b939f307c52df6c7c ****/
		%feature("compactdefaultargs") NbKnots;
		%feature("autodoc", "No available documentation.

Returns
-------
int
") NbKnots;
		Standard_Integer NbKnots();

		/****************** NbPoles ******************/
		/**** md5 signature: 52e5fadf897540545847ef59cc0ba942 ****/
		%feature("compactdefaultargs") NbPoles;
		%feature("autodoc", "No available documentation.

Returns
-------
int
") NbPoles;
		Standard_Integer NbPoles();

		/****************** OffsetCurve ******************/
		/**** md5 signature: c9712770a031ed315e762ca33ff3eddd ****/
		%feature("compactdefaultargs") OffsetCurve;
		%feature("autodoc", "No available documentation.

Returns
-------
opencascade::handle<Geom_OffsetCurve>
") OffsetCurve;
		opencascade::handle<Geom_OffsetCurve> OffsetCurve();

		/****************** Parabola ******************/
		/**** md5 signature: 68860abab63fd184ea5c7eb97f0762c1 ****/
		%feature("compactdefaultargs") Parabola;
		%feature("autodoc", "No available documentation.

Returns
-------
gp_Parab
") Parabola;
		gp_Parab Parabola();

		/****************** Period ******************/
		/**** md5 signature: 88909a321398632744c0d6841580c626 ****/
		%feature("compactdefaultargs") Period;
		%feature("autodoc", "No available documentation.

Returns
-------
float
") Period;
		Standard_Real Period();

		/****************** Reset ******************/
		/**** md5 signature: 7beb446fe26b948f797f8de87e46c23d ****/
		%feature("compactdefaultargs") Reset;
		%feature("autodoc", "Reset currently loaded curve (undone load()).

Returns
-------
None
") Reset;
		void Reset();

		/****************** Resolution ******************/
		/**** md5 signature: cc4a4d9111fadd20ad48e62bc4df1579 ****/
		%feature("compactdefaultargs") Resolution;
		%feature("autodoc", "Returns the parametric resolution.

Parameters
----------
R3d: float

Returns
-------
float
") Resolution;
		Standard_Real Resolution(const Standard_Real R3d);

		/****************** Tolerance ******************/
		/**** md5 signature: 9e5775014410d884d1a1adc1cd47930b ****/
		%feature("compactdefaultargs") Tolerance;
		%feature("autodoc", "Returns the edge tolerance.

Returns
-------
float
") Tolerance;
		Standard_Real Tolerance();

		/****************** Trim ******************/
		/**** md5 signature: 40a46ffe7379c6d919968b501b8343a5 ****/
		%feature("compactdefaultargs") Trim;
		%feature("autodoc", "Returns a curve equivalent of <self> between parameters <first> and <last>. <tol> is used to test for 3d points confusion. if <first> >= <last>.

Parameters
----------
First: float
Last: float
Tol: float

Returns
-------
opencascade::handle<Adaptor3d_Curve>
") Trim;
		opencascade::handle<Adaptor3d_Curve> Trim(const Standard_Real First, const Standard_Real Last, const Standard_Real Tol);

		/****************** Trsf ******************/
		/**** md5 signature: 97ab79d36bbfac916eee88e8b5acb351 ****/
		%feature("compactdefaultargs") Trsf;
		%feature("autodoc", "Returns the coordinate system of the curve.

Returns
-------
gp_Trsf
") Trsf;
		const gp_Trsf Trsf();

		/****************** Value ******************/
		/**** md5 signature: d7f310c73762cbaa285ace0a141bc7bf ****/
		%feature("compactdefaultargs") Value;
		%feature("autodoc", "Computes the point of parameter u on the curve.

Parameters
----------
U: float

Returns
-------
gp_Pnt
") Value;
		gp_Pnt Value(const Standard_Real U);

};


%make_alias(BRepAdaptor_Curve)

%extend BRepAdaptor_Curve {
	%pythoncode {
	__repr__ = _dumps_object
	}
};

/****************************
* class BRepAdaptor_Curve2d *
****************************/
class BRepAdaptor_Curve2d : public Geom2dAdaptor_Curve {
	public:
		/****************** BRepAdaptor_Curve2d ******************/
		/**** md5 signature: b7ed47cccfb977bc356e474765ba5816 ****/
		%feature("compactdefaultargs") BRepAdaptor_Curve2d;
		%feature("autodoc", "Creates an uninitialized curve2d.

Returns
-------
None
") BRepAdaptor_Curve2d;
		 BRepAdaptor_Curve2d();

		/****************** BRepAdaptor_Curve2d ******************/
		/**** md5 signature: e386e29ae63edd3b069e2ac2448ce78a ****/
		%feature("compactdefaultargs") BRepAdaptor_Curve2d;
		%feature("autodoc", "Creates with the pcurve of <e> on <f>.

Parameters
----------
E: TopoDS_Edge
F: TopoDS_Face

Returns
-------
None
") BRepAdaptor_Curve2d;
		 BRepAdaptor_Curve2d(const TopoDS_Edge & E, const TopoDS_Face & F);

		/****************** Edge ******************/
		/**** md5 signature: be590cff987799d8b7c28083399d0e9f ****/
		%feature("compactdefaultargs") Edge;
		%feature("autodoc", "Returns the edge.

Returns
-------
TopoDS_Edge
") Edge;
		const TopoDS_Edge Edge();

		/****************** Face ******************/
		/**** md5 signature: 91e216ebeb76e55c73eb9e179241a6ff ****/
		%feature("compactdefaultargs") Face;
		%feature("autodoc", "Returns the face.

Returns
-------
TopoDS_Face
") Face;
		const TopoDS_Face Face();

		/****************** Initialize ******************/
		/**** md5 signature: cf258179577adbc75b4efbc5847934f6 ****/
		%feature("compactdefaultargs") Initialize;
		%feature("autodoc", "Initialize with the pcurve of <e> on <f>.

Parameters
----------
E: TopoDS_Edge
F: TopoDS_Face

Returns
-------
None
") Initialize;
		void Initialize(const TopoDS_Edge & E, const TopoDS_Face & F);

};


%make_alias(BRepAdaptor_Curve2d)

%extend BRepAdaptor_Curve2d {
	%pythoncode {
	__repr__ = _dumps_object
	}
};

/****************************
* class BRepAdaptor_Surface *
****************************/
class BRepAdaptor_Surface : public Adaptor3d_Surface {
	public:
		/****************** BRepAdaptor_Surface ******************/
		/**** md5 signature: fd2163b01d125040a3f6f06ce9213655 ****/
		%feature("compactdefaultargs") BRepAdaptor_Surface;
		%feature("autodoc", "Creates an undefined surface with no face loaded.

Returns
-------
None
") BRepAdaptor_Surface;
		 BRepAdaptor_Surface();

		/****************** BRepAdaptor_Surface ******************/
		/**** md5 signature: 0cf16f4fea8b7b02de8e7d0a77cdc16a ****/
		%feature("compactdefaultargs") BRepAdaptor_Surface;
		%feature("autodoc", "Creates a surface to access the geometry of <f>. if <restriction> is true the parameter range is the parameter range in the uv space of the restriction.

Parameters
----------
F: TopoDS_Face
R: bool,optional
	default value is Standard_True

Returns
-------
None
") BRepAdaptor_Surface;
		 BRepAdaptor_Surface(const TopoDS_Face & F, const Standard_Boolean R = Standard_True);

		/****************** AxeOfRevolution ******************/
		/**** md5 signature: ba4a8d5fbd6cead47ee1b295e5469d5d ****/
		%feature("compactdefaultargs") AxeOfRevolution;
		%feature("autodoc", "No available documentation.

Returns
-------
gp_Ax1
") AxeOfRevolution;
		gp_Ax1 AxeOfRevolution();

		/****************** BSpline ******************/
		/**** md5 signature: 7edfedec29b3e090d1dbb1c560f9218f ****/
		%feature("compactdefaultargs") BSpline;
		%feature("autodoc", "Warning : this will make a copy of the bspline surface since it applies to it the mytsrf transformation be careful when using this method.

Returns
-------
opencascade::handle<Geom_BSplineSurface>
") BSpline;
		opencascade::handle<Geom_BSplineSurface> BSpline();

		/****************** BasisCurve ******************/
		/**** md5 signature: 3da13dd15bd6f8a74a4a076b13266260 ****/
		%feature("compactdefaultargs") BasisCurve;
		%feature("autodoc", "Only for surfaceofextrusion and surfaceofrevolution warning: this will make a copy of the underlying curve since it applies to it the transformation mytrsf. be careful when using this method.

Returns
-------
opencascade::handle<Adaptor3d_Curve>
") BasisCurve;
		opencascade::handle<Adaptor3d_Curve> BasisCurve();

		/****************** BasisSurface ******************/
		/**** md5 signature: de63a8a43356a45f5d395e828ec0014c ****/
		%feature("compactdefaultargs") BasisSurface;
		%feature("autodoc", "No available documentation.

Returns
-------
opencascade::handle<Adaptor3d_Surface>
") BasisSurface;
		opencascade::handle<Adaptor3d_Surface> BasisSurface();

		/****************** Bezier ******************/
		/**** md5 signature: 98b7293dc91af28a1a57c0bfbd1e467a ****/
		%feature("compactdefaultargs") Bezier;
		%feature("autodoc", "No available documentation.

Returns
-------
opencascade::handle<Geom_BezierSurface>
") Bezier;
		opencascade::handle<Geom_BezierSurface> Bezier();

		/****************** ChangeSurface ******************/
		/**** md5 signature: ead718e69fe53e8fd677c1b9c64ff5a3 ****/
		%feature("compactdefaultargs") ChangeSurface;
		%feature("autodoc", "Returns the surface.

Returns
-------
GeomAdaptor_Surface
") ChangeSurface;
		GeomAdaptor_Surface & ChangeSurface();

		/****************** Cone ******************/
		/**** md5 signature: 3ce87f79e83a129f74e88ef746e3e34b ****/
		%feature("compactdefaultargs") Cone;
		%feature("autodoc", "No available documentation.

Returns
-------
gp_Cone
") Cone;
		gp_Cone Cone();

		/****************** Cylinder ******************/
		/**** md5 signature: fdc0e133b47b8d299b834e1b65638963 ****/
		%feature("compactdefaultargs") Cylinder;
		%feature("autodoc", "No available documentation.

Returns
-------
gp_Cylinder
") Cylinder;
		gp_Cylinder Cylinder();

		/****************** D0 ******************/
		/**** md5 signature: 909f7ecc223d561155c9c3ba4b8e7b64 ****/
		%feature("compactdefaultargs") D0;
		%feature("autodoc", "Computes the point of parameters u,v on the surface.

Parameters
----------
U: float
V: float
P: gp_Pnt

Returns
-------
None
") D0;
		void D0(const Standard_Real U, const Standard_Real V, gp_Pnt & P);

		/****************** D1 ******************/
		/**** md5 signature: 0868b105367e01c443402a5728aa3395 ****/
		%feature("compactdefaultargs") D1;
		%feature("autodoc", "Computes the point and the first derivatives on the surface. raised if the continuity of the current intervals is not c1.

Parameters
----------
U: float
V: float
P: gp_Pnt
D1U: gp_Vec
D1V: gp_Vec

Returns
-------
None
") D1;
		void D1(const Standard_Real U, const Standard_Real V, gp_Pnt & P, gp_Vec & D1U, gp_Vec & D1V);

		/****************** D2 ******************/
		/**** md5 signature: 5bdb029d3f1561c55d7ab1d1b0b0282a ****/
		%feature("compactdefaultargs") D2;
		%feature("autodoc", "Computes the point, the first and second derivatives on the surface. raised if the continuity of the current intervals is not c2.

Parameters
----------
U: float
V: float
P: gp_Pnt
D1U: gp_Vec
D1V: gp_Vec
D2U: gp_Vec
D2V: gp_Vec
D2UV: gp_Vec

Returns
-------
None
") D2;
		void D2(const Standard_Real U, const Standard_Real V, gp_Pnt & P, gp_Vec & D1U, gp_Vec & D1V, gp_Vec & D2U, gp_Vec & D2V, gp_Vec & D2UV);

		/****************** D3 ******************/
		/**** md5 signature: 2fbd4d1b6bb5f19034b05b5a6e0ddec0 ****/
		%feature("compactdefaultargs") D3;
		%feature("autodoc", "Computes the point, the first, second and third derivatives on the surface. raised if the continuity of the current intervals is not c3.

Parameters
----------
U: float
V: float
P: gp_Pnt
D1U: gp_Vec
D1V: gp_Vec
D2U: gp_Vec
D2V: gp_Vec
D2UV: gp_Vec
D3U: gp_Vec
D3V: gp_Vec
D3UUV: gp_Vec
D3UVV: gp_Vec

Returns
-------
None
") D3;
		void D3(const Standard_Real U, const Standard_Real V, gp_Pnt & P, gp_Vec & D1U, gp_Vec & D1V, gp_Vec & D2U, gp_Vec & D2V, gp_Vec & D2UV, gp_Vec & D3U, gp_Vec & D3V, gp_Vec & D3UUV, gp_Vec & D3UVV);

		/****************** DN ******************/
		/**** md5 signature: 78200f5fa5a4060f4022c2e3d9d8ac0e ****/
		%feature("compactdefaultargs") DN;
		%feature("autodoc", "Computes the derivative of order nu in the direction u and nv in the direction v at the point p(u, v). raised if the current u interval is not not cnu and the current v interval is not cnv. raised if nu + nv < 1 or nu < 0 or nv < 0.

Parameters
----------
U: float
V: float
Nu: int
Nv: int

Returns
-------
gp_Vec
") DN;
		gp_Vec DN(const Standard_Real U, const Standard_Real V, const Standard_Integer Nu, const Standard_Integer Nv);

		/****************** Direction ******************/
		/**** md5 signature: 701909e88752dfbf540944de6bad9f3a ****/
		%feature("compactdefaultargs") Direction;
		%feature("autodoc", "No available documentation.

Returns
-------
gp_Dir
") Direction;
		gp_Dir Direction();

		/****************** Face ******************/
		/**** md5 signature: 91e216ebeb76e55c73eb9e179241a6ff ****/
		%feature("compactdefaultargs") Face;
		%feature("autodoc", "Returns the face.

Returns
-------
TopoDS_Face
") Face;
		const TopoDS_Face Face();

		/****************** FirstUParameter ******************/
		/**** md5 signature: 9f6a318ef39f30d9051cc243f6edc9ac ****/
		%feature("compactdefaultargs") FirstUParameter;
		%feature("autodoc", "No available documentation.

Returns
-------
float
") FirstUParameter;
		virtual Standard_Real FirstUParameter();

		/****************** FirstVParameter ******************/
		/**** md5 signature: 026c8b687e22be56263a275efcb1a191 ****/
		%feature("compactdefaultargs") FirstVParameter;
		%feature("autodoc", "No available documentation.

Returns
-------
float
") FirstVParameter;
		virtual Standard_Real FirstVParameter();

		/****************** GetType ******************/
		/**** md5 signature: 936170b269276a5a12605a71a86272c0 ****/
		%feature("compactdefaultargs") GetType;
		%feature("autodoc", "Returns the type of the surface : plane, cylinder, cone, sphere, torus, beziersurface, bsplinesurface, surfaceofrevolution, surfaceofextrusion, othersurface.

Returns
-------
GeomAbs_SurfaceType
") GetType;
		virtual GeomAbs_SurfaceType GetType();

		/****************** Initialize ******************/
		/**** md5 signature: f3aeecb0e2fbd866889f168f070cf082 ****/
		%feature("compactdefaultargs") Initialize;
		%feature("autodoc", "Sets the surface to the geometry of <f>.

Parameters
----------
F: TopoDS_Face
Restriction: bool,optional
	default value is Standard_True

Returns
-------
None
") Initialize;
		void Initialize(const TopoDS_Face & F, const Standard_Boolean Restriction = Standard_True);

		/****************** IsUClosed ******************/
		/**** md5 signature: 3889881a8bccaf01bdc63482d847fec7 ****/
		%feature("compactdefaultargs") IsUClosed;
		%feature("autodoc", "No available documentation.

Returns
-------
bool
") IsUClosed;
		virtual Standard_Boolean IsUClosed();

		/****************** IsUPeriodic ******************/
		/**** md5 signature: baaa80f0fba4fab1ff0458c41067535b ****/
		%feature("compactdefaultargs") IsUPeriodic;
		%feature("autodoc", "No available documentation.

Returns
-------
bool
") IsUPeriodic;
		virtual Standard_Boolean IsUPeriodic();

		/****************** IsURational ******************/
		/**** md5 signature: 972bde55bb1931ba89cfd38a75b346b4 ****/
		%feature("compactdefaultargs") IsURational;
		%feature("autodoc", "No available documentation.

Returns
-------
bool
") IsURational;
		virtual Standard_Boolean IsURational();

		/****************** IsVClosed ******************/
		/**** md5 signature: f5d8b2178f14695d158c648b5d67e50b ****/
		%feature("compactdefaultargs") IsVClosed;
		%feature("autodoc", "No available documentation.

Returns
-------
bool
") IsVClosed;
		virtual Standard_Boolean IsVClosed();

		/****************** IsVPeriodic ******************/
		/**** md5 signature: a7b7752f1716f49329b3486241deda0e ****/
		%feature("compactdefaultargs") IsVPeriodic;
		%feature("autodoc", "No available documentation.

Returns
-------
bool
") IsVPeriodic;
		virtual Standard_Boolean IsVPeriodic();

		/****************** IsVRational ******************/
		/**** md5 signature: bfc5bd774a4b38bf6259615a711f8ed2 ****/
		%feature("compactdefaultargs") IsVRational;
		%feature("autodoc", "No available documentation.

Returns
-------
bool
") IsVRational;
		virtual Standard_Boolean IsVRational();

		/****************** LastUParameter ******************/
		/**** md5 signature: 3133997e2ee3ea09c0b46a884e833ca4 ****/
		%feature("compactdefaultargs") LastUParameter;
		%feature("autodoc", "No available documentation.

Returns
-------
float
") LastUParameter;
		virtual Standard_Real LastUParameter();

		/****************** LastVParameter ******************/
		/**** md5 signature: f1f64233932dd0768276d78ffb537717 ****/
		%feature("compactdefaultargs") LastVParameter;
		%feature("autodoc", "No available documentation.

Returns
-------
float
") LastVParameter;
		virtual Standard_Real LastVParameter();

		/****************** NbUIntervals ******************/
		/**** md5 signature: ae4875076949dd10d5b3e8aa53673562 ****/
		%feature("compactdefaultargs") NbUIntervals;
		%feature("autodoc", "If necessary, breaks the surface in u intervals of continuity <s>. and returns the number of intervals.

Parameters
----------
theSh: GeomAbs_Shape

Returns
-------
int
") NbUIntervals;
		virtual Standard_Integer NbUIntervals(const GeomAbs_Shape theSh);

		/****************** NbUKnots ******************/
		/**** md5 signature: 9c52bcf67cce67b26f246c3aa4ea551f ****/
		%feature("compactdefaultargs") NbUKnots;
		%feature("autodoc", "No available documentation.

Returns
-------
int
") NbUKnots;
		virtual Standard_Integer NbUKnots();

		/****************** NbUPoles ******************/
		/**** md5 signature: 8d31152e70dd85bb21fb36dbd5b33693 ****/
		%feature("compactdefaultargs") NbUPoles;
		%feature("autodoc", "No available documentation.

Returns
-------
int
") NbUPoles;
		virtual Standard_Integer NbUPoles();

		/****************** NbVIntervals ******************/
		/**** md5 signature: f8d85deebab1e39694985284c6a9f17e ****/
		%feature("compactdefaultargs") NbVIntervals;
		%feature("autodoc", "If necessary, breaks the surface in v intervals of continuity <s>. and returns the number of intervals.

Parameters
----------
theSh: GeomAbs_Shape

Returns
-------
int
") NbVIntervals;
		virtual Standard_Integer NbVIntervals(const GeomAbs_Shape theSh);

		/****************** NbVKnots ******************/
		/**** md5 signature: 6aef7952062b9c9994e4e5162b5eecc2 ****/
		%feature("compactdefaultargs") NbVKnots;
		%feature("autodoc", "No available documentation.

Returns
-------
int
") NbVKnots;
		virtual Standard_Integer NbVKnots();

		/****************** NbVPoles ******************/
		/**** md5 signature: c198f9b4e351d69009dae4cc79544fc2 ****/
		%feature("compactdefaultargs") NbVPoles;
		%feature("autodoc", "No available documentation.

Returns
-------
int
") NbVPoles;
		virtual Standard_Integer NbVPoles();

		/****************** OffsetValue ******************/
		/**** md5 signature: ae23f5f41fc62b65137ff41b8ee27c47 ****/
		%feature("compactdefaultargs") OffsetValue;
		%feature("autodoc", "No available documentation.

Returns
-------
float
") OffsetValue;
		Standard_Real OffsetValue();

		/****************** Plane ******************/
		/**** md5 signature: 38bd3e56cdca70a78cd998154292a430 ****/
		%feature("compactdefaultargs") Plane;
		%feature("autodoc", "No available documentation.

Returns
-------
gp_Pln
") Plane;
		gp_Pln Plane();

		/****************** Sphere ******************/
		/**** md5 signature: d13f3935ec312564a2f8ef1b299ecf9a ****/
		%feature("compactdefaultargs") Sphere;
		%feature("autodoc", "No available documentation.

Returns
-------
gp_Sphere
") Sphere;
		gp_Sphere Sphere();

		/****************** Surface ******************/
		/**** md5 signature: e09b6aa0166ca76f2672af1ac0cf0ae2 ****/
		%feature("compactdefaultargs") Surface;
		%feature("autodoc", "Returns the surface.

Returns
-------
GeomAdaptor_Surface
") Surface;
		const GeomAdaptor_Surface & Surface();

		/****************** Tolerance ******************/
		/**** md5 signature: 9e5775014410d884d1a1adc1cd47930b ****/
		%feature("compactdefaultargs") Tolerance;
		%feature("autodoc", "Returns the face tolerance.

Returns
-------
float
") Tolerance;
		Standard_Real Tolerance();

		/****************** Torus ******************/
		/**** md5 signature: 13ce946397b0f1bcfd3f38f215bbadac ****/
		%feature("compactdefaultargs") Torus;
		%feature("autodoc", "No available documentation.

Returns
-------
gp_Torus
") Torus;
		gp_Torus Torus();

		/****************** Trsf ******************/
		/**** md5 signature: 97ab79d36bbfac916eee88e8b5acb351 ****/
		%feature("compactdefaultargs") Trsf;
		%feature("autodoc", "Returns the surface coordinate system.

Returns
-------
gp_Trsf
") Trsf;
		const gp_Trsf Trsf();

		/****************** UContinuity ******************/
		/**** md5 signature: 3d5af3bf8bc22c7a70f14bdb9e75696a ****/
		%feature("compactdefaultargs") UContinuity;
		%feature("autodoc", "No available documentation.

Returns
-------
GeomAbs_Shape
") UContinuity;
		virtual GeomAbs_Shape UContinuity();

		/****************** UDegree ******************/
		/**** md5 signature: 2acc7b7f865332e05b9779cd0a953da6 ****/
		%feature("compactdefaultargs") UDegree;
		%feature("autodoc", "No available documentation.

Returns
-------
int
") UDegree;
		virtual Standard_Integer UDegree();

		/****************** UIntervals ******************/
		/**** md5 signature: 5a653f364681c4a5c1065b7e92c5d659 ****/
		%feature("compactdefaultargs") UIntervals;
		%feature("autodoc", "Returns the intervals with the requested continuity in the u direction.

Parameters
----------
T: TColStd_Array1OfReal
S: GeomAbs_Shape

Returns
-------
None
") UIntervals;
		void UIntervals(TColStd_Array1OfReal & T, const GeomAbs_Shape S);

		/****************** UPeriod ******************/
		/**** md5 signature: 9816370c908f909f6185bf5b607b6ed4 ****/
		%feature("compactdefaultargs") UPeriod;
		%feature("autodoc", "No available documentation.

Returns
-------
float
") UPeriod;
		virtual Standard_Real UPeriod();

		/****************** UResolution ******************/
		/**** md5 signature: c908970ed85794b4b55fe21095a41df4 ****/
		%feature("compactdefaultargs") UResolution;
		%feature("autodoc", "Returns the parametric u resolution corresponding to the real space resolution <r3d>.

Parameters
----------
theR3d: float

Returns
-------
float
") UResolution;
		virtual Standard_Real UResolution(const Standard_Real theR3d);

		/****************** UTrim ******************/
		/**** md5 signature: 3604326125cf753b2a6722a946fb54be ****/
		%feature("compactdefaultargs") UTrim;
		%feature("autodoc", "Returns a surface trimmed in the u direction equivalent of <self> between parameters <first> and <last>. <tol> is used to test for 3d points confusion. if <first> >= <last>.

Parameters
----------
First: float
Last: float
Tol: float

Returns
-------
opencascade::handle<Adaptor3d_Surface>
") UTrim;
		opencascade::handle<Adaptor3d_Surface> UTrim(const Standard_Real First, const Standard_Real Last, const Standard_Real Tol);

		/****************** VContinuity ******************/
		/**** md5 signature: a992dce85d001ed1cf99e1672e6d07ff ****/
		%feature("compactdefaultargs") VContinuity;
		%feature("autodoc", "No available documentation.

Returns
-------
GeomAbs_Shape
") VContinuity;
		virtual GeomAbs_Shape VContinuity();

		/****************** VDegree ******************/
		/**** md5 signature: 40f217d7a0d71a97880e9ed212ed6f4e ****/
		%feature("compactdefaultargs") VDegree;
		%feature("autodoc", "No available documentation.

Returns
-------
int
") VDegree;
		virtual Standard_Integer VDegree();

		/****************** VIntervals ******************/
		/**** md5 signature: bf8bef8286fec18f81beea299dd5cb6d ****/
		%feature("compactdefaultargs") VIntervals;
		%feature("autodoc", "Returns the intervals with the requested continuity in the v direction.

Parameters
----------
T: TColStd_Array1OfReal
S: GeomAbs_Shape

Returns
-------
None
") VIntervals;
		void VIntervals(TColStd_Array1OfReal & T, const GeomAbs_Shape S);

		/****************** VPeriod ******************/
		/**** md5 signature: 72036cc062bfffc50fc8cd70671f4f03 ****/
		%feature("compactdefaultargs") VPeriod;
		%feature("autodoc", "No available documentation.

Returns
-------
float
") VPeriod;
		virtual Standard_Real VPeriod();

		/****************** VResolution ******************/
		/**** md5 signature: 6834713e8a40b99362514d586f78d876 ****/
		%feature("compactdefaultargs") VResolution;
		%feature("autodoc", "Returns the parametric v resolution corresponding to the real space resolution <r3d>.

Parameters
----------
theR3d: float

Returns
-------
float
") VResolution;
		virtual Standard_Real VResolution(const Standard_Real theR3d);

		/****************** VTrim ******************/
		/**** md5 signature: d094345261a4439c6edc98b200ea4e3d ****/
		%feature("compactdefaultargs") VTrim;
		%feature("autodoc", "Returns a surface trimmed in the v direction between parameters <first> and <last>. <tol> is used to test for 3d points confusion. if <first> >= <last>.

Parameters
----------
First: float
Last: float
Tol: float

Returns
-------
opencascade::handle<Adaptor3d_Surface>
") VTrim;
		opencascade::handle<Adaptor3d_Surface> VTrim(const Standard_Real First, const Standard_Real Last, const Standard_Real Tol);

		/****************** Value ******************/
		/**** md5 signature: bc01a119296408176c75cc0dfb0636ae ****/
		%feature("compactdefaultargs") Value;
		%feature("autodoc", "Computes the point of parameters u,v on the surface.

Parameters
----------
U: float
V: float

Returns
-------
gp_Pnt
") Value;
		gp_Pnt Value(const Standard_Real U, const Standard_Real V);

};


%make_alias(BRepAdaptor_Surface)

%extend BRepAdaptor_Surface {
	%pythoncode {
	__repr__ = _dumps_object
	}
};

/* harray1 classes */

class BRepAdaptor_HArray1OfCurve : public BRepAdaptor_Array1OfCurve, public Standard_Transient {
  public:
    BRepAdaptor_HArray1OfCurve(const Standard_Integer theLower, const Standard_Integer theUpper);
    BRepAdaptor_HArray1OfCurve(const Standard_Integer theLower, const Standard_Integer theUpper, const BRepAdaptor_Array1OfCurve::value_type& theValue);
    BRepAdaptor_HArray1OfCurve(const BRepAdaptor_Array1OfCurve& theOther);
    const BRepAdaptor_Array1OfCurve& Array1();
    BRepAdaptor_Array1OfCurve& ChangeArray1();
};
%make_alias(BRepAdaptor_HArray1OfCurve)

/* harray2 classes */
/* hsequence classes */
/* class aliases */
%pythoncode {
}
