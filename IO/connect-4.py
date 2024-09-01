def ask_user(prompt_message): 
    return input(prompt_message)

def create_game_board(rows = 4, cols = 4, content = []):
    def insert_horizontal_track(items):
        horizontal_track = []

        for grid_col_index in range(grid_width): 
            if grid_col_index % 2 == 0: 
                horizontal_track.append(items[int(grid_col_index / 2)])
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
            grid.append(insert_horizontal_track(content[int(grid_row_index / 2)]))
        else: 
            grid.append(add_horizontal_grid_line())
    
    return grid

def draw_game_board(game_board):
    grid = ''

    for horizontal_item_idx in range(len(game_board)): 
        if horizontal_item_idx % 2 == 0:         
            for player_move in game_board[horizontal_item_idx]:
                grid += player_move
            grid += '\n'
        else: 
            grid += game_board[horizontal_item_idx] + '\n'

    return grid

def traverse_diagonally_from_topleft_to_bottomright(matrix): 
    diagonal_paths = {}
    
    for i in range(len(matrix)): 
        for j in range(len(matrix[i])):
            if not (i + j) in diagonal_paths: 
                diagonal_paths[i + j] = [ matrix[i][j] ]
            else: 
                diagonal_paths[i + j].append(matrix[i][j])

    return [ diagonal_path for diagonal_path in diagonal_paths.values() ]

def traverse_diagonally_from_topright_to_bottomleft(matrix): 
    matrix_mirror = [ i[::-1] for i in matrix ]

    return traverse_diagonally_from_topleft_to_bottomright(matrix_mirror)

def traverse_vertically_from_top_to_botom(matrix): 
    return [ list(t) for t in list(zip(*matrix)) ]

def find_current_player_idx(players): 
    for index in range(len(players)): 
        if players[index]['is_turn']:
            return index
    return 0   

def find_next_player_idx(current_player_idx, players): 
    return (0 if current_player_idx == (len(players) - 1) else (current_player_idx + 1))

def make_player_move(marker, row_idx, col_idx, players_moves): 
    game_board = players_moves[:]
    game_board[row_idx][col_idx] = marker

    return game_board

def switch_players(current_player_idx, next_player_idx, players): 
        players_in_game = players[:]
        current_player = players_in_game[current_player_idx] 
        next_player = players_in_game[next_player_idx]

        current_player = { **current_player, 'is_turn': not current_player['is_turn'] }
        next_player = { **next_player, 'is_turn': not next_player['is_turn'] }
        players_in_game[current_player_idx] = current_player
        players_in_game[next_player_idx] = next_player       
        
        return players_in_game

def create_row_tracker(cols, rows):
    column_row_tracker = {}
    
    for col in range(cols): 
        column_row_tracker[col] = rows - 1
    
    return column_row_tracker

def update_row_tracker(row_tracker, column_index): 
    return {**row_tracker, column_index: row_tracker[column_index] - 1}

def calculate_next_row_index(row_tracker, column_index):
    return row_tracker[column_index] 

def filter_candidate_paths(paths, winning_path):
    return [ normalize_path(path) for path in paths if is_path_valid(path, winning_path) ] 

def is_path_valid(path, winning_path): 
    return is_path_length_valid(path, len(winning_path)) and is_path_not_empty(path)

def is_path_not_empty(path):
    return (''.join(path).strip() != '')

def is_path_length_valid(path, length): 
    return (len(path) >= length)

def normalize_path(path):
    return ''.join(path).strip()

def is_winner(player, players_moves): 
    winning_path = player['winning_path']
    
    if has_winner_in_diagonal_paths(winning_path, players_moves): 
        return True
    
    if has_winner_in_diagonal_inverse_paths(winning_path, players_moves):
        return True

    if has_winner_in_vertical_paths(winning_path, players_moves):
        return True
    
    if has_winner_in_horizontal_paths(winning_path, players_moves):
        return True

    return False

def has_winner_in_diagonal_paths(winning_path, game_board):
    paths = filter_candidate_paths(traverse_diagonally_from_topleft_to_bottomright(game_board), winning_path)

    return winning_path in ('|'.join(paths))

def has_winner_in_diagonal_inverse_paths(winning_path, game_board):
    paths = filter_candidate_paths(traverse_diagonally_from_topright_to_bottomleft(game_board), winning_path)

    return winning_path in ('|'.join(paths))

def has_winner_in_vertical_paths(winning_path, game_board):
    paths = filter_candidate_paths(traverse_vertically_from_top_to_botom(game_board), winning_path)

    return winning_path in ('|'.join(paths))

def has_winner_in_horizontal_paths(winning_path, game_board):
    paths = filter_candidate_paths(game_board, winning_path)

    return winning_path in ('|'.join(paths))

def start_game(game):     
    players = game['players']
    cols = game['board_dimension']['cols']
    rows = game['board_dimension']['rows']
    players_moves = [ [ ' ' for _ in range(cols) ] for _ in range(rows) ]
    row_tracker = create_row_tracker(cols, rows)
    game_total_turns = cols * rows
    current_game_turn = 1

    while current_game_turn <= game_total_turns:
        current_player_index = find_current_player_idx(players)
        next_player_index = find_next_player_idx(current_player_index, players)
        current_player = players[current_player_index]

        # Ask the player in turn for their move
        player_move_at_col = int(ask_user(current_player['player'] + '\'s move at col: '))
        # Program must calculate next row index to place player's move. 
        player_move_at_row = calculate_next_row_index(row_tracker, player_move_at_col)
        # Place the player's move in the moves list
        players_moves = make_player_move(current_player['marker'], player_move_at_row, player_move_at_col, players_moves)
        # Update Row Tracker.
        row_tracker = update_row_tracker(row_tracker, player_move_at_col)
        # Draw Gameboard
        print(draw_game_board(create_game_board(rows, cols, players_moves)), end='')

        # Check if current player's a winner
        if is_winner(current_player, players_moves):
            print(current_player['player'] + ' is the winner 😎')
            return

        # Calculate next player
        players = switch_players(current_player_index, next_player_index, players)

        current_game_turn = current_game_turn + 1  

    print('No winners this time 😛')

def main(): 
    connect4_configuration = {
        'players': [
            {'player': 'John Doe', 'is_turn': False, 'marker': 'x', 'winning_path': 'xxxx'}, 
            {'player': 'Jane Darling', 'is_turn': True, 'marker': 'o', 'winning_path': 'oooo'},
        ],
        'board_dimension': {
            'cols': 5,
            'rows': 5
        }
    }
    
    start_game(connect4_configuration)
    
main()