
# coding: utf-8

# In[119]:


import re
import pandas as pd# use to write the file
rx_dict = {
    
        #define a regular expression to search the certain line
    'kernelInput': re.compile(r'kernelInput=(?P<kernelInput>.*)\n'),
    'kernelCompute': re.compile(r'kernelcompute=(?P<kernelCompute>.*)\n'),
    'kernelOutput': re.compile(r'kernelOutput=(?P<kernelOutput>.*)\n'), 
    'void':re.compile(r'void=(?P<void>.*)\n'), 
    'define':re.compile(r'define=(?P<define>.*)\n'), 
    
}


# In[120]:


def _parse_line_chunk(line):
    for key,rx in rx_dict.items():
        findreturns = line.find(key)
        if (findreturns>0):
            return key
    #if there are no matches
    return None
    


# In[122]:


def parse_file(filepath):
    lines_out=[]
    Out_file=[]
    with open(filepath,'r') as file_object:
        line_in = file_object.readline()
       
        while line_in:
            key = _parse_line_chunk(line_in)
            if key == 'kernelInput':
                str_out=""
                words=line_in.split()

                
                #print(words)
                for words in words:
                    if (words !="noalias" and words != "nocapture"): 
                        str_out +=words
                    str_out +=' '
                    str_out_end=str_out.replace('#0','pipe').replace('32*','32')
                lines_out.append(str_out_end)
                lines_out +=''
               #print(str_out_end)
                #print (lines_out)
            if key == 'kernelCompute':
                str_out=""
                words =line_in.split()
                #print(words)
                for words in words:
                    if (words !="noalias" and words != "nocapture"): 
                        str_out +=words
                    str_out +=' '
                    str_out_end=str_out.replace('#0','pipe')
                lines_out.append(str_out_end)
                lines_out +=' '
                    
                #print (lines_out)
            if key == 'kernelOutput':
                str_out=""
                words =line_in.split()
                #print(words)
                for words in words:
                    if (words !="noalias" and words != "nocapture"): 
                        str_out +=words
                    str_out +=' '
                    str_out_end=str_out.replace('#1','pipe').replace('32*','32')
                lines_out.append(str_out_end)
                lines_out +=' '
            #read next line if available
            line_in = file_object.readline()  
    return lines_out
               # print (lines_out)

                        



if __name__ == '__main__':
    filepath = 'kernels_channels-final.ll'
    #filepath = 'kernels_channels.ll'
    data = parse_file(filepath)
    #print("Printing data")
    print("the final file is=\n",data)
                    
                        

