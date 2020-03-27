# ###########################################################
#            Copyright (c) 2020 BigCherry Team
#                   All Rights Reserved 
#
#  filename: dj_102.rpy
#  description: (story scripts) Dongji Main Story 10.2
#  Story Author: Alan Li
#  Script Author: Wentian Bu
#  Version: 1.0
#  
# ###########################################################

label dj_102:

label .s03apartment:
    scene

    show text "2018年10月2日" at truecenter
    with dissolve
    pause 1

    scene bg s03apartment
    with fade
    "终于到了约定在舟山集合的日子。"
    menu:
        "你准备怎么出行呢？"
        "硬卧到宁波":
            "你和韩韩、小汪同行，但是只有你买到了卧铺票。"
            "你假惺惺地说把卧铺让给女孩子，没想到小汪一口答应，于是你只好和韩韩一起硬座坐到了宁波车站。"
            jump .s04bus
        "在宁波中转":
            "你和连南小萝卜买了北京飞往宁波的机票。"
            "由于起飞时间很早，你们前一天晚上在清华集合，然后去吃了柳叶刀烧烤。柳叶刀的招牌菜刀拍黄瓜可真是好吃！你们一口气吃了三盘。"
            "晚上连南安排你们到了学生会活动室，你和小萝卜睡行军床，竟然把行军床睡塌了。终于混到凌晨四点，一起前往机场乘飞机。"
            jump .s04bus
        "在绍兴中转":
            "你和冠军、诺诺、小明一起去了绍兴鲁迅故居。"
            "然而那里人太多了。为了防止误车，你们只好放弃参观去了火车站。"
            jump .s04bus

label .s04bus:
    scene bg s04bus
    with fade
    "你所在的小组终于抵达了宁波南站的汽车站。"
    "幸亏冠军提前发现大巴票需要预约，不然可真有些难顶。"
    "第一次见识舟山跨海大桥，由于大家来自全国各个省市，自然组成了五个小组，虽然遭遇了堵车，但大家位置共享互相吐槽对方真慢，确实很有趣。"
    "好久没见大家了，期待一次和去年密云行一样的愉快经历。"

    conway"卧槽，我们忘记去超市采购食物了，刚才公交路过了一个商场感觉还挺大的，你们要不去看看？"
    me"好，我们组男生多，我们等会儿去吧。"

label .s05mall:
    scene bg station
    with fade
    "又经过了一个多小时的漫长堵车，你们终于到了舟山市的客运站"
    "走下大巴，天都已经黑了。果然，公交已经没有了，还是打出租吧。"
    "很快你们一行五人拦下了两辆出租，前往之前提到的那个商城。"
    scene bg s05mall
    with fade
    me"别看舟山是个岛，这个商场还蛮大捏"
    "小汪""我们去超市看看买什么吧"
    han"顺便看看有啥餐饮吧"
    bwt"在吗？捞吗？"
    "你们进入了商城，经过一个多小时的采购，终于完成了任务。"
    "你们买了一整辆购物车都装不下的东西，幸亏男生多，分成了五个大袋子提着。"
    "毕竟这是十几个人两天的口粮啊，要不然真要在东极岛上荒野求生了……"

label .s06street:
    scene bg s06street
    with fade
    "你们在商城门口遇到了一个难顶的问题，这里非常不好打出租车！"
    "滴滴加钱到20元都没有人接单，看了看地图，才发现去民宿必经的大桥上是全红！！！"
    "过了半个小时，你们不禁有一丝绝望，难道真的要提着这么多东西走过大桥吗？"
    menu:
        "怎么办？"
        "老子钱多，再加钱，重赏之下必有勇夫！":
            "你又加了五十块。"
            
        "没办法了，边走边看吧，可能走过桥就有人接单了。":
            "你们还是图样！显然过桥的出租车肯定没有空车啊！"
            "你们只好提着五袋东西走了八公里，到民宿的时候已经凌晨了，大家都累瘫了。"
            jump dj_103.s14villa
        "没办法了，再等等吧，总不能走过去吧":
            pass
            
    "终于两个app有一个被接单了！这就出现了很尴尬的情况：你们是五个人……"
    menu:
        "怎么办呢？"
        "我们跟司机商量一下挤挤吧？大家都瘦！":
            "好说歹说司机小哥终于同意了，但发现连南太胖了，完全塞不下。"
            "无奈之下，你们只好把买的东西抱着，然后让连南钻进后备箱里。"
            jump .s09taxi
        "你们四个先带着东西坐车走吧，德玛西亚不相信眼泪！":
            jump .s07street
        "摇骰子分两个人在这里等着，其他三个人带着东西先走":
            "于是你坐上了前一辆车。"
            jump .s09taxi
        
