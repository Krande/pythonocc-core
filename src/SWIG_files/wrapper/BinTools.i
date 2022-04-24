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
%define BINTOOLSDOCSTRING
"BinTools module, see official documentation at
https://www.opencascade.com/doc/occt-7.6.0/refman/html/package_bintools.html"
%enddef
%module (package="OCC.Core", docstring=BINTOOLSDOCSTRING) BinTools


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
#include<BinTools_module.hxx>

//Dependencies
#include<Standard_module.hxx>
#include<NCollection_module.hxx>
#include<TopoDS_module.hxx>
#include<Message_module.hxx>
#include<Geom2d_module.hxx>
#include<Geom_module.hxx>
#include<gp_module.hxx>
#include<TopAbs_module.hxx>
#include<TopLoc_module.hxx>
#include<Message_module.hxx>
#include<CDF_module.hxx>
#include<TColgp_module.hxx>
#include<TColStd_module.hxx>
#include<TCollection_module.hxx>
#include<Storage_module.hxx>
%};
%import Standard.i
%import NCollection.i
%import TopoDS.i
%import Message.i
%import Geom2d.i
%import Geom.i
%import gp.i
%import TopAbs.i
%import TopLoc.i

%pythoncode {
from enum import IntEnum
from OCC.Core.Exception import *
};

/* public enums */
enum BinTools_FormatVersion {
	BinTools_FormatVersion_VERSION_1 = 1,
	BinTools_FormatVersion_VERSION_2 = 2,
	BinTools_FormatVersion_VERSION_3 = 3,
	BinTools_FormatVersion_VERSION_4 = 4,
	BinTools_FormatVersion_CURRENT = BinTools_FormatVersion_VERSION_4,
};

enum  {
	BinTools_FormatVersion_LOWER = BinTools_FormatVersion_VERSION_1,
	BinTools_FormatVersion_UPPER = BinTools_FormatVersion_VERSION_4,
};

enum BinTools_ObjectType {
	BinTools_ObjectType_Unknown = 0,
	BinTools_ObjectType_Reference8 = 1,
	BinTools_ObjectType_Reference16 = 2,
	BinTools_ObjectType_Reference32 = 3,
	BinTools_ObjectType_Reference64 = 4,
	BinTools_ObjectType_Location = 5,
	BinTools_ObjectType_SimpleLocation = 6,
	BinTools_ObjectType_EmptyLocation = 7,
	BinTools_ObjectType_LocationEnd = 8,
	BinTools_ObjectType_Curve = 9,
	BinTools_ObjectType_EmptyCurve = 10,
	BinTools_ObjectType_Curve2d = 11,
	BinTools_ObjectType_EmptyCurve2d = 12,
	BinTools_ObjectType_Surface = 13,
	BinTools_ObjectType_EmptySurface = 14,
	BinTools_ObjectType_Polygon3d = 15,
	BinTools_ObjectType_EmptyPolygon3d = 16,
	BinTools_ObjectType_PolygonOnTriangulation = 17,
	BinTools_ObjectType_EmptyPolygonOnTriangulation = 18,
	BinTools_ObjectType_Triangulation = 19,
	BinTools_ObjectType_EmptyTriangulation = 20,
	BinTools_ObjectType_EmptyShape = 198,
	BinTools_ObjectType_EndShape = 199,
};

/* end public enums declaration */

