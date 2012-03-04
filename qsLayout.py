#!/usr/bin/python

from qsElement import qsElement

class qsLayout(qsElement):
    def __init__(self):
        qsElement.__init__(self)

class qsLayoutStack(qsLayout):
    def __init__(self):
        qsLayout.__init__(self)
    def addLayout(self, layout):
        self.children.append(layout)

class qsLayoutFixColumn(qsLayout):
    def __init__(self, width=800):
        qsLayout.__init__(self)
        if type(width)!=int:
            raise RuntimeError('width is not int')
        self.style['width']='%dpx'%width
        self.style['clear']='both'
        self.usedWidth = 0
    def addColumn(self, el, width, id=None, cl=None, alignRight=False):
        if id: el.id=id
        if cl: el.cl=cl
        if type(width)!=int:
            raise RuntimeError('width is not int')
        el.style['width']='%dpx'%width
        self.usedWidth += el.totalWidth()
        if self.usedWidth > self.width():
            raise RuntimeError('Acculmulated column width too large')
        if alignRight:
            el.style['float'] = 'right'
        else:
            el.style['float'] = 'left'
        #el.style['position'] = 'relative'
        el.style['overflow'] = 'hidden'
        self.children.append(el)
    def debug(self):
        print self.usedWidth, self.width()
    def html(self):
        str=self.htmlOpen()
        for column in self.children:
            str+=column.html()
        str+=self.htmlClose()
        return str
