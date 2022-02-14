##Comedians.py
# You will need the networkx package installed for this code to work, specially the last function, draw_graph


import networkx as nx
import matplotlib.pyplot as plt

## Function parse_csv_to_graph, where the keys are the influencers and the values are a list of all the people they've influenced
## The function is designed for a csv specifically like the file comedians.csv, where each line contains a source and a target separated by a comma (',').


##Exercise 1
def parse_csv_to_graph (filepath):
    adjacencylist={}
    try:
        infile= open(filepath, 'r')
        for i in infile.readlines():
            linecontents= i.split(',')
            source= linecontents[0]
            target= linecontents[1].replace('\n', '')
            if not (source in list(adjacencylist.keys())):
                adjacencylist[source]=[target]
            else: 
                adjacencylist[source].append(target)
                
            #to make sure every node has a key in the adjacency list, even if its value is just an empty list    
            if not (target in list(adjacencylist.keys())):
                adjacencylist[target]=[]
            else:
                pass
            
        infile.close()
            
    #Returning None in case there's any error. The messages are included to make the program more user-friendly
    except FileNotFoundError:
        print('The inserted path for the csv file is invalid.')
        return None
    
    except IndexError:
        print('Please review the csv file. It is possible that there\'s a line where a comma is missing.')
        return None
        
    except OSError: 
        print('Please check the inserted path as there seems to be a problem with the given path.')
        return None
    
    except:
        print('Something is not quite right')
        return None
             
    return adjacencylist


##Exercise 2
def influence_chains(diagram, start, end=None):
    ## "diagram" was interpreted as being the dictionary that contains the graph. 
    ## If instead, you want to give as input the filepath, uncomment the following line: 
    #diagram= parse_csv_to_graph(diagram)
    if not (end in list(diagram.keys())) or not (start in list(diagram.keys())):
        print('at least one of the comedian names you inserted is not included in the chosen csv file')
        return False
    
    #in the case there's no end target selected, it returns a dictionary with all the comedians influenced by the comedian (in the keys of the dictionary)
    if not end:
        newd={}
        for i in diagram[start]:
            newd[i]=diagram[start].index(i)+1
        return newd
    
    
    else:
        path=[start]
        if end in diagram[start]:
            path.append(end)
            return path
        elif not diagram[start]:
            return False
        else:
            listofnext=[]
            a=0 #this variable is only useful to avoid trouble when the function is detangling itself from recursion
            for i in diagram[start]:
                listofnext.append(len(diagram[i]))
                #Recursion
                new_element=  influence_chains(diagram, i, end)
                if new_element:
                    path.append(new_element)
                    #Note that this function doesn't return the list with the shortest path. It returns a list with
                    #       the first path between the two comedians that it finds
                    
                    break
                
            if len(path) == 2:
                if end in path[1]:
                    a = 1

            if max(listofnext) == 0 and a != 1:
                return False
            
            elif not (end in diagram[i]) and a!=1 :
            #in the case there's no connection between the two comedians, the outcome is False
                return False
            
        #making the end result more pretty. At this point we have a list with lists and strings. 
        c= 0
        listcheckr= True
        while type (c) == int and listcheckr:
            if type(path[c]) == list:
                for i in path[c]:
                    path.append(i)
                path.remove(path[c])
            c+= 1
            pathtypes= []
            for i in path:
                pathtypes.append(type(i))
            if not (list in pathtypes):
                listcheckr = False
            else: 
                pass
            
        return path 


## Exercise 3
def top_10_influencers(diagram):
    ## "diagram" was interpreted as being the dictionary that contains the graph. 
    ## If instead, you want to give, as input the filepath, uncomment the following line: 
    #diagram= parse_csv_to_graph(diagram)

    t10i= []
    
    #initialising the list with the first 10 comedians
    if len(list(diagram.keys())) >= 10:
        for i in range(10):
            t10i.append(list(diagram.keys())[i])      
    else:
        for i in (list(diagram.keys())):
            t10i.append(list(diagram.keys())[list(diagram.keys()).index(i)])
        return t10i
    
    listoflengths=[]
    for i in t10i:
        listoflengths.append(len(diagram[i]))
    for i in range(len(list(diagram.keys()))):
         if list(diagram.keys())[i] in t10i:
                 continue
         else:
             listofdifferences=[]
             for j in t10i:
                 listofdifferences.append(len(diagram[j]) - len(diagram[list(diagram.keys())[i]]))
                 
             if min(listofdifferences) < 0:
                 t10i.pop(listofdifferences.index(min(listofdifferences)))
                 t10i.append(list(diagram.keys())[i])
                    
    return t10i


##Exercise 4
def draw_graph(diagram, node_size= 4, edge_size= 0.2 ):
        ## "diagram" was interpreted as being the dictionary that contains the graph. 
        ## If instead, you want to give, as input the filepath, uncomment the following line: 
        #diagram= parse_csv_to_graph(diagram)
    
        G= nx.DiGraph()
        #constructing the graph object from the adjacency list obtained with parse_csv_to_graph
        for i in list(diagram.keys()):
            for j in range(len(diagram[i])):
                G.add_edge(i, diagram[i][j])
            
        #note that the code is supposed to open a new window with the graph represented,
        #                         where you can zoom in and see the graph in more detail.
        #if the window doesn't pop up try to see if you have the Graphics backend set to "Automatic"
        #                           (this should fix the problem at least in Spyder in a Windows OS)
        
        pos= nx.circular_layout(G)    
        plt.figure(figsize=(26,26))
        nx.draw_networkx(G, pos, node_size= node_size, edge_size= edge_size, font_size= 7, edge_color='gray' )
        plt.show()
