# CPWS_spider
裁判文书网爬虫（可用时间至2018.9）

# 注
1.于2018.9前破解裁判文书js算法，网站改版后解密文书id的js错误。
2.几个关键参数 vl5x，number，guid，其中v15x通过动态cookie提取(大约5分钟变动一次 需要单独启动线程进行cookie的维护)
3.找到几个关键参数生成的js 采用python库exejs运行 
4.最终docid为 js_fuck语言生成，需要node.js运行
3.具体的实现忘了，看源码。
