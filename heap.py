    # List to hold values from dictionary
    heap_dict=[]
    
    # extract the values from dictionary
    for i in docs_to_check.values():
        heap_dict.append(i)
        
    # heapify the values
    hq.heapify(heap_dict)  
    
    # list to hold final heapified dictionary
    new_dict=[]

    # mapping and reconstructing final dictionary
    for i in range(0,len(heap_dict)):

        # Iterating the oringinal dictionary
        for k,v in docs_to_check.items():

            if v==heap_dict[i] and (k,v) not in new_dict:
                new_dict.append((k,v))

    result_dict=dict(new_dict)

    
    return(result_dict)
