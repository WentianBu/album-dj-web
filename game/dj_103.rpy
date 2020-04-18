# ###########################################################
#            Copyright (c) 2020 BigCherry Team
#                   All Rights Reserved 
#
#  filename: dj_103.rpy
#  description: (story scripts) Dongji Main Story 10.3
#  Story Author: Alan Li
#  Script Author: Wentian Bu
#  Version: 1.0
#  
# ###########################################################

label dj_103:

label .s14villa:
    scene black with fade

    show text "2018年10月3日" at truecenter with dissolve
    pause 0.5
    image time1 = Text("凌晨6:00", xalign=0.5, yalign=0.55)
    show time1 with dissolve
    pause 1.0

    scene zs morning with fade

    play music journey fadein 2.0

    ming"出租车已经在路口那等候了，大家赶快点吧。"
    lian"走走，凑齐四个人就上车出发吧，千万别误船了。"
    shou"那个啥，诺诺还在化妆，大家先走吧……"
    conway"要化妆早点起啊！"
    shou"害，她四点就起来了，洗澡化妆鼓捣到了现在……"
    "……""……"
    nuo"来了来了~~"
    "众人纷纷上了出租车，陆续出发。"


label .s15port:
    scene zs port morning with fade
    python:
        if not renpy.music.is_playing(channel='music'):
            renpy.play("audio/bgm/journey.ogg", channel='music', fadein=2.0)
    "车上你有些困倦不知不觉睡着了，等醒来已经到了码头。"
    "不知为何还不到七点的码头都已经熙熙攘攘了。"
    dan"为啥这么早就这么多人了？"
    me"奇怪，这不离早班还有好久吗？"
    zhuang"那我们先吃点早饭吧。"
    "众人寻觅了一会，找到了一家门上贴着封条痕迹的面馆。"
    "但老板热情的招呼了大家，看大家人多就让上二楼去吃面。"
    "虽然所谓的肉丝面只有几根肉丝、海鲜面也只有几个未知的贝类生物，但热腾腾的汤还是让大家十分满意。"
    "距离登船只有不到十五分钟了，你们决定去码头等着，也看看海景。"

label .s16port:
    scene zs port go with fade
    "终于到了检票的时间……"
    yinyin"诶我怎么身份证刷不出来了过不了闸机？"
    lian"我试试，诶好像也不行啊……"
    yourong"我也不行诶？"
    shou"赶紧去咨询处问问？"
    "咨询处小姐姐""你们的票是早上六点半的啊，现在误船了。"
    "众人""什么！？"
    me"你们最早的班次不就是8:45这班吗？"
    "咨询处小姐姐""现在国庆增加了最早的6:30一班。"
    "众人""……"
    "你赶紧给淘宝老板打电话，三次之后终于接通，说明情况之后，希望老板能帮忙解决一下问题。"
    "老板""你们自己误了船，出票信息就写的6.30，返程票已经下单了，那部分的钱也不可能退的。"
    me"谁知道你最上面这个6.30是什么意思，正常人写时间不都是6:30吗？"
    "老板""那没办法了。"
    play sound hang_up
    "随即老板挂了电话，再也打不通。"
    default menuset = set()
    ## May jump story
    ## AutoSave 2-1
    python:
        renpy.take_screenshot()
        renpy.save("12-1", "黑心老板不接你们的电话……")

    menu .s16port_ques:
        set menuset
        "你们该怎么办..."
        "mmp啊这可咋整，坑爹的淘宝老板，换个手机给他打":
            "果然换个手机号，淘宝老板接电话了，但刚没说两句，老板就又给挂掉了。"
            jump .s16port_ques

        "事情已经发生了，我们试试找码头工作人员求情":
            jump .s17port

        "算了自认倒霉吧，到舟山找个民宿打牌也挺好":
            $ dunhuang_value -= 10
            "你们在舟山找到了一家价格合适的小别墅。"
            han"现在就去别墅也太早了吧，要不我们找个地方去逛逛？"
            ming"我昨天看到采购的那个商城旁边好像有一家密室逃脱，可以去玩一下。"
            "众人纷纷支持这个决定，于是打车去了商圈。"
            scene zs mall with fade
            "虽然舟山是个小地方，但是这个商圈里人可不少。"
            "大家玩完密室逃脱，又去看了场电影，虽然没能上岛，但玩得也很开心。"
            jump dj_104.s57taxi

        "舟山到东极也不过是两个多小时船程，不如我们一起游过去吧":
            $ dunhuang_value += 30
            scene dj swim with fade
            "你们一行十多人，经过十个小时的游泳，终于抵达了东极岛。"
            "当地媒体听说了你们的英勇行为，前来采访你们："
            $ renpy.music.set_pause(True, channel='music')
            "记者""你们为何一定要登岛呢？"
            play sing dj_island_2 fadein 1.0
            "你们一起唱：东极岛啊东极岛啊 除了这里 我们哪儿都不想去……"
            stop sing fadeout 1.0
            $ renpy.music.set_pause(False, channel='music')
            jump .s24villa

