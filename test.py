import requests

# import json


# url = "https://fanyi.baidu.com/basetrans"
# headers = {
#     "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1",
#     "Referer": "https://fanyi.baidu.com/?aldtype=16047",
#     "Cookie": "BAIDUID=B119776656517B374BC52FFFCABD12CB:FG=1;BIDUPSID=9F4397F7EE42057CFD3D5AB6E15ECCD2;"
# }
# datas = {
#     "query": "人生苦短，我用python",
#     "from": "zh",
#     "to": "en",
#     "sign": "289133.35420",
#     "token": "25af0fc3d37f67bb72c376f704f15292"}
# response = requests.post(url, data=datas, headers=headers)
#
# print(response)
# print(response.text)
str = """
"国家工商总局依法查处了一起奥运侵权案件：浙江一内裤生产厂家抢先注册两个商标：男式内裤叫“鸟巢”，女式内裤叫“水立方”，最令奥运组委会气恼的是其广告词是：“同一个地方，同一个梦想”！"
"从今天起，女人穿胸罩，穿短裤是违法的。因为戴胸罩犯包二奶罪；穿短裤犯包屁罪； 男人穿内裤那就更为严重，因为犯有窝藏枪支弹药罪！"
"我有一哥们得了癌症，弥留之际把我叫到跟前说：“我死后你千万别说我是得癌症死的，得说我是得爱滋病死的...”我奇怪：“为什么？爱滋病多难听啊！”哥们说：“只有这样说才没人敢打我老婆主意。”"
"告诫各位剩女，男生就像大学食堂里的菜，虽然不中意吃，……但是……但是…………去的晚了还是会没有的！！！"
"女生每个月都会来月经。又把来的那个称做&quot;好朋友&quot;，但知道为何要这样称呼呢？ 把好朋友这三字拆开不就很传神了吗? &quot;女子月月有&quot;！"
"<span style=\"color:rgb(51, 51, 51)\"><span style=\"font-family:&amp;quot\"><span style=\"font-size:15.5px\">老婆上街逛街，买了很多新衣服，到了晚上的时候老婆故意穿的刚买的新内衣跟老公说：老公，你看这款内衣是这个星期才出的新款呢。老公，看了一眼，说道：老婆，你被骗了，小黄上个月都穿着呐。</span></span></span>"
"<span style=\"color:rgb(51, 51, 51)\"><span style=\"font-family:&amp;quot\"><span style=\"font-size:15.5px\">男子去提亲，女方家长：请自我介绍。A说：我有一千万；B说：我有一栋豪宅，价值两千万；家长很满意。就问C，你家有什么？C答：我什么都没有，只有一个孩子，在你女儿肚子里。AB无语，走了。。在关键位置有人是多么的关键。。</span></span></span>"
"<span style=\"color: rgb(39, 39, 40); font-family: &#39;Microsoft YaHei&#39;, 宋体, HelveticaNeue-Light, &#39;Helvetica Neue Light&#39;, &#39;Helvetica Neue&#39;, Helvetica, Arial, sans-serif; font-size: 14px; line-height: 19.59375px;\">幼儿园开运动会。小班共有三个班，每个班出场时，要喊口号。小一班喊的口号是:小一，小一，勇争第一。小二:小二，小二，独一无二。等到小三班出场，喊出了令在场所有人都乐趴下的口号：小三，小三，爸爸喜欢！。。。园长太有才气。</span>"
"<span style=\"color: rgb(39, 39, 40); font-family: &#39;Microsoft YaHei&#39;, 宋体, HelveticaNeue-Light, &#39;Helvetica Neue Light&#39;, &#39;Helvetica Neue&#39;, Helvetica, Arial, sans-serif; font-size: 14px; line-height: 19.59375px;\"></span><span style=\"color: rgb(39, 39, 40); font-family: &#39;Microsoft YaHei&#39;, 宋体, HelveticaNeue-Light, &#39;Helvetica Neue Light&#39;, &#39;Helvetica Neue&#39;, Helvetica, Arial, sans-serif; font-size: 14px; line-height: 19.59375px;\">一群女人在一起聊各自的性福生活，单身女人说的口若悬河，兴趣盎然，旁边的已婚女人却性趣索然，于是羡慕至极的问单身女人“你们每天都过得这么快乐和性福吗”？“也不是，我们得趁你们没空的时候”……</span>"
"<span style=\"color: rgb(39, 39, 40); font-family: &#39;Microsoft YaHei&#39;, 宋体, HelveticaNeue-Light, &#39;Helvetica Neue Light&#39;, &#39;Helvetica Neue&#39;, Helvetica, Arial, sans-serif; font-size: 14px; line-height: 19.59375px;\"></span><span style=\"color: rgb(39, 39, 40); font-family: &#39;Microsoft YaHei&#39;, 宋体, HelveticaNeue-Light, &#39;Helvetica Neue Light&#39;, &#39;Helvetica Neue&#39;, Helvetica, Arial, sans-serif; font-size: 14px; line-height: 19.59375px;\">孩子：“妈妈什么叫度蜜月？”妈妈：“就是我和你爸爸结婚后一起去旅行，很好玩的。”孩子：“我去了么？”妈妈：“当然去了！”孩子：“我怎么不知道？”妈妈：“你还小嘛，当时是你爸爸带你去的，是我带你回来的。”</span>"
"<span style=\"color: rgb(39, 39, 40); font-family: &#39;Microsoft YaHei&#39;, 宋体, HelveticaNeue-Light, &#39;Helvetica Neue Light&#39;, &#39;Helvetica Neue&#39;, Helvetica, Arial, sans-serif; font-size: 14px; line-height: 19.59375px;\">一女研究生去交毕业论文，教授拿着论文，说：“你这篇论文啊，从上面往下看，首先是有两个很突出的特点；再接着看呢，就显得平淡；再往下看，就有些毛糙啦；看到最后，有一个明显的漏洞！”女生急了，忙问：“那怎么办呢？”教授：“插入我那一段就充实了。具体我们日后再说吧！</span><br/>"
"1，媳妇让戒烟，我在卫生间角落里藏了一盒，每次偷偷抽一根。那天又拿出来，发现里面有张她写的纸条：十三根！只好悻悻的放回去。过几天急中生智，抽到半根灭掉，再用牙签插在前面，放进烟盒弄平整，笨蛋果然没看出来。昨天老丈人来了，媳妇把那盒烟拿出来就去洗菜了，丈人拿出一根是个烟头插着牙签，又拿出几根还是这样，猛的扣上了盒子揣进了口袋。我觉得男人之间还真的需要默契。"
"<span style=\"color: rgb(39, 39, 40); font-family: &#39;Microsoft YaHei&#39;, 宋体, HelveticaNeue-Light, &#39;Helvetica Neue Light&#39;, &#39;Helvetica Neue&#39;, Helvetica, Arial, sans-serif; font-size: 14px; line-height: 19.59375px;\">以前放高利贷的现在都叫做金融的了，倒弄二手房的现叫做房地产的了，天桥算命的现都叫心理医生了，漫天扯淡的现在都叫专家了，以前的妓女现在都叫艺人了，媒婆老鸨现在都叫经纪人了，搞破鞋的现都叫蓝颜红颜知己了，夜里和爹干的白天都喊干爹了。。。</span>"
"<span style=\"color: rgb(39, 39, 40); font-family: &#39;Microsoft YaHei&#39;, 宋体, HelveticaNeue-Light, &#39;Helvetica Neue Light&#39;, &#39;Helvetica Neue&#39;, Helvetica, Arial, sans-serif; font-size: 14px; line-height: 19.59375px;\">甲：“老弟，你为什么下班后不马上回家，在这儿打转转？”</span><br style=\"color: rgb(39, 39, 40); font-family: &#39;Microsoft YaHei&#39;, 宋体, HelveticaNeue-Light, &#39;Helvetica Neue Light&#39;, &#39;Helvetica Neue&#39;, Helvetica, Arial, sans-serif; font-size: 14px; line-height: 19.59375px;\"/><span style=\"color: rgb(39, 39, 40); font-family: &#39;Microsoft YaHei&#39;, 宋体, HelveticaNeue-Light, &#39;Helvetica Neue Light&#39;, &#39;Helvetica Neue&#39;, Helvetica, Arial, sans-serif; font-size: 14px; line-height: 19.59375px;\">乙：“老兄有所不知，我和爱人约定下班后谁先到家谁做饭。”</span><br style=\"color: rgb(39, 39, 40); font-family: &#39;Microsoft YaHei&#39;, 宋体, HelveticaNeue-Light, &#39;Helvetica Neue Light&#39;, &#39;Helvetica Neue&#39;, Helvetica, Arial, sans-serif; font-size: 14px; line-height: 19.59375px;\"/><span style=\"color: rgb(39, 39, 40); font-family: &#39;Microsoft YaHei&#39;, 宋体, HelveticaNeue-Light, &#39;Helvetica Neue Light&#39;, &#39;Helvetica Neue&#39;, Helvetica, Arial, sans-serif; font-size: 14px; line-height: 19.59375px;\">甲：“噢！那你别往前走了——我看见你爱人正在那儿打转转呢！”</span>"
"<span style=\"color: rgb(39, 39, 40); font-family: &#39;Microsoft YaHei&#39;, 宋体, HelveticaNeue-Light, &#39;Helvetica Neue Light&#39;, &#39;Helvetica Neue&#39;, Helvetica, Arial, sans-serif; font-size: 14px; line-height: 19.59375px;\">上联：一天晚上两个甲方三更半夜四处催图只好周五加班到周六早上七点画好八点传完九点上床睡觉十分痛苦。</span><br style=\"color: rgb(39, 39, 40); font-family: &#39;Microsoft YaHei&#39;, 宋体, HelveticaNeue-Light, &#39;Helvetica Neue Light&#39;, &#39;Helvetica Neue&#39;, Helvetica, Arial, sans-serif; font-size: 14px; line-height: 19.59375px;\"/><span style=\"color: rgb(39, 39, 40); font-family: &#39;Microsoft YaHei&#39;, 宋体, HelveticaNeue-Light, &#39;Helvetica Neue Light&#39;, &#39;Helvetica Neue&#39;, Helvetica, Arial, sans-serif; font-size: 14px; line-height: 19.59375px;\">下联：十点才过九分甲方八个短信七个电话居然要六处调整加五张图纸四小时交三个文本两天周末只睡一个小时。</span><br style=\"color: rgb(39, 39, 40); font-family: &#39;Microsoft YaHei&#39;, 宋体, HelveticaNeue-Light, &#39;Helvetica Neue Light&#39;, &#39;Helvetica Neue&#39;, Helvetica, Arial, sans-serif; font-size: 14px; line-height: 19.59375px;\"/><span style=\"color: rgb(39, 39, 40); font-family: &#39;Microsoft YaHei&#39;, 宋体, HelveticaNeue-Light, &#39;Helvetica Neue Light&#39;, &#39;Helvetica Neue&#39;, Helvetica, Arial, sans-serif; font-size: 14px; line-height: 19.59375px;\">横批：用原来的。</span>"
"某男准备出家。方丈提出条件： 全裸JJ上挂铃铛，见美女而铃不响则成功。他照办。方丈请出美女，铃铛大响。男怒：不信寺里的和尚铃铛都不响。 方丈遂请出全 寺的和尚均挂铃铛。 美女再出，果然只有此男的铃铛大响。 此男羞愧，铃铛落地，弯腰去捡，后面铃声响成一片。。。"
"<span style=\"color: rgb(39, 39, 40); font-family: &#39;Microsoft YaHei&#39;, 宋体, HelveticaNeue-Light, &#39;Helvetica Neue Light&#39;, &#39;Helvetica Neue&#39;, Helvetica, Arial, sans-serif; font-size: 14px; line-height: 19.59375px;\">甲乙二人开车在路上相互蹭了一下，两人下车查看，问题不大。甲拍拍乙的肩膀：“大哥，缘分呐！来，我这有瓶茅台，整一口。”乙也很豪爽，接过来喝了一口，又递回去：“兄弟，你也来一口！”甲：“别，等警察来了再说。” 乙：“……”</span>"
"<span style=\"color: rgb(39, 39, 40); font-family: &#39;Microsoft YaHei&#39;, 宋体, HelveticaNeue-Light, &#39;Helvetica Neue Light&#39;, &#39;Helvetica Neue&#39;, Helvetica, Arial, sans-serif; font-size: 14px; line-height: 19.59375px;\">起床的真相：四点起的是送奶工，五点起的是菜场工，六点起的是小孩子和爸妈，七点起的是教授，八点起的是公务员，九点起的是小秘，十点起的是厨子，十一点起的是作家，十二点起的是主持人，十三点起的是二奶，十四点起的是小姐，十五点起的是病人，<span style=\"color: rgb(39, 39, 40); font-family: &#39;Microsoft YaHei&#39;, 宋体, HelveticaNeue-Light, &#39;Helvetica Neue Light&#39;, &#39;Helvetica Neue&#39;, Helvetica, Arial, sans-serif; font-size: 14px; line-height: 19.59375px;\">十<span style=\"color: rgb(39, 39, 40); font-family: &#39;Microsoft YaHei&#39;, 宋体, HelveticaNeue-Light, &#39;Helvetica Neue Light&#39;, &#39;Helvetica Neue&#39;, Helvetica, Arial, sans-serif; font-size: 14px; line-height: 19.59375px;\">六</span>点</span>以后还没起的请打120</span>"
"<span style=\"color: rgb(39, 39, 40); font-family: &#39;Microsoft YaHei&#39;, 宋体, HelveticaNeue-Light, &#39;Helvetica Neue Light&#39;, &#39;Helvetica Neue&#39;, Helvetica, Arial, sans-serif; font-size: 14px; line-height: 19.59375px;\">刚坐稳，一个姑娘双颊泛红地走到我面前，有些羞射地说：大哥，你好，我32D。我看了她一眼说：你32F也不好使呀，我有媳妇儿了。姑娘笑着说：呵呵呵，有媳妇就牛逼了？就能乱坐座位了？你特么给我起开！</span>"
"<span style=\"color: rgb(39, 39, 40); font-family: &#39;Microsoft YaHei&#39;, 宋体, HelveticaNeue-Light, &#39;Helvetica Neue Light&#39;, &#39;Helvetica Neue&#39;, Helvetica, Arial, sans-serif; font-size: 14px; line-height: 19.59375px;\">一个报童在大街上高声叫卖骇人听闻的诈骗案，受害者多达82人！” 某行人连忙上前买一份。可是，他把整个报纸翻个遍，也不见那个诈骗案，正在迷惑不解时，只听见报童又吆喝起来： “骇人听闻的诈骗案，上当者已达83人！”</span><br/>"
"<span style=\"color: rgb(39, 39, 40); font-family: &#39;Microsoft YaHei&#39;, 宋体, HelveticaNeue-Light, &#39;Helvetica Neue Light&#39;, &#39;Helvetica Neue&#39;, Helvetica, Arial, sans-serif; font-size: 14px; line-height: 19.59375px;\">男朋友问我：你喜欢哪个包？</span><br style=\"color: rgb(39, 39, 40); font-family: &#39;Microsoft YaHei&#39;, 宋体, HelveticaNeue-Light, &#39;Helvetica Neue Light&#39;, &#39;Helvetica Neue&#39;, Helvetica, Arial, sans-serif; font-size: 14px; line-height: 19.59375px;\"/><span style=\"color: rgb(39, 39, 40); font-family: &#39;Microsoft YaHei&#39;, 宋体, HelveticaNeue-Light, &#39;Helvetica Neue Light&#39;, &#39;Helvetica Neue&#39;, Helvetica, Arial, sans-serif; font-size: 14px; line-height: 19.59375px;\">我看了看：红色的那个吧。</span><br style=\"color: rgb(39, 39, 40); font-family: &#39;Microsoft YaHei&#39;, 宋体, HelveticaNeue-Light, &#39;Helvetica Neue Light&#39;, &#39;Helvetica Neue&#39;, Helvetica, Arial, sans-serif; font-size: 14px; line-height: 19.59375px;\"/><span style=\"color: rgb(39, 39, 40); font-family: &#39;Microsoft YaHei&#39;, 宋体, HelveticaNeue-Light, &#39;Helvetica Neue Light&#39;, &#39;Helvetica Neue&#39;, Helvetica, Arial, sans-serif; font-size: 14px; line-height: 19.59375px;\">男朋友笑了笑：傻瓜，那个不是名牌。别怕，挑你喜欢的就好。多贵都没关系。</span><br style=\"color: rgb(39, 39, 40); font-family: &#39;Microsoft YaHei&#39;, 宋体, HelveticaNeue-Light, &#39;Helvetica Neue Light&#39;, &#39;Helvetica Neue&#39;, Helvetica, Arial, sans-serif; font-size: 14px; line-height: 19.59375px;\"/><span style=\"color: rgb(39, 39, 40); font-family: &#39;Microsoft YaHei&#39;, 宋体, HelveticaNeue-Light, &#39;Helvetica Neue Light&#39;, &#39;Helvetica Neue&#39;, Helvetica, Arial, sans-serif; font-size: 14px; line-height: 19.59375px;\">我心中一暖，指了指路过的女人背着的LV：就她吧。</span><br style=\"color: rgb(39, 39, 40); font-family: &#39;Microsoft YaHei&#39;, 宋体, HelveticaNeue-Light, &#39;Helvetica Neue Light&#39;, &#39;Helvetica Neue&#39;, Helvetica, Arial, sans-serif; font-size: 14px; line-height: 19.59375px;\"/><span style=\"color: rgb(39, 39, 40); font-family: &#39;Microsoft YaHei&#39;, 宋体, HelveticaNeue-Light, &#39;Helvetica Neue Light&#39;, &#39;Helvetica Neue&#39;, Helvetica, Arial, sans-serif; font-size: 14px; line-height: 19.59375px;\">男朋友给我了一个吻，然后发动摩托，向那个女人冲了过去！</span>"
"<span style=\"color: rgb(39, 39, 40); font-family: &#39;Microsoft YaHei&#39;, 宋体, HelveticaNeue-Light, &#39;Helvetica Neue Light&#39;, &#39;Helvetica Neue&#39;, Helvetica, Arial, sans-serif; font-size: 14px; line-height: 19.59375px;\">爸爸检查儿子作业，其中有一题是用“肯定”造句。儿子造的是：爸爸悲伤地回家，肯定输钱了。爸爸看了很不高兴让儿子重新造句。儿子答应了很快又造了一句：妈妈冲着爸爸吼，爸爸肯定又输钱了。爸爸让儿子再造，别再写自己输钱了。儿子想了很久，最后写道：爸爸不让我写输钱，肯定怕妈妈知道他又输钱了。</span>"
"<span style=\"color: rgb(39, 39, 40); font-family: &#39;Microsoft YaHei&#39;, 宋体, HelveticaNeue-Light, &#39;Helvetica Neue Light&#39;, &#39;Helvetica Neue&#39;, Helvetica, Arial, sans-serif; font-size: 14px; line-height: 19.59375px;\">这几天回老家了。昨天下午小叔带着家里的狗去河里洗澡，小叔正在洗澡，狗就用嘴叼着他的衣服就跑回家了。奶奶以为小叔出事了，赶忙叫人去找小叔，到了就看到小叔光着屁股在河边骂街：大白天偷了我的狗还偷我衣服！</span>"
"<span style=\"color: rgb(39, 39, 40); font-family: &#39;Microsoft YaHei&#39;, 宋体, HelveticaNeue-Light, &#39;Helvetica Neue Light&#39;, &#39;Helvetica Neue&#39;, Helvetica, Arial, sans-serif; font-size: 14px; line-height: 19.59375px;\">和好朋友吵架，他突然说了一句：“祝你一辈子找不到女朋友。断手断脚看黄片。”我：“啥意思，你是骂我呢吗？” “这是诅咒！” 后来我想了想：“草了，真TM恶毒啊”</span>"
"<span style=\"color: rgb(39, 39, 40); font-family: &#39;Microsoft YaHei&#39;, 宋体, HelveticaNeue-Light, &#39;Helvetica Neue Light&#39;, &#39;Helvetica Neue&#39;, Helvetica, Arial, sans-serif; font-size: 14px; line-height: 19.59375px;\">夜，一女生赶上了末班公交车，车上只有两三乘客。女生无意间一抬头，看见车里的电子显示屏上滚动着“没有终点站”几个大字。女生一个激灵，联想到了各种鬼故事，她紧紧盯着那个显示屏，吓得冷汗都出来了…几分钟后，显示屏又滚到女生刚才看到的地方，她终于看全了：为您服务，满意没有终点站。</span>"
"美女和电冰箱有什么不同？<br/><br/>内涵人士秒懂的"
"""
