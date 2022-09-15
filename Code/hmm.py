from PIL import Image
grid_size = 133

def copy(width, height, img, imgnew):
    pix = imgnew.load()
    for i in range(1, grid_size):
        for j in range(1, grid_size):
            img.putpixel((i + width, j + height), pix[i, j])
    img.save('image1.bmp')

def reset_board(img):
    width, height = img.size
    pix = img.load()
    for i in range(height):
        for j in range(width):
            img.putpixel((j, i), pix[j, i])
    img.save('image1.bmp')

def display(img, imgx, imgo, player, choice):
    if choice == 1:
        width = 0
        height = 2*grid_size
    elif choice == 4:
        width = 0
        height = grid_size
    elif choice == 7:
        width = 0
        height = 0
    elif choice == 2:
        width = grid_size
        height = 2*grid_size
    elif choice == 5:
        width = grid_size
        height = grid_size
    elif choice == 8:
        width = grid_size
        height = 0
    elif choice == 3:
        width = 2*grid_size
        height = 2*grid_size
    elif choice == 6:
        width = 2*grid_size
        height = grid_size
    elif choice == 9:
        width = 2*grid_size
        height = 0

    if player == 1:
        imgnew = imgx
    else:
        imgnew = imgo
    copy(width, height, img, imgnew)

def check_for_winner(player, choice):
    if (positions[1] == positions[2] and positions[2] == positions[3]):
        if not positions[1] == -1:
            return 0
    if (positions[4] == positions[5] and positions[5] == positions[6]):
        if not positions[4] == -1:
            return 0
    if (positions[7] == positions[8] and positions[8] == positions[9]):
        if not positions[7] == -1:
            return 0
    if (positions[1] == positions[4] and positions[4] == positions[7]):
        if not positions[1] == -1:
            return 0
    if (positions[2] == positions[5] and positions[5] == positions[8]):
        if not positions[2] == -1:
            return 0
    if (positions[3] == positions[6] and positions[6] == positions[9]):
        if not positions[3] == -1:
            return 0
    if (positions[1] == positions[5] and positions[5] == positions[9]):
        if not positions[1] == -1:
            return 0
    if (positions[3] == positions[5] and positions[5] == positions[7]):
        if not positions[3] == -1:
            return 0
    return 1


if __name__ == '__main__':

    img_board = Image.open('image.bmp')
    img = Image.open('image1.bmp')
    imgx = Image.open('image_x.bmp')
    imgo = Image.open('image_o.bmp')

    reset_board(img_board)

    player = 1
    global positions
    positions = [-1]*10
    positions[0] = None
    flag = 1
    counter = 0

    while flag:
        print('Enter your choice: ')
        choice = int(input())
        while not (positions[choice] == -1):
            print("Invalid Input\nEnter choice again: ")
            choice = int(input())
        positions[choice] = player
        display(img, imgx, imgo, player, choice)
        flag = check_for_winner(player, choice)
        if flag == 0:
            break
        if player == 1:
            player = 2
        else:
            player = 1
        counter += 1
        if counter == 9:
            break
    
    if counter == 9:
        print("Draw Game, Better Luck Next Time!!")
    else:
        print("Player {} Wins the Game, LESS GOOO!!".format(player))
    
