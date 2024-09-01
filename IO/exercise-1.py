def ask_user(message): 
    return input(message)

def alert_user(message): 
    print(message)

def create_game_board(cols, rows):
    def insert_horizontal_track():
        horizontal_track = []

        for grid_col_index in range(grid_width): 
            if grid_col_index % 2 == 0: 
                horizontal_track.append(' ')
            else: 
                horizontal_track.append('|')

        return horizontal_track
    
    def add_horizontal_grid_line(): 
        return '-' * grid_width
       
    grid = []
    grid_vertical_lines = cols - 1
    grid_horizontal_lines = rows - 1
    grid_width = cols + grid_vertical_lines
    grid_height = rows + grid_horizontal_lines

    for grid_row_index in range(grid_height):
        if grid_row_index % 2 == 0: 
            grid.append(insert_horizontal_track())
        else: 
            grid.append(add_horizontal_grid_line())
    
    return grid

def draw_game_play(players_moves, game_board): 
    def update_empty_spots_with_players_moves(players_moves, free_spots):
        updated_spots = []

        for free_spot_index in range(len(free_spots)): 
            if free_spot_index % 2 == 0: 
                updated_spots.append(players_moves[int(free_spot_index / 2)])
            else:
                updated_spots.append(free_spots[free_spot_index])
        
        return updated_spots
 
    def insert_newline(): 
        return '\n'

    grid = ''

    for horizontal_item_index in range(len(game_board)): 
        if horizontal_item_index % 2 == 0:
            filled_spots = update_empty_spots_with_players_moves(
                players_moves[int(horizontal_item_index / 2)],
                game_board[horizontal_item_index]
            )
            
            for player_move in filled_spots:
                grid += player_move
            grid += insert_newline()
        else: 
            grid += game_board[horizontal_item_index] + insert_newline()

    return grid

def start_game(game):
    def get_current_player_index(): 
        for index in range(len(players)): 
            if players[index]['is_current_turn']:
                return index
            
    def get_next_player_index(current_player_index): 
        return (0 if current_player_index == (len(players) - 1) else (current_player_index + 1))
    
    def switch_players_turn(current_player, next_player): 
        current_player['is_current_turn'] = not current_player['is_current_turn']
        next_player['is_current_turn'] = not next_player['is_current_turn']
        players[current_player_index] = current_player
        players[next_player_index] = next_player

    def is_spot_taken(): 
        return True if players_moves[player_move_at_row][player_move_at_col] != ' ' else False
    
    def make_player_move(player_marker): 
        players_moves[player_move_at_row][player_move_at_col] = player_marker

    cols = game['board_size']['cols']
    rows = game['board_size']['rows'] 
    players = game['players']
    total_game_turns = cols * rows
    players_moves = [ [ ' ' for col in range(cols) ] for row in range(rows) ]
    current_turn = 1

    # Go through the game board
    while (current_turn <= total_game_turns):
        # Ask the player in turn for their move
        current_player_index = get_current_player_index()
        next_player_index = get_next_player_index(current_player_index)
        current_player = players[current_player_index]
        next_player = players[next_player_index]

        # Get the users's response
        player_move_at_row = int(ask_user(current_player['player'] + '\'s move at row: '))
        player_move_at_col = int(ask_user(current_player['player'] + '\'s move at col: '))

        # If the player's move is already in the moves list, ask again. 
        if is_spot_taken(): 
            alert_user('Spot is already taken. Please try again!')
            continue

        # Otherwise, place the player's move in the moves list
        make_player_move(current_player['marker'])

        # Create the Game Board
        game_board = create_game_board(cols, rows)

        # Draw game board with players' moves and display it to the user. 
        print(draw_game_play(players_moves, game_board), end='')

        # Change current player's move state
        switch_players_turn(current_player, next_player)

        # Next Turn.  
        current_turn = current_turn + 1
   
game_configuration = {
    'players': [
        {'player': 'John Doe', 'is_current_turn': False, 'marker': 'x'}, 
        {'player': 'Jane Darling', 'is_current_turn': True, 'marker': 'o'},
    ],
    'board_size': {
        'cols': 3,
        'rows': 3
    }
}

start_game(game_configuration)
