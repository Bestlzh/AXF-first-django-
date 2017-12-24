$(document).ready(function(){
    document.documentElement.style.fontSize = innerWidth / 10 + "px";
})

$(function () {
    // alert('hahhahah')
    redallnum = $('#redallnum').html()
    // alert('hahahah')
    if (redallnum == 0){

        $('#redallnum').css('display','none')
    }

    else{
        $('#redallnum').css('display','block')

        }
})