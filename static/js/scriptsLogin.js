$(document).ready(function () {
    setTimeout(function () {
        $('#mensagens').hide();
    }, 2500);

    $('#show_password').hover(function (e) {
        e.preventDefault();
        if ($('#senha').attr('type') == 'password') {
            $('#senha').attr('type', 'text');
            $('#senha').attr('data-type', 'text');
            $('#show_password').attr('class', 'fa fa-eye');
        } else {
            $('#senha').attr('type', 'password');
            $('#senha').attr('data-type', 'password');
            $('#show_password').attr('class', 'fa fa-eye-slash');
        }
    });
});

function mask(o, f) {
    setTimeout(function () {
        var v = mphone(o.value);
        if (v != o.value) {
            o.value = v;
        }
    }, 1);
}

function mphone(v) {
    var r = v.replace(/\D/g, "");
    r = r.replace(/^0/, "");
    if (r.length > 10) {
        r = r.replace(/^(\d\d)(\d{5})(\d{4}).*/, "($1) $2-$3");
    } else if (r.length > 5) {
        r = r.replace(/^(\d\d)(\d{4})(\d{0,4}).*/, "($1) $2-$3");
    } else if (r.length > 2) {
        r = r.replace(/^(\d\d)(\d{0,5})/, "($1) $2");
    } else {
        r = r.replace(/^(\d*)/, "($1");
    }
    return r;
}