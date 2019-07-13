# Spider-使用说明

## 运行项目

在 spiderDangdang/spiderDangdang 文件夹下进入控制台，输入：
```
scrapy crawl bookScrapy -o 小说.csv -t csv
```
PS： “小说.csv” 是文件名，可自由更换


## 爬取到的图书结构说明
|  列名  |  含义 |
| ------------ | ------------ |
|  name |  图书名称 |
|  author | 作者  |
|  press | 出版社  |
|  pub_date | 出版日期  |
|  outline |  图书描述 |
|  now_price | 当前价格  |
|  pre_size | 原价  |
|  discount | 折扣  |
| img_url  | 书籍图片URL  |
|  link | 图书详情页URL  |
| size  |  图书大小 |
|  pager |  纸张 |
|  package |  包装 |
|  suit | 是否套装  |
| isbn  | ISBN码  |
| category  | 类别  |
| detail  | 图书详情  |
| catalogue  | 图书目录  |
| content  | 书籍内容试读  |
