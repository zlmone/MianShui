# -*- coding: utf-8 -*-

import pymysql
from pymysql import cursors
import json
import base64
import datetime
import hashlib

my_any = """{'sections': [{'content': '<p><strong>三亚：</strong>至少提前<strong>24</strong>小时下单<br/></p><p><strong>海口、博鳌：</strong>至少提前<strong>40</strong>小时下单</p><p>温馨提示：最早可于离岛前<strong>20</strong>天购买。</p><p>特别注意：已暂停秀英港离岛提货方式，可选择从新海港离岛。</p>',
                                    'id': 10007,
                                    'name': 'Q：购买时间有什么要求吗？',
                                    'shortName': None},
                                   {'content': '<p>年满16周岁，乘飞机、火车或轮船，并持有效身份证件（国内旅客持居民身份证），离开海南本岛但不离境的国内旅客。</p>',
                                    'id': 1035,
                                    'name': 'Q：在官网购买免税品需要满足什么条件？',
                                    'shortName': None},
                                   {'content': '<p><span '
                                               'style=";font-family:宋体;color:black">在菜单栏“我的中免”中，点击“会员中心”根据提示注册。</span></p><p><br/></p>',
                                    'id': 10027,
                                    'name': 'Q：如何注册成为中免会员？',
                                    'shortName': None},
                                   {'content': '<p><span '
                                               'style=";font-family:宋体;color:black">官网购买后，中免会员可享有积分，在提货后24小时赠送。积分会发送于已交易的商城账号中（注册账号），但是官方商城购买产生的积分须在下次离岛消费时使用。</span></p><p><span '
                                               'style=";font-family:宋体;color:red">注明：已注册成为中免会员的顾客，需绑定会员卡后才可以享有积分。请在菜单栏“我的中免”中，点击“会员中心”进行绑定会员卡。</span></p><p><br/></p>',
                                    'id': 10029,
                                    'name': 'Q：官网购买，如何积分？',
                                    'shortName': None},
                                   {'content': '<p '
                                               'style="text-align:left"><span '
                                               'style=";font-family:宋体;color:black">中免会员积分可抵现金消费，一积分相当于一元人民币可在中免旗下免税店（参见适用门店）购买免税商品，积分每满十个以上可使用，限本人持卡享用。</span></p><p><span '
                                               'style=";font-family:宋体;color:black">更多会员积分权益，请在“会员中心”点击“查看会员手册”了解。</span></p><p><br/></p>',
                                    'id': 10031,
                                    'name': 'Q：中免会员有哪些权益？',
                                    'shortName': None},
                                   {'content': '<p><span '
                                               'style=";font-family:宋体;color:black">若在线下实体店使用积分消费时，已积分的商城账号（手机号）须与已绑定身份证的手机号一致，方可消费使用。</span></p><p><br/></p>',
                                    'id': 10033,
                                    'name': 'Q：线下实体店购买可使用官方商场的积分吗？',
                                    'shortName': None},
                                   {'content': '<p><span style="font-family: '
                                               '微软雅黑, " microsoft="" '
                                               'font-size:="">不可以，根据离岛免税政策规定，必须持有正确的离岛航班信息、火车票或轮渡船票信息才能购买。</span></p>',
                                    'id': 1036,
                                    'name': 'Q：还没有订机票、火车票或轮渡船票，可以购买吗？',
                                    'shortName': None},
                                   {'content': '<p><span style="font-family: '
                                               '微软雅黑, " microsoft="" '
                                               'font-size:="">若需变更或改签行程，请查看菜单栏“我的中免”中的“航班/火车票信息变更”。</span></p>',
                                    'id': 1022,
                                    'name': 'Q：飞机航班、火车车次或轮渡班次变更或改签，怎么办？',
                                    'shortName': None},
                                   {'content': '1、<strong>市场价、划线价</strong>：商品展示的划线价或市场价可能是品牌官网价、品牌专柜价、有税零售价；由于地区、时间的差异性和市场行情波动，品牌官网价、品牌专柜价、商品吊牌价等可能会与您购物时展示的不一致，该价格仅供您参考。<p>2、<strong>促销价</strong>：如无特殊说明，促销价是在免税价基础上给予的优惠价格。如有疑问，您可以在购买前与客服联系。<br/></p><p>3、<strong>价格异常</strong>：因可能存在系统缓存、页面更新延迟等不确定性情况，导致价格显示异常，商品具体售价请以订单结算页价格为准。如您发现异常情况出现，请立即联系我们修正，以便您能顺利购物。<br/></p>',
                                    'id': 10003,
                                    'name': 'Q：市场价、划线价、促销价指的是什么？',
                                    'shortName': None},
                                   {'content': '<p>每人每次购买免税品，化妆品30件，手机限购4件，酒类限购1500ML，其他品类不限件数。超出免税限额、限量的部分，照章征收进境物品进口税。\xa0'
                                               '</p>',
                                    'id': 1037,
                                    'name': 'Q：限购数量是怎么回事？',
                                    'shortName': None},
                                   {'content': '<p>（1）购物次数：离岛旅客不限购物次数</p><p>（2） '
                                               '免税限购额度：每个公历年内，免税额度为：单价人民币100000元以下商品，每年累计购物金额不超过人民币100000元（含100000元）。此外，单价人民币100000元以上商品征税后不限件数。</p><p><br/></p>',
                                    'id': 1057,
                                    'name': 'Q：购物次数、限购额度是怎么回事？',
                                    'shortName': None},
                                   {'content': '<p><span style="font-family: '
                                               '微软雅黑, " microsoft="" '
                                               'font-size:="">离岛一次，计一次购买次数，只要在离岛免税店购物，就会消耗本次购买机会的免税额度。飞机、火车和轮渡离岛限购额度与限购数量同享，购买免税品的限制以身份证计算，三种方式离岛均会消耗免税额度。</span></p>',
                                    'id': 1059,
                                    'name': 'Q：不同免税店购买，免税额度是分别计算的吗？',
                                    'shortName': None},
                                   {'content': '<p><strong>1. '
                                               '乘坐飞机离岛</strong>：在离岛机场隔离区cdf提货点取货，可直接带上飞机。<br/>（三亚凤凰机场在国内出发厅215号登机口对面；海口美兰机场在国内出发厅15号登机口旁；琼海博鳌机场在国内出发厅2楼1号登机口旁。）</p><p><strong>2. '
                                               '乘坐火车离岛</strong>：<br/>从三亚、东方火车站出发：火车到达海口火车站后，在站台处三亚国际免税城提货点提货；<br/>从海口火车站出发：在海口火车站站内三亚国际免税城提货点提货。<br/><strong '
                                               'style="white-space: '
                                               'normal;">3. 轮渡离岛</strong>：<br '
                                               'style="white-space: '
                                               'normal;"/>从新海港出发：<br/>散客提货进入安检后右转5米免税店散客提货点处；<br/>自驾提货通过车辆检票口后行至小车安检站右转50米免税店自驾提货点处。</p><p>从秀英港出发：<br/>散客提货安检后左转免税店散客提货点处；<br/>自驾提货经3号门进入码头①可向左行驶至7--8号码头免税店提货点自驾窗口提货；②或经过5号门和8号门前往11号码头免税店自驾提货处。<br/>特别注意：已暂停秀英港离岛提货方式，可选择从新海港离岛。</p>',
                                    'id': 1063,
                                    'name': 'Q：官网购买后，怎么提货呢？',
                                    'shortName': None},
                                   {'content': '<p>下单支付后，若订单成功您会收到由三亚国际免税城发出的下单成功的信息；若订单失败，系统也会短信提示您，为避免影响您的购物，请您及时关注我们的短信提醒，如有问题，可致电客服电话：400-699-6956，我们会竭诚为您服务。</p>',
                                    'id': 10005,
                                    'name': 'Q：下单成功后会收到短信通知吗？',
                                    'shortName': None},
                                   {'content': '<p><span style="font-family: '
                                               '微软雅黑, " microsoft="" '
                                               'font-size:="">提货时出示提货人身份证、登机牌、火车票或轮渡船票。</span></p>',
                                    'id': 1065,
                                    'name': 'Q：提货时需要出示哪些凭证？',
                                    'shortName': None},
                                   {'content': '建议您在登机、火车或轮渡出发时间前60分钟，到达提货处提取商品，避免因高峰期排队等候而延误您的行程。',
                                    'id': 1067,
                                    'name': 'Q：提货时间需要注意哪些？',
                                    'shortName': None},
                                   {'content': '购买免税商品，您在办理提货后，关注“cdf离岛免税一三亚国际免税城”官方微信公众号，进入菜单“我的服务--电子发票”自助开具电子发票。',
                                    'id': 1061,
                                    'name': 'Q：如何开具发票？',
                                    'shortName': None}],
                      'title': '常见问题'}"""

