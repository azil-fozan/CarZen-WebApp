SELECT_RATING_OPTIONS = `<select class="form-control" style="min-width: 60%" name="rating">
                            <option value="1">1</option>
                            <option value="2">2</option>
                            <option value="3">3</option>
                            <option value="4">4</option>
                            <option selected value="5">5</option>
                         </select>`;

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


function close_ticket(This){
    var row = This.closest('tr');
    var rating = row.find('select').val(),
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


function approve_cancel_appointment(This, option='approve'){
    var row = This.closest('tr');
    var ticket_id = row.find('[name="service_ticket_number"]').val();
    var estimated_cost = 0
    if (row.find('[name="estimated_cost"]').length){
        estimated_cost = row.find('[name="estimated_cost"]').val();
        if (estimated_cost===""){
            return show_snackbar_message("You can not approve without estimate", 'warning',  'center');
        }
    }

    $.ajax({
        url: '/dashboards/approve_cancel_appointment/',
        method: 'POST',
        dataType: 'json',
        data: {
            ticket_id: ticket_id,
            option: option,
            estimated_cost: estimated_cost,
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
        $($.parseHTML(SELECT_RATING_OPTIONS)).insertBefore($(this));
        $(this).text('Close');
        $(this).removeClass('rate_and_close');
        $(this).addClass('close_ticket');
    });
    $(document).on('click', '.close_ticket', function (e) {
        close_ticket($(this));
    });
    $(document).on('click', '.approve_appointment', function (e) {
        approve_cancel_appointment($(this), "approve");
    });
    $(document).on('click', '.cancel_appointment', function (e) {
        approve_cancel_appointment($(this), "reject");
    });
});