/* python proy classes for enums */
%pythoncode {

class BinTools_FormatVersion(IntEnum):
	BinTools_FormatVersion_VERSION_1 = 1
	BinTools_FormatVersion_VERSION_2 = 2
	BinTools_FormatVersion_VERSION_3 = 3
	BinTools_FormatVersion_VERSION_4 = 4
	BinTools_FormatVersion_CURRENT = BinTools_FormatVersion_VERSION_4
BinTools_FormatVersion_VERSION_1 = BinTools_FormatVersion.BinTools_FormatVersion_VERSION_1
BinTools_FormatVersion_VERSION_2 = BinTools_FormatVersion.BinTools_FormatVersion_VERSION_2
BinTools_FormatVersion_VERSION_3 = BinTools_FormatVersion.BinTools_FormatVersion_VERSION_3
BinTools_FormatVersion_VERSION_4 = BinTools_FormatVersion.BinTools_FormatVersion_VERSION_4
BinTools_FormatVersion_CURRENT = BinTools_FormatVersion.BinTools_FormatVersion_CURRENT

class BinTools_ObjectType(IntEnum):
	BinTools_ObjectType_Unknown = 0
	BinTools_ObjectType_Reference8 = 1
	BinTools_ObjectType_Reference16 = 2
	BinTools_ObjectType_Reference32 = 3
	BinTools_ObjectType_Reference64 = 4
	BinTools_ObjectType_Location = 5
	BinTools_ObjectType_SimpleLocation = 6
	BinTools_ObjectType_EmptyLocation = 7
	BinTools_ObjectType_LocationEnd = 8
	BinTools_ObjectType_Curve = 9
	BinTools_ObjectType_EmptyCurve = 10
	BinTools_ObjectType_Curve2d = 11
	BinTools_ObjectType_EmptyCurve2d = 12
	BinTools_ObjectType_Surface = 13
	BinTools_ObjectType_EmptySurface = 14
	BinTools_ObjectType_Polygon3d = 15
	BinTools_ObjectType_EmptyPolygon3d = 16
	BinTools_ObjectType_PolygonOnTriangulation = 17
	BinTools_ObjectType_EmptyPolygonOnTriangulation = 18
	BinTools_ObjectType_Triangulation = 19
	BinTools_ObjectType_EmptyTriangulation = 20
	BinTools_ObjectType_EmptyShape = 198
	BinTools_ObjectType_EndShape = 199
BinTools_ObjectType_Unknown = BinTools_ObjectType.BinTools_ObjectType_Unknown
BinTools_ObjectType_Reference8 = BinTools_ObjectType.BinTools_ObjectType_Reference8
BinTools_ObjectType_Reference16 = BinTools_ObjectType.BinTools_ObjectType_Reference16
BinTools_ObjectType_Reference32 = BinTools_ObjectType.BinTools_ObjectType_Reference32
BinTools_ObjectType_Reference64 = BinTools_ObjectType.BinTools_ObjectType_Reference64
BinTools_ObjectType_Location = BinTools_ObjectType.BinTools_ObjectType_Location
BinTools_ObjectType_SimpleLocation = BinTools_ObjectType.BinTools_ObjectType_SimpleLocation
BinTools_ObjectType_EmptyLocation = BinTools_ObjectType.BinTools_ObjectType_EmptyLocation
BinTools_ObjectType_LocationEnd = BinTools_ObjectType.BinTools_ObjectType_LocationEnd
BinTools_ObjectType_Curve = BinTools_ObjectType.BinTools_ObjectType_Curve
BinTools_ObjectType_EmptyCurve = BinTools_ObjectType.BinTools_ObjectType_EmptyCurve
BinTools_ObjectType_Curve2d = BinTools_ObjectType.BinTools_ObjectType_Curve2d
BinTools_ObjectType_EmptyCurve2d = BinTools_ObjectType.BinTools_ObjectType_EmptyCurve2d
BinTools_ObjectType_Surface = BinTools_ObjectType.BinTools_ObjectType_Surface
BinTools_ObjectType_EmptySurface = BinTools_ObjectType.BinTools_ObjectType_EmptySurface
BinTools_ObjectType_Polygon3d = BinTools_ObjectType.BinTools_ObjectType_Polygon3d
BinTools_ObjectType_EmptyPolygon3d = BinTools_ObjectType.BinTools_ObjectType_EmptyPolygon3d
BinTools_ObjectType_PolygonOnTriangulation = BinTools_ObjectType.BinTools_ObjectType_PolygonOnTriangulation
BinTools_ObjectType_EmptyPolygonOnTriangulation = BinTools_ObjectType.BinTools_ObjectType_EmptyPolygonOnTriangulation
BinTools_ObjectType_Triangulation = BinTools_ObjectType.BinTools_ObjectType_Triangulation
BinTools_ObjectType_EmptyTriangulation = BinTools_ObjectType.BinTools_ObjectType_EmptyTriangulation
BinTools_ObjectType_EmptyShape = BinTools_ObjectType.BinTools_ObjectType_EmptyShape
BinTools_ObjectType_EndShape = BinTools_ObjectType.BinTools_ObjectType_EndShape
};
/* end python proxy for enums */

/* handles */
/* end handles declaration */

/* templates */
/* end templates declaration */

/* typedefs */
typedef BinTools_LocationSet * BinTools_LocationSetPtr;
/* end typedefs declaration */

