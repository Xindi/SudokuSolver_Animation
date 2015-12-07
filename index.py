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
    #Get action field from action input"
    #action value: 
    #load_easy, load_medium, load_hard, b_easy(bruteforce easy), 
    #b_medium, b_hard, s_easy(simulated annelling easy),
    #s_medium, s_hard
    def POST(self):
        signal = web.input().action
        if signal == 'load_easy':
            return "hahaha"
        return "..."

if __name__ == "__main__": 
    app = web.application(urls, globals())
    app.run() 