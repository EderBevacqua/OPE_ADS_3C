$(document).ready(function() {
    setTimeout(function() {
        $('#mensagens').hide();
    }, 2500);

    $('#datetimepicker1').DateTimePicker();

    $('#datetimepicker2').DateTimePicker();

    
});

function soEquip() {
    document.getElementById("chooseUser").style.display = "none";
    document.getElementById("chooseEquip").style.display = "block";
}


function soUser() {
    document.getElementById("chooseEquip").style.display = "none";
    document.getElementById("chooseUser").style.display = "block";
}
