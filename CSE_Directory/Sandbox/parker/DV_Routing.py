# Parker Steach
# 1001843388

import socket
import threading
import os
import pickle
import time
import tkinter as tk
from tkinter import ttk
import copy

'''
TODO:
        #steps: 
            2) look into changing link cost
            3) finish comments & writeup
''' 
DVTables = []
previousTable = []
tree_lock = threading.Lock()
isPaused = False


#Class
class DVTable(object):
    
    def __init__(self, nodes):
        self.id = -1
        self.nodeID = nodes                 #this is the id for each node
        self.values = [-1] * len(nodes)     #these will act as no connection until real values get entered
        self.path = [None] * len(nodes)     #this will track the pathing to each node, handle as a string per element, 
                                                #the start of the string is the start of the path, the last node_number in the string is the end of path

class DVTableGUI:
    def __init__(self, root, dv_table,textState):
        self.root = root
        self.root.title("DVTable GUI")

        self.dv_table = dv_table

        self.tree = ttk.Treeview(root, columns=("Value", "Path"))
        self.tree.heading("#0", text="Node")
        self.tree.heading("#1", text="Value")
        self.tree.heading("#2", text="Path")
        self.tree.pack()

        self.statusLabel = tk.Label(root, textvariable=textState)
        self.statusLabel.pack()
        #self.update_gui()

    def update_gui(self):
        if not isPaused:
            with tree_lock: 
                #clear existing tables in view
                for item in self.tree.get_children():
                    self.tree.delete(item)

                #populate view with new data
                for i in range(len(self.dv_table[0].nodeID)):
                    node_id = self.dv_table[i].nodeID
                    value = self.dv_table[i].values
                    path = self.dv_table[i].path

                    self.tree.insert("", "end", text=node_id, values=(value, path))
                    

#functions ---------------------------------------------------
#initate a thread to send out dvtables
def stepThroughThreadCreate(DVTables, nodes, gui, root, cycleCountLock, textState):
    stepThroughThread = threading.Thread(target=stepThrough, args=(DVTables, nodes, gui, root, cycleCountLock))
    stepThroughThread.start()
    

# def stepThrough(DVTables, nodes, gui, root, cycleCount, cycleCountLock):
def stepThrough(DVTables, nodes, gui, root,  cycleCountLock):
    global cycleCount   #keep track of current cycles

    #save copy of current table, to compare later
    previousTable = copy.deepcopy(DVTables)

    #create threads to send, receive, & update tables
    threads = []
    for i in range(nodes):
        thread = threading.Thread(target=createNodeServers, args=(i, DVTables[i], nodes, gui, root))
        threads.append(thread)
        thread.start()
    
    #wait for threads to finish
    for thread in threads:
        thread.join()

    with cycleCountLock:
        cycleCount += 1
        #print(cycleCount, flush=True)

    #if we're at a stable point, update user
    if stableState(previousTable, DVTables):
        textState.set("Table is stable, cycle count: " + str(cycleCount))
    
    #notify user they can continue
    print("continue",flush=True)




#called from button, needed to create a thread to handle sending tables
def runThroughThreadCreate(DVTables, nodes, gui, root, cycleCountLock, textState):
    runThroughThread = threading.Thread(target=runThrough, args=(DVTables, nodes, gui, root, cycleCountLock))
    runThroughThread.start()

def runThrough(DVTables, nodes, gui, root,  cycleCountLock):    
    global cycleCount       #count cycles just in case
    start = time.time()     #start the timer on how long this takes
    
    #Pseudo do-while loop
    while True:
        #copy the current status of DVTables to compare later in stableState
        previousTable = copy.deepcopy(DVTables)

        #create threads to send, receive, & update tables
        threads = []
        for i in range(nodes):
            thread = threading.Thread(target=createNodeServers, args=(i, DVTables[i], nodes, gui, root))
            threads.append(thread)
            thread.start()

        #wait for threads to update
        for thread in threads:
            thread.join()

        print("all threads, have sent and updated tables", flush = True)

        #keep track of cycles, just in case
        with cycleCountLock:    
            cycleCount += 1

        #check if stable, if so, notify user in GUI
        if stableState(previousTable, DVTables):
            end = time.time()
            textState.set("Table is stable, total time: " + str(round(end-start, 3)))
            break


