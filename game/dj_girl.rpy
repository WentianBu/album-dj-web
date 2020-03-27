# ###########################################################
#            Copyright (c) 2020 BigCherry Team
#                   All Rights Reserved 
#
#  filename: dj_girl.rpy
#  description: (story scripts) Dongji Girl Story
#  Story Author: Wentian Bu
#  Script Author: Wentian Bu
#  Version: 1.0
#  
# ###########################################################

default dj_girl_opinion = 0
default dj_gs01_ques1_flag = False


label dj_girl:

label .gs01room:
    scene bg gs01room
    with fade
    "闹了一晚上，你和连南回到房间。"
    me"？？？这咋是大床房？"
    lian"哈哈哈哈没想到吧"
    me"？你想干什么？"
    lian"让你近距离感受磨牙的乐音"
    "气氛诡异了起来，你迫切想更换话题。"
    me"对了，你明天给我们买的什么时候的船票来着？"
    lian"九点多的吧。你和小茶可以睡个好觉，好好在船上上等仓享受二人世界"
    me"......你有毒吧"
    lian"哈哈哈哈加油。你不洗我先去洗了。"
    menu:
        "这时你选择："
        "好，你先去洗吧，明天你还要早起":
            "话音未落连南已经脱掉了上衣，冲进卫生间，于是你坐在床边玩手机。"
            jump .gs04sos

        "不行，老子天下第一，我要先洗":
            "说着你马上脱掉了衣服，冲进卫生间。"
            lian"狗屎！"
            $ gs01room_ques1_flag = True
            jump .gs02shower

        "（娇羞地）安南哥哥，我想和你一起洗":
            lian"呕！没看出来啊你这么变态，快出去出去。"
            "说着他把你推出了房间，并反锁了门。"
            me"狗屎！你要多久"
            lian"快的很快的很，你先去找小茶玩。"
            "你只好坐在大厅的沙发上玩手机。"
            jump .gs04sos

label .gs02shower:
    scene bg gs02shower
    with fade
    "你走进卫生间。"
    "？这个水龙头为什么这么像麦克风？"
    "不如来高歌一首，表达对明天旅程的期待。"
    menu:
        "你准备唱什么浴室金曲捏？"
        "死了都要爱":
            me"“死了都要爱，不淋漓尽致不痛快。感情多深，只有这样。才足够表白……”"
            "浴室传来你撕心裂肺的歌声，响彻全楼。"
            bwt"狗屎，抢我金曲"
            
        "平凡之路":
            me"“我曾经跨过山和大海，也穿过人山人海，我曾经拥有着的一切，转眼都飘散如烟，我曾经失落失望失掉所有方向，直到看见平凡才是唯一的答案……”" 
            "浴室传来你惊天动地的歌声，响彻全楼。"
            conway"狗屎，抢我金曲"

        "告白气球":
            me"“你说 你有点难追，想让 我知难而退，礼物 不需挑最贵，只要 香榭的落叶，喔 营造浪漫 的约会，不害怕 搞砸一切，拥有你就拥有 全世界……”"
            "浴室传来你不可言传的歌声，响彻全楼。"
            lian"狗屎，抢我金曲"

    # 手机铃声音效
    "突然连南的手机铃声打断了你的歌声，你似乎听到了里面传来女生的尖叫和扔东西的声音……"
    lian"学妹们遇到了点问题，我先去看一下"
    menu:
        "这时你选择："
        "等等我，我马上擦干，我们一起去":
            "你们一起过去，原来是房间刚才出现了蜘蛛。"
            "你们找了半天也没有找到蜘蛛，只好无功而返。"
            "于是连南去洗澡了，你坐在床上玩手机。"
            jump .gs04sos

        "有点担心，赶紧拿出手机，给小茶发了个消息问问":
            "结果小茶一直没回复，你有一丝担心。但想着可能问题已经解决了，于是继续唱歌。"
            jump .gs03room

        "关我屁事，还是浴室唱歌比较重要":
            me"再来一首《成都》吧。"
            me"“和我在成都的街头走一走，污喔污喔，直到 所有的灯都熄灭了，也不停留……”"
            jump .gs03room

# FIXME: 这里与前面衔接似乎有点不流畅
label .gs03room:
    scene bg gs03room
    with fade
    "过了十分钟连南回来了，这时你已经洗完澡坐在床上。"
    me"她们怎么了？"
    lian"没啥，就是房间里有个大蜘蛛，我过去了找了半天，蜘蛛已经不见了，可能已经爬出去了。"
    "于是连南去洗漱了。"
    jump .gs04sos

