import prettytable as pt
import os, sys
import time
from random import shuffle, randrange

mapName = [ [""]*20 for i in range(20)] 

position = "↑→↓←"

# Wall of the maze
maze = [   [9, 	5,	5,	5,	5,	5,	5,	5,	5,	5,	5,	5,	5,	5,	5,	5,	5,	5,	5,	2],	 
           [12,	5,	5,	5,	5,	5,	5,	5,	5,	1,	5,	5,	5,	5,	5,	5,	5,	5,	5,	2],	 
           [9,	5,	5,	5,	5,	5,	5,	5,	5,	6,	13,	5,	5,	5,	5,	5,	5,	5,	5,	6],	 
           [8,	5,	5,	1,	1,	3,	9,	3,	9,	5,	5,	5,	1,	5,	5,	5,	1,	3,	9,	3],	
           [12,	5,	3,	10,	10,	10,	10,	10,	10,	9,	5,	5,	6,	9,	5,	5,	6,	10,	10,	10],
           [9,	5,	6,	10,	10,	10,	10,	10,	10,	12,	5,	5,	3,	12,	5,	5,	3,	10,	10,	10],
           [12,	5,	3,	10,	10,	10,	10,	10,	10,	9,	5,	5,	6,	9,	5,	5,	6,	10,	10,	10],
           [9,	5,	6,	10,	10,	10,	10,	10,	10,	8,	3,	9,	3,	8,	3,	9,	3,	10,	10,	10],
           [12,	5,	3,	10,	10,	10,	10,	10,	10,	10,	10,	10,	10,	10,	10,	10,	10,	10,	10,	10],
           [9,	3,	10,	10,	10,	12,	6,	12,	2,	10,	10,	10,	10,	10,	10,	10,	10,	10,	10,	10],
           [10,	10,	10,	10,	12,	5,	5,	7,	10,	10,	10,	10,	10,	10,	10,	10,	10,	8,	6,	14],
           [10,	10,	10,	10,	9,	5,	5,	3,	10,	14,	12,	6,	10,	10,	10,	10,	10,	8,	1,	3],
           [10,	10,	10,	10,	10,	9,	5,	6,	8,	5,	5,	5,	2,	10,	10,	10,	10,	10,	10,	10],
           [10,	10,	10,	10,	10,	12,	5,	1,	2,	9,	5,	5,	6,	10,	10,	10,	10,	10,	10,	10],
           [10,	10,	10,	10,	10,	9,	5,	6,	10,	12,	5,	5,	3,	10,	10,	10,	10,	10,	10,	10],
           [10,	10,	10,	10,	10,	12,	5,	3,	10,	9,	5,	5,	6,	10,	12,	6,	14,	10,	10,	10],
           [10,	10,	10,	10,	10,	9,	5,	6,	10,	12,	5,	5,	3,	12,	5,	5,	3,	10,	10,	10],
           [10,	10,	10,	10,	10,	12,	5,	3,	12,	5,	5,	5,	6,	9,	5,	5,	6,	10,	10,	10],
           [10,	12,	6,	10,	10,	9,	5,	6,	9,	5,	5,	5,	5,	4,	5,	5,	3,	10,	10,	10],
           [12,	5,	5,	4,	6,	12,	5,	5,	4,	5,	5,	5,	5,	5,	5,	7,	12,	6,	14,	10]]

class my_mouse ():
    def __init__(self):
        self.position_number = 0
        self.location_x = 19
        self.location_y = 0
        self.head = position[self.position_number]
        self.move = [[-1,0], [0, 1], [1,0], [0,-1]]
    
    def getXY(self):
        return self.location_x, self.location_y
    def getHead(self):
        return self.head
    
    def forward(self):
        self.location_x += self.move[0][0]
        self.location_y += self.move[0][1]
        self.head = position[self.position_number]

    def right(self):
        self.location_x += self.move[1][0]
        self.location_y += self.move[1][1]
        self.move = self.move[1:] + self.move[:1]
        self.position_number += 1
        if(self.position_number == 4):
            self.position_number = 0
        self.head = position[self.position_number]

    def back(self):
        # Not use
        self.location_x += self.move[2][0]
        self.location_y += self.move[2][1]
        
        self.head = position[self.position_number]

    def left(self):
        self.location_x += self.move[3][0]
        self.location_y += self.move[3][1]
        self.move = self.move[3:] + self.move[:3]
        self.position_number -= 1
        if(self.position_number == -1):
            self.position_number = 3
        self.head = position[self.position_number]
    
    def isGoal(self):
        if mapName[self.location_x][self.location_y] == "G" or mapName[self.location_x][self.location_y] == "g":
            return True
        else:
            return False

