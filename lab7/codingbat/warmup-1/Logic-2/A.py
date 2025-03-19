def make_bricks(small, big, goal):
    max_big = min(goal // 5, big)  
    remaining = goal - max_big * 5  
    
    return remaining <= small  