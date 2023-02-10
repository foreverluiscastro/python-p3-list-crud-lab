def create_an_empty_list():
    # return None
    # empty_list = []
    # return empty_list
    return []

def create_a_list():
    # return None
    return [1,2,3,4]

def add_element_to_end_of_list(l, element):
    # return None
    l.append(element)
    return l

def add_element_to_start_of_list(l, element):
    # return None
    l.insert(0, element)
    return l

def remove_element_from_end_of_list(l):
    # return None
    l.pop(-1)
    return l

def remove_element_from_start_of_list(l):
    # return None
    l.pop(0)
    return l

def retrieve_first_element_from_list(l):
    # return None
    return  l[0]

def retrieve_element_from_index(l, index):
    # return None
    return l[index]

def retrieve_last_element_from_list(l):
    # return None
    return l[-1]
