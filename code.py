import web

urls = (
  '/', 'index'
)

class index:
    def GET(self):
        render = web.template.render('templates')
        return render.index('world')


if __name__ == "__main__": 
    app = web.application(urls, globals())
    app.run() 