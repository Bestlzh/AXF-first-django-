$(function () {

    var url1 = 'http://127.0.0.1:8000/axf/addchangecart/';
    $('.addgoods').click(function () {
        // $(this).parent().find('.redgoods').css('display', 'block');
        // $(this).parent().find('.goodsnum').css('display', 'block');
        pid = this.getAttribute("ga");
        console.log(pid)
        $.post(url1, {"productid": pid}, function (data) {

            if (data.status === "success") {
                //添加成功，把中间的span的innerHTML变成当前的数量

                document.getElementById(pid).innerHTML = data.data

                document.getElementById('allnum').innerHTML = data.allnum
                document.getElementById('allprice').innerHTML = data.allprice

                document.getElementById(pid+"price").innerHTML = data.price

            } else {

                window.location.href = "http://127.0.0.1:8000/axf/home/"

            }
        })
    })


var url2 = 'http://127.0.0.1:8000/axf/subchangecart/';

      $('.redgoods').click(function () {


        pid = this.getAttribute("ga");


        $.post(url2, {"productid": pid}, function (data) {

            if (data.status === "success") {


                document.getElementById(pid).innerHTML = data.data
                document.getElementById('allnum').innerHTML = data.allnum
                document.getElementById('allprice').innerHTML = data.allprice


                if (   data.data == '0') {
                         //整个物品消失
                         document.getElementById(pid+"li").style.display='none'
          }
                document.getElementById(pid+"price").innerHTML = data.price


            } else {

                window.location.href = "http://127.0.0.1:8000/axf/home/"

            }
        })
    })


})