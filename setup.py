from dependencies import *
from get_game_state import get_game_state

# SETUP ===========================================================================================

# Clear DB ----------------------------------------------------------------------------------------

# def clear_db():
#     # NEED TO CLEAR ORDER HISTORY
#     mongo.db.pieces.remove({})
#     mongo.db.users.remove({})
#     mongo.db.ownership.remove({})
#     mongo.db.orders.remove({})
#     mongo.db.nations.remove({})
#     mongo.db.game_properties.remove({})
    
# Initialise game DB ------------------------------------------------------------------------------

# def initialise_game_db():
#     clear_db()
#     pieces = mongo.db.pieces
#     for piece in initial_pieces:
#         pieces.insert(piece)
#     nations = mongo.db.nations
#     for nation in initial_nations:
#         nations.insert(nation)
#     mongo.db.ownership.insert(initial_ownership)
#     mongo.db.game_properties.insert(initial_game_properties)
#     flash('Game initialised!', 'success')
    
# Populate Users ----------------------------------------------------------------------------------

# """ creates seven dummy users """

# def populate_users():
#     mongo.db.users.remove({})
#     users = mongo.db.users
#     for player in dummy_players:
#         users.insert(player)
#     session["username"] = dummy_players[0]["username"]
        
# Fill out orders ---------------------------------------------------------------------------------

""" creates a list of pre-written orders """
        
def fill_out_orders(file_name):
    orders = get_orders_from_txt(file_name)
    # orders = mongo.db.orders
    # for order in get_orders_from_txt(file_name):
    #     orders.insert(order)
        
# Are seven players registered --------------------------------------------------------------------

# def are_seven_players_registered():
#     return mongo.db.users.count() >= 7
        
# Update nation availability ----------------------------------------------------------------------
    
# def update_nation_availability(player_nation):
#     nation_to_update = mongo.db.nations.find_one({'name': player_nation})
#     update_doc={"available": False}
#     mongo.db.nations.update_one(nation_to_update, {'$set': update_doc})

    
    

    
# Start game --------------------------------------------------------------------------------------
    
# def start_game():
#     mongo.db.game_properties.update_one({}, {"$set": {"game_started": True}})
#     flash('Game Started!', 'success')
#     return get_game_state()