label .gs04sos:
    scene bg gs03room
    with fade
    "正在玩手机，突然QQ上小茶突然来找你："
    tea"哥哥我好害怕，房间里刚才有个大蜘蛛在到处乱爬，我们不敢打。"
    menu:
        "你如何回复："
        "好，你别怕，我马上过来":
            $ dj_girl_opinion += 10
            jump .gs05spider

        "蜘蛛有啥害怕的，蜘蛛其实很怕人的……":
            me"中国的蜘蛛又不咬人，美洲才有那种有毒的咬人蜘蛛，这里又分北美洲和南美洲……"
            "你开始大谈世界蜘蛛的分类以及他们的特点，刷了五屏消息。"
            me"综上所述，你不用害怕它的，诶你怎么不回复我了？"
            $ dj_girl_opinion -= 40
            jump .gs06morning

        "连南太辣鸡了，还是得我亲自出场啊" if dj_gs01_ques1_flag:
            $ dunhuang_value += 20
            $ dj_girl_opinion += 10
            jump .gs05spider

label .gs05spider:
    scene bg room
    with fade
    "你来到她们房间。"
    me"诶你们怎么躲在卫生间啊？"
    tea"它一直乱爬...厕所有个门可能安全一点"
    me"我来找找它。"
    """
    你找了半天没找到蜘蛛，于是无奈之下跟她们聊了会儿天。

    你的眼神频频落在小茶身上，小茶也很是健谈，总是能把你的话题恰到好处地接下。

    小茶真是个温柔可爱的女孩子啊。和我太合适了。

    旁边的万千儿话却比较少，显得有些尴尬，
    
    感觉她们应该不太害怕了，我还是回去吧。
    """
    "小茶似乎看出来了你准备离开："
    tea"哥哥你在这陪着我们吧。"
    menu:
        "你该如何选择呢？"
        "“这...似乎不太好吧”":
            tea"有啥不好的，又不睡觉，我们聊聊天算了，反正也就几个小时。"
            "于是你留了下来，跟她们聊天，不知不觉万千儿已经睡着了，只剩你们两个再说话，时不时含情脉脉的看着对方……"
            "就这样聊着聊着你们不知道什么时候也睡着了，直到被闹铃闹醒发现万千已经走了，你和小茶竟然挤在一张床上。"
            "你犹豫了一会儿，还是叫醒了她。"
            $ dj_girl_opinion += 20
            jump .gs07sleep

        "“陪啥陪，蜘蛛早就不见了，你们要还是怕我也没啥办法，实在不行再躲到厕所里吧，我困了，晚安”":
            "你回到房间，在连南的磨牙声中入眠了。"
            $ dj_girl_opinion -= 20
            jump .gs06morning

        "“你不是喜欢荷兰弟嘛，你把这只小蜘蛛当他不就好咯”":
            """
            小茶喜欢的超级英雄只有蜘蛛侠，其实她是馋荷兰弟的身子。

            听到你这么说，她开始犯花痴了。

            你笑笑，有些许无语也有点难过，于是回到房间，在连南的磨牙声中入眠了。
            """
            jump .gs06morning

label .gs06morning:
    scene

    show text "2018年10月3日" at truecenter
    with dissolve
    pause 1

    scene bg gs06room
    with fade
    "你被几遍闹钟叫醒，发现九点了，于是你给小茶打了电话。"
    "小茶的声音听起来有些疲倦，你不禁有些心疼。"
    tea"你过来我房间吧"
    menu:
        "你怎么回复："
        "好的，我过来了":
            $ dj_girl_opinion += 10
            
        "你怎么磨磨唧唧的，十点半都要开船了你想误船？搞快点我在楼下等你":
            $ dj_girl_opinion -= 20
            "过了好一会儿，小茶才收拾好，带着行李下楼，你们走到大街上准备前往码头。"
            "然而你们在公交站等了好一会儿，一辆车都没有来，离开船的时间却越来越近……"
            jump .gs10taxi

    "你来到了楼上，小茶为你开了门。你看到她面色不太好，黑眼圈很重。"
    me"昨天晚上没休息好吗？"
    tea"呜呜呜，别提了。昨天晚上你走以后，我们还是害怕大蜘蛛又从哪里爬出来，怕睡着了爬到床上，于是我和万千儿在卫生间洗漱台上坐了一夜……然后也几乎没睡着。"
    me"是我不好，早知道我在这里陪你们的。"
    jump .gs07sleep

