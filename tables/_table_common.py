"""
Here is defined the Table class (common).

:Author:   Ivan Vilata i Balaguer
:Contact:  ivan@selidor.net
:Created:  2007-02-15
:License:  BSD
:Revision: $Id$
"""

from tables.path import joinPath, splitPath

def _indexNameOf(node):
    return '_i_%s' % node._v_name

def _indexPathnameOf(node):
    nodeParentPath = splitPath(node._v_pathname)[0]
    return joinPath(nodeParentPath, _indexNameOf(node))

def _indexPathnameOfColumn(table, colpathname):
    return joinPath(_indexPathnameOf(table), colpathname)

def _tableColumnPathnameOfIndex(indexpathname):
    names = indexpathname.split("/")
    for i, name in enumerate(names):
        if name.startswith('_i_'):
            break
    tablepathname = "/".join(names[:i])+"/"+name[3:]
    colpathname = "/".join(names[i+1:])
    return (tablepathname, colpathname)