#create nodes to send and receive dvtables
def createNodeServers(nodeID, DVTable, nodeNum, gui, root):        

    #establish this nodesID for the portID
    serverPort = 5001 + nodeID

    #establish neighbor ports
    neighborPorts = []
    for node in range(nodeNum):
        if (DVTable.values[node] > 0):
            neighborPorts.append(5000 + DVTable.nodeID[node]) 

    #create server socket to listen dvtable
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', serverPort))
    server_socket.listen(5)

    #create client socket to send dvtable
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #send table
    sendTableThread = threading.Thread(target=sendTable, args=(neighborPorts, DVTable, client_socket, serverPort))
    sendTableThread.start()

    #listen for incoming connections
    updateLock = threading.Lock()   

    try:
        while True:
            server_socket.settimeout(2)       
            client_socket, client_addr = server_socket.accept()
            data = client_socket.recv(1024)

            #save the old path to compare for later
            oldPath = DVTable.path.copy()       

            #if data is received, update table
            if data:
                #reload data from sender
                receivedTable = pickle.loads(data)
                
                #update table
                DVTable = updateTable(DVTable, receivedTable)
                
                #if the table has changed at all from updateTable, resend the updated path
                if DVTable.path != oldPath: 
                    #print(DVTable.path, " != ", oldPath, ' at ' , str(DVTable.id), flush=True)
                    with updateLock:
                        root.after(0, gui.update_gui())
    #no more received tables
    except socket.timeout:
        pass
    finally:
        server_socket.close() 

#sends table to all neighbor ports
def sendTable(neighborPorts,DVTable, client_socket, serverPort ):  
    #wait for all node threads to be initialized
    #time.sleep(2)   #TODO: look into changing this so that sends instantly
    global isPaused


    #For each neighboring port set up connection and send
    for neighbor in neighborPorts:
        temp1 = True
        temp2 = True
        client_socket = None
        while temp1: #retry if connection failed
            try:
                #Connect to neighbor, send table, close connection
                client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                client_socket.connect(('127.0.0.1', neighbor))
                temp1 = False
            except socket.error as e:
                print("temp1 ", "socket error at ", str(DVTable.id), flush=True)
                while isPaused:
                    pass
                continue
        while temp2:
            try:   
                #Serialize the table before sending
                dv_data = pickle.dumps(DVTable)
                client_socket.send(dv_data)
                temp2 = False
            except socket.error as e:
                print("temp2 ","socket error at ", str(DVTable.id), flush=True)
                while isPaused:
                    #print("isPaused is True", flush=True)
                    pass
                continue
    
        client_socket.close()

    #time.sleep(4)

#update contents of DVTable with receivedTable contents, 
def updateTable(DVTable, receivedTable):
    #for each node connection re-evaluate connection values
    for i in range(len(DVTable.nodeID)):

        #if we're not looking at a self reference, and new value is less than current value of table, or the value is set to -1
        #honestly this section could probably be re-written so it's easier to follow but it works (i think) and i need to move on
        if receivedTable.values[i] > 0 and (receivedTable.values[i] < DVTable.values[i] or DVTable.values[i] == -1):
            #if the current value is set to -1, update value and path
            if DVTable.values[i] == -1:
                #add the path from the received table and the current path cost to the received table
                DVTable.values[i] = DVTable.values[receivedTable.id - 1] + receivedTable.values[i]
                DVTable.path[i] = str(DVTable.id) + str(receivedTable.path[i])
            #compare new value to current value
            elif (receivedTable.values[i] + receivedTable.values[DVTable.id - 1]) < DVTable.values[i]:
                #change values and path to updated info
                DVTable.values[i] = receivedTable.values[i] + receivedTable.values[DVTable.id - 1]
                DVTable.path[i] = receivedTable.path[i]
                
    return DVTable

#dead function, but need to keep the variables around or i need to rewrite other code
def togglePause():
    global isPaused
    isPaused = not isPaused