label .s17port:
    "你们分成三波，大部队留在旁边查找舟山的酒店，一小部分在购票处排长队，你和另外几人准备找工作人员求情。"
    $ menuset = set()
    ## Not important
    menu .s17port_ques:
        set menuset
        "找哪个工作人员呢？"
        "售票处忙碌着收钱卖票、操着本地口音的阿姨":
            "阿姨""排队去。"
            me"我们不是想买票……"
            "阿姨""排队去。"
            me"我们…"
            "阿姨""排队去。"
            "……"
            jump .s17port_ques

        "咨询处非常同情我们遭遇、但表示无可奈何的的小姐姐":
            "小姐姐""是的我很同情你们这个遭遇，但是确实没有办法，船上也没有多的座位了。"
            jump .s17port_ques

        "检票处的看起来对我们有些兴趣、没事就瞅瞅我们的小哥":
            "小哥""以后要注意看官网的消息，不要走黄牛代购啊。"
            jump .s17port_ques

        "售票处管排队秩序的、胸前戴着党徽但说话有点凶的大叔":
            pass

    "大叔""现在确实船上没有空座位了，你们也看到了。"
    me"是...但我们大学生出来玩，实在没办法了，您能通融一下吗？"
    "大叔""你们每个人都有票对吧？"
    me"对，都是6:30的票"
    "大叔""当时买票花了多少钱？"
    me"每个人多了100代购费"
    "大叔""呵呵，你们先到旁边等着吧。" 
    "你们听不出来大叔语气中的意思，只好站到一边去了...."
    jump .s18port

label .s18port:
    scene zs port gather with fade
    "你们与其他人会合，讨论进一步的方法。"
    ming"我们刚才看到了一个价格适合的酒店，还有一个套间目前空出。"
    han"套间确实适合我们去住。"
    ## May jump story
    ## AutoSave 2-2
    ## Add Note
    python:
        renpy.take_screenshot()
        renpy.save("12-2", "要不要订下那个套间呢？")

    menu:
        "这时你们准备怎么办？"
        "继续等着，但很担心酒店房间被别人抢定下来，先下单吧":
            $ dunhuang_value -= 10
            ming"携程上说退这个酒店要赔四百块……"
            lian"哎，就当花钱买保险了。"
            
        "还是不等了，现在就下单直接去酒店吧":
            $ dunhuang_value -= 20
            "你们在舟山找到了一家价格合适的小别墅。"
            han"现在就去别墅也太早了吧，要不我们找个地方去逛逛？"
            ming"我昨天看到采购的那个商城旁边好像有一家密室逃脱，可以去玩一下。"
            "众人纷纷支持这个决定，于是打车去了商圈。"
            scene zs mall with fade
            "虽然舟山是个小地方，但是这个商圈里人可不少。"
            "大家玩完密室逃脱，又去看了场电影，虽然没能上岛，但玩得也很开心。"
            jump dj_104.s57taxi

        "想想还有什么骚操作":
            "小明突然意识到可以先给酒店打个电话，让他们给我们留着，结果发现酒店真的答应了"
            
    conway"刚才那个大叔最后问我们花多少钱买票是什么意思啊？"
    me"不会是想让我们给他点好处费吧？"
    "大家想了想觉得有道理。"
    lian"那么...大家有没有现金，四百五百块应该差不多？"
    "小老弟""我这有两百"
    yourong"我一点现金都没有"
    wqbh"我这三百"
    zheng"够了够了。"
    ## Not important
    menu:
        "你准备："
        "当众“行贿”？？？这可不行，我们是新时代大学生，赶紧制止大家":
            $ dunhuang_value -= 20
            jump .s20port

        "五百块可能不够吧？他问我们花了多少代购费，我们竟然实话说了每人100，就算折半也得800吧":
            $ dunhuang_value += 10
            jump .s19port

        "可以先准备800现金准备好，先把400块放里面，如果他暗示不够，再把另外400补上":
            jump .s19port

