const $ = window.$;
$(document).ready(function () {
    $('#btn_translate').click(function () {
        const lang = $('#language_code').val();
        $.get('https://www.fourtonfish.com/hellosalut/?lang=' + lang, function (data) {
        $('#hello').text(data.hello);
        });
    });
    $('#language_code').keypress(function (e) {
        if (e.which === 13) {
        $('#btn_translate').click();
        }
    });
    }
);
