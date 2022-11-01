 def get_move(self, match_count, min_remove, max_remove):
        # if computer is losing it should try to make a random move to confuse the player
        if match_count > 8:
            move = 1
        elif match_count == 8 or match_count == 4:
            move = 3
        elif match_count == 7 or match_count == 3:
           move = 2
        else:
            move = 1    
        return move
        # i imagine computer should do calcs on each turn how to lead the player into leaving 2,3,4 after him but too tired now
        # so only slightly improving pc's chances...