label .s19port:
    scene zs port go with fade
    "你包好了钱，再走到大叔面前。"
    "大叔""不是说了让你们在旁边等着吗？"
    ## Not important
    menu:
        "你准备怎么说？"
        "“辛苦您了，这是我们的一点小心意”，说着把纸包递过去":
            pass

        "“那个...我们...想...这个...嗯...”":
            $ dunhuang_value -= 10

        "“你咋还没搞定啊，不就是想要钱吗？800块给你，我们时间很紧的，搞快点。”":
            $ dunhuang_value += 20

    "大叔""你们在干什么？说让你们在旁边等着就等着啊"

    "你们更加丈二和尚摸不到头脑。"
    zheng"难道是刚才做的太明显了，旁边这么多人，他没法收？"
    "陷入沉默..."
    "这时淫淫和兽兽终于排队到达了售票处，朝众人招手："
    shou"还需要买票吗？"
    me"有几张？"
    shou"只有三张。"
    zheng"那还差得远啊……"
    lian"要不算了，同进退吧。"
    yinyin"嗯。"
    jump .s20port

label .s20port:
    han"这会小天他们应该起来了，要不给他们打个电话告诉他们这个好消息？"
    ming"是滴，他和小茶可以两个人住那么多房间了"
    yourong"哈哈哈万万没想到"
    dan"都怪我们忘记禁言诺诺了才误了船"
    nuo"？？？狗屎"
    "……可能的解决方案几乎都试过，虽然都没走通，但气氛也因此轻松起来了。"
    "大家开始愉快的讨论这两天在舟山玩什么，以及如何举报这个黑心商家。"
    jump .s21port

label .s21port:
    scene zs port go with fade
    "突然，大叔朝大家打招呼，你赶紧过去……"
    "大叔""你们每个人确实都有票是吗？"
    me"是的"
    "大叔""跟上级请示过了，说可以让你们用6:30的纸质票过检上船。"
    me"太棒了！！！谢谢您！"
    "大叔""但是没有座位哈，年轻人应该还行。拿着身份证去咨询处开纸质票吧。"
    me"没关系！谢谢大叔！！！奥利给！"
    "你们感到非常惊喜，满满的正能量！"

    "时间紧迫，距离开船还有五分钟，你们一行人赶紧去打印纸质票。"
    "但奇怪的是，淫淫等四人莫名其妙打印出了两张去程的船票，一张是6:30，另一张是14:30的。"
    ## Not important
    menu:
        "你们准备？"
        "时间紧任务重，管他三七二十一，多开就拿着，先上了船再说":
            jump .s22ship

        "是你们系统的bug吧？我们有程序员，需不需要留下来协助你们修复系统？时薪很高的哦":
            $ dunhuang_value += 20
            "于是淫淫被留下来debug了，等到大家从东极回来，他把大家旅行的费用都挣回来了，表示“我土豪，我请客”"
            jump .s22ship

        "这个票不是我们买的，你们留下吧，可以送给有缘人":
            $ dunhuang_value += 10
            jump .s22ship

label .s22ship:
    scene ship go1 with fade
    """
    终于，一顿操作猛如虎，你们竟然在五分钟内提着行李过安检上了船。
    
    果然没有座位了，你们只好回到货仓，在冷藏肉水果萝卜白菜可乐啤酒旁边安置了行李。
    
    船开了，大家吹着海风，回想起当年在密云螺旋稳赶火车的操作，不禁感慨。
    
    闲聊间，突然手机响了，原来是那个可恶的淘宝老板……
    """
    ## Not important
    menu:
        "你准备？"
        "狗屎，你不是说不管我们了吗？怎么又来电话？接？接个p！":
            "众人纷纷说：“可以！”"
            "于是你怒挂了电话。"
            
        "接，大家轮流骂他一通":
            $ dunhuang_value += 10
            "众人纷纷口吐芬芳，但因为船上是在是太吵了，老板什么都没听到。"
            
        "接，跟他说明情况返程票不要退":
            "因为船上是在是太吵了，你们互相之间什么都没听到。"

    lian"还是跟他打字说一下吧，返程票千万别被他退掉了。"
    me"有道理。"
    "于是通过淘宝客服跟老板说明了现在的情况。"
    "过了一会儿……"
    "老板""你们是不是多取了四张票？"
    me"码头那边是多打了几张重复的。"
    "老板""那是我给你们买的，你们要补钱啊。"
    me"我们没有请宁给我们买票吧？宁当时直接挂电话，我们最终自行解决了上船的问题。"
    "老板""你们不补钱的话，小心返程还会出问题。"
    me"那你这是在威胁我们了？" 
    "老板""你们下船之后在对面码头问问能不能退。"
    me"多的票能退的话，我们会把钱还给你。但如果返程敢出问题，我们只好请平台介入了。"

    scene ship go2 with fade
    """
    一路在广阔的海平面上没有信号，好久没有这么惬意了。
    
    听着海浪和引擎的轰鸣声，不远的天空还飞着几只海鸥。
    
    大家分成三三两两吹海风聊天，连南靠在行李上睡着了……
    """
    scene ship go3 with fade

    "不知过了多久，船终于靠岸了，你们纷纷下船，民宿老板娘过来接你们。"
    "跟着老板娘，你们走在渔村的小路上，唱着东极岛岛歌："
    play sing dj_island_3 fadein 1.0
    """
    东极岛 东极岛 我们不会离开你
    
    生是你的老百姓 死是你的小精灵……”

    ……
    """
    stop sing fadeout 1.0
    jump .s24villa

