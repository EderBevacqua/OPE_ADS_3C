$(document).ready(function () {
    setTimeout(function () {
        $('#mensagens').hide();
    }, 2500);

    $('#password-eye').on('touchstart mouseenter', function () {
        $(this).removeClass("fa-eye-slash").addClass("fa-eye");
        $('#senha').attr('type', 'text');
        $('#senha').attr('data-type', 'text');

    });

    $('#password-eye').on('mouseleave', function () {
        $(this).removeClass("fa-eye").addClass("fa-eye-slash");
        $('#senha').attr('type', 'password');
        $('#senha').attr('data-type', 'password');

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