#detect if DVTable has changed after calling updateTable
def stableState(previousTable, DVTables):
    #check if tables have actually changed

    # print(previousTable[0].values, flush=True)
    # print(DVTables[0].values, flush=True)
    if len(previousTable) != len(DVTables):
           print("different sizes", flush= True)
           print(str(len(previousTable)), " != ", str(len(DVTables)), flush=True)
           return False

    for i in range(len(DVTables[0].values)):
        #check values for each node
        if previousTable[i].values != DVTables[i].values:
            return False
        
        #check path for each node
        if previousTable[i].path != DVTables[i].path:
            return False
        
    return True

#function for Closethread to actually close server/program
def close_thread():
    while True:
        userInput = input("Type 'exit' to closer server:\n")            #user can input exit to quit program, anything else is ignored and will wait for "exit"
        if userInput =="exit":
           os._exit(1)                                                  #closes program




# main ---------------------------------------------

"""
#get input file from user
inputFile = input("Enter the name of the distance vector file (.txt): ")

#checking for vaild input
if (inputFile.find('.txt') == -1):
    print("ERROR: Must be a .txt file")               #TODO: change to a loop that will continue to get input unless user quits

if(os.path.isfile("./" + inputFile) == 0 ):
    print("ERROR: File does not exist")    #TODO: change to a loop that will continue to get input unless user quits
    exit()                          
"""
inputFile = "input.txt" #TODO, remove this once fished coding, this is done to reduce need to type input.txt every time

#if passed all checks, open file and read info into links
file = open(inputFile, "r")
links = file.readlines()
file.close()

#initialize DV tables for each node 
    #note: MAX NUM OF NODES IS 6

#reading contents of input file
nodes = []
for link in links:
    values = link.split()

    #seach values to make sure there are only 6 nodes being referenced
    if int(values[0]) <= 6 and int(values[0]) >= 0:
        nodes.append(int(values[0]))
    if int(values[1]) <= 6 and int(values[1]) >= 0:
        nodes.append(int(values[1]))

# get the number of nodes from this file
nodes = set(nodes)      #this is done to eliminate duplicates and order them
nodes = list(nodes)     #turn it back to a list, easier to work with

#create DV tables
#DVTables = []
for (i, node) in enumerate(nodes):
    # create socket
    DVTables.append(DVTable(nodes)) # pass socket

# for each in DVTables:
#     pass
#     # create listening thread.

# tables are now created, go back through links and add the edges
#set the link(edge) to itself to zero
for i in range(len(nodes)):
    DVTables[i].id = int(i + 1)
    DVTables[i].values[i] = 0

#set up links(edges) from file & the path
for link in links:
    values = link.split()
    DVTables[int(values[0]) - 1].values[int(values[1]) - 1] = int(values[2])    #value of the edge
    DVTables[int(values[1]) - 1].values[int(values[0]) - 1] = int(values[2])    #value of the edge on the opposite table
    DVTables[int(values[0]) - 1].path[int(values[1]) - 1] = str(values[0]) + str(values[1])           #pathway of the edge, right now that is just the starting node
    DVTables[int(values[1]) - 1].path[int(values[0]) - 1] = str(values[1]) + str(values[0])          #pathway of the edge, right now that is just the starting node

cycleCount = 0
cycleCountLock = threading.Lock()

#gui setup
root = tk.Tk()

textState = tk.StringVar()
textState.set("Table is not stable")

gui = DVTableGUI(root, DVTables, textState)
# pauseButton = tk.Button(root, text="Pause/Resume", command=togglePause)
# pauseButton.pack()
# stepButton = tk.Button(root, text="Step through routing", command=lambda: stepThroughThreadCreate(DVTables, len(nodes), gui, root, cycleCount,cycleCountLock))
stepButton = tk.Button(root, text="Step through routing", command=lambda: stepThroughThreadCreate(DVTables, len(nodes), gui, root, cycleCountLock, textState))
stepButton.pack()

runButton = tk.Button(root, text="Run through the rest", command=lambda: runThroughThreadCreate(DVTables, len(nodes), gui, root, cycleCountLock, textState))
runButton.pack()


gui.update_gui()


#create thread to close the program
Closethread = threading.Thread(target=close_thread, args=())                         
Closethread.start()

#function to handle updating table
# cycleThread = threading.Thread(target=cycleGenerator, args=(i, DVTables[i], len(nodes), gui, root))
# cycleThread.start()


root.mainloop()




