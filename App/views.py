import random
import time

import os
from django.conf import settings
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from App.models import *




def home(request):
    # 轮播
    wheelList = Wheel.objects.all()
    # 导航
    navList = Nav.objects.all()
    #必买
    mustBuyList = MustBuy.objects.all()
    #下面的十一个
    shop = Shop.objects.all()
    shop1 = shop[0:1]
    shop2 = shop[1:3]
    shop3 = shop[3:7]
    shop4 = shop[7:11]

    # 下面重复的菜单
    mainshowList =  MainShow.objects.all()

    # 下面的红色的物品数目
    user = request.COOKIES.get('user')
    if user != None:
        redallnum = 0
        goodsnums = Cart.objects.filter(userName=user)
        for i in goodsnums:
            redallnum = int(redallnum) + int(i.productnum)

    else:
        redallnum = 0
    context = {'pageTitle':'主页','wheelList':wheelList,'navList':navList,'mustBuyList':mustBuyList,
               "shop1":shop1,'shop2':shop2,'shop3':shop3,'shop4':shop4,
               'mainshowList':mainshowList,'redallnum':redallnum}
    return render(request,'App/Home.html',context)


def market(request):
    # 获取所有类型
    foodtypes = FoodType.objects.all()
    # 获取列表商品
    goodsList = Goods.objects.all().filter(productnum = '4')

    # context = {'pageTitle':'闪送','foodtypes':foodtypes,'goodsList':goodsList}


    # print(len(goodsList))
    context = {'pageTitle':'闪送','foodtypes':foodtypes,'goodsList':goodsList}
    return render(request, 'App/Market.html',context)





# 筛选物品

def marketCategory(request,foodtype,childcid,ordering):
    # 获取所有类型
    foodtypes = FoodType.objects.all()
    # 获取列表商品
    # goodsList = Goods.objects.all().filter(categoryid=foodtype)
    user = request.COOKIES.get('user')
    #让闪购页面显示购物车中物品数量
    catGoods = Cart.objects.filter(userName=user)
    # 下面的红色的物品数目
    if user != None:

        redallnum = 0
        goodsnums = Cart.objects.filter(userName=user)

        for i in goodsnums:

            redallnum = int(redallnum) + int(i.productnum)

        print(redallnum)

    else:
        redallnum = 0

    foodid = foodtype

    if ordering == '0':
        orderRule = 'id'
    elif ordering == '1':
        orderRule = 'price'
    elif ordering == '2':
        orderRule = '-price'
    elif ordering == '3':
        orderRule = 'storenums'
    else:
        orderRule = 'id'

    if childcid == '0':
        goodsList = Goods.objects.all().filter(categoryid=foodtype).order_by(orderRule)
    else:
        goodsList = Goods.objects.all().filter(categoryid=foodtype).filter(childcid=childcid).order_by(orderRule)


        # 让闪购页面显示购物车中物品数量,还没实现
    # catGoods = Cart.objects.filter(userName=user)
    # numlist = []
    # print('购物车物品',catGoods)
    # print('闪购物品',goodsList)
    # if user != None:
    #     for i in catGoods:
    #         for j in goodsList:
    #             if j.productid == i.productid:
    #                 numlist.append({i.productid:i.productnum})
    #
    # print(numlist)



    childTypes = FoodType.objects.all().filter(typeid=foodtype).first().childtypenames.split('#')
    # print(childTypes)
    item = []
    for childs in childTypes:
        # print(childs)
        Child = childs.split(":")
        oneChild = {'childName':Child[0],'childTypeId':Child[1]}
        # print(oneChild)
        item.append(oneChild)
    # print(item)
    context = {'pageTitle':'闪送','foodtypes':foodtypes,'goodsList':goodsList,'items':item,'foodtypeid':foodtype,'orderRule':ordering,'childcid':childcid,'foodid':foodid,'redallnum':redallnum,}
    return render(request, 'App/Market.html',context)






def mine(request):

    redallnum = 0
    username = request.COOKIES.get("user")
    if username == None:
        username = '未登录'
        redallnum = 0
        imgpath = User.objects.filter(userName='lizihao').first().userImg

    # 下面的红色的物品数目
    else:
        goodsnums = Cart.objects.filter(userName=username)
        for i in goodsnums:
            redallnum = int(redallnum) + int(i.productnum)

        # 头像
        imgpath = '/'+User.objects.filter(userName=username).first().userImg
        print('111111111111111111111111111111')
        print(imgpath)
        imgs = imgpath.split('/')
        img = imgs[1] +'/' +imgs[2]
        print(img)

    return render(request, 'App/Mine.html', {'img':imgpath,"pageTitle":"我的","username":username,'redallnum':redallnum,})

def login(request):
    return render(request,'App/Login.html')

# 登录
def dologin(request):
    username = request.POST.get('username')
    userpassword = request.POST.get('userpassword')
    user = User.objects.filter(userName=username).first()
    if user == None:
        response = HttpResponseRedirect(reverse('axf:error'))

        return response
    else:
        if  userpassword == user.userPasswd:

            # request.session['user'] = username

            response = HttpResponseRedirect(reverse('axf:mine'))

            response.set_cookie('user', username)

            return response
        else:
            response = HttpResponseRedirect(reverse('axf:error'))

            return response