label .s24villa:
    scene dj villa day with fade
    "终于到了住宿的地方，原来是相距两百米的两栋民宅。"
    "于是你们决定，大的这栋作为闹腾活动场地，小的民宅作为晚上累了的人休息的地方。"
    $ menuset = set()
    ## Not important
    menu .s24villa_ques:
        set menuset
        "距离上一顿早餐已经快七个小时了，你们准备："
        "让民宿老板帮忙介绍一家岛上正宗馆子":
            "老板""那你们可问对人了，到我朋友那去吧，保证实惠！"
            jump .s25restaurant

        "从舟山带过来了这么多食材，自己做吧！":
            wqbh"累死了！我不要做饭"
            "众人""任劳任怨的厨房大师傅主席要是在就好了"
            jump .s24villa_ques

        "冲冲冲，直接下海捞海鲜啊":
            $ dunhuang_value += 20
            "你们被渔民用渔网救了起来，当地媒体听说了你们的英勇行为，前来采访："
            "记者""请问你们为何一定要在东极岛亲自下海呢？"
            $ renpy.music.set_pause(True, channel='music')
            play sing dj_island_3 fadein 1.0
            """
            你们一起唱：
            
            东极岛 东极岛 我们不会离开你
            
            生是你的老百姓 死是你的小精灵……
            """
            stop sing fadeout 1.0
            $ renpy.music.set_pause(False, channel='music')
            jump .s25restaurant

label .s25restaurant:
    scene dj restaurant1 with fade
    "老板带着你们走到了海边的一家大排档，门口摆着各种活蹦乱跳的、不知名的海洋生物，1000元包席，保证海鲜过半管饱。"
    "你们立刻决定就在这家吃了，感受渔家的原始与新鲜。"
    conway"大家都客气点啊！我就不客气了。"
    scene dj restaurant2 with fade
    ## Not important
    menu:
        "桌上自然分为了两派，你是哪一派？"
        "不吃贝壳不吃虾，青椒肉丝西红柿鸡蛋是我的爱":
            "你很快加入了冠军、壮壮等人对家常菜的抢夺战，可恶的冠军竟然一个人抢走了半盘青椒肉丝！"

        "海产怎么选？小孩子才做选择，成年人全都要":
            "这也太棒了吧，果然1000元海产几乎吃不完，啥都有了。"

    "风卷残云，不一会桌上就没剩什么菜了。"
    "这时小天突然说他们俩上岛了。"

    ## Not important
    menu:
        "于是你们准备？"
        "赶紧吃完，一点都不给他们留！":
            pass

        "等他们来了再一起吃，让他们也摊钱哈哈哈哈哈哈":
            $ dunhuang_value += 20
            
    "不一会小茶和小天两人终于到了，听完我们讲述刚刚经历的传奇，感觉他们来岛实在是顺利。"
    ming"太久没吃过这么爽的海鲜了！"
    zhuang"我虚了，只能吃海草，这竟然没有鱼香肉丝。"
    nuo"我去，都三点了"
    conway"我们到石头那里拍个合影吧。"

    scene dj stone photo with fade
    "众人进行了“东极”游客打卡沙雕合影，随后回民宿睡觉。"
    play sound take_photo
    scene dj stone photo with phototake
    pause 2
    stop music fadeout 2.0
    scene black with Fade(2.0, 2.0, 0.0)
    jump .s26villa

label .s26villa:
    scene dj villa kitchen1 with fade
    play music melody_of_night_23 fadein 2.0
    """
    一觉睡的昏天暗地，起床都快六点了。

    喊醒众人，简单洗漱之后，你来到厨房，不知如何下手。
    
    万万没想到，小明竟然这次接替主席食堂大师傅的身份，担当了掌勺的重任，万千等人也纷纷下场做了几道炒菜。
    """
    han"你们这些老学姐怎么回事？怎么一个个的都不会做菜，还得人家学妹上场。"
    nuo"嘻嘻嘻嘻我会吃就行。"
    zheng"谁倒下垃圾啊，桶都装满了！"
    shou"专业倒垃圾的小萝卜怎么还不来？"
    "……""……"
    jump .s27villa

