#!/usr/bin/python

def qsRenderCssElement(style):
    str = u''
    for i in style:
        str += "%s:%s;" % (i, style[i])
    return str

def qsRenderCss(styleDict):
    str = u''
    for part in styleDict:
        str += part + ' {'
        str += qsRenderCssElement(styleDict[part])
        str += '}\n'
    return str

def parsePx(str):
    if not str: return 0
    i = str.index('px')
    if 'px' not in str:
        raise RuntimeError('only px width supported')
    return int(str[:i].rsplit(None,1)[-1])

class qsElement:
    style = dict()
    def __init__(self,id=None,cl=None):
        self.id=id
        self.cl=cl
        self.style=dict()
        self.children=[]
    def html(self):
        str=u''
        for c in self.children:
            str+=c.html()
        return str
    def htmlOpen(self, tag='div'):
        str=u'<%s'%tag
        if self.id: str+=' id="%s"'%self.id
        if self.cl: str+=' class="%s"'%self.cl
        if self.style:
            str+=' style="%s"' % qsRenderCssElement(self.style)
        str+='>\n'
        return str
    def htmlClose(self, tag='div'):
        return u'</%s>\n'%tag
    def css(self, classesDone):
        str=u''
        if self.__class__.__name__ not in classesDone:
            if self.__class__.style:
                str += qsRenderCss(self.__class__.style)
        classesDone.add(self.__class__.__name__)
        for c in self.children:
            str += c.css(classesDone)
        return str
    def width(self):
        return parsePx(self.style.get('width') or self.__class__.style.get('width'))
    def totalWidth(self):
        w=parsePx(self.style.get('width') or self.__class__.style.get('width'))
        for i in ['padding','border','margin','outline']:
            w+=parsePx(self.style.get(i) or self.__class__.style.get(i))*2
            w+=parsePx(self.style.get(i+'-left') or self.__class__.style.get(i+'-left'))
            w+=parsePx(self.style.get(i+'-right') or self.__class__.style.get(i+'-right'))
        return w
    def setBackgroundColor(self, val):
        self.style['background-color']=val
    def setBorder(self, val):
        self.style['border']=val
    def setMargin(self, val):
        if type(val)==int:
            self.style['margin'] = '%dpx'%val
        else:
            self.style['margin'] = val
    def setMarginTop(self, val):
        self.style['margin-top'] = '%dpx'%val
    def setMarginBottom(self, val):
        self.style['margin-bottom'] = '%dpx'%val
    def setMarginLeft(self, val):
        self.style['margin-left'] = '%dpx'%val
    def setMarginRight(self, val):
        self.style['margin-right'] = '%dpx'%val

class qsBox(qsElement):
    style = {
        #'.qsBox': '',
        '.qsBox-title': {
            'color': '#777',
            'background': 'url(boxtopbg.gif) repeat-x left top',
            'padding': '3px',
            'font-size': '12px',
            'font-weight': 'bold',
            'border-left': '1px solid #ddd',
            'border-right': '1px solid #ddd',
            'border-top': '1px solid #ddd',
        },
        '.qsBox-body': {
            'border-left': '1px solid #ddd',
            'border-right': '1px solid #ddd',
            'border-bottom': '1px solid #ddd',
            'padding': '8px',
            'overflow': 'auto',
        }
    }
    def __init__(self, id=None, title='', body=''):
        qsElement.__init__(self, id, 'qsBox')
        self.title=title
        self.body=body
    def html(self):
        str=self.htmlOpen()
        if self.title:
            str+='<div class="qsBox-title">' + self.title + '</div>'
        str+='<div class="qsBox-body">' + self.body + '</div>'
        str+=self.htmlClose()
        return str

class qsSidebar(qsElement):
    def __init__(self, id=None):
        qsElement.__init__(self, id)
    def addSection(self, section):
        self.children.append(section)
    def html(self):
        str=self.htmlOpen()
        for s in self.children:
            str+=s.html()
        str+=self.htmlClose()
        return str