/*****************
* class BinTools *
*****************/
%rename(bintools) BinTools;
class BinTools {
	public:
		/****************** Read ******************/
		/**** md5 signature: 8f3081f8c29c84c71da9267be3a08fa6 ****/
		%feature("compactdefaultargs") Read;
		%feature("autodoc", "Reads a shape from <thefile> and returns it in <theshape>.

Parameters
----------
theShape: TopoDS_Shape
theFile: char *
theRange: Message_ProgressRange,optional
	default value is Message_ProgressRange()

Returns
-------
bool
") Read;
		static Standard_Boolean Read(TopoDS_Shape & theShape, const char * theFile, const Message_ProgressRange & theRange = Message_ProgressRange());

		/****************** Write ******************/
		/**** md5 signature: 3881a3762eede8c671fff2911d095012 ****/
		%feature("compactdefaultargs") Write;
		%feature("autodoc", "Writes the shape to the file in binary format bintools_formatversion_current. @param theshape [in] the shape to write @param thefile [in] the path to file to output shape into @param therange the range of progress indicator to fill in.

Parameters
----------
theShape: TopoDS_Shape
theFile: char *
theRange: Message_ProgressRange,optional
	default value is Message_ProgressRange()

Returns
-------
bool
") Write;
		static Standard_Boolean Write(const TopoDS_Shape & theShape, const char * theFile, const Message_ProgressRange & theRange = Message_ProgressRange());

		/****************** Write ******************/
		/**** md5 signature: b26fc24f9c2e022ffc6d11aa96e8af41 ****/
		%feature("compactdefaultargs") Write;
		%feature("autodoc", "Writes the shape to the file in binary format of specified version. @param theshape [in] the shape to write @param thefile [in] the path to file to output shape into @param thewithtriangles [in] flag which specifies whether to save shape with (true) or without (false) triangles;  has no effect on triangulation-only geometry @param thewithnormals [in] flag which specifies whether to save triangulation with (true) or without (false) normals;  has no effect on triangulation-only geometry @param theversion [in] the bintools format version @param therange  the range of progress indicator to fill in.

Parameters
----------
theShape: TopoDS_Shape
theFile: char *
theWithTriangles: bool
theWithNormals: bool
theVersion: BinTools_FormatVersion
theRange: Message_ProgressRange,optional
	default value is Message_ProgressRange()

Returns
-------
bool
") Write;
		static Standard_Boolean Write(const TopoDS_Shape & theShape, const char * theFile, const Standard_Boolean theWithTriangles, const Standard_Boolean theWithNormals, const BinTools_FormatVersion theVersion, const Message_ProgressRange & theRange = Message_ProgressRange());

};


%extend BinTools {
	%pythoncode {
	__repr__ = _dumps_object
	}
};

/****************************
* class BinTools_Curve2dSet *
****************************/
class BinTools_Curve2dSet {
	public:
		/****************** BinTools_Curve2dSet ******************/
		/**** md5 signature: d70cda135813c59090ea3f4c48ff061f ****/
		%feature("compactdefaultargs") BinTools_Curve2dSet;
		%feature("autodoc", "Returns an empty set of curves.

Returns
-------
None
") BinTools_Curve2dSet;
		 BinTools_Curve2dSet();

		/****************** Add ******************/
		/**** md5 signature: 947264273ed6b5c72eac1f308b1f2487 ****/
		%feature("compactdefaultargs") Add;
		%feature("autodoc", "Incorporate a new curve in the set and returns its index.

Parameters
----------
C: Geom2d_Curve

Returns
-------
int
") Add;
		Standard_Integer Add(const opencascade::handle<Geom2d_Curve> & C);

		/****************** Clear ******************/
		/**** md5 signature: ae54be580b423a6eadbe062e0bdb44c2 ****/
		%feature("compactdefaultargs") Clear;
		%feature("autodoc", "Clears the content of the set.

Returns
-------
None
") Clear;
		void Clear();

		/****************** Curve2d ******************/
		/**** md5 signature: aca04b75893a006fca996d6d157d858d ****/
		%feature("compactdefaultargs") Curve2d;
		%feature("autodoc", "Returns the curve of index <i>.

Parameters
----------
I: int

Returns
-------
opencascade::handle<Geom2d_Curve>
") Curve2d;
		opencascade::handle<Geom2d_Curve> Curve2d(const Standard_Integer I);

		/****************** Index ******************/
		/**** md5 signature: e1559320ddf80ce0263d324c781a3407 ****/
		%feature("compactdefaultargs") Index;
		%feature("autodoc", "Returns the index of <l>.

Parameters
----------
C: Geom2d_Curve

Returns
-------
int
") Index;
		Standard_Integer Index(const opencascade::handle<Geom2d_Curve> & C);


            %feature("autodoc", "1");
            %extend{
                void ReadFromString(std::string src) {
                std::stringstream s(src);
                self->Read(s);}
            };

        %feature("autodoc", "1");
        %extend{
            std::string WriteToString() {
            std::stringstream s;
            self->Write(s);
            return s.str();}
        };
		/****************** WriteCurve2d ******************/
		/**** md5 signature: fb004cea29fe8c8fbe520368a3fabd33 ****/
		%feature("compactdefaultargs") WriteCurve2d;
		%feature("autodoc", "Dumps the curve on the binary stream, that can be read back.

Parameters
----------
C: Geom2d_Curve
OS: BinTools_OStream

Returns
-------
None
") WriteCurve2d;
		static void WriteCurve2d(const opencascade::handle<Geom2d_Curve> & C, BinTools_OStream & OS);

};


%extend BinTools_Curve2dSet {
	%pythoncode {
	__repr__ = _dumps_object

	@methodnotwrapped
	def Dump(self):
		pass
	}
};

/**************************
* class BinTools_CurveSet *
**************************/
class BinTools_CurveSet {
	public:
		/****************** BinTools_CurveSet ******************/
		/**** md5 signature: 704e116f502121bb0a6c7a57e0f9f8ac ****/
		%feature("compactdefaultargs") BinTools_CurveSet;
		%feature("autodoc", "Returns an empty set of curves.

Returns
-------
None
") BinTools_CurveSet;
		 BinTools_CurveSet();

		/****************** Add ******************/
		/**** md5 signature: 4548eacacd2a36c829559b37d6b57411 ****/
		%feature("compactdefaultargs") Add;
		%feature("autodoc", "Incorporate a new curve in the set and returns its index.

Parameters
----------
C: Geom_Curve

Returns
-------
int
") Add;
		Standard_Integer Add(const opencascade::handle<Geom_Curve> & C);

		/****************** Clear ******************/
		/**** md5 signature: ae54be580b423a6eadbe062e0bdb44c2 ****/
		%feature("compactdefaultargs") Clear;
		%feature("autodoc", "Clears the content of the set.

Returns
-------
None
") Clear;
		void Clear();

		/****************** Curve ******************/
		/**** md5 signature: 3509a433898cb7510761da8b37eedb3b ****/
		%feature("compactdefaultargs") Curve;
		%feature("autodoc", "Returns the curve of index <i>.

Parameters
----------
I: int

Returns
-------
opencascade::handle<Geom_Curve>
") Curve;
		opencascade::handle<Geom_Curve> Curve(const Standard_Integer I);

		/****************** Index ******************/
		/**** md5 signature: c53cbf4d0efdfb90843e67e9b32c5252 ****/
		%feature("compactdefaultargs") Index;
		%feature("autodoc", "Returns the index of <l>.

Parameters
----------
C: Geom_Curve

Returns
-------
int
") Index;
		Standard_Integer Index(const opencascade::handle<Geom_Curve> & C);


            %feature("autodoc", "1");
            %extend{
                void ReadFromString(std::string src) {
                std::stringstream s(src);
                self->Read(s);}
            };

        %feature("autodoc", "1");
        %extend{
            std::string WriteToString() {
            std::stringstream s;
            self->Write(s);
            return s.str();}
        };
		/****************** WriteCurve ******************/
		/**** md5 signature: 0fd9a95014467f2918a41d1253d1067c ****/
		%feature("compactdefaultargs") WriteCurve;
		%feature("autodoc", "Dumps the curve on the stream in binary format that can be read back.

Parameters
----------
C: Geom_Curve
OS: BinTools_OStream

Returns
-------
None
") WriteCurve;
		static void WriteCurve(const opencascade::handle<Geom_Curve> & C, BinTools_OStream & OS);

};


%extend BinTools_CurveSet {
	%pythoncode {
	__repr__ = _dumps_object
	}
};

/*************************
* class BinTools_IStream *
*************************/
class BinTools_IStream {
	public:

            %feature("autodoc", "1");
            %extend{
                void BinTools_IStreamFromString(std::string src) {
                std::stringstream s(src);
                self->BinTools_IStream(s);}
            };
		/****************** GoTo ******************/
		/**** md5 signature: 1fe69aacfcc260f4ddb0656b14d66864 ****/
		%feature("compactdefaultargs") GoTo;
		%feature("autodoc", "Moves the current stream position to the given one.

Parameters
----------
thePosition: uint64_t

Returns
-------
None
") GoTo;
		void GoTo(const uint64_t & thePosition);

		/****************** IsReference ******************/
		/**** md5 signature: 11bf38cb98971c9e5ccf25c3e7196288 ****/
		%feature("compactdefaultargs") IsReference;
		%feature("autodoc", "Returns true if the last restored type is one of a reference.

Returns
-------
bool
") IsReference;
		Standard_Boolean IsReference();

		/****************** LastType ******************/
		/**** md5 signature: 66664a4851bd7b26d721095076c1abef ****/
		%feature("compactdefaultargs") LastType;
		%feature("autodoc", "Returns the last read type.

Returns
-------
BinTools_ObjectType
") LastType;
		const BinTools_ObjectType  LastType();

		/****************** Position ******************/
		/**** md5 signature: 64d72ad336abb5bbb5dfa2ec57cd5eb5 ****/
		%feature("compactdefaultargs") Position;
		%feature("autodoc", "Returns the current position in the stream.

Returns
-------
uint64_t
") Position;
		uint64_t Position();

		/****************** ReadBool ******************/
		/**** md5 signature: a4825180ad332e12c5b602c1d17abb29 ****/
		%feature("compactdefaultargs") ReadBool;
		%feature("autodoc", "Reads boolean value from the stream (stored as one byte).

Returns
-------
bool
") ReadBool;
		Standard_Boolean ReadBool();

		/****************** ReadBools ******************/
		/**** md5 signature: 9d72052f894e0f41af2fab24f7804963 ****/
		%feature("compactdefaultargs") ReadBools;
		%feature("autodoc", "Reads 3 boolean values from one byte.

Parameters
----------

Returns
-------
theBool1: bool
theBool2: bool
theBool3: bool
") ReadBools;
		void ReadBools(Standard_Boolean &OutValue, Standard_Boolean &OutValue, Standard_Boolean &OutValue);

		/****************** ReadBools ******************/
		/**** md5 signature: b3cb4234e944d39e648cb25f83aff6dd ****/
		%feature("compactdefaultargs") ReadBools;
		%feature("autodoc", "Reads 7 boolean values from one byte.

Parameters
----------

Returns
-------
theBool1: bool
theBool2: bool
theBool3: bool
theBool4: bool
theBool5: bool
theBool6: bool
theBool7: bool
") ReadBools;
		void ReadBools(Standard_Boolean &OutValue, Standard_Boolean &OutValue, Standard_Boolean &OutValue, Standard_Boolean &OutValue, Standard_Boolean &OutValue, Standard_Boolean &OutValue, Standard_Boolean &OutValue);

		/****************** ReadByte ******************/
		/**** md5 signature: 26883bd0be0109c33d64687a5ad2bba9 ****/
		%feature("compactdefaultargs") ReadByte;
		%feature("autodoc", "Reads byte value from the stream.

Returns
-------
Standard_Byte
") ReadByte;
		Standard_Byte ReadByte();

		/****************** ReadInteger ******************/
		/**** md5 signature: 1a43e2dd899813b8f5851954685ed16e ****/
		%feature("compactdefaultargs") ReadInteger;
		%feature("autodoc", "Reads integer value from the stream.

Returns
-------
int
") ReadInteger;
		Standard_Integer ReadInteger();

		/****************** ReadPnt ******************/
		/**** md5 signature: 6b1c8446a888ab924d279f3b982bd641 ****/
		%feature("compactdefaultargs") ReadPnt;
		%feature("autodoc", "Reads point coordinates value from the stream.

Returns
-------
gp_Pnt
") ReadPnt;
		gp_Pnt ReadPnt();

		/****************** ReadReal ******************/
		/**** md5 signature: 8f4d19bf024cca668dd4f25655169051 ****/
		%feature("compactdefaultargs") ReadReal;
		%feature("autodoc", "Reads real value from the stream.

Returns
-------
float
") ReadReal;
		Standard_Real ReadReal();

		/****************** ReadReference ******************/
		/**** md5 signature: 7bcec36d0ac28f0e16f17c62afe9c643 ****/
		%feature("compactdefaultargs") ReadReference;
		%feature("autodoc", "Reads a reference istream using the last restored type.

Returns
-------
uint64_t
") ReadReference;
		uint64_t ReadReference();

		/****************** ReadShortReal ******************/
		/**** md5 signature: 5dd569c48ee221b4303f448a1388d226 ****/
		%feature("compactdefaultargs") ReadShortReal;
		%feature("autodoc", "Reads short real value from the stream.

Returns
-------
Standard_ShortReal
") ReadShortReal;
		Standard_ShortReal ReadShortReal();

		/****************** ReadType ******************/
		/**** md5 signature: 956b3fca42505e2d622fa6ded352bb0b ****/
		%feature("compactdefaultargs") ReadType;
		%feature("autodoc", "Reads and returns the type.

Returns
-------
BinTools_ObjectType
") ReadType;
		BinTools_ObjectType ReadType();

		/****************** ShapeOrientation ******************/
		/**** md5 signature: 23532024d3ca03be2f94e2e4776b5a46 ****/
		%feature("compactdefaultargs") ShapeOrientation;
		%feature("autodoc", "Returns the shape orientation by the last retrieved type.

Returns
-------
TopAbs_Orientation
") ShapeOrientation;
		TopAbs_Orientation ShapeOrientation();

		/****************** ShapeType ******************/
		/**** md5 signature: ff79d0071ab03bb4d85edf6abfb20e76 ****/
		%feature("compactdefaultargs") ShapeType;
		%feature("autodoc", "Returns the shape type by the last retrieved type.

Returns
-------
TopAbs_ShapeEnum
") ShapeType;
		TopAbs_ShapeEnum ShapeType();

		/****************** Stream ******************/
		/**** md5 signature: 0e084ac680f04f56dd60813f21628f4f ****/
		%feature("compactdefaultargs") Stream;
		%feature("autodoc", "Returns the original istream.

Returns
-------
Standard_IStream
") Stream;
		Standard_IStream & Stream();

		/****************** UpdatePosition ******************/
		/**** md5 signature: d06d6970b3eec4776dcb8f48d798c8c3 ****/
		%feature("compactdefaultargs") UpdatePosition;
		%feature("autodoc", "Makes up to date the myposition because mystream was used outside and position is changed.

Returns
-------
None
") UpdatePosition;
		void UpdatePosition();

};


%extend BinTools_IStream {
	%pythoncode {
	__repr__ = _dumps_object
	}
};

/*****************************
* class BinTools_LocationSet *
*****************************/
class BinTools_LocationSet {
	public:
		/****************** BinTools_LocationSet ******************/
		/**** md5 signature: a107009cfc36014e539e33dde2461af7 ****/
		%feature("compactdefaultargs") BinTools_LocationSet;
		%feature("autodoc", "Returns an empty set of locations.

Returns
-------
None
") BinTools_LocationSet;
		 BinTools_LocationSet();

		/****************** Add ******************/
		/**** md5 signature: 6d3b7662960d74b2d6e66b85d46b59f7 ****/
		%feature("compactdefaultargs") Add;
		%feature("autodoc", "Incorporate a new location in the set and returns its index.

Parameters
----------
L: TopLoc_Location

Returns
-------
int
") Add;
		Standard_Integer Add(const TopLoc_Location & L);

		/****************** Clear ******************/
		/**** md5 signature: ae54be580b423a6eadbe062e0bdb44c2 ****/
		%feature("compactdefaultargs") Clear;
		%feature("autodoc", "Clears the content of the set.

Returns
-------
None
") Clear;
		void Clear();

		/****************** Index ******************/
		/**** md5 signature: fbb01960bb9b443c36d99f6e7b11f6c5 ****/
		%feature("compactdefaultargs") Index;
		%feature("autodoc", "Returns the index of <l>.

Parameters
----------
L: TopLoc_Location

Returns
-------
int
") Index;
		Standard_Integer Index(const TopLoc_Location & L);

		/****************** Location ******************/
		/**** md5 signature: dc46e30cfdcf3a3cf13e5f29298f5163 ****/
		%feature("compactdefaultargs") Location;
		%feature("autodoc", "Returns the location of index <i>.

Parameters
----------
I: int

Returns
-------
TopLoc_Location
") Location;
		const TopLoc_Location & Location(const Standard_Integer I);

		/****************** NbLocations ******************/
		/**** md5 signature: e6c134b8d9aa92e37488cc54961e88e4 ****/
		%feature("compactdefaultargs") NbLocations;
		%feature("autodoc", "Returns number of locations.

Returns
-------
int
") NbLocations;
		Standard_Integer NbLocations();


            %feature("autodoc", "1");
            %extend{
                void ReadFromString(std::string src) {
                std::stringstream s(src);
                self->Read(s);}
            };

        %feature("autodoc", "1");
        %extend{
            std::string WriteToString() {
            std::stringstream s;
            self->Write(s);
            return s.str();}
        };
};


%extend BinTools_LocationSet {
	%pythoncode {
	__repr__ = _dumps_object
	}
};

/*************************
* class BinTools_OStream *
*************************/
class BinTools_OStream {
	public:

        %feature("autodoc", "1");
        %extend{
            std::string BinTools_OStreamToString() {
            std::stringstream s;
            self->BinTools_OStream(s);
            return s.str();}
        };
		/****************** Position ******************/
		/**** md5 signature: eea5cdd19f879bd0fc8bf484a6fea27e ****/
		%feature("compactdefaultargs") Position;
		%feature("autodoc", "Returns the current position of the stream.

Returns
-------
uint64_t
") Position;
		const uint64_t & Position();

		/****************** PutBools ******************/
		/**** md5 signature: 2d4a6a64ad4a530e260efb887baed059 ****/
		%feature("compactdefaultargs") PutBools;
		%feature("autodoc", "Writes 3 booleans as one byte to the stream.

Parameters
----------
theValue1: bool
theValue2: bool
theValue3: bool

Returns
-------
None
") PutBools;
		void PutBools(const Standard_Boolean theValue1, const Standard_Boolean theValue2, const Standard_Boolean theValue3);

		/****************** PutBools ******************/
		/**** md5 signature: af90107804e96e75252eb88b579c548e ****/
		%feature("compactdefaultargs") PutBools;
		%feature("autodoc", "Writes 7 booleans as one byte to the stream.

Parameters
----------
theValue1: bool
theValue2: bool
theValue3: bool
theValue4: bool
theValue5: bool
theValue6: bool
theValue7: bool

Returns
-------
None
") PutBools;
		void PutBools(const Standard_Boolean theValue1, const Standard_Boolean theValue2, const Standard_Boolean theValue3, const Standard_Boolean theValue4, const Standard_Boolean theValue5, const Standard_Boolean theValue6, const Standard_Boolean theValue7);

		/****************** WriteReference ******************/
		/**** md5 signature: 988783a8ada9006b19780d87f93098d9 ****/
		%feature("compactdefaultargs") WriteReference;
		%feature("autodoc", "Writes the reference to the given position (an offset between the current and the given one).

Parameters
----------
thePosition: uint64_t

Returns
-------
None
") WriteReference;
		void WriteReference(const uint64_t & thePosition);

		/****************** WriteShape ******************/
		/**** md5 signature: f95185899ddc51ec95fe4057bbb7a099 ****/
		%feature("compactdefaultargs") WriteShape;
		%feature("autodoc", "Writes an identifier of shape type and orientation into the stream.

Parameters
----------
theType: TopAbs_ShapeEnum
theOrientation: TopAbs_Orientation

Returns
-------
None
") WriteShape;
		void WriteShape(const TopAbs_ShapeEnum & theType, const TopAbs_Orientation & theOrientation);

};


%extend BinTools_OStream {
	%pythoncode {
	__repr__ = _dumps_object
	}
};

/******************************
* class BinTools_ShapeSetBase *
******************************/
class BinTools_ShapeSetBase {
	public:
		/****************** BinTools_ShapeSetBase ******************/
		/**** md5 signature: 5e43c3efb8ab1132c1c4608ac75a31b0 ****/
		%feature("compactdefaultargs") BinTools_ShapeSetBase;
		%feature("autodoc", "A default constructor.

Returns
-------
None
") BinTools_ShapeSetBase;
		 BinTools_ShapeSetBase();

		/****************** Clear ******************/
		/**** md5 signature: ee228ed41450ea46d6b542478ce426ba ****/
		%feature("compactdefaultargs") Clear;
		%feature("autodoc", "Clears the content of the set.

Returns
-------
None
") Clear;
		virtual void Clear();

		/****************** FormatNb ******************/
		/**** md5 signature: 279a4e17d42738d62d3eac08d8631329 ****/
		%feature("compactdefaultargs") FormatNb;
		%feature("autodoc", "Returns the bintools_formatversion.

Returns
-------
int
") FormatNb;
		Standard_Integer FormatNb();

		/****************** IsWithNormals ******************/
		/**** md5 signature: 49f5baecd893691e08f163fb559d8b06 ****/
		%feature("compactdefaultargs") IsWithNormals;
		%feature("autodoc", "Return true if shape should be stored triangulation with normals.

Returns
-------
bool
") IsWithNormals;
		Standard_Boolean IsWithNormals();

		/****************** IsWithTriangles ******************/
		/**** md5 signature: 2adacf1f8e5d4c926108b4db84751e9a ****/
		%feature("compactdefaultargs") IsWithTriangles;
		%feature("autodoc", "Return true if shape should be stored with triangles.

Returns
-------
bool
") IsWithTriangles;
		Standard_Boolean IsWithTriangles();


            %feature("autodoc", "1");
            %extend{
                void ReadFromString(std::string src) {
                std::stringstream s(src);
                self->Read(s);}
            };
		/****************** SetFormatNb ******************/
		/**** md5 signature: efa61c5f0aa586c699f53e1139cd95f9 ****/
		%feature("compactdefaultargs") SetFormatNb;
		%feature("autodoc", "Sets the bintools_formatversion.

Parameters
----------
theFormatNb: int

Returns
-------
None
") SetFormatNb;
		void SetFormatNb(const Standard_Integer theFormatNb);

		/****************** SetWithNormals ******************/
		/**** md5 signature: 9f03f91e56766f46bd17d99a089a0a21 ****/
		%feature("compactdefaultargs") SetWithNormals;
		%feature("autodoc", "Define if shape will be stored triangulation with normals. ignored (always written) if face defines only triangulation (no surface).

Parameters
----------
theWithNormals: bool

Returns
-------
None
") SetWithNormals;
		void SetWithNormals(const Standard_Boolean theWithNormals);

		/****************** SetWithTriangles ******************/
		/**** md5 signature: 7b7f7b1dd0aaac0992d59e75b5df79e1 ****/
		%feature("compactdefaultargs") SetWithTriangles;
		%feature("autodoc", "Define if shape will be stored with triangles. ignored (always written) if face defines only triangulation (no surface).

Parameters
----------
theWithTriangles: bool

Returns
-------
None
") SetWithTriangles;
		void SetWithTriangles(const Standard_Boolean theWithTriangles);


        %feature("autodoc", "1");
        %extend{
            std::string WriteToString() {
            std::stringstream s;
            self->Write(s);
            return s.str();}
        };
};


%extend BinTools_ShapeSetBase {
	%pythoncode {
	__repr__ = _dumps_object
	}
};

/****************************
* class BinTools_SurfaceSet *
****************************/
class BinTools_SurfaceSet {
	public:
		/****************** BinTools_SurfaceSet ******************/
		/**** md5 signature: ea04fcb2e657ae6371aebb78e4178d8d ****/
		%feature("compactdefaultargs") BinTools_SurfaceSet;
		%feature("autodoc", "Returns an empty set of surfaces.

Returns
-------
None
") BinTools_SurfaceSet;
		 BinTools_SurfaceSet();

		/****************** Add ******************/
		/**** md5 signature: 6108c9acf8995214a7cb8b8e5a0b937c ****/
		%feature("compactdefaultargs") Add;
		%feature("autodoc", "Incorporate a new surface in the set and returns its index.

Parameters
----------
S: Geom_Surface

Returns
-------
int
") Add;
		Standard_Integer Add(const opencascade::handle<Geom_Surface> & S);

		/****************** Clear ******************/
		/**** md5 signature: ae54be580b423a6eadbe062e0bdb44c2 ****/
		%feature("compactdefaultargs") Clear;
		%feature("autodoc", "Clears the content of the set.

Returns
-------
None
") Clear;
		void Clear();

		/****************** Index ******************/
		/**** md5 signature: 7fc50802d17ebd7c660284e6560fb7f6 ****/
		%feature("compactdefaultargs") Index;
		%feature("autodoc", "Returns the index of <l>.

Parameters
----------
S: Geom_Surface

Returns
-------
int
") Index;
		Standard_Integer Index(const opencascade::handle<Geom_Surface> & S);


            %feature("autodoc", "1");
            %extend{
                void ReadFromString(std::string src) {
                std::stringstream s(src);
                self->Read(s);}
            };
		/****************** Surface ******************/
		/**** md5 signature: f08a9f2a886e0a3933ae15a38f9b8dda ****/
		%feature("compactdefaultargs") Surface;
		%feature("autodoc", "Returns the surface of index <i>.

Parameters
----------
I: int

Returns
-------
opencascade::handle<Geom_Surface>
") Surface;
		opencascade::handle<Geom_Surface> Surface(const Standard_Integer I);


        %feature("autodoc", "1");
        %extend{
            std::string WriteToString() {
            std::stringstream s;
            self->Write(s);
            return s.str();}
        };
		/****************** WriteSurface ******************/
		/**** md5 signature: 41c510c34876aa6bbad25b27f75b3a30 ****/
		%feature("compactdefaultargs") WriteSurface;
		%feature("autodoc", "Dumps the surface on the stream in binary format that can be read back.

Parameters
----------
S: Geom_Surface
OS: BinTools_OStream

Returns
-------
None
") WriteSurface;
		static void WriteSurface(const opencascade::handle<Geom_Surface> & S, BinTools_OStream & OS);

};


%extend BinTools_SurfaceSet {
	%pythoncode {
	__repr__ = _dumps_object
	}
};

/*****************************
* class BinTools_ShapeReader *
*****************************/
class BinTools_ShapeReader : public BinTools_ShapeSetBase {
	public:
		/****************** BinTools_ShapeReader ******************/
		/**** md5 signature: 0d4b9cf10eed36a00f9df0f855784c98 ****/
		%feature("compactdefaultargs") BinTools_ShapeReader;
		%feature("autodoc", "Initializes a shape reader.

Returns
-------
None
") BinTools_ShapeReader;
		 BinTools_ShapeReader();

		/****************** Clear ******************/
		/**** md5 signature: f671931d03948860d0ead34afbe920aa ****/
		%feature("compactdefaultargs") Clear;
		%feature("autodoc", "Clears the content of the set.

Returns
-------
None
") Clear;
		virtual void Clear();

		/****************** ReadLocation ******************/
		/**** md5 signature: bd5aa45e9ea119dbeec11eb219039ce0 ****/
		%feature("compactdefaultargs") ReadLocation;
		%feature("autodoc", "Reads location from the stream.

Parameters
----------
theStream: BinTools_IStream

Returns
-------
TopLoc_Location *
") ReadLocation;
		const TopLoc_Location * ReadLocation(BinTools_IStream & theStream);

};


%extend BinTools_ShapeReader {
	%pythoncode {
	__repr__ = _dumps_object
	}
};

/**************************
* class BinTools_ShapeSet *
**************************/
class BinTools_ShapeSet : public BinTools_ShapeSetBase {
	public:
		/****************** BinTools_ShapeSet ******************/
		/**** md5 signature: 00998afe0732062ff7e083d4a72a15a0 ****/
		%feature("compactdefaultargs") BinTools_ShapeSet;
		%feature("autodoc", "Builds an empty shapeset. @param thewithtriangles [in] flag to write triangulation data.

Returns
-------
None
") BinTools_ShapeSet;
		 BinTools_ShapeSet();

		/****************** Add ******************/
		/**** md5 signature: 53c72d7ee288afd721c7b0a7e7296012 ****/
		%feature("compactdefaultargs") Add;
		%feature("autodoc", "Stores <s> and its sub-shape. returns the index of <s>. the method addgeometry is called on each sub-shape.

Parameters
----------
S: TopoDS_Shape

Returns
-------
int
") Add;
		Standard_Integer Add(const TopoDS_Shape & S);

		/****************** AddShape ******************/
		/**** md5 signature: c53353d34d3c27129aeecdacd6371580 ****/
		%feature("compactdefaultargs") AddShape;
		%feature("autodoc", "Stores the shape <s>.

Parameters
----------
S: TopoDS_Shape

Returns
-------
None
") AddShape;
		virtual void AddShape(const TopoDS_Shape & S);

		/****************** AddShapes ******************/
		/**** md5 signature: e51de0c8f9d77467626b59e64779aeff ****/
		%feature("compactdefaultargs") AddShapes;
		%feature("autodoc", "Inserts the shape <s2> in the shape <s1>.

Parameters
----------
S1: TopoDS_Shape
S2: TopoDS_Shape

Returns
-------
None
") AddShapes;
		virtual void AddShapes(TopoDS_Shape & S1, const TopoDS_Shape & S2);

		/****************** ChangeLocations ******************/
		/**** md5 signature: 647c90bf8c4ec50f4f4adabd19dff9ef ****/
		%feature("compactdefaultargs") ChangeLocations;
		%feature("autodoc", "No available documentation.

Returns
-------
BinTools_LocationSet
") ChangeLocations;
		BinTools_LocationSet & ChangeLocations();

		/****************** Clear ******************/
		/**** md5 signature: 1badd2d119b64dbdb177834e510c3af9 ****/
		%feature("compactdefaultargs") Clear;
		%feature("autodoc", "Clears the content of the set.

Returns
-------
None
") Clear;
		virtual void Clear();

		/****************** Index ******************/
		/**** md5 signature: 9e94bb6d7b4221be4165f8639cd27d92 ****/
		%feature("compactdefaultargs") Index;
		%feature("autodoc", "Returns the index of <s>.

Parameters
----------
S: TopoDS_Shape

Returns
-------
int
") Index;
		Standard_Integer Index(const TopoDS_Shape & S);

		/****************** Locations ******************/
		/**** md5 signature: 1891bed2b7331683f81d8635ed2a6f3e ****/
		%feature("compactdefaultargs") Locations;
		%feature("autodoc", "No available documentation.

Returns
-------
BinTools_LocationSet
") Locations;
		const BinTools_LocationSet & Locations();

		/****************** NbShapes ******************/
		/**** md5 signature: ea90d1514db96ad18becf0e04a33abf6 ****/
		%feature("compactdefaultargs") NbShapes;
		%feature("autodoc", "Returns number of shapes read from file.

Returns
-------
int
") NbShapes;
		Standard_Integer NbShapes();


            %feature("autodoc", "1");
            %extend{
                void ReadFromString(std::string src) {
                std::stringstream s(src);
                self->Read(s);}
            };

            %feature("autodoc", "1");
            %extend{
                void ReadGeometryFromString(std::string src) {
                std::stringstream s(src);
                self->ReadGeometry(s);}
            };

            %feature("autodoc", "1");
            %extend{
                void ReadPolygon3DFromString(std::string src) {
                std::stringstream s(src);
                self->ReadPolygon3D(s);}
            };

            %feature("autodoc", "1");
            %extend{
                void ReadPolygonOnTriangulationFromString(std::string src) {
                std::stringstream s(src);
                self->ReadPolygonOnTriangulation(s);}
            };

            %feature("autodoc", "1");
            %extend{
                void ReadTriangulationFromString(std::string src) {
                std::stringstream s(src);
                self->ReadTriangulation(s);}
            };
		/****************** Shape ******************/
		/**** md5 signature: e70e8ec038f807ea515f2fa1e45089cf ****/
		%feature("compactdefaultargs") Shape;
		%feature("autodoc", "Returns the sub-shape of index <i>.

Parameters
----------
I: int

Returns
-------
TopoDS_Shape
") Shape;
		const TopoDS_Shape Shape(const Standard_Integer I);


        %feature("autodoc", "1");
        %extend{
            std::string WriteToString() {
            std::stringstream s;
            self->Write(s);
            return s.str();}
        };

        %feature("autodoc", "1");
        %extend{
            std::string WriteGeometryToString() {
            std::stringstream s;
            self->WriteGeometry(s);
            return s.str();}
        };

        %feature("autodoc", "1");
        %extend{
            std::string WritePolygon3DToString() {
            std::stringstream s;
            self->WritePolygon3D(s);
            return s.str();}
        };

        %feature("autodoc", "1");
        %extend{
            std::string WritePolygonOnTriangulationToString() {
            std::stringstream s;
            self->WritePolygonOnTriangulation(s);
            return s.str();}
        };

        %feature("autodoc", "1");
        %extend{
            std::string WriteTriangulationToString() {
            std::stringstream s;
            self->WriteTriangulation(s);
            return s.str();}
        };
};


%extend BinTools_ShapeSet {
	%pythoncode {
	__repr__ = _dumps_object
	}
};

/*****************************
* class BinTools_ShapeWriter *
*****************************/
class BinTools_ShapeWriter : public BinTools_ShapeSetBase {
	public:
		/****************** BinTools_ShapeWriter ******************/
		/**** md5 signature: c3fd1614740ecac6a5e3b29e2072d4db ****/
		%feature("compactdefaultargs") BinTools_ShapeWriter;
		%feature("autodoc", "Builds an empty shapeset. parameter <thewithtriangles> is added for xml persistence.

Returns
-------
None
") BinTools_ShapeWriter;
		 BinTools_ShapeWriter();

		/****************** Clear ******************/
		/**** md5 signature: f671931d03948860d0ead34afbe920aa ****/
		%feature("compactdefaultargs") Clear;
		%feature("autodoc", "Clears the content of the set.

Returns
-------
None
") Clear;
		virtual void Clear();

		/****************** WriteLocation ******************/
		/**** md5 signature: 650139b9f368324efb64446489116d9f ****/
		%feature("compactdefaultargs") WriteLocation;
		%feature("autodoc", "Writes location to the stream (all the needed sub-information or reference if it is already used).

Parameters
----------
theStream: BinTools_OStream
theLocation: TopLoc_Location

Returns
-------
None
") WriteLocation;
		virtual void WriteLocation(BinTools_OStream & theStream, const TopLoc_Location & theLocation);

};


%extend BinTools_ShapeWriter {
	%pythoncode {
	__repr__ = _dumps_object
	}
};

/* harray1 classes */
/* harray2 classes */
/* hsequence classes */
/* class aliases */
%pythoncode {
}