label .s27villa:
    scene dj villa kitchen2 with dissolve
    "而你和老板娘聊的非常投机。"
    "老板娘""其实我是专门跑到这里隐居的。"
    "难不成这是个富婆？？"
    "老板娘""这边生活真的很舒适，我也喜欢吃海鲜。我是北京人，北航毕业的，后来觉得工作没什么意思，就跑到东极岛开民宿了。"
    me"哇，北航吗这么厉害！"
    "老板娘""你们看起来也是大学生吧？什么大学？"
    me"什么大学都有23333我们是高中同学。"
    "……"
    scene dj villa flag with dissolve
    "这时，连南正在和韩韩有容两位身高担当一起挂桃旗，找来找去终于决定悬挂到小院的面前，十分满意。"
    "老板娘""你们这个旗子是什么含义啊？"
    me"这是一个很长的故事了……"
    "……"
    "最终，老板娘表示相逢是缘，送你们一件东极岛特产的啤酒。"
    jump .s28villa

label .s28villa:
    scene dj villa food with fade
    "终于开饭了，仍然是依照传统“大樱桃的饭和菜”，所有人都不准坐下，抢菜的气氛一度非常愉悦。"
    "酒虽不足，但煮的十五包方便面十分管饱，果然最后吃不完。"
    ## Not important
    menu:
        "于是你选择："
        "不如喂给他们家的斗牛犬狗不理！":
            "狗不理吃的很开心，但也只吃了一盆，还有半盆怎么办呢？"
            
        "不能浪费粮食，死撑也要撑进去！":
            $ dunhuang_value += 10
            "你们又端起碗继续吃，人多力量大，大家齐心协力把一盆分了，但还是剩下半盆。"
            
        "唉，只能倒掉了，没办法":
            $ dunhuang_value -= 10
            
    "唉没办法，只能倒掉了，可惜就可惜了。大家平时在海底捞可不是这个样子……"
    "大家开始很自觉地刷锅洗碗收拾桌子，各司其职。"
    "昏暗的灯光下，你看到这种景象感觉很美好。"
    scene dj villa photo with fade
    "收拾完后已经十点半了，你们一起在桃旗前拍了合影。"
    play sound take_photo
    scene dj villa photo with phototake
    jump .s29villa

label .s29villa:
    if dj_withgirl:
        "其他人简短地开了个讨论会，讨论了一下船票的问题。"
        "听说他们来岛时被黑心代购坑惨了，差点就没有来成，最后还是在货舱里坐船上的岛。"
        "你内心很庆幸选择了和小茶一起，没和他们走同一个代购的途径。"
        "……"
        jump .s30villa

    pause 1
    "你们决定开一个全员讨论会，告知大家淘宝船票店家的情况。"
    "在下午，你告知了船票老板，这边码头不给退票的情况，他却咬死要求你们把多买的那几张票的尾款补齐，不然威胁返程可能会出问题。"

    lian"这件事还比较严重，可能必须得我们全员讨论才能做决定了。"
    conway"嗯，其实说起来也简单，两个选择"
    ## Not important
    menu:
        "这时你赞同哪一种呢？"
        "多花钱买平安，但出了不该出的钱，憋屈":
            $ dunhuang_value -= 20
            "但众人在各自发表看法之后，发现还是认为店家不敢动手脚的人居多。"
            "他们的理由也很有道理：台风即将来袭，如果他动手脚导致我们困在岛上，之后投诉他，甚至告他，他需要赔偿的就多了。"
            "于是你最终也赞同了这个观点。"

        "冒着风险，笃定他不敢在返程票上做手脚":
            $ dunhuang_value += 10
            "大部分人和你持有相同的观点：台风即将来袭，如果他动手脚导致我们困在岛上，之后投诉他，甚至告他，他需要赔偿的就多了。"
            
    "最终你们决定，跟老板说明情况，并以这个理由反威胁他，量他也不敢做手脚，之后不再接老板的电话。"
    stop music fadeout 2.0

label .s30villa:
    scene dj villa uno with dissolve
    play music excuse_me fadein 2.0
    "严肃的话题说完了，连南拿出祖传的两大盒UNO，这次有十几个人一起打，从来没有这么多过。"
    "都是熟练玩家了，游戏速度如同快了二倍速一般，完全应接不暇。"
    "不知过了多久，疯狂加四已经是老套路了，大家有点困了。"

    if dj_withgirl:
        me"对了，我记得上次淫淫说有个新玩法，我们可以试试！"
        jump .s30villa_tmp

    ## May jump story
    ## AutoSave 2-3
    python:
        renpy.take_screenshot()
        renpy.save("12-3", "UNO玩得有点困了……")

    menu:
        "这时你说："
        "我们大家去睡觉吧！":
            $ dunhuang_value -= 20
            "大家说你不行，看日出前喊你。"
            "于是你去睡觉了，直到第二天凌晨四点多被喊醒。"
            stop music fadeout 2.0
            jump dj_104.s39villa

        "对了，我记得上次淫淫说有个新玩法，我们可以试试！":
            pass

        "我们来换个活动，爱情保卫战吧！":
            jump .s31love