class Node:     
    def __init__(self, x, y, g = 0, h = 0):  
        self.x = x
        self.y = y
        self.father = None
        self.g = g
        self.h = h
    
    def getXY(self):
        return self.x, self.y
    # Using Manhattan 
    def manhattan(self, endNode):
        self.h = ( (endNode.x - self.x) ** 2 + (endNode.y - self.y)**2) ** 0.5 * 10 
    
    def setG(self, g):
        self.g = g

    def setFather(self, node):
        self.father = node

def convertToBinary(n):
    try:
        num = int(n)
    except:
        print("Error")
        return 0

    binStr = bin(n)
    binStr = binStr[2:]
    while(len(binStr) < 4):
        binStr = "0" + binStr
    return binStr

def make_maze(w = 20, h = 20, need_print = True):
    
    # Point in the maze
    with open('mapName.txt', 'r') as f:
        for line in f:
            newline = line.split('	')
            newline[2] = newline[2].replace("\n","")
            mapName[int(newline[0])][int(newline[1])] = newline[2]

    # Init wall
    ver = [["|   "] * w + ['|'] for _ in range(h)] + [[]]
    hor = [["+---"] * w + ['+'] for _ in range(h + 1)]

    for x in range(0, 20):
        for y in range(0, 20):
            tmp = convertToBinary(maze[x][y])
            if(tmp[3] == "0"):
                hor[x][y] = "+   "
            if(tmp[2] == "0"):
                ver[x][y+1] = "    "
            if(tmp[1] == "0"):
                hor[x+1][y] = "+   "
            if(tmp[0] == "0"):
                if(mapName[x][y] != ""):
                    ver[x][y] = "  " + mapName[x][y] + " "
                else:
                    ver[x][y] = "    "
            else:
                if(mapName[x][y] != ""):
                    ver[x][y] = "| " + mapName[x][y] + " "
    if need_print:
        print_maze(hor, ver)
    return hor, ver

def print_maze(hor, ver):
    s = ""
    for (a, b) in zip(hor, ver):
        s += ''.join(a + ['\n'] + b + ['\n'])
    print(s, end ="") 

def draw_list_path(hor, ver, path_list):
    for i in path_list:
        if type(i) == Node:
            x, y = i.getXY()
        else:
            x, y = i

        tmp = convertToBinary( maze[ x ][ y ])
        
        if(tmp[0] == "0"):
            if(mapName[ x ][ y ] != ""): 
                ver[ x ][ y ] = "  @ "
            else:
                ver[ x ][ y ] = "  @ "
        else:
            if(mapName[ x ][ y ] != ""):
                ver[ x ][ y ] = "| @ "
            else:
                ver[ x ][ y ] = "| @ "

    print_maze(hor, ver)

def wall_follower(mouse):
    mouse_path = []
    start_time = time.time()

    while not mouse.isGoal():
        location_x, location_y = mouse.getXY()
        mouse_path.append((location_x, location_y))
        head = mouse.getHead()

        tmp = convertToBinary(maze[location_x][location_y])
        if head == "→":
            tmp = tmp[3:] + tmp[:3]
        elif head == "↓":
            tmp = tmp[2:] + tmp[:2]
        elif head == "←":
            tmp = tmp[1:] + tmp[:1]
    
        if(tmp[0] == "0"):
            mouse.left()

            continue
        if(tmp[3] == "0"):
            mouse.forward()
        else:
            mouse.right()

    mouse_path.append((mouse.getXY()))
    end_time = time.time()

    return mouse_path, end_time-start_time

