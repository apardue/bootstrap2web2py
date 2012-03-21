class MENUBUILDER(DIV):
    """
    Used to build menus

    Optional arguments
      _class: defaults to 'web2py-menu web2py-menu-vertical'
      ul_class: defaults to 'web2py-menu-vertical'
      li_class: defaults to 'web2py-menu-expand'

    Example:
        menu = MENU([['name', False, URL(...), [submenu]], ...])
        {{=menu}}
    """

    tag = 'ul'

    def __init__(self, data, **args):
        self.data = data
        self.attributes = args
        if not '_class' in self.attributes:
            self['_class'] = 'nav'
        if not 'ul_class' in self.attributes:
            self['ul_class'] = 'dropdown-menu'
        if not 'li_class' in self.attributes:
            self['li_class'] = 'dropdown'
        if not 'li_active' in self.attributes:
            self['li_active'] = 'active'

    def serialize(self, data, level=0):
        if level == 0:
            ul = UL(**self.attributes)
        else:
            ul = UL(_class=self['ul_class'])
        for item in data:
            (name, active, link) = item[:3]
            
            if isinstance(link,DIV):
                li = LI(link)
            elif isinstance(link,LI):
                li = link
            elif 'no_link_url' in self.attributes and self['no_link_url']==link:
                li = LI(DIV(name))
            elif len(item) > 3 and not item[3]:
                 li = LI(A(name,_href=link))
            elif link:
                aa = A(name, _href=link, _class="dropdown-toggle")
                #aa.attributes['_data-toggle']='dropdown'
                #aa.append(B(_class='caret'))
                li = LI(aa)
            else:
                aa = A(name, _href='#', _class="dropdown-toggle")
                aa.attributes['_data-toggle']='dropdown'
                aa.append(B(_class='caret'))
                li = LI(aa)
            if len(item) > 3 and item[3]:
                li['_class'] = self['li_class']
                li.append(self.serializeinner(item[3], level+1))
            if active or ('active_url' in self.attributes and self['active_url']==link):
                if li['_class']:
                    li['_class'] = li['_class']+' '+self['li_active']
                else:
                    li['_class'] = self['li_active']
            ul.append(li)
        return ul

    def serializeinner(self, data, level=0):
        if level == 0:
            ul = UL(**self.attributes)
        else:
            ul = UL(_class=self['ul_class'])
        for item in data:
            (name, active, link) = item[:3]
            if isinstance(link,DIV):
                li = LI(link)
            elif 'no_link_url' in self.attributes and self['no_link_url']==link:
                li = LI(DIV(name))
            elif link:
                li = LI(A(name, _href=link,))
            else:
                li = LI(A(name, _href='#',
                          _onclick='javascript:void(0);return false;',))
            if len(item) > 3 and item[3]:
                li['_class'] = self['li_class']
                li.append(self.serializeinner(item[3], level+1))
            if active or ('active_url' in self.attributes and self['active_url']==link):
                if li['_class']:
                    li['_class'] = li['_class']+' '+self['li_active']
                else:
                    li['_class'] = self['li_active']
            ul.append(li)
        return ul

    def xml(self):
        return self.serialize(self.data, 0).xml()


class BREADCRUMB(DIV):
    tag = 'ul'

    def __init__(self, data=None, **args):
        self.attributes = args
        if not '_class' in self.attributes:
            self['_class'] = 'breadcrumb'

        if not data:
            self.data = []
            self.data.append((request.controller, URL(request.controller,'index') ))
            self.data.append((request.function, URL(request.function) ))
            if request.args and len(request.args)<3:
                for arg in request.args:
                    self.data.append((arg, URL(request.controller,request.function,args=arg) ))

   
    def serialize(self, data):
        ul = UL(**self.attributes)
        divider = SPAN("/",_class='divider')
        for item in data[0:-1]:
           ul.append(LI(A(T(item[0]),_href=item[1]),divider))
        ul.append(LI(T(data[-1][0]),_class='active'))
        return ul

    def xml(self):
        return self.serialize(self.data).xml()

        



