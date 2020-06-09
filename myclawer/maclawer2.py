from bs4 import  BeautifulSoup
import  requests
import csv






# data={
# "CurrentAggs": "College",
# "Honorary_Index":1,
# "Position_Index": 1,
# "College_Index": 1,
# "Company_Index": 1,
# "Subject_Index": 1,
# "Department_Index": 1,
# "PageName": "Scholar",
# "IncludeFieldList": "Position",
# "KeywordList[0][FieldName]": "FirstLetter",
# "KeywordList[0][Aggs]": "Condition",
# "KeywordList[0][FieldValue][]": "N",
# "KeywordList[0][FieldValueName][]": "首字母",
# "CurrentScholarOrder": "AchivementCount",
# "pageSizeSelect": 15,
# "isResult" : "true",
# "PageIndex": 3,
# "PageSize": 15,
# "FirstLetter":" N"
# }
data={


"Honorary_Index": 1,
"Position_Index": 1,
"College_Index": 1,
"Company_Index": 1,
"Subject_Index": 1,
"Department_Index": 1,
"PageName": "Scholar",
"IncludeFieldList": "Position",
"isResult": "true"
}


# CurrentAggs: College
# Honorary_Index: 1
# Position_Index: 1
# College_Index: 1
# Company_Index: 1
# Subject_Index: 1
# Department_Index: 1
# PageName: Scholar
# IncludeFieldList: Position
# (empty)
# keyword:
# CurrentScholarOrder: AchivementCount
# pageSizeSelect: 15
# isResult: true
# PageIndex: 2
# PageSize: 15
# FirstLetter:







for a in range(1,324):
  print("第%d页" % a)
  data["PageIndex"]=a
  response = requests.post("http://dlutir.dlut.edu.cn/Scholar/ResultListPage",data)

  bs = BeautifulSoup(response.text,"lxml")
  scholoar={}
  for b in bs.find_all("div",class_="scholoar_text leftfloat") :
      href=str( b.find("a").get("href"))
      partment=href.split("/")
      id = partment[-1]
      text=list(b.stripped_strings)
      scholoar["scholoar_name"]=text[0]
      scholoar["scholoar_department"]=text[1]
      scholoar["scholoar_id"]=id
      out = open('scholoar_csv.csv', 'a',encoding="utf-8",newline='')
      list1 = [scholoar["scholoar_name"], scholoar["scholoar_department"], scholoar["scholoar_id"]]
      csv_write = csv.writer(out, dialect='excel')
      csv_write.writerow(list1)
      print(scholoar)