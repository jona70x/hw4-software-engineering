def cacti_number(plot):

    rows = len(plot)
    cols = len(plot[0])
    count = 0
    
    #checking for empty arrays
    if not plot or not len(plot[0]) < 1:
        return 0

    # iterate rows and columns

    for i in range(rows):
        for j in range(cols):
            # use a guard to check for safe spots
            if plot[i][j] == 0:
                is_safe = True
                
                #checking if a cacti is planted up, right, down, and left
                if i > 0 and plot[i-1][j] == 1:
                    is_safe = False
                # cheking down
                if i < rows - 1 and plot[i+1][j] == 1:
                    is_safe = False
                # checking left
                if j > 0 and plot[i][j-1] == 1:
                    is_safe = False
                # ckcking right
                if j < cols - 1 and plot[i][j+1] == 1:
                    is_safe = False
                # plant cactus if it is safe
                if is_safe:
                    plot[i][j] = 1
                    #increment cactus count
                    count += 1
 
    return count
