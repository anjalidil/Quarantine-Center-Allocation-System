
# coding: utf-8

# In[2]:



import re
from collections import defaultdict 

class mainMenuChoices:
    
    def bubbleSort(self,arr,n): 
        for i in range(n-1): 
            for j in range(0, n-i-1):           
                if arr[j] > arr[j+1] : 
                    arr[j], arr[j+1] = arr[j+1], arr[j] 
        return
        #print ("\nRemaining number of seats in each center( smallest to largest):\t\n",arr) 
           
        
    ###Dijkstra's start###
    def minimumDistance(self,dist,queue): 
         # Initialize min value and min_index as -1
        minimum = float("Inf") 
        min_index = -1

        # from the dist array,pick one which has min value and also still in queue           
        for i in range(len(dist)): 
            if dist[i] < minimum and i in queue: 
                minimum = dist[i] 
                min_index = i 
        return min_index 
  
   # Function to print shortest path
    def printshortestpath(self, parent, j,vertLet): 
          
        if parent[j] == -1 :  
            print("\t\t\t\t\t\t\t\t%s" %(vertLet[j])) 
            return
        self.printshortestpath(parent , parent[j],vertLet) 
        print("\t\t\t\t\t\t\t\t%s" %(vertLet[j])) 
          
     #Function to print the distance
    def printTable(self, dist, parent,vertLet,letter): 
        
        i=letter
        print("\nCenter \t\t\tDistance from The Airport(km)\t\tPath to the center") 
        print("-----------------------------------------------------------------------------------")
        if len(dist): 
            print("%s --> %s \t\t%d \t\t\t\t\t" % (vertLet[0], vertLet[i], dist[i])), 
            self.printshortestpath(parent,i,vertLet) 


     #Function that implements Dijkstra's single source shortest path algorithm for a graph represented using adjacency matrix representation      
    def dijkstra(self, graph, vertLet,letter): 
  
        row = len(graph) 
        col = len(graph)
        
        # Initialize all distances as INFINITE 
        dist = [float("Inf")] * row 

        #to store shortest path tree
        parent = [-1] * row 

        # Distance of source vertex from itself is always 0 
        dist[0] = 0

        queue = [] 
        for i in range(row): 
            queue.append(i) 
            
        while queue:

            # Pick the minimum dist vertex  
            # from the set of vertices 
            # still in queue
            u = self.minimumDistance(dist,queue)
            
            # remove min element
            queue.remove(u) 
            
            for i in range(col):             
                if graph[u][i] and i in queue: 
                    
                    if dist[u] + graph[u][i] < dist[i]:
                        
                        dist[i] = dist[u] + graph[u][i] 
                        parent[i] = u 
                    
        # call the printSolution function    
        self.printTable(dist,parent,vertLet,letter) 
         
    def centers(self,arr,center,letCen,graph, vertLet):

        fix = 250
        for i in range (0, len(center)):
            ele = int(input("Center {0} existing count\t  :\t" .format(center[i])))
            if ele <0 or ele>250:
                print("Invalid input. Please enter only correct counts. (Should be a integer within range of 0-250)")
                print("Please enter from the begining\n")
                self.centers(arr,center,letCen,graph, vertLet)
            else:             
                remain = fix-ele
                letter = str(remain) + str(center[i])
                letCen.append(letter)
                arr.append(remain)
            
        print("\n\nRemaining Number of seats in each center(A->Z):\t\n",arr)
        n = len(arr)
        self.bubbleSort(arr,n) 
        print ("\nRemaining number of seats in each center( smallest to largest):\t\n",arr)

        letCen.sort(key=locationSort)
        print("\n\nCenters with their remaining seats in the center: \n",letCen)
        self.submenu(arr,center,letCen,graph, vertLet)
    
    
    def submenu(self,arr,center,letCen,graph, vertLet):
        print("\n\tSub Menu\n")
        print("\t1)Check whether there's enough space for passengers that going to be arrived \n\t2)Allocate a center for passengers who has already arrived to Sri Lanka\n\t3)Back to main menu/Input exsiting count in centers\n\t0)Exit from all")
        choice2 = int(input("\nMy Choice: "))
        
        if choice2 == 1:
            tobe = int(input("\nEnter Number of passengers going to arrived: "))
            if tobe>arr[10]:
                print("\nSorry, there's no enough space in a center for that passengers")
                self.submenu(arr,center,letCen,graph, vertLet)
            else:
                print("\nThere's more than enough spaces have. Let them come  :) !!!")
                self.submenu(arr,center,letCen,graph, vertLet)
               
               
        elif choice2 ==2:
            self.planes(arr,center,letCen,graph, vertLet)
         
        elif choice2 ==3:      
            home()
        elif choice2 == 0:
            exit()
            
        else:
            print("Invalid Input. Please give your choices according to the give menu")
            self.submenu(arr,center,letCen,graph, vertLet)
         
    def planes(self,arr,center,letCen,graph, vertLet):
        plane=[]
        
        n = int(input("\nnumber of planes to be allocated in centers: "))
        
       
        for i in range (0, n):
            planeId = input("\nPlane ID: ")
            deptCountry = input("departed country: ")
            passcount = int(input("Enter no of passengers arrived: " ))
            
            if passcount<0 or passcount>arr[10]:
                print(arr[0])
                print("Invalid input. Please enter correct inputs.(Passengers count should be interger within the range of 0 and largest remaining count of centers)")
                print("Please enter from the begining")
                self.planes(arr,center,letCen,graph, vertLet)
                break
            else:
                plane.append(passcount)
        #print(plane)
        
        self.bubbleSort(plane,n) 
        
        print ("\nPassenger count in smallest to largest:",plane) 

        splited=[]
        for i in range (0,len(plane)):

            for j in range(0,len(center)):
                if plane[i]<=arr[j]:

                    splited = re.split('\d+',letCen[j],1)
                    print("\nAllocated center: ",splited[1])     

                    for k in range(0, len(center)):
                        if splited[1] == center[k]:
                            letter = k
                       
                    #print(j)
                    arr[j] = arr[j]-plane[i]
                    print("Updated remaining count in center {0}: ".format(splited[1]),arr[j])
                   
                    self.dijkstra(graph,vertLet,letter)
                    break
        #print(arr)
        self.submenu(arr,center,letCen,graph, vertLet)
                
