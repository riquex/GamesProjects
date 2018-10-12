import os

def only_odd(n:int):
    result = n if n % 2 == 1 else n+1
    return result

def board(coord):
    '''print the board'''
    _board = [[' ', ' | ', ' ',' | ' ,' ',] for _ in range(3)]
    for i in range(3):
        for e, c in enumerate(coord[i]):
            if c: _board[i][only_odd(i)] = c
        os.system(''.join(_board[i]))
    

def main():
    done = False
    coord = [[0, 0, 0] for _ in range(3)]
    while not done:
        board(coord)
        
        msg = input('>>> ')
        if msg == 'done': done = True

if __name__ == '__main__':
    main()