label .gs07sleep:
    scene bg gs07room
    with fade
    tea"哥哥，我好累。我想躺一会儿。"
    menu:
        "现在九点十分，你们的船票是十点半，坐车去码头路上可能会堵车，需要大半个小时。你怎么回复？"
        "那你休息一会儿吧，我二十分钟后叫你，应该不会误船的。":
            jump .gs08bed

        "你怎么回事，屁事比诺诺还多？":
            me"没睡好去船上睡，现在睡觉误船了怎么办？出来旅游有几个睡得好的？？这点困难都克服不了？？？"
            $ dj_girl_opinion -= 30
            tea"对不起，哥哥，我马上就收拾好……"
            "十分钟后，你们离开了民宿，准备前往码头。"
            "在公交车站等了好一会儿，一辆车都没有，离开船的时间却越来越近……"
            jump .gs10taxi

        "去tmd船票，我妹妹最重要，你尽管睡，大不了不去了！":
            "于是小茶安心地睡下了。"
            "等小茶醒来已经是下午了，你们索性不再上岛，在舟山找了个海边的酒店住下。"
            jump .gs13chat

label .gs08bed:
    scene bg gs08bed
    with fade
    "小茶重新到了床上，你坐在床边。"
    tea"哥哥，其实……要不是因为你，我是不会来东极岛的。我想找个安静的地方散散心。"
    me"是...我知道的"
    tea"我和学长们都不熟悉，感觉在一起玩得好尴尬。"
    me"……其实学长们人都挺nice的，大家玩熟悉了就好了。"
    tea"我现在没有旅游的心情。我满脑子都还是他……你知道的，我那么喜欢他，我们说好了在一起的，他为什么突然就对我冷淡了呢……"
    me"都出来散心了，我们就别提他了好吗？我们聊点轻松的……"
    tea"我心里真的好累……我甚至都不想上岛了，也不想搞什么爱情保卫战。要是我们能一直这样，安安静静的聊聊天该多好……"
    me"没关系的，大不了我们晚上不跟他们一起玩嘛。我们去岛上找个安静的地方，聊聊天，看星星。"
    tea"嗯..."
    me"你不用害怕啦，我会一直陪着你的。"
    tea"哥哥，你真好。"
    tea"你要是我的亲哥哥该有多好。"
    me"我会陪着你走出来的。他不喜欢你，还有哥哥在呢。"
    tea"哥哥……"
    tea"抱抱我好吗……"
    menu:
        "现在已经过九点半了，如果还不出发时间会很紧张，你该怎么办？"
        "哎呀九点半了我们该出发了，赶紧收拾一下准备走吧":
            $ dj_girl_opinion -= 20
            
        "稍微抱一下，然后催她出发。":
            pass

        "机不可失时不再来，船票什么的见鬼去吧":
            $ dj_girl_opinion += 20
            # scene bg gs09hug
            """
            你张开双手抱住了小茶，一阵一阵的发香扑面而来，抱女孩子原来是这样的一种感觉啊……

            你闭上了眼睛，什么也不再想，慢慢陶醉在这种感受中了。

            等到你们回过神来，走出门，已经快十点了。还有半个小时的时间……

            十点半的船，时间确实有点紧张。

            昨天你没有查具体的线路，刚才一查才发现，公交车路上就得一个多小时，根本不可能。
            """

    jump .gs10taxi
    

label .gs10taxi:
    scene bg gs10street
    with fade
    "看来要去码头只能坐出租车了。"
    "问题是，放眼一望，周围一辆车都没有。"
    "你有一些焦虑，如果不是小茶之前磨蹭，就算打不到出租也可以坐公交的……"
    tea"哥哥对不起，是我之前耽误了太多时间，害的我们现在要误船了"
    menu:
        "你准备怎么回应？"
        "傻瓜，别担心，如果误船了我们就不去了呗，在舟山找个沿海的落地房”":
            tea"那要多花好多钱啊"
            me"不就多花点钱吗？我包了，你开心更重要啊，千金难买爷高兴。"
            $ dj_girl_opinion += 30

        "你怎么回事，我之前都说了要抓紧时间":
            me"本来就住的远，你还这么磨蹭，你看现在可好，打不到出租，公交也来不及了。"
            tea"对不起哥哥，下次一定听你的..."
            me"船票钱都浪费了，狗屎他们那群人民宿钱肯定也不给我们退，早点听我的，怎么会发生这种事情......"
            $ dj_girl_opinion -= 30
            
        "嗯":
            $ dj_girl_opinion -= 10

    "你们漫无目的地往一个方向走，结果走到一个路口，发现一个出租车旁边有人正在嫌贵不坐了，于是你们赶紧上了车。"
    "运气很好，路上并没有堵车，你们还是按时赶到了码头上了船。"
    jump .gs11ship

