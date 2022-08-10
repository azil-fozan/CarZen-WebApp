function load_services(page=1){
    var user_id = $('#user_id').val(),
        search_str = $('#sevice_history_search_string').val();

    $.ajax({
        url: window.location.pathname,
        method: 'POST',
        dataType: 'json',
        data: {
            search_str: search_str,
            csrfmiddlewaretoken: window.csrfToken
        },
        beforeSend: function () {
            $('.loader').show();
        },
        success: function (resp) {
                if (resp.success) {
                    $('.service_table_body').html(resp.table_rows_html)
                    // show_snackbar_message(resp.message, 'success',  'center');
                } else {
                    show_snackbar_message(resp.message, 'warning',  'center');
                }
        },
        error: function (resp) {
            show_snackbar_message('Something went wrong.', 'error', 'center');
        },
        complete: function () {
             $('.loader').hide();
        }
    });
}


$(document).ready(function () {
    load_services(1);
    $(document).on('submit', '#search_sevice_history', function (e) {
        e.preventDefault();
        load_services();
    });
    $(document).on('keyup', '#sevice_history_search_string', function (e) {
        if (!$(this).val().length){
            $('.cancel-search').click();
        }
    });
});