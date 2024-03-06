#pragma once

// python stuff
#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include "structmember.h"

// mcl stuff
#include <mcl/bn_c384_256.h>

/*******************************************************************************
* pymcl.h                                                                      *
*                                                                              *
* Originally written by Jemtaly                                                *
* Licensed under GPLv3                                                         *
* Released 5 March 2024                                                        *
*                                                                              *
* This file contains the types and functions needed to use MCL from Python 3.  *
*******************************************************************************/

// We're going to need a few types
// the G1 type
typedef struct {
    PyObject_HEAD
    mclBnG1 mcl_g1; 
} G1;

G1 *G1_create();
PyObject *G1_new(PyTypeObject *type, PyObject *args, PyObject *kwds);
void G1_dealloc(PyObject *self);

PyMemberDef G1_members[];
PyMethodDef G1_methods[];
PyTypeObject G1Type;

// the G2 type
typedef struct {
    PyObject_HEAD
    mclBnG2 mcl_g2; 
} G2;

G2 *G2_create();
PyObject *G2_new(PyTypeObject *type, PyObject *args, PyObject *kwds);
void G2_dealloc(PyObject *self);

PyMemberDef G2_members[];
PyMethodDef G2_methods[];
PyTypeObject G2Type;

// the GT type
typedef struct {
    PyObject_HEAD
    mclBnGT mcl_gt; 
} GT;

GT *GT_create();
PyObject *GT_new(PyTypeObject *type, PyObject *args, PyObject *kwds);
void GT_dealloc(PyObject *self);

PyMemberDef GT_members[];
PyMethodDef GT_methods[];
PyTypeObject GTType;

// the Fr type
typedef struct {
    PyObject_HEAD
    mclBnFr mcl_fr; 
} Fr;

Fr *Fr_create();
PyObject *Fr_new(PyTypeObject *type, PyObject *args, PyObject *kwds);
void Fr_dealloc(PyObject *self);

PyMemberDef Fr_members[];
PyMethodDef Fr_methods[];
PyTypeObject FrType;
