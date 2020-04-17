
def current(x,y):											
	current_array = []												# Retrieves information about the celles surrounding the current one. 
	Current_nodes.append(x)											
	current_array.append(north(x))
	current_array.append(south(x))
	current_array.append(west(x))
	current_array.append(east(x))
	current_array.append(northeast(x))
	current_array.append(northwest(x))
	current_array.append(southeast(x))
	current_array.append(southwest(x))

	if  len(Current_nodes) != 1:								   # Stops potential recursion errors within during the search. 
		if x == Current_nodes[-2]: 
			checked_nodes.remove(x) 
			Current_nodes.remove(Current_nodes[-1])
			x = Current_nodes[-1]
	
	for i in current_array:			
		if i in unchecked_nodes and i >= 1:
			checked_nodes.append(i)
			unchecked_nodes.remove(i)
			checked_nodes_value.append(y)
		if i == endnode:
			Current_nodes.append(endnode)
			return(print("The fastest route within the bounds you gave me is:" + " " + str(Current_nodes) ))						   # Stores the information about the right kind of nodes. 
	near = closest(checked_nodes, endnode)
	return current(near, y+1)

def closest(checked_nodes, K): 									  # Checks which node is closest based on endnode, by itself would produce errors, but with potentialerrorstopper its no worries. 
    return checked_nodes[min(range(len(checked_nodes)), key = lambda i: abs(checked_nodes[i]-K))] 
 
def north(CD):													  # The retrieval of the information about the node, has a series of rules concerning the direction each node can take to insure structural integrity.
	if CD != C1 and CD != C2:	
		C = CD - inputer
		return C

def south(CD):
	if CD not in South and CD != C3 and CD != C4:
		C = CD + inputer
		return C

def west(CD):
	if CD not in West and CD != C1 and CD != C3:
		C = CD - 1
		return C

def east(CD):
	if CD not in East and CD != C2 and CD != C4:
		C = CD + 1
		if C not in RTG:
			return C

def northeast(CD):
	if CD not in Northeast and CD != C1 and CD != C2 and CD != C4:
		C = north(CD) + 1
		return C

def northwest(CD):
	if CD not in Northwest and CD != C1 and CD != C2 and CD != C3:
		C = north(CD) - 1
		return C

def southeast(CD):
	if CD not in Southeast and CD != C2 and CD != C4 and CD != C3:
		C = south(CD) + 1
		return C

def southwest(CD):
	if CD not in Southwest and CD != C1 and CD != C4 and CD != C3:
		C = south(CD) - 1
		return C

if __name__ == "__main__":
	inputer = int(input("Please enter the amount of rows you want:"))
	startnode = int(input("Please enter your startnode:"))
	endnode = int(input("Please enter your endnode:"))
	unchecked_nodes = []
	checked_nodes = []
	checked_nodes_value = []
	RTG = []
	Northeast = []
	Northwest = []
	East = []
	South = []
	Southeast = []
	Southwest = []
	West = []
	Current_nodes = []
	k = 3

	C1 = 1
	C2 = inputer 
	C3 = inputer**2-inputer+1
	C4 = inputer**2

	for i in range((inputer**2)+1):
		unchecked_nodes.append(i)

	for i in range(inputer+inputer, inputer**2, inputer):
		East.append(i)
		Northeast.append(i)
		Southeast.append(i)

	for i in range(inputer**2-inputer+2, inputer**2):
		South.append(i)
		Southeast.append(i)
		Southwest.append(i)

	for i in range(1+inputer,inputer**2-inputer+1,inputer):
		West.append(i)
		Southwest.append(i)
		Northwest.append(i)

	current(startnode,1)
	north(0)
	south(0)
	west(0)
	east(0)
	northeast(0)
	northwest(0)
	southeast(0)
	southwest(0)
	closest(checked_nodes, k)

	











