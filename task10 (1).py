def common_characters(string1,string2):
    common=[]
    for i in string1:
        
        if i in string2:
            common.append(i)
            new_common=",".join(common)
               
    return("Common letters: " + new_common )