#--------------------------------------------
# A* Algorithm
#--------------------------------------------
def getMinFNode(open_list):
    temp_node = open_list[0]  
    
    for node in open_list:  
        if node.g + node.h < temp_node.g + temp_node.h:  
            temp_node = node

    return temp_node

def isNodeinList(node, temp_list):
    for temp_node in temp_list:
        if temp_node.getXY() == node.getXY():
            return True
    return False

def getNodefromList(node, temp_list):
    for temp_node in temp_list:
        if temp_node.getXY() == node.getXY():
            return temp_node
    return None


def nodeSetup(temp_node, end_node, current_node, open_list, close_list):
    if not isNodeinList(temp_node, close_list):
        if not isNodeinList(temp_node, open_list):
            temp_node.setG(10)
            temp_node.manhattan(end_node)
            temp_node.father = current_node
            open_list.append(temp_node)
        else:
            getNodefromList(temp_node, open_list)
            if current_node.g + 10 < temp_node.g:
                temp_node.g = current_node.g + 10  
                temp_node.father = current_node
    return

def Astar(start_x, start_y, end_x, end_y):
    mouse_path = []
    start_node = Node(start_x, start_y)
    end_node = Node(end_x, end_y)
    current_node = start_node

    open_list = []
    close_list = []

    start_node.manhattan(end_node)
    start_node.setG(0)
    open_list.append(start_node)

    start_time = time.time()

    while len(open_list) != 0:
        current_node = getMinFNode(open_list)
        close_list.append(current_node)
        open_list.remove(current_node)

        location_x , location_y = current_node.getXY()
        if location_x > 19 or location_x < 0 or location_y > 19 or location_y < 0:
            continue
        tmp = convertToBinary(maze[location_x][location_y])

        if tmp[0] == "0":
            temp_node = Node(location_x, location_y - 1)
            nodeSetup(temp_node, end_node, current_node, open_list, close_list)

        if tmp[1] == "0":
            temp_node = Node(location_x + 1, location_y)
            nodeSetup(temp_node, end_node, current_node, open_list, close_list)
        
        if tmp[2] == "0":
            temp_node = Node(location_x, location_y + 1)
            nodeSetup(temp_node, end_node, current_node, open_list, close_list)
        
        if tmp[3] == "0":
            temp_node = Node(location_x - 1, location_y)
            nodeSetup(temp_node, end_node, current_node, open_list, close_list)
        
        if isNodeinList(end_node, open_list):
            temp_node = getNodefromList(end_node, open_list)
            while True:
                mouse_path.append(temp_node)
                if temp_node.father != None:
                    temp_node = temp_node.father
                else:
                    end_time = time.time()
                    return True, mouse_path, end_time-start_time
    end_time = time.time()
    return False , None, end_time-start_time
#--------------------------------------------

if __name__ == '__main__':
    
    # init a maze
    print("\nInitial Maze...")
    maze_hor, maze_ver = make_maze(need_print = False)
    print("\n=================================================================================\n\n")

    # init a mouse
    mouse = my_mouse()

    # start traversing using "wall follower"
    mouse_path, wall_follower_time = wall_follower(mouse)
    draw_list_path(maze_hor, maze_ver, mouse_path)
    print("The traversing path: ")
    print(mouse_path)
    # end

    # init a maze
    print("\nInitial Maze...")
    maze_hor, maze_ver = make_maze(need_print = False)
    print("\n=================================================================================\n\n")

    # init a mouse
    mouse = my_mouse()
    success , node_list, astar_time = Astar(19, 0, 0, 19)
    if success:
        print("A* found the path!")
        draw_list_path(maze_hor, maze_ver, node_list)
        print("The traversing path: ")
        for node in node_list:
            print(node.getXY(), end="")
    
    print("\n=================================================================================\n\n")
    print("Result: ")
    print("Wall Follower: ", len(mouse_path), "steps!")
    print("Use : ", wall_follower_time, "second!")
    print("A* Search: ",len(node_list), "steps!")
    print("Use : ", astar_time, "second!")