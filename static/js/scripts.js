$(document).ready(function() {
    setTimeout(function() {
        $('#mensagens').hide();
    }, 2500);

    $('#datetimepicker1').datetimepicker({
        autoclose: true,
        format: 'd/m/Y H:i',
        lang: 'pt-BR'
    });

    $('#datetimepicker2').datetimepicker({
        autoclose: true,
        format: 'd/m/Y H:i',
        lang: 'pt-BR'
    });


});

function soEquip() {
    document.getElementById("chooseUser").style.display = "none";
    document.getElementById("chooseEquip").style.display = "block";
}


function soUser() {
    document.getElementById("chooseEquip").style.display = "none";
    document.getElementById("chooseUser").style.display = "block";
}
