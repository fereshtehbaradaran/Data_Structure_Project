import AVL_Tree

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