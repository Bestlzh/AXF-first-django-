$(function () {

    $(".Market .leftBox ul li .leftSmileBox").mouseenter(function () {
        $(this).css('background','orange');
    })

    $(".Market .leftBox ul li .leftSmileBox").mouseleave(function () {
        $(this).css('background','#f2eeff');
    })

    $(".Market .topNav .leftNav").click(function () {
        $('.leftChildType').css("display",'block');
        $('.rightOrder').css('display','none')
    })

    $(".leftChildType").click(function () {
        $(this).css('display','none')

    })


    $(".Market .topNav .rightNav").click(function () {
        $('.leftChildType').css("display",'none');
        $('.rightOrder').css('display','block')
    })

    $(".rightOrder").click(function () {
        $(this).css('display','none')

    })


    //增加购物车商品
    var url1 = 'http://127.0.0.1:8000/axf/addchangecart/';
    $('.addgoods').click(function () {

        pid = this.getAttribute("ga");
        console.log(pid)
        $.post(url1, {"productid": pid}, function (data) {

            if (data.status === "success") {

                document.getElementById(pid).innerHTML = data.data
                document.getElementById(pid).style.display = 'block'
                document.getElementById(pid+'redgoods').style.display = 'block'
                document.getElementById('redallnum').innerHTML = data.allnum

            } else {

                window.location.href = "http://127.0.0.1:8000/axf/login/"

            }
        })
    })



        //减

        var url2 = 'http://127.0.0.1:8000/axf/subchangecart/';

      $('.redgoods').click(function () {

        pid = this.getAttribute("ga");
        console.log(pid)
        $.post(url2, {"productid": pid}, function (data) {

            if (data.status === "success") {

                document.getElementById(pid).innerHTML = data.data
                if (data.data == 0){
                    document.getElementById(pid + 'redgoods').style.display='none'
                    document.getElementById(pid).style.display='none'
                }
                document.getElementById('redallnum').innerHTML = data.allnum


            } else {

                window.location.href = "http://127.0.0.1:8000/axf/login/"

            }
        })
    })




})