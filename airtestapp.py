# -*- encoding=utf8 -*-
__author__ = "Administrator"

from airtest.core.api import *

auto_setup(__file__)
start_app("com.yigongla.xflwl2017")

wait(Template(r"shortwork.png", record_pos=(-0.333, 0.068), resolution=(720, 1280)))

# 首页UI检查点
assert_exists(Template(r"tpl1558668082937.png", record_pos=(-0.336, -0.006), resolution=(720, 1280),target_pos=7), "短工招聘icon")

assert_exists(Template(r"tpl1558668124278.png", record_pos=(-0.006, -0.013), resolution=(720, 1280)), "平台活动icon")


assert_exists(Template(r"tpl1558668158173.png", record_pos=(0.335, -0.015), resolution=(720, 1280)), "易工头条icon")

assert_exists(Template(r"tpl1558668209531.png", record_pos=(-0.424, -0.233), resolution=(720, 1280)), "易工头条")

assert_exists(Template(r"tpl1558668239019.png", record_pos=(0.419, -0.235), resolution=(720, 1280)), "易工头条查看更多")

assert_exists(Template(r"tpl1558668269357.png", record_pos=(-0.39, 0.235), resolution=(720, 1280)), "全部职位")

assert_exists(Template(r"tpl1558668282813.png", record_pos=(0.353, 0.207), resolution=(720, 1280)), "对最新和最近排序")

assert_exists(Template(r"tpl1558669560176.png", record_pos=(0.008, 0.811), resolution=(720, 1280)), "底部找工布局")


assert_exists(Template(r"tpl1558668325444.png", record_pos=(-0.336, 0.811), resolution=(720, 1280)), "底部找工icon已选中")

assert_exists(Template(r"tpl1558668343628.png", record_pos=(0.004, 0.815), resolution=(720, 1280)), "底部消息icon未选中")

assert_exists(Template(r"tpl1558668378976.png", record_pos=(0.329, 0.811), resolution=(720, 1280)), "底部个人中心icon未选中")

# 消息UI检查点

touch(Template(r"tpl1558668629842.png", record_pos=(0.003, 0.814), resolution=(720, 1280)))

wait(Template(r"tpl1558668649010.png", record_pos=(-0.007, -0.771), resolution=(720, 1280)))

assert_exists(Template(r"tpl1558668669273.png", record_pos=(0.0, -0.772), resolution=(720, 1280)), "消息页面title:消息")

assert_exists(Template(r"tpl1558669531912.png", record_pos=(-0.003, -0.574), resolution=(720, 1280)), "三大功能布局")

assert_exists(Template(r"tpl1558668695968.png", record_pos=(-0.333, -0.567), resolution=(720, 1280)), "谁看过我icon")

assert_exists(Template(r"tpl1558668725998.png", record_pos=(0.003, -0.575), resolution=(720, 1280)), "平台消息icon")

assert_exists(Template(r"tpl1558668744250.png", record_pos=(0.332, -0.579), resolution=(720, 1280)), "交易消息icon")

assert_exists(Template(r"tpl1558669504431.png", record_pos=(0.008, 0.812), resolution=(720, 1280)), "底部消息布局")

assert_exists(Template(r"tpl1558668772584.png", record_pos=(-0.333, 0.808), resolution=(720, 1280)), "底部找工icon未选中")

assert_exists(Template(r"tpl1558668799773.png", record_pos=(0.001, 0.814), resolution=(720, 1280)), "底部消息icon已选中")

assert_exists(Template(r"tpl1558668821956.png", record_pos=(0.336, 0.815), resolution=(720, 1280)), "底部个人中心icon未选中")


# 个人中心UI检查点
touch(Template(r"tpl1558668929944.png", record_pos=(0.333, 0.815), resolution=(720, 1280)))

wait(Template(r"tpl1558668960168.png", record_pos=(-0.382, 0.0), resolution=(720, 1280)))


assert_exists(Template(r"tpl1558669158273.png", record_pos=(-0.224, -0.682), resolution=(720, 1280)), "个人信息显示布局")


assert_exists(Template(r"tpl1558668996312.png", record_pos=(-0.369, -0.674), resolution=(720, 1280)), "有边框的头像")

assert_exists(Template(r"tpl1558669023762.png", record_pos=(-0.103, -0.674), resolution=(720, 1280)), "名称+电话+未认证标签")

assert_exists(Template(r"tpl1558669193173.png", record_pos=(-0.008, -0.439), resolution=(720, 1280)), "易工信用、易工币、余额布局")

assert_exists(Template(r"tpl1558669068975.png", record_pos=(-0.331, -0.465), resolution=(720, 1280)), "易工信用")

assert_exists(Template(r"tpl1558669089257.png", record_pos=(0.0, -0.463), resolution=(720, 1280)), "易工币")

assert_exists(Template(r"tpl1558669103409.png", record_pos=(0.335, -0.471), resolution=(720, 1280)), "余额")


assert_exists(Template(r"tpl1558669256497.png", record_pos=(0.003, -0.208), resolution=(720, 1280)), "常用服务布局")

assert_exists(Template(r"tpl1558669131699.png", record_pos=(-0.329, -0.206), resolution=(720, 1280)), "我的简历")

assert_exists(Template(r"tpl1558669281650.png", record_pos=(0.001, -0.208), resolution=(720, 1280)), "申请记录")

assert_exists(Template(r"tpl1558669295357.png", record_pos=(0.336, -0.208), resolution=(720, 1280)), "我的收藏")

assert_exists(Template(r"tpl1558669325467.png", record_pos=(-0.017, 0.114), resolution=(720, 1280)), "我的服务布局")

assert_exists(Template(r"tpl1558669339053.png", record_pos=(-0.374, 0.164), resolution=(720, 1280)), "邀请有奖")

assert_exists(Template(r"tpl1558669359240.png", record_pos=(-0.122, 0.165), resolution=(720, 1280)), "反馈教程")

assert_exists(Template(r"tpl1558669374665.png", record_pos=(0.126, 0.169), resolution=(720, 1280)), "客服中心")

assert_exists(Template(r"tpl1558669385530.png", record_pos=(0.375, 0.163), resolution=(720, 1280)), "设置")

assert_exists(Template(r"tpl1558669416813.png", record_pos=(0.008, 0.815), resolution=(720, 1280)), "个人中心底部布局")

assert_exists(Template(r"tpl1558669397013.png", record_pos=(-0.335, 0.811), resolution=(720, 1280)), "底部找工icon未选中")

assert_exists(Template(r"tpl1558669447215.png", record_pos=(-0.004, 0.812), resolution=(720, 1280)), "底部消息icon未选中")

assert_exists(Template(r"tpl1558669465278.png", record_pos=(0.336, 0.811), resolution=(720, 1280)), "底部个人中心icon已选中")

sleep(1)
stop_app("com.yigongla.xflwl2017")


