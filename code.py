# -*- coding: utf-8 -*-

import web

render = web.template.render('templates/')

urls = (
    '/(.*)','index'
)

class index:
    def GET(self,name):  
        return render.first(name)

if __name__=="__main__":
    app = web.application(urls,globals())
    app.run()
