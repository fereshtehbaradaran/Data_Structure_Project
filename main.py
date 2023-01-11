import AVL_Tree
import node

patientsBalancedByID = AVL_Tree()
patientsBalancedByIDRoot = None
patientsBalancedByHM = AVL_Tree()
patientsBalancedByHMRoot = None
patientsBalancedByOrder = AVL_Tree()
patientsBalancedByOrderRoot = None
numberOfPatients = 0



def add(ID,HM):
    global patientsBalancedByIDRoot
    global patientsBalancedByHMRoot
    global patientsBalancedByOrderRoot
    global numberOfPatients
    
    patientsBalancedByIDRoot = patientsBalancedByID.insert(patientsBalancedByIDRoot,node(ID,HM,numberOfPatients))
    patientsBalancedByHMRoot = patientsBalancedByHM.insert(patientsBalancedByHMRoot,node(HM,ID,numberOfPatients))
    patientsBalancedByOrderRoot = patientsBalancedByOrder.insert(patientsBalancedByOrderRoot,node(numberOfPatients, ID, HM))
    numberOfPatients += 1



def serveFirst():
    global patientsBalancedByIDRoot
    global patientsBalancedByHMRoot
    global patientsBalancedByOrderRoot
    global numberOfPatients
    
    toServe = patientsBalancedByOrder.getMinValueNode(patientsBalancedByOrderRoot)
    print(toServe.second,toServe.third)
    patientsBalancedByIDRoot = patientsBalancedByID.delete(patientsBalancedByIDRoot, toServe.second)
    patientsBalancedByHMRoot = patientsBalancedByHM.delete(patientsBalancedByHMRoot, toServe.third)
    patientsBalancedByOrderRoot = patientsBalancedByOrder.delete(patientsBalancedByOrderRoot, toServe.first)
    numberOfPatients -= 1



def serveSickest():
    global patientsBalancedByIDRoot
    global patientsBalancedByHMRoot
    global patientsBalancedByOrderRoot
    global numberOfPatients
    
    toServe = patientsBalancedByHM.getMinValueNode(patientsBalancedByHMRoot)
    print(toServe.second,toServe.first)
    patientsBalancedByIDRoot = patientsBalancedByID.delete(patientsBalancedByIDRoot, toServe.second)
    patientsBalancedByHMRoot = patientsBalancedByHM.delete(patientsBalancedByHMRoot, toServe.first)
    patientsBalancedByOrderRoot = patientsBalancedByOrder.delete(patientsBalancedByOrderRoot, toServe.third)
    numberOfPatients -= 1



def update(ID,newHM):
    global patientsBalancedByIDRoot
    global patientsBalancedByHMRoot
    global patientsBalancedByOrderRoot
    global numberOfPatients
    
    toUpdate = patientsBalancedByID.searchNode(patientsBalancedByIDRoot,ID)
    HM = toUpdate.second
    order = toUpdate.third
    patientsBalancedByIDRoot = patientsBalancedByID.delete(patientsBalancedByIDRoot, ID)
    patientsBalancedByHMRoot = patientsBalancedByHM.delete(patientsBalancedByHMRoot, HM)
    patientsBalancedByOrderRoot = patientsBalancedByOrder.delete(patientsBalancedByOrderRoot, order)
    patientsBalancedByIDRoot = patientsBalancedByID.insert(patientsBalancedByIDRoot,node(ID,newHM,order))
    patientsBalancedByHMRoot = patientsBalancedByHM.insert(patientsBalancedByHMRoot,node(newHM,ID,order))
    patientsBalancedByOrderRoot = patientsBalancedByOrder.insert(patientsBalancedByOrderRoot,node(order, ID, newHM))



for i in range(1,7):
    fileName = "inpute"+str(i)+".txt"

    with open(fileName, 'r') as inpute:

        for line in inpute:
            value = line.split()

            if value[0] == "Add":
                add(value[1],value[2])
            elif value[0] == "Update":
                update(value[1],value[2])
            elif value[0] == "Serve" and value[1] == "First":
                serveFirst()
            elif value[0] == "Serve" and value[1] == "Sickest":
                serveSickest()
            else:
                print("\nOutput "+str(i)+":")