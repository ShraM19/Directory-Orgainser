'''d={
    "fruit1":{
        "old":"",
        "new":""
    },
    "fruit2":{
        "old":"12",
        "new":"11"
    }
}
print ("Dictionary",d)

for element in d:
    print(element)
    print (d[element]["old"])'''
dict1={}
dir_list=['Book1.xlsx', 'Doc1.docx', 'Doc2.docx', 'Presentation1.pptx']
dict1["Book1.xlsx"]["old"]= "anc"
for i in dir_list:
    dict1[i]["old_src"]="abc"
print (dict1)


'''dict1={
    dir_list[i]:{
        "old_src":old_path,
        "new_src":one_path
        ,
    }
                    } '''