label .gs11ship:
    scene bg ship
    with fade
    "上等舱的环境确实很不错，人不多，座位也还算宽敞，开船后还可以在甲板上享受海风、欣赏浪花。"
    "唯一美中不足的是没有信号，上不了网，但这也挺好，正好断绝了玩手机的机会，竟然有一种两个人与世隔绝、浪迹江湖的感觉。"
    tea"哥哥，你说，我们要是一直都在船上有多好啊"
    me"是啊，没有外界消息，自然也没有烦恼"
    tea"我真的很羡慕那些古代人，生活节奏慢，也没有那么多的焦虑和烦恼"
    me"你也不要太难过了，一切都有我在呢，你要是遇到什么问题或者麻烦我会一直帮你的。"
    tea"哥哥你真好。"
    tea"可是哥哥你不在我身边啊。我要是再有几个哥哥就好了，一个在北京，一个在南京，一个在襄阳，我到哪儿都不怕了。"
    menu:
        "你该如何回答呢？"
        "我不在你身边没关系的啊，如果你需要，我随时都可以来南京找你":
            $ dj_girl_opinion += 20
            
        "是啊，这样我也不会一直担忧你没有人照顾了":
            pass
            
        "你要那么多哥哥干啥，我一个就够了":
            $ dj_girl_opinion -= 10
            

    tea"其实我挺抗拒异地的，以为那样双方很难体会到对方的细微感受"
    me"但也不是一定的吧，你看小明和诺诺，不也那样过来了吗，现在也挺好。"
    me"异地不是问题，重要的是爱，没有爱了，就算每天都见面，也只会觉得对方很烦吧。"
    tea"嗯...哥哥你说的对。"
    """
    你和小茶分享了带的巧克力作为早餐，之后没休息好的小茶靠在你的肩膀上休息了一会儿。

    看着她熟睡的脸庞，你真的很想用这一生去呵护她，但她又是怎么想的呢？今天船上这些话，又意味着什么呢？

    你思索着这些问题，逐渐也睡着了。
    """
    scene bg restaurant
    with fade
    "经过两个多小时的航行，你们终于上了岛，也联系上了众人。他们在一家餐馆吃海鲜。"
    "等到你们过去，发现他们已经吃得差不多了，于是你们只好随便吃了几口，然后和众人合影返回民宿睡觉。"

    scene bg villa
    with fade
    "不知过了多久，众人纷纷醒了过来，已经是晚上了。"
    "大家都前往厨房做饭，但小茶说要洗澡，你决定留下来陪她。"
    jump dj_103.s28villa


label .gs12message:
    scene bg villaroom
    with fade
    "大家正在起劲地打着UNO，突然你的手机收到了一条消息。"
    tea"我们偷偷出去吧。"
    tea"我先出去，你过几分钟再出来，我在楼下门口等你。"
    "你抬起头，发现她眼睛亮亮的，偷偷给你使眼色。"
    menu:
        "你如何回复："
        "好":
            pass

        "干什么啊，UNO这么好玩，我不想去":
            jump .gs16love

    "小茶悄悄出去了。过了几分钟，你借口上洗手间也出来了。来到楼下，小茶正等着你。"
    tea"我们去看星星吧。"
    me"嗯，走吧。"

label .gs13chat:
    scene bg outside
    with fade
    """
    10月的海边已经进入了秋天，夜晚已经有点凉了。
    你们沿着狭窄的巷子走出了民宿区，来到一小片稍微开阔的地带。
    岛上的夜晚，天空格外清澈，繁星点点。你们找到一张长椅坐下来。
    """
    tea"哥哥，其实我是不想搞什么爱情保卫战才出来的。"
    tea"他们太闹腾了，我想散散心，清静清静。"
    me"没关系，我们这不就很清静嘛。"
    me"你今天上午说想要安安静静地聊会儿天的。"
    tea"嗯。"
    tea"哥哥……我心里还是很难过……"
    tea"六月份的时候我认识了小殷。当时我们忙着筹划招生、宣传、找场地，每天都有好多事情要做。渐渐地，在工作以外，我和他也时常聊天，以至于无话不谈。后来衔接班开课了，我和他每天都要坐班，就坐在教室后面聊一天。我们聊人生，聊理想，聊爱好，聊过去……他说，你的眼睛真好看，就像星星一样闪亮。在认识之前，我们都打算大学好好学习四年；认识之后，我们的计划里都有了对方的位置。我和他都互相表白了，我们约好，在大学里再正式在一起。我真的好喜欢好喜欢他……我们在一起的每一分每一秒都好甜好甜……"
    tea"可是我没想到，八月份开始军训以后，他突然对我冷淡了很多。那以前我给他发消息，他看到了都是秒回，那之后，我给他发消息，他总是过很长时间才回一两句，有时候甚至第二天才草草敷衍，而我却在屏幕另一端等得心力交瘁……最开始我以为我说错了话或者做错了事让他生气了，可是问他他却说我没错……他说，对不起，我们还是做回普通朋友吧。我当时快要崩溃了，我问他为什么，他说他也许没有他以为的那么喜欢我。于是，我们的恋爱还没有开始，就这么分手了……"
    tea"我不知道为什么……为什么别人就能拥有甜甜的恋爱，为什么他之前那么温暖现在却又那么冷漠，为什么要给我美好的幻梦然后再狠狠地打碎，为什么计划里已经有了彼此他却绝情地转身离开……我真的喜欢他啊……"

    "小茶的声音渐渐哽咽了，迎着星光，她脸颊上晶莹的泪水闪闪发亮。"
    menu:
        "你该怎么办？"
        "什么都不说，紧紧抱住她":
            jump .gs14winner

        "这种人就tm是渣男，你值得更好的，比如我，跟我在一起吧，我会永远对你好的":
            jump .gs15loser

        "我懂，这种感觉真的很难受，彼此喜欢却不能在一起。但你这样我真的好心疼，我们以后就把他当做一个故事，不要再因为他伤心了，好吗？":
            jump .gs16sucker