label .s30villa_tmp:
    yinyin"对对对，可可跟我说了个很有趣的玩法。"
    yinyin"就是，不能说“他她它”这三个字。"
    "你们觉得很有意思，开始进行游戏了！"
    ming"啊？啥啥意思啊？"
    conway"你真是个憨批，不管你"
    ## Not important
    menu:
        "于是你："
        "冠军好凶啊，还是给小明讲一下吧":
            me"就是，不能说“他她它”三个字。"
            "大家一起坏笑起来："
            "众人""冠军两张桃神三张！快摸！"
            "md原来小明在钓鱼！真是臭狗屎！"

        "冠军说得对，小明就是憨批":
            $ dunhuang_value += 10
            me"大家别管他，他就是憨批。"
            "大家一起坏笑起来："
            "众人""都要摸两张摸两张！哈哈哈哈……"
            "md原来小明在钓鱼！真是臭狗屎！"

        "虽然你也没太听懂规则，但还是默不作声吧……":
            $ dunhuang_value -= 10
            "于是淫淫又把规则讲了一遍。"
            "话音刚落，大家一起坏笑起来："
            "众人""摸三张摸三张！哈哈哈哈……"
            "原来小明在钓鱼。哈哈哈哈哈哈哈笑死我了我也想钓！"

    "欢声笑语中，大家都不敢说话，但又憋不住，随着大家手里的牌越来越多，全场笑作一片。"
    dan"坑爹小明，艾要明牌了！大家别看！"
    "艾是什么鬼？"
    "靠原来是英语啊……"
    "真是一场诡异的污诺局！牌组的牌都几乎快被大家拿在手上，甚至可以比谁牌多了。"

    if dj_withgirl:
        if dj_girl_opinion >= 40:
            jump dj_girl.gs12message

        else:
            jump dj_girl.gs17love
            
    else:
        jump .s31love

label .s31love:
    scene dj villa love1 with fade
    "渐渐地，大家都笑累了。"
    me"来搞爱情保卫战！"
    wqbh"啥叫爱情保卫战？"
    lian"大人讲话，小屁孩别插"
    ming"这回我要当主持人，上回在密云做嘉宾被那个谁的臭脚一直熏，太难顶了。"
    "纪念册开发组""插播一个广告：敬请关注大樱桃纪念册第二部——密云篇"
    han"我和诺诺是情感导师！"
    lian"灯光师！"
    wqbh"我要当配乐！"
    dan"那谁来做嘉宾呢？"
    nuo"那肯定是上回主持人做嘉宾嘛！"
    conway"喵喵喵？哪来的爱情？"
    shou"关你p事，你继续主持人吧"
    "大家一齐把目光投向了在角落自闭的小天。"
    stop music fadeout 2.0
    
    scene dj villa love2 with Fade(1.0, 0.3, 1.0)
    play music melody_of_night_3
    "大家安静围坐在房间里，聚光灯照在本次节目的两位主角——小茶和小天身上。"
    "舒缓的配乐响起，小茶低头羞涩一笑。"
    tea"啊？主角是我嘛……那你们想听什么呢？"
    ## May jump story
    ## AutoSave 2-4
    python:
        renpy.take_screenshot()
        renpy.save("12-4", "你想听小茶讲什么呢？")

    menu:
        "你想听："
        "夏日限定心动之男生都和我告白怎么办":
            jump .s32summer
            
        "大学恋爱初体验之哥哥旧爱我都要":
            tea"哎，我还是按照时间顺序先讲暑假的故事吧，要不然前因后果对不上。"
            jump .s32summer

        "晚安，老子去睡觉了，你们都猝死吧，再见.jpg":
            $ dunhuang_value -= 20
            "于是你去睡觉了，后来众人告诉你你错过了许多精彩的故事……"
            stop music fadeout 2.0
            scene black with fade
            jump dj_104.s39villa

