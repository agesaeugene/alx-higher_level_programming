// Adding <li>Item</li> to UL.my_list when DIV#add_item is clicked
// Remove last element in UL.my_list when DIV#remove_item is clicked

const $ = window.$;
$(function () {
  const url = 'https://www.fourtonfish.com/hellosalut/hello/';
  $('input#btn_translate').click(function () {
    const lang = $('input#language_code').val();
    $('div#hello').text(lang);
    $.ajax({
      url: url,
      data: { lang: lang },
      success: function (response) {
        $('div#hello').text(response.hello);
      }
    });
  });
});