label .gs14winner:
    """
    呜呜呜，小茶开始呜咽了起来，泪水打湿了你的肩膀。

    岛上的夜晚分外安静，清冷的星光洒在大地上，被泪水湿润的衣服传来丝丝凉意。

    不知道过了多久，怀中的女孩渐渐停止了哭泣。
    """ 
    me"好了好了，我们不提他了好吗？你不是想看星星嘛。"
    tea"嗯……"
    # 这里可以插入星空的背景图，后面再换回来
    """
    你们抬起头，看着璀璨的星空。

    虽然已经是秋天，但是西南边天空上的“夏季大三角”仍然醒目。那是由牛郎星、织女星和天津四组成的一个三角形。

    传说中，每年的七夕，牛郎和织女这一对分隔两地的情侣会在鹊桥上相会，而这座鹊桥就是“天津”。

    你突然联想到上午在船上她说的话……
    """
    me"我可以问你一个问题吗？"
    tea"嗯。"
    me"在你眼中，我是一个什么样的角色呢？"
    tea"……我觉得你是我最好的哥哥。"
    me"可是你知道吗"
    me"在我眼中，你是银河中最亮的一颗星星。"
    tea"可惜...只能在夜晚看到。"
    me"但是我白天能看到你啊。"
    tea"噗…"
    tea"可是……银河中的星星都好遥远，遥远到牛郎和织女每年只能见一面。"
    me"但是它们发出的光芒却能跨越光年温暖彼此。"
    me"而且，我们之间的距离比星星近多了。"
    me"如果你需要，我会随时来到你身边的。"
    tea"哥哥…可是那样你会很辛苦的。"
    "你轻轻地握住了小茶的手，她没有反抗。她的手小小的，有一点凉，乖巧地躺在你的手心里。"
    me"""
    小茶，我喜欢你。

    从见到你那一天，就一直、一直都喜欢你。

    只要你能开心，无论多么遥远多么辛苦，我都是快乐的。
    """
    tea"我知道的，你一直都在我身边。"
    me"答应我好吗？"
    tea"嗯！"
    """
    你轻轻与她十指相扣。

    不知不觉已是下半夜，月亮不知道什么时候悄悄挂在了东边的天空中，将温柔的光芒洒在在大陆最东端的岛屿上，也洒在了两个紧紧相依的人的身上。
    
    ……
    """
    scene bg villa
    with fade
    """
    不知道过了多久，你们牵着手回到了另一边的民宿。

    他们似乎并没有回来，也许还在打UNO，或者搞爱情保卫战。幸亏提前偷偷跑了出来，才不想搞什么爱情保卫战呢。

    身边的女孩散发出淡淡的清香，你不禁有些恍惚。真正互相喜欢的人，又怎么会需要保卫战这种强行撮合呢？
    """
    tea"哎呀，他们刚才找不到我们，都跑来私聊问了。应该也找你了的，你也回复一下让他们放心吧。"
    """
    你掏出手机一看，不仅七八个人发来消息，还有好几个未接电话。幸好习惯性静音，没有破坏刚才美好的气氛。

    你给他们回了消息，抬头看到小茶正在专注地看手机，她可爱的侧脸毫无防备地暴露在你的眼前。你忍不住亲了一口她的脸蛋。

    小茶抬起头来，红着脸说：“讨厌~”，却忍不住露出了甜蜜的笑容。

    你伸出双手与她紧紧相拥……
    """
    jump dj_endings.g_end06

