bayes_model
===========

使用朴素贝叶斯分类器，对新闻数据进行分类

* test_model.py 模型测试程序
* bin/bayes_model.py 贝叶斯模型文件
* bin/data_process.py 数据预处理文件
* bin/gen_news_test_data.py 将数据随进分成训练数据和测试数据

* test_data/train_data.txt 训练数据
* check_data.txt 测试数据 
 
##分为三步骤
###1 数据的预处理
* 将所有新闻存储在一个文件中，每一行为一篇新闻，行末端为新闻的类型，并以\t进行分隔；
* 新闻数据以空格进行分隔；
* 过滤掉新闻数据中停用词，以及一些新闻中出现的符号；

###2 模型的训练
* createVocabList() 获取到训练数据的词袋
* 将新闻数据表示成词向量
* 根据朴素贝叶斯公式进行计算
* 本程序采用多项式进行计算
* 模型参数为 每个类别的词权重向量 和 类别在的先验概率。
  trianNB()  
  return p0Vect,p1Vect,p2Vect,pAuto,pBusiness,pSport
  
###3 模型的评估 
"Usage [%s] [train] [test] [model] [result]"
示例：./python ./test_data/train_data.txt ./check_data.txt model.txt result.txt 2>log

train_data.txt 训练数据
check_data.txt 测试数据
model.txt 模型得到参数存储文件
result.txt 评估结果文件

准确率在 96.2%

### 有待改进之处
* 将数据中的文字用数字进行替换

* 去掉统计文中的高频词汇

* 数据格式用二进制进行保存
* 没有设计成在线系统，通过获取到新的数据和已有的模型参数，得到新的模型参数

###参考
《Machine Learning in Action》