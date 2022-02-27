SNACKBAR_TYPE_COLORS = {
    'error': '#800000',
    'success': '#006600',
    'warning': '#CCCC00',
    'none': '#333',
};
NO_RECORD_FOUND_ROW_HTML = `<tr>
                                <td class="no_date_row text-center text-danger" colspan="100%">No Records found</td>
                            </tr>`;

function get_url_params() {
    var url = location.href,
        params_dict = {};
    if (url.includes('?')) {
        var params_string = url.split('?')[1],
            params_list = params_string.split('&');
        params_list.forEach(function (param) {
            param = param.split('=');
            params_dict[param[0]] = param[1];
        });
    }
    return params_dict;
}

function show_snackbar_message(message='Test Text', type='none', position='left', timeout=2000) {
    var snackbar = $('#snackbar'),
        _timeout = timeout,
        _position = position;
    snackbar.addClass('show');
    snackbar.addClass(position);
    snackbar.text(message);
    snackbar.css('background-color', SNACKBAR_TYPE_COLORS[type]);
    setTimeout(function(){
        snackbar.removeClass('show');
        snackbar.removeClass(_position);
    }, _timeout);
}

$(document).ready(function(){
    $('[data-toggle="tooltip"]').tooltip();
    $('.selectpicker').selectpicker();
    $(document).on('keyup', '.header-search', function (e) {
        if ($(this).val().length){
            $('.cancel-search').show();
        } else {
            $('.cancel-search').hide();
            // $(this).closest('form').submit();
        }
    });
    $(document).on('click', '#go_to_last_page', function (e) {
        history.back();
    });
    $(document).on('click', '.cancel-search', function (e) {
        $(this).parent().find('input').val('');
        $(this).parent().submit();
        $(this).hide();
    });
});