label .gs15loser:
    tea"哥哥，你别这样……给我点时间好吗？"
    me"他就是个渣男，他欺骗了你，他抛弃了你，他把你的希望你的憧憬重重地扔在尘土里，还要狠狠地踩上一脚，对你说，他不在乎你……"
    me"可是我不一样啊！小茶，我是真的喜欢你，从第一次见到你，就一直、一直地喜欢着你。"
    me"我知道你还对他有幻想，可是他已经走了啊！为什么不能接受我呢？"
    tea"哥哥……你听我说好吗？"
    tea"""
    其实，我也一直在思考我们之间的关系和感情……

    每每我遇到困难时你给我帮助，每每我心情难过时你给我安慰，每每都是我享受着你给我的温暖……

    对不起……我早应该猜到你喜欢我的。

    可是我却一直贪恋着那种被人爱被人呵护的感觉，{w}
    又天真地在你的面前，讲另一个男孩子多好多好，讲我有多么喜欢。

    谢谢你，这几个月以来的爱和容忍，就像亲哥哥一样。

    但是对不起，我暂时还是忘不掉他。

    他给我留下了太深太深的印记……也许我还需要一些时间来抹平伤口。

    我还是想等他……也许这是我不切实际的幻想但是我还是愿意，{w}
    等到他脱单的那一天，等到我死心的那一刻。
    """
    me"""
    没关系啊，你愿意等他，我也愿意等你……

    也许你现在心里没有我的位置，也许你觉得现在还谈不了一场恋爱，都没关系的……

    我愿意等你，就像哥哥和妹妹一样，就像今天晚上的事情都没有发生一样，

    我愿意做你最好的哥哥，一直等待你，一直守护你……

    如果你真的等到了他，或者遇到了对的那个人，我也会祝福你。
    """
    tea"""
    之前有一次，诺诺姐和我聊过，她说，我这样对你太不公平了，是在养备胎。

    我当时还是太天真，以为我们之间真的是很单纯的哥哥和妹妹的关系。

    我还天真地以为，我没有向你要什么东西，也没有接受你的礼物，就不算备胎。

    现在我理解了，精神上的索取也是一种索取。
    我贪婪地享受着你给我的恋人一般的爱，却以妹妹的借口，逃避了付出的义务。
    
    我给了你对未来的幻想，却又根本不给你机会，这确实对你太不公平了。
    """
    me"""
    但是没关系啊，我喜欢你，我愿意为你付出，

    无论你是继续喜欢着他也好，心里全都是他也好，愿意等到他脱单等到自己死心也好

    只要我能一直在你身边就够了……

    其他的，我什么都不要……都可以……
    """
    tea"""
    哥哥，对不起。但是这也是我最后一次叫你哥哥。

    这样对你确实不公平，我本来没有资格享受你的爱。

    去找到属于你的那个人吧。

    去找到、除了我之外，也能让你幸福的人吧。

    有你这样的男朋友，相信她一定会很幸福。
    """
    me"可是……"
    "小茶站了起来。迎着星光，她的脸上挂着晶莹的泪珠。但是她毅然地转过身，向民宿走去。"
    me"小茶！你听我说！"
    "没有停留，脚步声渐行渐远……"
    jump dj_endings.g_end08

label .gs16sucker:
    tea"嗯……"
    me"我会一直陪着你的……直到你走出来。"
    tea"哥哥，你对我真好。"
    tea"之前小殷也说会陪我一辈子……可是……"
    me"我和他不一样"
    tea"可是他当时真的特别认真特别期待……"
    me"""
    你看着我的眼睛，人的眼睛是不会说谎的。
    你知道吗？其实，我一直都喜欢你。
    从我们第一次在火锅店见面、从我们第一次聊天的那个晚上，就一直、一直喜欢你。
    """
    tea"……！！"
    me"小茶，你是我见过的最单纯、最善良的女孩子，无论你接不接受我，我都愿意一直守护你。"
    me"我和别的男生不一样。很多男生追求女孩子，追的时候特别猛烈千方百计要追到手，真的追到了却一点都不负责任，我看不起他们。"
    tea"可是……哥哥，你这样好突然……让我考虑考虑好吗？"
    me"""
    好。其实，如果你对我没有感觉的话也没关系的，我们还可以继续当哥哥和妹妹。
    
    我还会继续像亲哥哥一样一直守护着你，为你付出我所有的爱。
    
    你要是遇到了喜欢的男生，也可以去撩，去和他在一起，我不会吃醋不会难过的。
    
    我真的非常喜欢你，所以只要你能够开开心心的，我就满足了。
    """
    tea"……哥哥……可是你为什么对我这么好呢？"
    me"因为我是真的喜欢你，所以真心希望你能幸福。"
    """
    你轻轻握住了小茶的手，她似乎犹豫了一下。

    两人都没有再说话，寂静的夜晚，只有偶尔的风吹过树叶的声音。天上的星星有些黯淡，月光洒在东极岛的大地上。

    就这样不知过了多久……
    """
    me"小茶，你怎么想的呢？"
    tea"对不起……我觉得对你还是没有恋爱的感觉。你在我心里还是更像哥哥一些。"
    me"嗯……谢谢你对我说了实话。没关系的，你也不要有心理压力，我们继续做哥哥和妹妹就好。"
    tea"""
    嗯……
    
    哥哥，我还需要一段时间走出来，谢谢你能陪着我。
    
    我会尽量找感觉的，如果有一天我找到了，我会告诉你，我们就在一起，好吗？

    哥哥，但在我走出来之前，我们之间就是很单纯的哥哥和妹妹的感情。
    
    你要是遇到了喜欢的女孩子就告诉我一声，然后大胆地去追，我会真心地祝福你们的。
    """
    me"""
    好。
    
    无论怎么样，我都会一直一直支持你，守护你，成为你的港湾。
    
    我愿意等你走出来，等你找到感觉的那一天；如果你找不到也不要紧，哪怕你脱单了，我也愿意继续做你最好的哥哥。
    """
    tea"哥哥……你是我最好的哥哥。抱抱小茶好吗？"
    "你伸出双手抱住了她。"
    me"你永远我最好的妹妹。我愿守护你直到天涯海角。"
    "……"
    jump dj_endings.g_end07