label .s07street:
    "你们突然意识到后面还有一组是万千和壮壮，于是决定由你在这里等他俩的出租，这样问题就迎刃而解了。"
    "你来到了旁边一家标志性建筑洗浴娱乐城的门口，等待最后一组的出租车。"
    zhuang"我们下大巴了，但tm拦出租一看目的地都拒载。"
    me"是，那边桥上堵的很严重，都不愿意过去，我们刚才也遇到了。"
    menu:
        "怎么办？？？"
        "壮壮你不是会开车吗？要不抢辆车算了？":
            # scene 09fight
            "壮壮模仿GTA5拦了辆车，拉开车门试图把司机拉出来。"
            "没想到司机出来反手就是一个过肩摔把壮壮摔在车顶上一通殴打，万千儿见事不妙以武当亲传的太极拳法救人于危难之际。"
            "你们三人最终在派出所待了一晚上 ，直到第二天清晨才和众人在港口汇合。"
            jump dj_103.s16port
            
        "没办法，加钱呗...说不定就有人接单了。":
            "你又加了50块，但是可能目的地太远都不想载，过了好久好久终于有人接单了。"
            "等到你们到民宿，已经很晚了，大家都说你们没参加海边狂欢真遗憾。"
            if dj_withgirl:
                jump dj_girl.gs01room
            else:
                jump .s13rooom

        "先把滴滴的目的地选到我这这个洗浴城吧。":
            "果然目的地改到洗浴城就被接单了，我套路还是深啊。"
            "等出租车到你这之后，你们一起给司机小哥求情，赖着不下来，小哥只好答应送我们过去。"
            jump .s09taxi

label .s09taxi:
    "终于逐渐度过了这个堵死的桥。但这个导航似乎越走越奇怪了，韩韩发的定位emmmmmm..."
    "百度地图""到达目的地附近，导航结束。"
    "但是……此时出租处于一个导航上看不到路、车灯被环境的黑暗吞没的未知地点。你们和司机小哥都沉默了，沉默是今晚的康桥...."
    "……"

    "司机小哥""我靠我们竟然被导航带到了村子后面的荒山上。我们从前面绕一下。"
    "从前面绕下来，终于看到了路灯和民居，双方都松了一口气。"

    "终于，你们历经千辛，终于到了照片上的民宿，你们非常感谢小哥。"
    me"这个鸟不拉屎村也太偏了，明天我们要赶早班船，可以留个手机号，我们如果有需要提前预定一下？"
    "司机小哥""吼啊！"

    "但...大家，人呢？"
    jump .s11beach

label .s11beach:
    """
    寻声而去，原来大家都在下面的石滩上玩耍，好久不见，甚是想念。
    
    不知道谁把音箱打开了，你们一起纵声歌唱：
    
    东极岛啊你人杰又地灵，太平洋的风儿最先吹到你
    
    东极岛东极岛，大陆最东的岛屿，海浪都来亲吻你，鱼儿都来拥抱你

    ……
    
    尽管淘宝老板还没有告知明早船票是否购买成功，但和这样有趣的一群人在一起，不管是窝在舟山民宿，还是成功前往东极，都是也一样不枉此行吧。
    """

    if dj_withgirl:
        jump dj_girl.gs01room

    "正在热闹着，突然发现原本坐在身边的卜和汪两人不见了。"
    "众人疑惑，终于发现这两个人竟然偷偷跑到上面的入口处坐着，似乎在窃窃私语聊着什么……"
    menu:
        "这时你："
        "我们跑过去一言不发坐在他们周围把他们围住吧，形成大π键":
            $ dunhuang_value += 10
            "你们突然冲了上去把他俩围起来，他们吓了一跳"
            bwt"你们有毒吧！"
            "众人憋笑，最终一哄而散。"
            jump .s12villa

        "还是不打扰他们了":
            $ dunhuang_value -= 10
            jump .s12villa

        "这种时候，怎么能不拍照留下罪证呢！":
            ming"卜文添！"
            bwt"干啥"
            "众人一起打开了闪光灯拍照。"
            bwt"你们有毒吧！"
            jump .s12villa