def home():

    #MAIN MENU
    print("\t\t\t\n~~~~~Welcome to Bandaranaika International Airport~~~~~~~\n\n This software will helps you to allocate newly arrived passengers for quarantine centers")
   
    print("\nPlease reference below table for centers\n\n\n \t\tCenter Letter\t|\tCenter name\t\t\t| \tLocated District\t\t\t\t\t\t\t\t\t\t\t------------------------------------------------------------------------------------------")
    print("""\t\t\tA\t|\tColombo General Hospital\t| \tColombo\t\n
\t\t\tB\t|\tDGH\t\t\t\t|\tNegombo\t\n
 \t\t\tC\t|\tWelisara    \t\t\t|\tGampaha\t\n
\t\t\tD\t|\tTeaching Hospital\t\t|\tKurunagala\t\n
\t\t\tE\t|\tNational Hospital   \t\t|\tKandy\t\n
\t\t\tF\t|\tGeneral Hospital \t\t|\tRathnapura \t\n
\t\t\tG\t|\tNaval camp-Boossa\t\t|\tGalle\t\n
\t\t\tH\t|\tTeaching Hospital\t\t|\tJaffna\t\n
\t\t\tI\t|\tKandakadu\t\t\t|\tAnuradhapura\t\n
\t\t\tJ\t|\tPunanai\t\t\t\t|\tBatticaloa\t\n
\t\t\tK\t|\tDiyathalawa\t\t\t|\tBadulla\t\n""")

    
    print("Main menu\n Choose your option from below\n")
    print("1) Add number of lodgers existing in Centers \n0) Exit from main menu\n")
   
    main = mainMenuChoices()
    

    #program arrays
    arr=[] 
    center=["A","B","C", "D", "E", "F", "G", "H", "I", "J", "K"]
    letCen=[]
    
      
    graph = [[0, 40, 35, 100, 120, 110, 140, 0, 0, 0, 0], 
        [40, 0, 25, 0, 0, 0, 0, 0, 0, 0, 0], 
        [35, 25, 0, 65, 0, 0, 0, 0, 0, 0 ,0], 
        [100, 0, 65, 0, 45, 0, 0, 0, 110, 170, 0], 
        [120, 0, 0, 45, 0, 120, 0, 0, 0,0 ,0], 
        [110, 0, 0, 0, 120, 0, 0, 0, 0, 0, 130], 
        [140, 0, 0, 0, 0, 0, 0, 0, 0, 0, 220], 
        [0, 0, 0, 0, 0, 0, 0, 0, 200, 0, 0], 
        [0, 0, 0, 110, 0, 0, 0, 200, 0, 150, 0],
        [0, 0, 0, 170, 0, 0, 0, 0, 150, 0, 0],
        [0, 0, 0, 0, 0, 130, 220, 0, 0, 0, 0]
        ] 
    vertLet=["Colombo","Negombo", "Gampaha", "Kurunagala", "Kandy", "Rathnapura", "Galle", "Jaffna", "Anuradhapura", "Batticaloa", "Badulla"]
  
    
    opt = int(input("\nMy Option: \n"))
    if opt == 1:
        #calling centers function
        main.centers(arr,center,letCen,graph, vertLet)
  
    elif opt == 0:
        print("Thank you for using our software. Hope you enjoyed!!!")
        exit()
    else:
        print("Invalid input. Please give option as the given menu")
        home()
    
    

    
def locationSort(key):
    val = re.split('(\d*\.\d+|\d+)', key) 
    return tuple((e.swapcase() if i % 2 == 0 else float(e))
            for i, e in enumerate(val))

home()
   
   

