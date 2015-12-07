import web
import json
from board import *
from brute_force import *
from local_search import *

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
            board = json.dumps(get_easy_board())
            return board
        if signal == 'b_easy':
            board = get_easy_board()
            result = []
            brute_force(board, result)
            return json.dumps(result)
        if signal == 's_easy':
            board = get_easy_board()
            result = []
            simulated_annealing(board, 3, result)
            return json.dumps(result)
        if signal == 'load_medium':
            board = json.dumps(get_medium_board())
            return board
        if signal == 'b_medium':
            board = get_medium_board()
            result = []
            brute_force(board, result)
            return json.dumps(result)
        if signal == 's_medium':
            board = get_medium_board()
            result = []
            simulated_annealing(board, 3, result)
            return json.dumps(result)
        if signal == 'load_hard':
            board = json.dumps(get_hard_board())
            return board
        if signal == 'b_hard':
            board = get_hard_board()
            result = []
            brute_force(board, result)
            return json.dumps(result)
        if signal == 's_hard':
            board = get_hard_board()
            result = []
            simulated_annealing(board, 3, result)
            return json.dumps(result)
        return "..."

if __name__ == "__main__": 
    app = web.application(urls, globals())
    app.run() 