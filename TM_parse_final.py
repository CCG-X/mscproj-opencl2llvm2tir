
# coding: utf-8

# In[48]:




def parse_file(filepath,filepath2):
    lines_out=[]
    lines_for_top=[]
    
    file_write_obj = open(filepath2, 'w')
    

    my_function_name=[]
    
    with open(filepath,'r') as file_object:
        
        line_in_1 = file_object.readline()
        #line_in_2 = file_object.readline()
        
        while line_in_1:
            
            words=line_in_1.replace('#0','pipe ').replace('*',' ').split()#"_"replacement is dangerous
            #words_for_top=line_in.replace('#0','pipe ').split()
            
            if not words:
                print ("line is BLANK")
           
            elif (words[0]=="define" and words[1]=="void") :
                if (words[2].find("pipe")==-1):
                    my_function_name.append(words[2])#split the name
            line_in_1 = file_object.readline()
            
    with open(filepath,'r') as file_object_1:
        line_in_2 = file_object_1.readline()
        
        while line_in_2:
            Dictionary={}
            Dictrunk={}
            str_out = ""
            str_out_for_top = ""
            #print(line_in_2)
            ADDlist=[]
            name=''
            #print("$$$$$$$$$$$$$$",line_in_2)

            #checking if line has "define void"
            #detect = _parse_line_find_func_def(line_in)
            #print "inside parse_file, line = ", line_in, "detect =", detect
            words=line_in_2.replace('#0','pipe ').replace('*',' ').replace(',',' ').split()#"_"replacement is dangerous
            line_in_2=line_in_2.replace('#0','pipe ').replace('*',' ')
            words_for_top=line_in_2.replace('#0','pipe ').split()
            #print("++++++++++=",words)
            
    #parse the KernelInput KernelCompute KernelOutput part
            if not words:
                print ("inside parse_file, line is BLANK")
            #by finding define void, to find function s  
            

        
            elif (len(words)>=3 and words[2] in my_function_name ):
                #print(line_in_2)
                #print("+++++++++",words[2])
                file_write_obj.writelines(line_in_2)
                #file_write_obj.write('\n') 
                
                while  line_in_2 :
                    
                    #print("!!!!!!!!!!!!!!!!!!!",line_in_2)
                    words=line_in_2.replace('#0','pipe ').replace('*',' ').replace(',',' ').split()
                    


                    if(len(words)>6):
                        #print('#############',words)
                        if(words[2]=='alloca' or words[0]=='define'):
                            print("ignore these lines",words)
                        elif(words[2].find('trunc')>-1):
                            #print('trunc!!!!!!!!')
                            Dictrunk[words[0]]=words[4]
                        elif(words[2].find('write')>-1):
                            #print('write!!!!!!!!!!')
                            words=line_in_2.replace(',',' ').replace(')',' ').split()
                            Dictionary[words[4]]=words[6]
                        elif(words[2].find('read')>-1):
                            #print('read!!!!!!!!!!')
                            words=line_in_2.replace(',',' ').replace(')',' ').split()
                            Dictionary[words[6]]=words[4]
                        elif(words[2].find('load')>-1):
                            #print('load!!!!!!!!!!')
                            Dictionary[words[0]]=words[5]
                        elif(words[0].find('store')>-1):
                            #print('store!!!!!!!!!!!')
                            words=line_in_2.replace(',',' ').split()
                            #print(words)
                            Dictionary[words[4]]=words[2]    
                        else:
                            ADDlist.append(line_in_2)
                            name=words[2]
                            #print("ignore this line",words)  
                    
                    elif(words[0]=="ret"):
                        break
                    #elif(words[0]=="ret"):
                     #                           
                      #  for chunk in words:               
                       #     str_out+=chunk+' '             
                        #str_out+="}"
                        #str_out+='\n'
                        #file_write_obj.writelines(str_out)
                        #break
 
                    line_in_2 = file_object_1.readline()
    

                #print("**********",Dictionary)
                #print("++++++++++",Dictrunk)
        
            #line_in_2 = file_object_1.readline()
            #file_write_obj.writelines(lines_out)
            #file_write_obj.write('\n')   
            #replace dictrunk with dictionary
            #print("¬¬¬¬¬¬¬¬¬¬",Dictrunk)
            for key in Dictrunk:
                #print("3333333",Dictionary,"3333333")
                if key in Dictionary:
                    #print(key)
                    #print("*************************",Dictionary)
                    #print("#########################",Dictrunk)
                    Dictionary[Dictrunk[key]]=Dictionary.pop(key)
                else:
                    continue
                #for k in Dictionary:
                 #   Dictionary[Dictrunk[key]]=Dictionary[k]
                  #  del Dictionary[k]
            
            for key in Dictrunk:
                #print("¬¬¬¬¬¬¬¬¬¬",Dictrunk)
                #print("%%%%%%%%%%%",Dictionary,"%%%%%")
                for k in Dictionary:
                    if (key == Dictionary[k]):
                        Dictionary[k]=Dictrunk[key]
                    else:
                        continue
            #input kernel+ output kernel
            #print("££££££££££££££££££££££££££££",ADDlist)
            if len(ADDlist)==0:
                k=''
                dic={}
                for key in Dictionary:
                    
                    
                    for K in Dictionary:
                        
                        if (key==Dictionary[K]):
                            k=K
                            if Dictionary[K] in dic:
                                dic[K]=dic.pop(Dictionary[K])
                            Dictionary[K]=Dictionary[key] 
                            #Dictionary[K]=Dictionary.pop[key] 
                            
                            dic[K]=Dictionary[K]
                for k in dic:
                        
                    #print(k,"+++++++++++") 
                    str_out=' i32 '+ k+ ' = '+ 'load ' +'i32 '     
                    str_out+=dic[k]+' '
                    str_out+='\n' 
                    file_write_obj.writelines(str_out)
                    #print(">>>>>>>>>>>>>>>>>>>>>",str_out)
                    str_out=""
                    str_out+=" ret void"             
                    str_out+='\n'
                    str_out+="}"
                    str_out+='\n'
                file_write_obj.writelines(str_out)
                            
                            
            #compute kernel         
            else:
                #print("+++++++++++++",ADDlist)
                for Sentence in ADDlist:
                    Chunk=Sentence.replace(',',' ').split()
                    
                    variable=[]
                    
                  
                    for i in range(5,len(Chunk)):
                        if (Chunk[i] not in variable):
                            variable.append(Chunk[i])
                    if(Chunk[0] not in Dictionary.values() ):
                        str_out='i32 '+Chunk[0]
                    else:
                        while (k in Dictionary.values()):
                            
                            k=list (Dictionary.keys()) [list (Dictionary.values()).index (k)]
                        str_out='i32 '+ k
                    #print("kkkkkkkkkkkkkkkk",k)        
                    str_out+=' '+'='+ name+' i32 '
                    #print("£££££££££££",variable)
                    for v in variable:
                        while (v in Dictionary.keys()):
                            v=Dictionary[v]
                        str_out+=v+' '
                        #print("!!!!!!!!!!!!!!",str_out)
                    str_out+='\n'
                    file_write_obj.writelines(str_out)
                #str_out='\n '
                str_out=" ret void"             
                str_out+='\n'
                str_out+="}"
                str_out+='\n'
                file_write_obj.writelines(str_out)
                                
                            
            
            
            
  #lines provided for KernelTop with *, and fine the * argument in TOP function
                
            if not words_for_top:
                print ("inside parse_file, line is BLANK")
            
            elif (words_for_top[0]=="define" and words_for_top[1]=="void") :
               
                
      
                my_function_name_for = words_for_top[2]#split the name 
                if (words_for_top[2].find("@read_pipe") and words_for_top[2].find("@write_pipe")): 
                    
                    #print ("line = ", line_in_2, "found function definition, function name is: ", my_function_name)
                    #print ("words are as follows not PIPE: ", words)
                    for chunk in words_for_top:
                        if (chunk!="noalias"and chunk!="nocapture"):
                            str_out_for_top+= chunk+' '
                            

                    lines_for_top.append(str_out_for_top)
                 
                    #file_write_obj.writelines(lines_out)
                    #file_write_obj.write('\n')
                
                        
            elif(words_for_top[0]=="ret" and words_for_top[1]=="void"):                   
                #print("ret void found:",words)
                for chunk in words_for_top:
                    str_out_for_top+=chunk+' '
                str_out_for_top+="}"
                str_out_for_top+='\n'
                lines_for_top.append(str_out_for_top)
                


            #print('&&&&&&&&&',Dictionary)        
            line_in_2 = file_object_1.readline()  
        file_write_obj.writelines(lines_out)
        file_write_obj.write('\n')       
        file_write_obj.close()
        #print('&&&&&&&&&',Dictionary)
    return lines_for_top

