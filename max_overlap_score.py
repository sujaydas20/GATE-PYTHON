import sys

def solve():
   
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return
        
    n = int(input_data[0])
    

    events = [None] * (2 * n)
    
    idx = 1
    event_idx = 0
    for _ in range(n):
        l = int(input_data[idx])
        r = int(input_data[idx+1])
        s = int(input_data[idx+2])
        
        events[event_idx] = (l, s)
        events[event_idx + 1] = (r + 1, -s)
        
        event_idx += 2
        idx += 3

    events.sort(key=lambda x: x[0])
    
    max_score = 0
    current_score = 0
    
    i = 0
    m = len(events)
    
    while i < m:
        time = events[i][0]
       
        while i < m and events[i][0] == time:
            current_score += events[i][1]
            i += 1
            
     
        if current_score > max_score:
            max_score = current_score
            
    
    print(max_score)

if __name__ == '__main__':
    solve()
