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