from configparser import ConfigParser

from array import *
import re
import os
import cv2
def Creat_Newfile(namefile):
    with open(namefile) as file:
        all_file = file.read()
    regex = re.compile('%')
    if(regex.search( all_file) != None):
        all_file1 = re.sub('%', '%%',all_file)
    new_name = namefile+'new'
    with open(new_name, 'w') as newf:
        newf.write(all_file1)
    return new_name

class Node(object):
    def __init__(self,num_Node = 0,in_Node = None, out_Node= None, Check_In= False):#out_n
        self.num_Node = num_Node#day la so thu tu Node trong file cell.ap 
        self.in_Node = in_Node
        self.out_Node = out_Node
        self.Check_In = Check_In
    def __eq__(self, obj):#ham de so sanh object = num_Node
        if isinstance(obj, Node) and obj.num_Node == self.num_Node: 
            return True
        return False
def Check_Node(number , ListNode):
    return Node(number,None,None,False) in ListNode
ListNode = []

with open('filecheck.txt') as file:
        all_file = file.read()
with open('final.py', 'w') as newf:
        newf.write(all_file)
        

with open('file_funtion.txt') as file:
        all_file = file.read()
with open('funtion.py', 'w') as newf:
        newf.write(all_file)

list_name = []

def Process(file):
    newfile = Creat_Newfile(file)
    config = ConfigParser()
    config.read(newfile)
   


    i = 0
    j = 0
    for options in config.options("Connections"):
        # print(options , config.get("Connections", options))
        number = options.split(".")
        
        #tao node theo so ben trai 
        if(Check_Node(int(number[0]) , ListNode) == False):
            NewNode = Node(int(number[0]) , None, None , False)#nho kiem tra num_Node la int 
            ListNode.append(NewNode)
   
        
        #Xu ly dau ";"
        Right = config.get("Connections", options)
        last_right = Right[len(Right)-1] 
        right1 = Right[:len(Right)-1] if last_right == ';' else Right  
        list_right = right1.split(';') if ';' in right1 else [right1]
        j = j + len(list_right)


        #Xu ly ben phai 
        for value in list_right : 
            
            value1 = value.split(".")
            #print(giatri1)
            node_number_0 =  Node(int(number[0]) , None, None , False)
            get_node = ListNode[ListNode.index(node_number_0)]
            #lay Node ben trai 
            dict3 = {int(value1[1]) : get_node}#tao dictionary dau vao cua tung thang ben phai 
            if(Check_Node(int(value1[0]) , ListNode) == True):
                i = i+1
            if(Node(int(value1[0]) , dict3 , None , False) not in ListNode): 
                NewNode1 = Node(int(value1[0]) , dict3 , None , False)
                ListNode.append(NewNode1)
            else:
                node_number_value10 =  Node(int(value1[0]) , None, None , False)
                get_node_value1 = ListNode[ListNode.index(node_number_value10)]
                if get_node_value1.in_Node is not None:
                    get_node_value1.in_Node.update(dict3)
                else: get_node_value1.in_Node = dict3
    
    list_input_element = []
    for section in config.sections():#Kiem tra tung section 1 
        if 'Node:' in section:#neu ma section có Node t bat dau xu ly 
            # print(options , config.get("Connections", options))
                #if 'Node:' in section:
                config_section =  config[section]#tao bien moi la lay bat dau tu section dang xet 
                id = config_section['id']# lay parametr
                if('%' in id):
                    id =''
                num_node = int(section.split(':')[1])#lay so thu tu Node minh dang xet (Node trong file cell.ap)
                output_num = 0#so luong dau ra = 0
                list_element_of_node = config.options(section)# lay tap hop cac thong so cua Node 
                
                if 'file' in list_element_of_node: #neu thong so file co trong Node 
                    str_value_of_file = config_section['file'] #lay gia tri trong option file 
                    
                    output_num =  1 if ',' not in  str_value_of_file else  len(str_value_of_file.split(','))#dem so luong dau vao bang cach kiem tra so luong any trong option file 
                if 'name' not in list_element_of_node:#kiem tra Node nao ko cos name 
                    #num_node da mang gia tri int roi 
                    node_number =  Node(num_node, None, None , False)#tao node cos num_Node bang so thu node cua node minh dang xet 
                    get_node = ListNode[ListNode.index(node_number)]
                    #2 dong kia la de tim Node co so thu tu bang gia tri Node m dang xet 
                    out_node = {1 : config_section['file']}#tao ra 1 dictionary 
                
                    get_node.out_Node = out_node # vi day xu ly file dau vao nen out_Node bang dictionay vua tao luon 
                    
                    get_node.Check_In = True
                    list_input_element.append(get_node)
    while(all( map(lambda node: node.Check_In, ListNode)) == False):    
        
        for section in config.sections():#Kiem tra tung section 1  
            
            if 'Node:' in section:#neu ma section có Node t bat dau xu ly 
                list_element_of_node = config.options(section)
                
                if 'name' in list_element_of_node:
                    config_section1 =  config[section]#tao bien moi la lay bat dau tu section dang xet 
                    
                    name = config_section1['name']#lay ten ham 
                    if(name == 'heqm'):
                        name = 'heq'
                    if(name == 'avg2'):
                        name = 'avg'
                    if(name == 'movl2'):
                        name = 'movl'
                    if(name == 'movl3'):
                        name = 'movl'
                    if(name == 'max2'):
                        name = 'max'
                    
                    
                    
                    
                    id = config_section1['id']# lay parametr
                    if('%' in id):
                        id =''
                    
                    num_node = int(section.split(':')[1])#lay so thu tu Node minh dang xet (Node trong file cell.ap)
                    output_num = 0#so luong dau ra = 0
                    if 'file' in list_element_of_node: #neu thong so file co trong Node      
                        str_value_of_file = config_section1['file'] #lay gia tri trong option file  
                        output_num =  1 if ',' not in  str_value_of_file else  len(str_value_of_file.split(','))#dem so luong dau vao bang cach kiem tra so luong any trong option file 
                    
                        
                        #list_value_of_file = [str_value_of_file] if ','  not in str_value_of_file else str_value_of_file.split(',')
                    #3 dong tren kiem tra xem co bn dau ra cua node 
                    
                    #kiem tra neu toan bo node chua có dau ra het thi van chay 
                        #lay node trong listnode la node minh dnag xet 
                    node_number =  Node(num_node, None, None , False)
                    node = ListNode[ListNode.index(node_number)]
                    
                    if name not in list_name:
                        list_name.append(name)
                        if node.in_Node is not None:
                            with open('funtion.py', 'a') as newf1:
                                        newf1.write('\ndef '+name+'_result(command ,id , input ,output):')
                                        newf1.write('\n\tos.system(command+\' -o '+name+' \'+id+\' \'+input+\' \'+output)')
                                        newf1.write('\n\treturn output\n')
                        else:
                            with open('funtion.py', 'a') as newf1:
                                        newf1.write('\ndef '+name+'_result(command ,id , output):')
                                        newf1.write('\n\tos.system(command+\' -o '+name+' \'+id+\' \'+output)')
                                        newf1.write('\n\treturn output\n')

                
                    # for node in ListNode:
                    #list_input  = list(node.in_Node.values())
                    if(node.Check_In == True):
                        continue
                
                    # print(node.num_Node)
                    if(node not in list_input_element):#kiem tra neu ma node dang xet ko phai la node dau vao 
                        
                        output_list = ['node'+str(node.num_Node)+'out'+str(x)+'.out' for x in range(1,output_num+1,1)]#dat ten cho output
                        #print(output_list)
                    else:
                        output_list = [node.out_Node[1]]
                    

                    if output_num == 0:
                        
                        node.Check_In = True
                        continue
                    
                    if node.in_Node is not None:#kiem tra dau vao ko phai None (co ham ko phai ham input nhung dau vao van None vd nhu strel ne phai ktra ntn )
                        print("Node" , num_node)
                        list_input  = list(node.in_Node.values())#lay tap Node cua in_Node


                        #   take all value of node with 'map' and check with method 'all'
                        list_test = all(map(lambda node : node.Check_In, list_input))#kiem tra du dao vao chua 
                        #print(type(list_test))
                        if list_test:
                            *temp1,  = node.in_Node
                            temp = sorted([*map(lambda x: int(x), temp1)])
                            #print(node.num_Node)
                            input = ','.join(map(lambda x:'path_data+\''+node.in_Node[x].out_Node[1]+'\'',temp))
                        # output_list = ['node'+node.num_Node+'out'+str(x)+'.out' for x in range(1,output_num+1,1)]
                        
                            output = ','.join('path_data+\''+x+'\'' for x in output_list)
                            with open('final.py', 'a') as newf:
                                #newf.write('\nos.system(command+\' -o '+name+' '+id+' '+input+' '+output+'\')')
                                newf.write('\ninput = ('+input+')')
                                newf.write('\noutput = ('+output+')')
                                newf.write('\nif type(output) != type(\'abc\'):')
                                newf.write('\n\toutput = \',\'.join(output)')
                                newf.write('\nif type(input) != type(\'abc\'):')
                                newf.write('\n\tinput = \',\'.join(input)')
                                newf.write('\nfun.'+name+'_result(command,'+'\''+id+'\''+',input,output)')
                                newf.write('\nimg = cv2.imread(\''+output_list[0]+'\')')
                                newf.write('\nif(show_flag == 1 and img is not None):')
                                newf.write('\n\tcv2.imshow(\'photo\',img)')
                                newf.write('\n\tcv2.waitKey(500)\n')      
                            #os.system('prostak.exe -o '+name+' '+id+' '+input+' '+output)
                            print('prostak.exe -o '+name+' '+id+' '+input+' '+output)
                            #img = cv2.imread(output_list[0])          
                            # if(img is not None):
                            #     cv2.imshow('photo',img)
                            node.out_Node = {}
                            for (i,x) in enumerate(output_list):
                                node.out_Node.update({i+1:x})
                            node.Check_In = True
                            
                    else : 
                            print("Node" , num_node)
                            output = ','.join('path_data+\''+x+'\'' for x in output_list)
                            #os.system('prostak.exe -o '+name+' '+id+' '+output)
                            with open('final.py', 'a') as newf:
                                #newf.write('\nos.system(command+\' -o '+name+' '+id+' '+output+'\')')
                                newf.write('\noutput = ('+output+')')
                                newf.write('\nif type(output) != type(\'abc\'):')
                                newf.write('\n\toutput = \',\'.join(output)')
                                newf.write('\nfun.'+name+'_result(command,''\''+id+'\',output)')
                                newf.write('\nimg = cv2.imread(\''+output_list[0]+'\')')
                                newf.write('\nif(show_flag == 1 and img is not None):')
                                newf.write('\n\tcv2.imshow(\'photo\',img)')
                                newf.write('\ncv2.waitKey(500)\n')      
                            print('prostak.exe -o '+name+' '+id+' '+output)
                            # img = cv2.imread(output_list[0])          
                            # if(img is not None):
                            #     cv2.imshow('photo',img)
                            node.out_Node = {}
                            for (i,x) in enumerate(output_list):
                                node.out_Node.update({i+1:x})
                            node.Check_In = True
                

                 
                 


Process("cells.ap")
                    
            
                    
                

                    










