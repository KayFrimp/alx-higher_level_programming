$(document).ready(function() {
    $('INPUT#btn_translate').click(function() {
	const langCode = $('INPUT#language_code').val();
	fetchAndPrintHello(langCode);
    });

    $('INPUT#language_code').keypress(function(e) {
	if (e.which == 13) {
	    const langCode = $('INPUT#language_code').val();
	    fetchAndPrintHello(langCode);
	}
    });

    function fetchAndPrintHello(langCode) {
	const url = `https://www.fourtonfish.com/hellosalut/?lang=${langCode}`;
	$.get(url, function(data, status){
	    $('DIV#hello').text(data.hello);
	});
    }
});
~
