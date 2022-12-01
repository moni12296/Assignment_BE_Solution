'''
To change the number of passengers or the seating layout of the flight,
head to the main function on line 146 and change the passenger_count and arr variable respectively.
The code currently runs the test case provided in the question.
'''
#initialising the matrix of seat_matrix
def arrange(arr):
    #initilasing 3d array for all blocks and seats
    seat_matrix = []
    for i in arr:
        matrix = []
        rows = i[1]
        col = i[0]
        for i in range(rows):
            matrix.append([0]*col)
        seat_matrix.append(matrix)
    return seat_matrix

#function to fill aisle seats          
def aisle():
    global filled_seats
    row = 0
    temp_filled_count = 0
    #while loop to make sure filled seats do not exceed passenger count and not all seats are aisle
    while filled_seats < passenger_count and filled_seats != temp_filled_count+1:
        temp_filled_count = filled_seats
        for i in range(length):
            if arr[i][1] > row:
                #checking first block for aisle seats
                if i == 0 and arr[i][0] > 1:
                    filled_seats += 1
                    aisle_col = arr[i][0] - 1
                    seat_matrix[i][row][aisle_col] = filled_seats
                    #aisle seats of blocks filled and filled_seats incremented
                    if filled_seats >= passenger_count:
                        break
                #checking for last block making sure to not add window seats
                elif i == length - 1 and arr[i][0] > 1:
                    filled_seats += 1
                    aisle_col = 0
                    seat_matrix[i][row][aisle_col] = filled_seats
                    if filled_seats >= passenger_count:
                        break
                #checking middle blocks for aisle seats on both ends
                else:
                    filled_seats += 1
                    aisle_col = 0
                    seat_matrix[i][row][aisle_col] = filled_seats
                    if filled_seats >= passenger_count:
                        break
                    if arr[i][0] > 1:
                        filled_seats += 1
                        aisle_col = arr[i][0] - 1
                        seat_matrix[i][row][aisle_col] = filled_seats
                        if filled_seats >= passenger_count:
                            break
        row += 1

#function to fill middle seats
def middle():
    global filled_seats
    row = 0
    temp_filled_count = 0
    #making sure seats filled is not more than passenger count and not all seats are middle seats
    while filled_seats < passenger_count and filled_seats != temp_filled_count:
        temp_filled_count = filled_seats
        for i in range(length):
            if arr[i][1] > row:
                if arr[i][0] > 2:
                    for col in range(1, arr[i][0] - 1):
                        if filled_seats >= passenger_count:
                            break
                        filled_seats += 1
                        seat_matrix[i][row][col] = filled_seats
        row += 1


#function to fill window seats
def window():
    row = 0
    global filled_seats
    global passenger_count
    temp_filled_count = 0
    #making sure seats filled does not exceed passenger count and not all seats are window seats
    while filled_seats < passenger_count and filled_seats != temp_filled_count:
        temp_filled_count = filled_seats
        if arr[0][1] > row:
            filled_seats += 1
            window = 0
            seat_matrix[0][row][window] = filled_seats
            if filled_seats >= passenger_count:
                break
        if arr[length-1][1] > row:
            filled_seats += 1
            window = arr[length-1][0] - 1
            seat_matrix[length-1][row][window] = filled_seats
            if filled_seats >= passenger_count:
                break
        row += 1

#function to map numbers from seat_matrix to matrix
def assign(seat_matrix):
    block_size = len(str(passenger_count))
    rows = [x[1] for x in arr]
    col = [x[0] for x in arr]
    maxi = max(rows)
    start = True
    #creating 2 lists to append values to rows and columns
    for i in range(maxi):
        row_list1 = []
        row_list2 = []
        for j in range(length):
            row = ' '
            row2 = ' '
            if len(seat_matrix[j]) <= i:
                for k in range(col[j]):
                    row += ' '*block_size
                    row2 += ' '*block_size
                    row += ' '
                    row2 += ' '
            else:
                row = ' '
                row2 = ' '
                for k in seat_matrix[j][i]:
                    if k == 0:
                        row += ' '*block_size
                        row2 += ' '*block_size
                        row += ' '
                        row2 += ' '
                    else:
                        row += str(k)+(' '*(block_size - len(str(k))))
                        row2 += ' '*block_size
                        row += ' '
                        row2 += ' '
            
            row_list1.append(row)
            row_list2.append(row2)
        if start:
            print('  '.join(row_list2))
            start = False
        print('  '.join(row_list1))
        print('  '.join(row_list2))

#main function
if __name__=='__main__':
    arr = [[3,2], [4,3], [2,3], [3,4]]  #change this 2d array 'arr' to change the layout of the seating
    passenger_count=30  #change the passenger count by changing this 'passenger_count' variable
    row = 0
    filled_seats = 0
    temp_filled_count = 0
    seat_matrix = arrange(arr)
    length = len(arr)
    aisle()
    window()
    row = 0
    temp_filled_count = 0
    middle()
    assign(seat_matrix)