def Top(data,filepath2):
    lines_out=[]
    Out_file=[]
    dic_top={}
    list_variable=[]
    file_write_obj = open(filepath2, 'a')  
    file_write_obj.write(';---------------\n')
    file_write_obj.write(';KernelTop\n')
    file_write_obj.write(';---------------\n')    
    #with open(filepath2,'r') as file_object:

    for line_in in data:


        
     
        words1=line_in.replace(',',' ').replace(')',' ').replace('(',' ').split()
            #delete ret void in each line, only add ret void at the end

        #print("WWWWWWWWWWWW",words1)
        for i in range(len(words1)-1):

            if (words1[i]=='i32' and words1[i+1] not in dic_top):
                
                dic_top[words1[i+1]]=0
        if (words1[0]=="define"):
            for w in words1:
                if (w in dic_top):
                    dic_top[w]=dic_top[w]+1
    file_write_obj.write('define void @kernelTop (')
    for key in dic_top:
        if (dic_top[key]==1):
            file_write_obj.writelines("i32 "+ key+", ")  
    
    file_write_obj.write(' )'+"pipe "+"{")  
    file_write_obj.write('\n') 
        
    for line_in in data:    
        list=[]
        str_out=""
           
        words=line_in.split()
        for words in words:
            #print(words)
            
            if (words!="}"and words!="{" and words!="ret" and words!="void" and words!="pipe" and words!="define"):
                str_out+=words 
        if (str_out!='\n'and str_out!="" ):

            list="call "+str_out
            #print(list)
            file_write_obj.writelines(list)
            file_write_obj.write('\n') 
       # line_in = file_object.readline()
    
    file_write_obj.write("ret void")
    file_write_obj.write('\n')
    file_write_obj.write("}")
    file_write_obj.close()

            
            
    
    


if __name__ == '__main__':
    filepath = 'debug0.ll'
    filepath2='Main_0.txt'
    #filepath = 'kernels_channels.ll'
    data = parse_file(filepath,filepath2)
        #print("Printing data")
    #print("the final file is=\n",data)
    Top(data,filepath2)
    


# In[18]:




