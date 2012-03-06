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
            raise RuntimeError('Accumulated column width too large')
        if alignRight:
            el.style['float'] = 'right'
        else:
            el.style['float'] = 'left'
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

class qsLayout2ColLeftMenu(qsLayout):
    """
    Layout implementing The 'Left Menu' 2 column Liquid Layout
    See also http://matthewjamestaylor.com/blog/ultimate-2-column-left-menu-pixels.htm
    """
    style = {
	    '.colmask': {
		    'position':'relative',
	        'clear':'both',
	        'float':'left',
            'width':'100%',
		    'overflow':'hidden',
	    },
	    '.leftmenu': {
	    },
        '.leftmenu .colright': {
            'float':'left',
            'width':'200%',
    		'position':'relative',
    		'left':'200px',
            'background':'#fff',
        },
        '.leftmenu .col1wrap': {
	        'float':'right',
	        'width':'50%',
	        'position':'relative',
	        'right':'200px',
	        'padding-bottom':'1em',
	    },
	    '.leftmenu .col1': {
            'margin':'0 15px 0 215px',
	        'position':'relative',
	        'right':'100%',
	        'overflow':'hidden',
	    },
        '.leftmenu .col2': {
            'float':'left',
            'width':'170px',
            'position':'relative',
            'right':'185px',
        }
    }
    def __init__(self):
        qsLayout.__init__(self)
        self.children=[None, None]
        self.cl='colmask leftmenu'
    def setSidebar(self, el, width=170, id=None, cl=None):
        if id: el.id=id
        if cl: el.cl=cl
        el.style['width']='%dpx'%width
        self.children[1]=el
    def setMain(self, el, id=None, cl=None):
        if id: el.id=id
        if cl: el.cl=cl
        self.children[0]=el
    def html(self):
        str=self.htmlOpen()
        str+='<div class="colright"><div class="col1wrap"><div class="col1">'
        str+=self.children[0].html()
        str+='</div></div><div class="col2">'
        str+=self.children[1].html()
        str+='</div></div>'
        str+=self.htmlClose()
        return str

if __name__ == "__main__":
    print qsLayout2ColLeftMenu.__doc__