# mylist=['a', 'b', 'c', 'd', 'e']
# connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456',
#                              db='spider_cdf', cursorclass = pymysql.cursors.DictCursor)
# stringlistvalue=json.dumps(mylist)
# encodedlistvalue=base64.b64encode(stringlistvalue)
# sql_article1 = json.dumps(encodedlistvalue)
# sql_json = """INSERT INTO t1 VALUES(sql_article1);"""
#
#
#
# try:
#     # 通过cursor创建游标
#     cursor = connection.cursor()
#     cursor.execute(sql_json)
#     connection.commit()
# except BaseException as e:
#     print(e)



import pymysql
import json
import base64
mylist=['a','b','v','wgyll55']
# dbhost="127.0.0.1"
# dbuser="root"
# dbpwd="123456"
# dbdatabase="spider_cdf"
# serialize list into a string, and then encode in SQL-safe base64 format



db = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456',
                             db='spider_cdf', cursorclass = pymysql.cursors.DictCursor)


# 可用的将世间任何东西存入mysql的写法 ，todo: 取出解析有问题。
myany_json=json.dumps(my_any, ensure_ascii=False)

# string_byte = myany_json.encode('utf-8')
# encoded_str_byte=base64.b64encode(string_byte)
# # db = pymysql.connect(dbhost,dbuser,dbpwd,dbdatabase )
#
store_sql = f"INSERT INTO `t1`(mytext) VALUES (\'\'\'{myany_json}\'\'\')"
print(store_sql)

# select_sql = "select * from myany where id=4"



# import time
# t0 = time.time()
# time.sleep(1)
# name = 'processing'
#
# # 以 f开头表示在字符串内支持大括号内的python 表达式
# print(f'{name} done in {time.time() - t0:.2f} s')



try:
   # Execute the SQL command
   cursor = db.cursor()
   cursor.execute(store_sql)

   #查询写法
   # articles = cursor.fetchall()

   # print(articles)
   #
   # print(articles[0]["text"])
   # befor_json = base64.b64decode(articles[0]["text"]).decode()
   #
   # print("1111",json.loads(befor_json))

   # Commit your changes in the database
   db.commit()
except BaseException as e:
   # Rollback in case there is any error
   db.rollback()
   print(e)


finally:
	# disconnect from server
	db.close()