label .gs17love:
    "渐渐地，大家都笑累了。"
    lian"来搞爱情保卫战！"
    wqbh"啥叫爱情保卫战"
    lian"大人讲话，小屁孩别插"
    ming"这回我要当主持人，上回在密云做嘉宾被那个谁的臭脚一直熏，太难顶了。"
    "纪念册制作组""现在插播一条广告：敬请关注大樱桃纪念册第二部——密云之旅。"
    han"我和诺诺是情感导师！"
    lian"灯光师！"
    wqbh"我要当配乐"

    dan"那谁来做嘉宾呢"
    nuo"那肯定是上回主持人做嘉宾嘛"
    conway"喵喵喵？哪来的爱情"
    shou"关你p事，你继续主持人吧"
    "大家一齐把目光投向了你和小茶。"
    "……"
    "大家安静围坐在房间里，聚光灯照在本次节目的两位主角——小茶和你身上。舒缓的配乐响起，安静的房间里，小茶开始了她的讲述……"
    tea"""
    高中毕业的那个暑假，我喜欢上了一个男孩子，他叫小殷。

    我们考上了同一所大学，互相暗生情愫，但是约好大学再正式开始恋爱。
    
    在那个暑假里，我也认识了很多别的男孩子，他们都和我关系很好，其中包括一位学长……
    """
    "众人""学长？"
    tea"""
    嗯... 小天学长真的好耐心好温柔，我不会做海报，也不会写推送，不论我的问题有多傻，每次问他他都特别特别耐心地教我。
    
    渐渐地，在工作以外，我和他也时常聊天，以至于无话不谈。我觉得他就像我的哥哥一样。

    但我还是放不下小殷，那段时间衔接班开课了，我和他每天都要坐班。
    
    我们经常坐在教室后面聊一天，我们聊人生，聊理想，聊爱好，聊过去，他知道我的所有，我也知道他的所有，我好像遇到了世界上另一个自己……
    
    可是我没想到，八月份开始军训以后，他突然对我冷淡了很多，我给他发消息，他总是过很长时间才回一两句，有时候甚至第二天才草草敷衍，而我却在屏幕另一端等得心力交瘁……最开始我以为我说错了话或者做错了事让他生气了，可是问他他却说我没错……后来我鼓起勇气约他出来聊聊，可他却拒绝了。他说，对不起，我们还是做回普通朋友吧。
    
    我当时快要崩溃了，我问他为什么，他说他也许没有他以为的那么喜欢我。于是，我们的恋爱还没有开始，就这么分手了……

    就在我非常绝望的时候，哥哥就像一束光照亮了我的世界，但我后来才意识到，他一直都在的。
    
    我们无话不谈，上课下课、教室寝室、白天黑夜，他就像一直陪伴着我，虽然他并不在南京......
    
    哥哥手把手教我面对大学里遇到的一切困难。他永远都站在我一边，理解我的小情绪，也支持我做的一切。
    
    他的安慰是那么的恰到好处，我好像遇到了世界上另一个自己。
    
    后来你们计划来东极岛玩，他问我要不要一起来散散心，所以这次我就跟他来了。
    """
    
    nuo"你觉得这是爱情吗？"
    tea"我觉得更像是亲情，他就跟哥哥一样爱护我。"
    nuo"但他不这样觉得"
    han"你怎么看待这段关系？"
    me"她一直觉得我是她的哥哥，但我是真的喜欢她。"
    han"那你不会觉得这样很卑微吗？"
    me"我不在乎，只要她开心，只要我能陪在她身边，这就够了。这次真的她来东极岛是想散散心的，她本来就情绪不太好，我也想陪陪她。"
    conway"下面请情感导师诺诺同学向女嘉宾提问："
    nuo"小茶，你会觉得对不起他吗？"
    tea"我没有想太多，我只是单纯觉得哥哥真的很好，就像亲人一样。"
    nuo"那你觉得之后有可能在一起吗？"
    tea"……"
    me"""
    这个问题我替她回答吧，我们之前也聊起过这个话题，她真的是个很善良很单纯的女孩子。
    
    我愿意努力追她，但是也许我真的没有办法让她喜欢上我……
    
    无论如何，我尊重她最后的决定。只要能让她开开心心的，我为她付出再多都愿意。
    """
    "众人""……"
    nuo"小茶，你知道这样对他很不公平吗？"
    me"我知道你们是什么意思，这听起来确实很像备胎，但我觉得这件事还需要从主观意愿上来看待……"
    me"她不是养备胎的女孩子，我也不觉得我是备胎，我愿意为她付出，因为我觉得人生在世需要一段感情寄托。"
    conway"女嘉宾能回答这个问题吗？"
    tea"我真的没有想过，我只觉得两个人都开心不就好了。"
    tea"但我也一直没有接受过哥哥物质上的礼物，而且我也非常希望他能找一个别的女孩子，我真的只把他当哥哥。"
    han"我不接受，我觉得所有异姓兄妹都是扯淡。"
    nuo"""
    你说你没有物质上的接受，但情感上的接受也是接受，而且绝对不亚于物质上的接受。

    你知道你这样会让他产生对未来的幻想吗？

    他为你付出了男朋友一样的爱，你就心安理得接受了然后用哥哥的名分去打发他？
    """
    tea"但我真的跟他说的很清楚，我还在等小殷，我会等到他脱单的那一天……"
    nuo"所以你平时追求喜欢的男生从不考虑他，遇到麻烦了受伤了就来无偿享受哥哥的爱，你这是把他当成什么了？"
    nuo"创可贴？永久性的、全自动的、只要你一受伤就会自动贴上来的创可贴？"
    "众人""……"
    "小茶清澈的眼睛里浮上一层水雾，她低下头，双肩轻轻耸动，突然拉开房门头也不回地冲了出去……"
    menu:
        "你怎么办呢？"
        "跟上她":
            jump .gs18follow

        "算了……":
            "房间里众人面面相觑，都不知道该说什么，你的脑子更是如同乱麻一般……"
            "身旁的连南小声跟你说："
            lian"你快跟上去看看。"
            jump .gs19giveup