label .s12villa:
    "众人继续聊天，突然你接到了淘宝老板的短信，说明天船票已出票，按照你们要求是最早的一班。"
    "最早的一班，那就是8：45开船，提前一小时登船那就是7点45开始检票，从民宿到码头如果畅通无阻大概是四十分钟的出租车程。"
    menu:
        "你们准备什么时候起床？"
        "这个鸟不拉屎村，哪来的出租，我们可能需要四点起床，走到最近的公交站...":
            "众人""靠，这都一点了那我们还睡个啥，直接玩通宵吧。"
            "于是众人玩了个通宵，果然打不到出租车，坐公交前往港口。"
            jump dj_103.s16port

        "使用滴滴预约明天的出租车吧":
            "人有点多，至少需要四辆车。滴滴预约没有师傅接单，你们到前台问了老板。"
            "老板""我给你们一个司机电话吧，你们联系一下他。"

        "我们来的时候幸亏留了出租车小哥的电话，给小哥打个电话问问吧？":
            pass

    "明老板给出租小哥打了电话，很快确定了明天5点半约四辆出租过来。"
    conway"不愧是外联部长！正部级干部就是不一样！"
    "夜已深，大家约定明天五点起床，五点半在门口集合，各自分了房间，回去睡觉。"
    jump .s13rooom

label .s13rooom:
    scene bg villaroom
    with fade

    "你回到房间，正和汪闲聊着有没有什么吃的，突然发现床旁边的地板上出现了一只超级大的蜘蛛！"
    "小汪""啊！！！！！！"
    menu:
        "蜘蛛竟然还在到处乱爬！你怎么办？"
        "赶紧让汪呼叫卜前来救驾":
            pass

        "二话不说，抄起旁边的拖鞋上去就打":
            "大蜘蛛被你拍死了，但汪仍然不敢睡觉，只好呼叫卜前来救驾。"
            
        "这有什么可怕的，你看多好玩？":
            $ dunhuang_value += 20
            "你把大蜘蛛拿起来把玩，小汪非常恐惧。"
            "据她事后说，就好像看着炸鸡一样，甚至轻微吞咽了口水。"
            "汪假装害怕蜘蛛，赶紧呼叫卜前来救驾，实际上是害怕你。"

        "跑到楼下要求老板换房间":
            "老板""没有多的房间了。"
            "你们上来之后，却发现蜘蛛已经不见了。"
            "汪还是很害怕，于是呼叫卜前来救驾。"

    "卜文添接到呼救之后立即赶到，却发现蜘蛛早就不知去向，无奈之下只好安慰两句准备离去，"
    menu:
        "这时你怎么说？"
        "别走了，到这陪着我们吧":
            $ dunhuang_value += 10
            bwt"这...似乎不太好吧。"
            me"有啥不好的，又不睡觉，我们聊聊天算了，反正也就几个小时。"
            "于是你跟他们俩尴尬的聊着天，时刻感觉自己在发光发热……"
            "混过了一夜，不知道什么时候睡着了，直到被闹铃闹醒发现三人竟然挤在一张床上。"

        "行吧...那我们只好躲到厕所里面":
            "虽然民宿的厕所也不是特别干净，但至少门关上会稍微安心一些。"
            "你们慢慢的糊弄着坐在洗漱台上睡着了，直到被闹钟闹醒。"

        "我们能和你们换个房间吗？":
           bwt"连南都已经脱光光睡着了，我还是在这陪着你们聊天吧。"
           "于是你跟他们俩尴尬的聊着天，时刻感觉自己在发光发热……"
           "混过了一夜，不知道什么时候睡着了，直到被闹铃闹醒发现三人竟然挤在一张床上。"
    jump dj_103.s14villa