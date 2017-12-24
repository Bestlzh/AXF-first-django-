

$(function () {

    //姓名格式
    $('#name').change(function () {
        var preUsername = $(this).val()
        if (preUsername.length > 12 || preUsername.length < 6 ){
            $('#nameerr').css('display','block')
        }
        else{
             $('#nameerr').css('display','none')

        }
        //判断用户名是否已经存在
        var url = 'http://127.0.0.1:8000/axf/checkusername/'
        $.post(url,{'username':preUsername},function (data){

             if ( data.status === "error"){
                $('#checkerr').css('display',"block")
            }
                else{
               $('#checkerr').css('display',"none")

            }
        })
    })

    //密码格式
    $('#pass').change(function () {
        var prePass = $(this).val()
        if (prePass.length < 6 || prePass.length > 20) {
            $('#passerr').css('display', 'block')
        }
        else {
            $('#passerr').css('display', 'none')

        }
    })


//    密码验证
       $('#passwd').change(function () {
            var prePasswd = $(this).val()
            var prePass = $('#pass') .val()
        if (prePass != prePasswd) {
            $('#passwderr').css('display', 'block')
        }
        else {
            $('#passwderr').css('display', 'none')

        }
    })




})
