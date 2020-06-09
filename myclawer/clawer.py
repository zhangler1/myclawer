import csv
import pandas as pd
import pickle
import  time
import json
import  re
import jsonlines

def scholoar_search(scholoar_id):
    import requests
    from bs4 import BeautifulSoup




    res_str="http://dlutir.dlut.edu.cn/Scholar/Detail/"+scholoar_id
    s = requests.Session()

    # 设置session对象的auth属性，用来作为请求的默认参数

    s.auth = ('user', 'pass')
    res = s.get(res_str)


    bs = BeautifulSoup(res.text,"lxml")




    total_information={}

    regex = re.compile(r"\w+[^:|：]") #去除尾部的字符串
    scholoar_name={}
    for b in  bs.find_all("p", class_="scholoar_name") :
     inforscholoar_name=list(b.stripped_strings)
     scholoar_name.update({inforscholoar_name[0]:inforscholoar_name[1]})



    scholoar_jsdd={}
    for a in bs.find_all("ul", class_="scholoar_jsdd"):

         for b in a.find_all("li"):
             infor_scholoar_jsdd = list(b.stripped_strings)
             for c in b.find_all("a"):
                 infor_scholoar_jsdd.insert(infor_scholoar_jsdd.index("个人主页：") + 1, c.get('href'))

             if len(infor_scholoar_jsdd) >= 2:
                 scholoar_jsdd.update({re.match(regex,infor_scholoar_jsdd[0]).group():infor_scholoar_jsdd[1:]})
             else:
                 scholoar_jsdd.update({re.match(regex,infor_scholoar_jsdd[0]).group():""})


    info_scholar={}
    for a in bs.find_all("div",class_="info_scholar") :
     inforinfo_scholar=list(a.stripped_strings)
     if len(inforinfo_scholar) >= 2:
         info_scholar.update({inforinfo_scholar[0]: inforinfo_scholar[1:]})
     else:
         info_scholar.update({inforinfo_scholar[0]: ""})








    help_tip={}
    for a in  bs.find_all("div", class_="help-tip") :

            infor_help_tip = list(a.stripped_strings)
            help_tip.update({infor_help_tip[0]: infor_help_tip[1:]})

    part_jj_right={}
    for b in bs.find_all("div", class_="part_jj_right leftfloat"):
        for a in b.find_all("li"):
          infor_part_jj_right = list(a.stripped_strings)
          part_jj_right.update({infor_part_jj_right[1]:infor_part_jj_right[0] })
    yjfx={}
    for b in bs.find_all("div", class_="yjfx"):
        infor_yjfx = list(b.stripped_strings)
        yjfx.update({re.match(regex,infor_yjfx[0]).group(): infor_yjfx[1:]})
        # print(infor_yjfx)


    data={

    "KeywordList[0][FieldName]": "OwnerCancel_UserId",
    "KeywordList[0][Aggs]": "Owner_UserId",
    "KeywordList[0][FieldValue][]": 4739,
    "KeywordList[0][FieldValueName][]": 4739,
    "KeywordList[0][IsShow][]": "false",
    "UserId": 4739,
    "Type_Index": 1,
    "SubjectId_Index": 1,
    "Index_Index": 1,
    "ImportantType_Index": 1,
    "ScientificSource_Index": 1,
    "JournalCondition_Index": 1,
    "Year_Index": 1,
    "KeywordCondition_Index": 1,
    "Language_Index": 1,
    "CurrentIndex": 1,
    "Id": 4739,
    # PageSize:
    "PageIndex": 1,
    "PageName": "scholarAchivement",
    "IncludeFieldList": "Type",

    "CurrentOrder": "PrintDate",
    "isResult": "false",
    }
    datas_paras = ['Type',
                   "SubjectId",
                   "Index",
                   "ImportantType",
                   "ScientificSource",
                   "JournalCondition",
                   "Year",
                   "KeywordCondition"
                   "ScholarContribue",
                   "Fulltext",
                   "Language"
                   ]

    data["KeywordList[0][FieldValue][]"]=scholoar_id
    data[ "KeywordList[0][FieldValueName][]"]=scholoar_id
    data[ "UserId"]=scholoar_id
    data[ "UserId"]=scholoar_id
    data[ "Id"] = scholoar_id

    headers ={
 "Accept": "*/*",
"Accept-Encoding": "gzip, deflate",
"Accept-Language": "zh-CN,zh;q=0.9",
"Connection": "keep-alive",
"Content-Length": "828",
"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
"Cookie": "ASP.NET_SessionId=lvwmk0dnsdxhlgqdtkde0foy",
"Host": "dlutir.dlut.edu.cn",
"Origin": "http://dlutir.dlut.edu.cn",
"Referer": "http://dlutir.dlut.edu.cn/Scholar/Detail",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
"X-Requested-With": "XMLHttpRequest"
}




    total_information.update({"学者信息":scholoar_name})
    total_information.update({"经历":scholoar_jsdd})
    total_information.update({"职称":help_tip})
    total_information.update({"概况":part_jj_right})
    total_information.update({"研究":yjfx})




    info_scholar={}
    for a in datas_paras :
     data["IncludeFieldList"]=a
     response = s.post("http://dlutir.dlut.edu.cn/SearchResult/FilterPage",data,headers=headers,)
     temp={}
     for b in BeautifulSoup(response.text,"lxml").find_all("dd")[0:-1]:
        info_bs=list(b.stripped_strings)
        temp.update({info_bs[0]: info_bs[1]})
     total_information.update({a: temp})

    return total_information




      # , newline = ''

input_file = open('scholoar_csv.csv', 'r',)
csv_read = csv.reader(input_file, dialect='excel')


# 输出文件
row=1
with open("break", "r") as fr:
      try:
            num=int((fr.read()))


            for line in csv_read:

                if row < num:
                    row = row + 1
                    continue

                else :

                    if num %100 ==0 :
                     time.sleep(10)




                    print("读取信息如下")  #
                    print(line) #打印文件每一行的信息
                    id=line[2]
                    infor_array=scholoar_search(id)

                    js = json.dumps({id: infor_array}, ensure_ascii=False, indent=4)  # 打印文件每一行的信息
                    with open(r"schooloar"+str(num),"w") as f:
                        f.write(js)



                    print("写入第  % d 个成功"%num)
                    num=num+1
                    break



      except :
          with open("break", "w") as fw:
           fw.write(str(num))











