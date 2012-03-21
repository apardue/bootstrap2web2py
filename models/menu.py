# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## Customize your APP title, subtitle and menus here
#########################################################################

response.title = request.application
response.subtitle = T('customize me!')

## read more at http://dev.w3.org/html5/markup/meta.name.html
response.meta.author = 'Your Name <you@example.com>'
response.meta.description = 'a cool new app'
response.meta.keywords = 'web2py, python, framework'
response.meta.generator = 'Web2py Web Framework'
response.meta.copyright = 'Copyright 2011'

## your http://google.com/analytics id
response.google_analytics_id = None

#layout 
response.pagename = request.function.capitalize()
response.tagline = "My awesome web2py application"
response.brand = request.application.capitalize()
response.brand_url = URL('default','index')
response.alerttype = 'warning' #info, error, success, warning
#########################################################################
## this is the main application menu add/remove items as required
#########################################################################

response.menu = [
    (T('Home'), False, URL('default','index'), [])
    ]

if auth.user:
    response.auth_menu = [
    (T('Profile'), False, URL('default','user',args=['profile']), []),
    (T('Logout'), False, URL('default','user',args=['logout']), [])
    ]
else:
    response.auth_menu = [
    (T('Login'), False, URL('default','user',args='login'), []),
    (T('Register'), False, URL('default','user',args='register'), [])
    ]


#########################################################################
## provide shortcuts for development. remove in production
#########################################################################

def _():
    # shortcuts
    app = request.application
    ctr = request.controller    
    # useful links to internal admin and appadmin pages
    response.menu+=[
        (T('This App'),False, None, [
                (T('Edit Application'),False,
                 URL('admin','default','design/%s' % app)),
                (T('Controller'),False,
                 URL('admin','default','edit/%s/controllers/%s.py' % (app,ctr))),
                (T('View'),False,
                 URL('admin','default','edit/%s/views/%s' % (app,response.view))),
                (T('Layout'),False,
                 URL('admin','default','edit/%s/views/layout.html' % app)),
                (T('Stylesheet'),False,
                 URL('admin','default','edit/%s/static/base.css' % app)),
                (T('DB Model'),False,
                 URL('admin','default','edit/%s/models/db.py' % app)),
                (T('Menu Model'),False,
                 URL('admin','default','edit/%s/models/menu.py' % app)),
                (T('Database'),False, URL(app,'appadmin','index')),
                (T('Errors'),False, URL('admin','default','errors/' + app)),
                (T('About'),False, URL('admin','default','about/' + app)),
                ]
         )]    

    # useful links to external resources
    response.menu+=[
        (T('Resources'),False, None, [
                (T('Documentation'),False,'http://www.web2py.com/book', []),
                (T('Preface'),False,'http://www.web2py.com/book/default/chapter/00'),
                (T('Introduction'),False,'http://www.web2py.com/book/default/chapter/01'),
                (T('Python'),False,'http://www.web2py.com/book/default/chapter/02'),
                (T('Overview'),False,'http://www.web2py.com/book/default/chapter/03'),
                (T('The Core'),False,'http://www.web2py.com/book/default/chapter/04'),
                (T('The Views'),False,'http://www.web2py.com/book/default/chapter/05'),
                (T('Database'),False,'http://www.web2py.com/book/default/chapter/06'),
                (T('Forms and Validators'),False,'http://www.web2py.com/book/default/chapter/07'),
                (T('Access Control'),False,'http://www.web2py.com/book/default/chapter/08'),
                (T('Services'),False,'http://www.web2py.com/book/default/chapter/09'),
                (T('Buy this book'),False,'http://stores.lulu.com/web2py'),
                (False,False,LI(_class='divider'),[]),
                (T('Community'),False, None, []),
                (T('Groups'),False,'http://www.web2py.com/examples/default/usergroups'),
                (T('Twitter'),False,'http://twitter.com/web2py'),
                (False,False,LI(_class='divider'),[]),
                (T('Web2py'),False,'http://www.web2py.com', []),
                (T('Recipes'),False,'http://web2pyslices.com/'),
                ]
         )]
_()
