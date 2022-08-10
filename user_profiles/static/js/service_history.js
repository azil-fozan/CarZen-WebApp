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


function close_ticket(This=1){
    // debugger;
    var row = This.closest('tr');
    var rating = row.find('input').val(),
        comments = row.find('textarea').val(),
        ticket_id = row.find('[name="service_ticket_number"]').val();

    $.ajax({
        url: '/dashboards/close_ticket/',
        method: 'POST',
        dataType: 'json',
        data: {
            ticket_id: ticket_id,
            rating: rating,
            comments: comments,
            csrfmiddlewaretoken: window.csrfToken
        },
        beforeSend: function () {
            $('.loader').show();
        },
        success: function (resp) {
                if (resp.success) {
                    $('#search_sevice_history').submit();
                    show_snackbar_message(resp.message, 'success',  'center');
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
    $(document).on('click', '.rate_and_close', function (e) {
        // $(this).append('<input class="form-control m-1" type="text" name="rating" />');
        $('<input class="form-control w-50" type="number" min="1" max="5" placeholder="1-5" name="rating" />').insertBefore($(this));
        $(this).text('Close');
        $(this).removeClass('rate_and_close');
        $(this).addClass('close_ticket');
    });
    $(document).on('click', '.close_ticket', function (e) {
        close_ticket($(this));
    });
});