label .s32summer:
    "安静的房间里，小茶开始了她的讲述……"
    scene bg love summer with fade
    tea"""
    刚加入这个精英校友组织的时候，同届的伙伴里除了我之外还有两个男孩子，分别是小殷和小陶。
    
    经历了宣讲招生开课等一系列忙碌，我们三个之间的关系越来越紧密，经常聊天到深夜，讨论的内容也从工作相关逐渐转向其他……
    
    小殷帅气能干，小陶温柔细心，他们俩对我来说都是亲人一样的存在。
    
    但就在这时，单纯的感情逐渐发生了变化……
    """
    ## Not important
    menu:
        "如果是你，会期待谁的表白呢？"
        "帅气能干的小殷":
            call .s33ying from _call_dj_103_s33ying
            "众人""那小陶为什么告白呢？"
            call .s34tao from _call_dj_103_s34tao
            jump .s35campus

        "温柔细心的小陶":
            call .s34tao from _call_dj_103_s34tao_1
            "众人""那这另一个身影是小殷了？"
            tea"嗯……"
            call .s33ying from _call_dj_103_s33ying_1
            jump .s35campus
            
        "小孩子才做选择，成年人全都要":
            $ dunhuang_value += 20
            tea"哎，谁说不是呢。我先说小殷吧。"
            call .s33ying from _call_dj_103_s33ying_2
            "众人""那小陶为什么告白呢？"
            call .s34tao from _call_dj_103_s34tao_2
            jump .s35campus


label .s33ying:
    scene bg love ying with fade
    tea"""
    在日常工作中遇到的难题，我常常向小殷请教。
    
    虽然因为我们俩经验不足，最后往往都要求助于学长，但是一路互相扶持互相依靠，让我们的关系越来越近。
    
    他略带宠溺地叫我小傻瓜，我红着脸低下头：“猪猪就是笨了点嘛，但是猪猪会努力的！”
    
    抬起头时刚好碰上他没有收回的目光，他含情脉脉地望着我，说：“你是我见过最清纯的女孩……”
    
    我和他约好，在大学里再开始正式恋爱。
    
    然而，小陶突然的告白也让我不知所措，这个在我心里一直是弟弟一样重要的男孩好像突然长大了……
    """
    ## Not important
    menu:
        "此刻你的反应是："
        "这茶味道不错":
            tea"什么茶？"
            me"没什么没什么你继续讲"

        "你真是个美好善良的女孩子":
            $ dunhuang_value -= 10
            tea"谢谢，但我真的很苦恼"

        "我也想和学妹谈恋爱":
            $ dunhuang_value += 10
            "众人""学妹？哪有学妹？你给我找一个？"
    return # must return to call point

label .s34tao:
    scene bg love tao with fade
    tea"""
    因为工作交流，我和小陶在qq上经常聊到深夜。
    
    他有时和我讲起自己烦心事，我总是温柔地鼓励他：“你真的是个很好的男孩子呢，肯定会有很多优秀的女孩子喜欢你的，以后会有更好的女孩子陪你，
    {w}不像我这么笨，只能听你讲，也帮不了什么忙。”
    
    小陶回复：“其实你在我心里一直是最好的女孩，我喜欢你。”
    
    我不知所措，因为心里已经完全被另一个身影占领……
    
    我辗转难眠许久，终于回复他：“也许是我们缘分不够，但你在我心里依然特别，就像是我的弟弟，让我们一直做彼此最重要的人吧……”
    """
    ## Not important
    menu:
        "此刻你的反应是："
        "这茶味道不错":
            tea"什么茶？"
            me"没什么没什么你继续讲"

        "你真是个美好善良的女孩子":
            $ dunhuang_value -= 10
            tea"谢谢，但我真的很苦恼"

        "我也想和学妹谈恋爱":
            $ dunhuang_value += 10
            "众人""学妹？哪有学妹？你给我找一个？"
    return # must return to call point


label .s35campus:
    scene dj villa love2 with fade
    "众人""那另外一个故事呢？"
    tea"在那个暑假里，我也认识了很多别的男孩子，他们都和我关系很好，其中包括一位学长……"
    "众人""学长？"
    tea"""
    嗯...小天学长真的好耐心好温柔，我不会做海报，也不会写推送，不论我的问题有多傻，每次问他他都特别特别耐心地教我。
    
    渐渐地，在工作以外，我和他也时常聊天，以至于无话不谈。

    但我还是放不下小殷，那段时间衔接班开课了，我和他每天都要坐班。
    
    我们经常坐在教室后面聊一天，我们聊生活的一切，他知道我的所有，我也知道他的所有，我好像遇到了世界上另一个自己……

    可是我没想到，八月份开始军训以后，他突然对我冷淡了很多。
    
    我给他发消息，他总是过很长时间才回一两句，有时候甚至第二天才草草敷衍，而我却在屏幕另一端等得心力交瘁……
    
    最开始我以为我说错了话或者做错了事让他生气了，可是问他他却说我没错……
    
    他说，对不起，我们还是做回普通朋友吧。
    
    我当时快要崩溃了，我问他为什么，他说他也许没有他以为的那么喜欢我。
    
    于是，我们的恋爱还没有开始，就这么分手了……

    就在我非常绝望的时候，哥哥就像一束光照亮了我的世界，但我后来才意识到，他一直都在的。
    
    我们无话不谈，上课下课、教室寝室、白天黑夜，他就像一直陪伴着我，虽然他并不在南京……
    
    哥哥手把手教我面对大学里遇到的一切困难。我一直很要强，跟班上男同学关系都很好，但不知道为什么总有一些女生时常说我坏话，我跟爸妈、老师说，他们却总说一定是我不对。
    
    但哥哥不一样，他永远都站在我一边，理解我的小情绪，也支持我做的一切。他的安慰是那么的恰到好处，我好像遇到了世界上另一个自己……
    
    后来你们计划来东极岛玩，他问我要不要一起来散散心，所以这次我就跟他来了。

    ……
    """

