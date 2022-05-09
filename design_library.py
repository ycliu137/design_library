### Licenser: Yuchen Liu
### Email: ycliu137@gmail.com
### Last Update Date: May 9, 2022

### 程序说明：

import pandas as pd


#读取.csv文件
codes1 = pd.read_csv('h3_design_addgene.csv',encoding='gbk',index_col=None,dtype={'code':str}) #index_col=0 不再添加index列

codes2 = pd.read_csv('gene_list.csv',encoding='gbk',index_col=None,dtype={'code':str}) #index_col=0 不再添加index列

codes3 = pd.merge(codes1,codes2,how='inner') #codes1在左,codes2在右,保留codes1排序方式

codes3 = pd.merge(codes3,codes2,how='outer')

print(codes3)


codes3.to_csv('design_result.csv',encoding='gbk') #保存文件