label .gs18follow:
    scene bg outside
    with fade
    """
    你赶紧穿上鞋子冲出了民宿追上了小茶。

    她走得很快，但任凭你怎么叫，她都不肯理你，只是不停地抹着脸上的泪水……

    不知走了多远，她看到路边的一张长椅，坐了下来。
    """
    me"不哭了好吗？今天他们说得不太好听，你别往心里去。"
    me"我确实喜欢你，但我也是真心把你当妹妹的，我愿意为你付出，也从来没觉得你是在养备胎。"
    me"对不起，我没想到他们会这么尖锐……反正明天就离岛了，我们在一起开心就好，别管他们的看法就行了。"
    """
    小茶还是没有说话，任凭大滴的泪水滴落在衣服上……

    ……

    清冷的月光洒在岛上，一阵秋风让你不禁打了个寒战。身边的小茶渐渐地停止了哭泣。
    """
    tea"哥哥，对不起。诺诺姐说得确实有道理……我明知道你喜欢我，还在你面前提别的男生有多好，这太残忍了。我也不应该这样理所当然地享受你给我的爱，却只给你一个哥哥的名分，让你沉浸在对未来的幻想中……这对你太不公平了。"
    me"小茶你听我说，我真的不这么认为……我是心甘情愿对你好的，真的是很单纯的哥哥对妹妹的爱……"
    tea"哥哥，谢谢你这么久以来对我的关爱，但是我真的不能再这样接受下去了。这也是我最后一次叫你哥哥。我对你没有男朋友的感觉，就不应该呆在你身边，给你留下任何幻想。你值得比我更好的女孩子。要是遇到了的话，就放手去追吧，我会默默地祝福你们的。"
    "小茶起身向民宿走去。迎着月光，她的眼中还有泪水在打转。"
    me"小茶！你听我说！"
    "没有回头，小茶的背影渐行渐远……"
    jump dj_endings.g_end08

label .gs19giveup:
    scene bg gs19outside
    with fade
    """
    你机械麻木地走下楼，秋夜的凉风迎面吹来，你打了个寒战，似乎稍微清醒了一点。

    小茶已经走出了民宿，你在她身后不远处走着，一直跟着她走到了相隔百米的另一处民宿，她上了楼，走进了房间，砰地关上了门。

    你伸出手悬在门上犹豫着，却最终没有敲下去的勇气，只好走进了旁边的房间躺了下来……

    也许，这段不对等的感情，本来就不该发生吧……
    """
    jump dj_endings.g_end08
