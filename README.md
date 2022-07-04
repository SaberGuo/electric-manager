# electricManager

#### 介绍
中国软件杯, 使用python3.8运行


#### 使用方法

1. 下载[git客户端](https://git-scm.com/downloads)
2. 打开cmd或者git bash, `git clone https://github.com/SaberGuo/electric-manager.git`
3. pip install -r requirements.txt
4. 任务1:python tools/statistic.py

#### 软件架构
软件架构说明
>doc:文档

>config:配置文件

>interface:交互界面

>release:生成应用

>tools:使用的相关辅助工具脚本
>>statistic.py:统计总体情况

>algorithms:使用的算法  
>>cluster.py:


#### 任务

1.  计算 平均缴费金额、平均缴费次数，并以 csv 格式输出结果保存
2.  对每个居民客户的用电缴费情况按照上述四种居民客户类型进行归类，结果保存
3.  依据时间序列，预测最有可能成为高价值客户的TOP5，结果保存
4.  根据电力客户数据编码，建立电力用户用电模型，对企业电力营销和调度进行决策支撑，需要模型参数优化与评估分析，保存模型为 “企业电力营销模型.mdl”
5.  根据不同的标准对用户进行集群划分，如某一用户的行为特征、用户基本属性、电器设备使用、用电曲线形态等，保存为“电力用户集群分析模型.mdl”

#### 非功能要求

1.  系统运行顺畅无卡顿，无严重BUG
2.  逻辑合理、交互友好
3.  场景复杂，算法精确，有创意均为加分项
4.  文档应详细阐述所使用的技术算法，以及实现思路
5.  作品中应输出运行结果的准确率并有效评估

#### 参与贡献

1.  gx xiaoguo@buaa.edu.cn
2.  
