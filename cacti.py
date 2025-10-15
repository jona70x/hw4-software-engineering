def cacti_number(plot):

   
    #checking for empty arrays
    if not plot or not plot[0]:
        return 0
    
    rows = len(plot)
    cols = len(plot[0])
    count = 0

    # iterate rows and columns

    for i in range(rows):
        for j in range(cols):
            # use a guard to check for safe spots
            if plot[i][j] != 0:
                continue
                
            # block if any 4-neighbor has a cactus
            if (i > 0 and plot[i-1][j] == 1) or \
               (i < rows - 1 and plot[i+1][j] == 1) or \
               (j > 0 and plot[i][j-1] == 1) or \
               (j < cols - 1 and plot[i][j+1] == 1):
                continue

            # plant and count
            plot[i][j] = 1
            count += 1
 
    return count
