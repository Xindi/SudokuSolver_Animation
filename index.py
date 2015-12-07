import web

urls = (
  '/', 'index',
  '/test', 'test'
)

class index:
    def GET(self):
        render = web.template.render('templates')
        return render.index('world')

class test:
	def GET(self):
		return "hahaha"


if __name__ == "__main__": 
    app = web.application(urls, globals())
    app.run() 