label .s37love:
    nuo"你觉得这是爱情吗？"
    tea"我觉得更像是亲情，他就跟哥哥一样爱护我。"
    nuo"但他不这样觉得。"
    ming"下面有请男嘉宾发言："
    tian"熔化的柏油马路冒着丝丝热气，我行走在北街后的小巷上，我遇到了一个撑伞的姑娘……"
    tea"我没撑伞！"
    tian"我又没说是你！她撑着一把油纸伞，在那小巷的尽头，彷徨着，我看着那凄美的背影...扭头走了。"
    tian"我走进了晓宇火锅店，然后我坐在桌子旁边，拿起了我的筷子，我夹起一片牛肉，放在锅里，看着那沸腾的油汤，变成一成熟，变成两成熟，变成三成熟……"
    "众人""？？？"
    ming"说重点，你是怎么看待你们这段关系的？"
    tian"说起这个话题，一般来讲，我们都必须慎重的考虑考虑。这种事实对本人来说意义重大，相信对这个世界也是有一定意义的。本人也是经过了深思熟虑，在每个日日夜夜思考这个问题。"
    conway"？？？再说废话你的女嘉宾要被其他男嘉宾抢走了。"
    han"就一句话吧，你怎么看待这段关系？"
    tian"她一直觉得我是她的哥哥，但我是真的喜欢她。"
    han"那你不会觉得这样很卑微吗？"
    tian"我不在乎，只要她开心，这就够了。这次真的她来东极岛是想散散心的，她本来就情绪不太好，我也想陪陪她。"
    conway"下面请情感导师诺诺同学向女嘉宾提问："
    nuo"小茶，你会觉得对不起小天吗？"
    tea"我没有想太多，我只是单纯觉得哥哥真的很好，就像亲人一样。"
    nuo"那你觉得之后有可能在一起吗？"
    tea"……"
    tian"这个问题我替她回答吧，我们之前也聊起过这个话题，我也不奢望之后能和她在一起，我也尊重她最后的决定。"
    tian"还是那句话，我不在乎，只想要她开心。"
    nuo"小茶，你知道这样对小天很不公平吗？"
    tian"我知道你们是什么意思，只索取不付出确实听起来很像备胎，但她不是这样的，我不这样觉得，我觉得人生在世需要一段感情寄托。"
    conway"女嘉宾能回答这个问题吗？"
    tea"我真的没有想过，我只觉得两个人都开心不就好了。{w}但我也一直没有接受过哥哥物质上的礼物，而且我也非常希望他能找一个别的女孩子，我真的只把他当哥哥。"
    han"我不接受，我觉得所有异姓兄妹都是扯淡。"
    nuo"而且你说你一直没有物质上的接受，但我觉得情感上的接受其实更过分，让对方产生对未来的幻想。"
    tea"但我真的跟他说的很清楚，我还在等小殷，我会等他三年。"
    "众人""……"
    conway"那其实...可能跟我们最近几天观察的结果不太一样..."
    nuo"我们这个活动也不是为了撮合或者拆散，只是想作为旁观者的提问，能提醒在身在其中的两个人。"
    nuo"那如果你们都觉得在这段关系中所收获，那我们觉得也可以了吧..."
    "小茶无辜的眼睛里浮上一层水雾，她低下头，双肩轻轻耸动，突然拉开房门头也不回地冲了出去。小天紧紧跟上，两人先后没入黑暗里..."
    
    stop music fadeout 2.0
    scene black with fade
    "房间里陷入一阵短暂的沉寂。"
    lian"我们这样逼问是不是有点凶？"
    nuo"但小天明明就是被绿茶蒙蔽了双眼，我们作为朋友不应该把他打醒吗！"
    conway"这咋打醒呢..."
    han"确实困难……我们也不好说啥。"
    ming"早晚摔跤！"
    "……""……"
    jump dj_104.s38villa