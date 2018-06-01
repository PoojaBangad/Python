#!usr/bin/python


def replacement(str):
    if str.endswith('ly'):
        str=str[:-2]
        str+='ing'
    elif str.endswith('ing'):
        str=str[:-3]
        str+='ly'
        
    return str

        
if(__name__=='__main__'):
    str=raw_input('Enter a word:')
    result=replacement(str)
    if(result==str):
        print("No ly or ing available")
    else:
        print(result)
    
