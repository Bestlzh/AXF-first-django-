$(document).ready(function(){
    var name = document.getElementById("name")
    var nameerr = document.getElementById("nameerr")
    var checkerr = document.getElementById("checkerr")

    var pass = document.getElementById("pass")
    var passerr = document.getElementById("passerr")

    var passwd = document.getElementById("passwd")
    var passwderr = document.getElementById('passwderr')

    name.addEventListener("focus", function(){
        nameerr.style.display = "none"
        checkerr.style.display = "none"
    },false)

    name.addEventListener("blur", function(){
        instr = this.value
        if (instr.length < 6 || instr.length > 12){
            nameerr.style.display = "block"
            return
        }

        $.post("/checkuserid/", {"userid":instr}, function(data){
            if (data.status == "error"){
                checkerr.style.display = "block"
            }
        })
    },false)



    pass.addEventListener("focus", function(){
        passerr.style.display = "none"
    },false)
    pass.addEventListener("blur", function(){
        instr = this.value
        if (instr.length < 6 || instr.length > 16){
            passerr.style.display = "block"
            return
        }
    },false)


    passwd.addEventListener("focus", function(){
        passwderr.style.display = "none"
    },false)
    passwd.addEventListener("blur", function(){
        instr = this.value
        if (instr != pass.value){
            passwderr.style.display = "block"
        }
    },false)

})