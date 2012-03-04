#!/usr/bin/python

from qsElement import *
from qsLayout import *
from qsSkin import *

class qsPage:
    def __init__(self, title='', skin=qsSkin(), root=qsLayoutStack()):
        self.root = root
        self.skin = skin
        self.title = title

    def css(self):
        str = self.skin.cssPage()
        str += self.root.css(set())
        return str

    def html(self):
        str = u"""<html>
<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml" >
<head>
"""
        str += '<title>' + self.title + '</title>\n'
        str += '<style media="screen" type="text/css">\n'
        str += self.css()
        str += '</style>\n'

        str += "<body>\n"+self.root.html()+u"</body>\n</html>"
        return str

if __name__ == "__main__":
    page = qsPage()

    sidebar = qsSidebar(id="sidebar")
    sidebar.addSection(qsBox(id="color", title="Color", body="Hallo"))
    sidebar.addSection(qsBox(id="empty", body="Box only"))

    mainText = qsBox(id="mainText", body="Lorem larim lipso")
    mainText.setMargin(12)
    mainText.setBackgroundColor('#888')
    mainText.setBorder('3px solid #842')

    layoutCol = qsLayoutFixColumn()
    layoutCol.setMargin('auto')
    layoutCol.addColumn(sidebar, 160)
    layoutCol.addColumn(mainText, 410)
    layoutCol.addColumn(qsBox(id="right1", body="right 1"), width=60, alignRight=True)
    layoutCol.addColumn(qsBox(id="right2", body="right 2"), width=128, alignRight=True)
    layoutCol.setBorder('1px solid black')

    page.root.addLayout(layoutCol)
    print page.html()