# 退出
def quit(request):
    response = HttpResponseRedirect(reverse('axf:mine'))
    response.delete_cookie('user')
    return response


def register(request):
    return render(request, 'App/Register.html')


# 注册
def doregister(request):
    if request.method == "POST":
        userName = request.POST.get("userName")
        userPasswd  = request.POST.get("userPass")
        userPhone   = request.POST.get("userPhone")
        userAdderss = request.POST.get("userAdderss")
        userRank    = 0
        # token = time.time() + random.randrange(1, 100000)
        # userToken = str(token)
        f = request.FILES["userImg"]
        userImg = os.path.join(r'static/uploadfile/', userName + ".png")
        with open(userImg, "wb") as fp:
            for data in f.chunks():
                fp.write(data)

        user = User.createuser(userName,userPasswd,userPhone,userAdderss,userImg,userRank)
        user.save()

        # request.session["username"] = userName
        # request.session["token"] = userToken

        return HttpResponseRedirect(reverse('axf:success'))
    else:
        return render(request, 'App/Register.html', {"pageTitle":"注册"})


# 验证用户名
def checkusername(request):
    username = request.POST.get("username")
    user = User.objects.filter(userName = username)
    if len(user) == 0:
        context =  { "status": "success"}
    else:
        context = {'status':'error'}

    return JsonResponse(context)


def success(request):
    return render(request,'App/Success.html')


def error(request):
    return render(request,'App/Error.html')

# 购物车
def cart(request):
    user = request.COOKIES.get("user")
    if user != None:


        # print('aaaaaa',cartslist)
        # 去除数目为0的   不知道为什么数目为0  还能存进去
        c = Cart.objects.filter(productnum= 0)
        for i in c:
            i.delete()
        cartslist = Cart.objects.filter(userName=user)
        allprice = 0   #设置购物车最后的物品总数量，和总价格
        allnum = 0
        for i in cartslist:
            allprice = float(allprice) + float(i.productprice)
            allnum = allnum + int(i.productnum)
        cartslist = Cart.objects.filter(userName=user)
        context = {"pageTitle": "购物车", "cartslist": cartslist,'allnum':allnum,'allprice':allprice }
        return render(request, 'App/Cart.html',context)
    # 'allprice': allprice, 'allnum': allnum
    else:
        return  render(request,'App/Login.html')

# 增加购物车数据库
def addchangecart(request):
    # cartlist = []
    user = request.COOKIES.get('user')
    if user==None:
        return render(request, 'App/Login.html')
    # print(user)
    productid = request.POST.get("productid")
    # print('qqqqqqqqqqqq',productid,type(productid))
    product = Goods.objects.filter(productid=productid).first()

    cartslist = Cart.objects.filter(userName=user)
    allprice = 0   #设置购物车最后的物品总数量，和总价格
    allnum = 0
    for i in cartslist:
        allprice = float(allprice) + float(i.productprice)
        allnum = allnum + int(i.productnum)


    carts = Cart.objects.filter(userName=user).filter(productid=productid)
    # if flag == 0:
    if carts.count() == 0:
        c = Cart.createcart(user,productid,1,product.price,True,product.productimg,product.productlongname,False)
        c.save()
    else:
        # try:
        c = carts.filter(productid = productid).first()
        #修改数量和价格
        c.productnum += 1
        c.productprice = "%.2f"%(float(product.price) * c.productnum)
        c.save()
        # except Cart.DoesNotExist as e:
        #     # 直接增加一条订单
        #     c = Cart.createcart(user, productid, 1, product.price, True, product.productimg,product.productlongname, False)
        #     c.save()

    cartslist = Cart.objects.filter(userName=user)
    allprice = 0  # 设置购物车最后的物品总数量，和总价格
    allnum = 0
    for i in cartslist:
        allprice = float(allprice) + float(i.productprice)
        allnum = allnum + int(i.productnum)

    return JsonResponse({"data":c.productnum, "price":c.productprice,"status":"success",'allprice':allprice,'allnum':allnum})



# 减少数据库
def subchangecart(request):
    user = request.COOKIES.get('user')
    # print(user)
    productid = request.POST.get("productid")
    # print('qqqqqqqqqqqq',productid,type(productid))
    product = Goods.objects.filter(productid=productid).first()
    carts = Cart.objects.filter(userName=user).filter()

    c = carts.filter(productid = productid).first()
    if c.productnum >= 1:
        c.productnum -= 1
        c.productprice ="%.2f"%(float(product.price) * c.productnum)
        c.save()
    elif c.productnum == 0:
        c.delete()
    else:
        c.delete()

    cartslist = Cart.objects.filter(userName=user)
    allprice = 0  # 设置购物车最后的物品总数量，和总价格
    allnum = 0
    for i in cartslist:
        allprice = float(allprice) + float(i.productprice)
        allnum = allnum + int(i.productnum)

    return JsonResponse({"data":c.productnum, "price":c.productprice,"status":"success",'allprice':allprice,'allnum':allnum})

