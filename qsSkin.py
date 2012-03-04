#!/usr/bin/python

class qsSkin:
    def __init__(self):
        self.parts = dict()

        # Reset everything
        self.parts['body'] = {
            'margin': '0',
            'padding': '0',
            'border': '0',
            'width': '100%',
            'min-width': '800px',
            'font-family': 'verdana,helvetica,arial,sans-serif',
            'font-size': '12px',
            'background': '#FFF',
            'color': '#000',
        }
        self.parts['h1,h2,h3'] = {
            'margin': '0',
            'padding': '0',
        }
        self.parts['p'] = {
            'margin': '0',
            'padding': '0',
        }
        self.parts['img'] = {
            'margin': '0',
	        'border': '0',
            'vertical-align': 'top',
        }
        self.parts['ul'] = {
            'padding': '0',
	        'margin': '0',
            'list-style': 'none',
        }
        self.parts['a:link'] = { 'color': '#039' }
        self.parts['a:visited'] = { 'color': '#909' }
        self.parts['a:hover,a:active'] = { 'color': '#E20' }

        self.parts['.text'] = {
            'font-size': '12px',
            'color': '#000',
        }
        self.parts['.box'] = {
            'border': '1px solid #DDD'
        }

    def css(self, partName):
        str = u''
        if partName in self.parts:
            part = self.parts[partName]
            for i in part:
                str += "  %s:%s;\n" % (i, part[i])
        return str

    def cssPage(self):
        str = u''
        for part in self.parts:
            str += part + ' {\n'
            str += self.css(part)
            str += '}\n'
        return str

    def addClass(self, cl, cldef=dict()):
        self.parts['.'+cl] = cldef


if __name__ == "__main__":    
    skin = qsSkin()
    print skin.cssPage()
