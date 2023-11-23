def create_an_empty_list():
    return list()

def create_a_list():
    return list([1,2,3,4])

def add_element_to_end_of_list(l, element):
    out = list(l)
    out.append(element)
    return out

def add_element_to_start_of_list(l, element):
    out = list(l)
    out.insert(0,element)
    return out

def remove_element_from_end_of_list(l):
    # listo = list(l)
    # listo.pop()
    list_length = len(l)
    return [li for idx, li in enumerate(l) if idx < list_length -1]
    # return listo
    #alternate solution

def remove_element_from_start_of_list(l):
    # return [li for idx, li in enumerate(l) if idx > 0]
    #alternate solution
    listo = list(l)
    listo.pop(0)
    return listo
def retrieve_first_element_from_list(l):
    # return [li for idx, li in enumerate(l) if idx == 0][0]
    #alternate solution
    listo = list(l)
    return listo[0]

def retrieve_element_from_index(l, index):
    listo = list(l)
    return listo[index]
    

def retrieve_last_element_from_list(l):
    listo = list(l)
    return listo[-1]
