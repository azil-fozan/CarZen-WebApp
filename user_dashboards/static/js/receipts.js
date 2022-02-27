var receipt_form_html = `<form class="form-inline w-100 mb-3 d-flex justify-content-start create_receipt">
                            <customer_list_here>
                            <input class="form-control form-style mr-3" name="due_date" placeholder="Due Date" type="date" required>
                            <span>
                                <button type="submit">
                                    <i class="fas fa-check" style="color:Green;"></i>
                                </button>                            
                                <button class="cancel_create_receipt">
                                    <i class="fas fa-times" style="color:Red;width: 20px;height: 20px;"></i>
                                </button>
                            </span>
                       </form>`;
function render_receipt_rows(rows) {
    var row_html = '';
    if (rows.length) {
        rows.forEach(function (row) {
            row_html+= `<tr class="show-receipt-details">
                            <td class="column1 receipt-id">${ row.id }</td>
                            <td>${ row.customer__name }</td>
                            <td class="text-center">${ row.active_date }</td>
                            <td class="text-center">${ row.total_amount }</td>
                            <td class="text-center">${ row.paid_amount }</td>
                            <td class="text-center">${ row.expiry_date }<span id="expiry_status"
                                                          class="ml-2"
                                                          style="background-color: ${ row.alarm_color };"
                                                          title="${ parseInt(row.days_left)>-1?row.days_left + ' day(s) left':(parseInt(row.days_left)*-1)+' day(s) over due' }"
                                                          data-toggle="tooltip"
                                                          data-placement="top"></span></td>
                            <td class="text-center">${ row.status }</td>
                            <td class="text-center pl-2 py-2 edit-col-2">
                                <a href="#" class="edit-receipt no-text-decore" data-toggle="tooltip" data-placement="top" title="Edit" data-receipt-id="${ row.id }">
                                    <span class="px-2">
                                        <svg width="17px" height="18px" viewBox="0 0 17 18" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
                                            <!-- Generator: Sketch 50.2 (55047) - http://www.bohemiancoding.com/sketch -->
                                            <defs></defs>
                                            <g id="Icon-Edit-Normal" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
                                                <g id="Group-2" fill="#93A4BA">
                                                    <g id="Group-Copy" transform="translate(8.131728, 8.505393) scale(1, -1) rotate(-45.000000) translate(-8.131728, -8.505393) translate(5.631728, -0.494607)">
                                                        <rect id="Rectangle-3" x="0" y="4.36363636" width="4.36363636" height="8.72727273"></rect>
                                                        <path d="M2.18181818,0 L2.18181818,0 C2.44536679,-4.84130935e-17 2.68236371,0.160454727 2.7802432,0.405153465 L4.36363636,4.36363636 L0,4.36363636 L1.58339316,0.405153465 C1.68127265,0.160454727 1.91826958,4.84130935e-17 2.18181818,0 Z" id="Rectangle-3-Copy-2"></path>
                                                        <path d="M0,14.5454545 L4.36363636,14.5454545 L4.36363636,16.4545455 C4.36363636,17.0068302 3.91592111,17.4545455 3.36363636,17.4545455 L1,17.4545455 C0.44771525,17.4545455 6.76353751e-17,17.0068302 0,16.4545455 L0,14.5454545 Z" id="Rectangle-3-Copy"></path>
                                                    </g>
                                                    <rect id="Rectangle-5" x="0" y="16.3333333" width="14.5454545" height="1.45454545"></rect>
                                                </g>
                                            </g>
                                        </svg>
                                    </span>
                                </a>
                                <a href="#" class="delete-receipt no-text-decore" data-toggle="tooltip" data-placement="top" title="Delete" data-receipt-id="${ row.id }">
                                    <span class="px-2">
                                        <svg width="16px" height="17px" viewBox="0 0 16 17" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
                                            <!-- Generator: Sketch 50.2 (55047) - http://www.bohemiancoding.com/sketch -->
                                            <defs></defs>
                                            <g id="Icon-Delete-Normal" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
                                                <g id="Group-23-Copy-5" fill="#93A4BA">
                                                    <path d="M2.95277423,16.6347691 C2.57992713,16.6347691 2.27334729,16.3778291 2.25759319,16.0521628 L1.45454545,4.15384615 L14.5272529,4.15384615 L13.8017662,16.0521264 C13.786012,16.3778291 13.4794322,16.6347691 13.1065851,16.6347691 L2.95277423,16.6347691 Z M4.74481896,6.60788628 L4.74481896,13.3679809 C4.74481896,13.669532 5.05635843,13.9139843 5.44062516,13.9139843 C5.82493358,13.9139843 6.13647304,13.669532 6.13647304,13.3679809 L6.13647304,6.60788628 C6.13647304,6.30636789 5.82493358,6.06188292 5.44062516,6.06188292 C5.05635843,6.06188292 4.74481896,6.30636789 4.74481896,6.60788628 Z M7.54400625,6.60788628 L7.54400625,13.3679809 C7.54400625,13.669532 7.85554572,13.9139843 8.23985413,13.9139843 C8.62412086,13.9139843 8.93566033,13.669532 8.93566033,13.3679809 L8.93566033,6.60788628 C8.93566033,6.30636789 8.62412086,6.06188292 8.23985413,6.06188292 C7.85554572,6.06188292 7.54400625,6.30636789 7.54400625,6.60788628 Z M10.3431935,6.60788628 L10.3431935,13.3679809 C10.3431935,13.669532 10.654733,13.9139843 11.0390414,13.9139843 C11.4233082,13.9139843 11.7348476,13.669532 11.7348476,13.3679809 L11.7348476,6.60788628 C11.7348476,6.30636789 11.4233082,6.06188292 11.0390414,6.06188292 C10.654733,6.06188292 10.3431935,6.30636789 10.3431935,6.60788628 Z" id="Combined-Shape"></path>
                                                    <path d="M5.81818182,2.76923077 L10.1821303,2.76923077 L10.1821303,1.38461538 L5.81818182,1.38461538 L5.81818182,2.76923077 Z M11.6387163,1.38388957 L11.6387163,0.433140604 C11.6387163,0.193922258 11.3271351,0 10.9428684,0 L5.06149377,0 C4.67718536,0 4.36564589,0.193922258 4.36564589,0.433140604 L4.36564589,1.38388957 L0,1.38388957 L0,4.10947616 L15.9737082,4.10947616 L15.9737082,1.38388957 L11.6387163,1.38388957 Z" id="Fill-1"></path>
                                                </g>
                                            </g>
                                        </svg>
                                    </span>               
                                </a>
                            </td>
                        </tr>`;
        });
    } else {
        row_html += NO_RECORD_FOUND_ROW_HTML;
    }
    return row_html;
}

function load_receipts(page=1){
    if (!$('#receipts_data_div').length){
        show_snackbar_message('No receipts available');
    }
    $.ajax({
        url: "/dashboards/receipts/",
        method: 'POST',
        dataType: 'json',
        data: {
            search_query: $('#searchQuery').val(),
            csrfmiddlewaretoken: window.csrfToken
        },
        beforeSend: function () {
            $('.loader').show();
        },
        success: function (resp) {
                if (resp.success) {
                    var rows_html = render_receipt_rows(resp.data);
                    $('#receipts_data_div').html(rows_html);
                    $('[data-toggle="tooltip"]').tooltip();
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

function delete_receipt(id, row_obj){
    $.ajax({
        url: "/dashboards/receipts/delete_receipt/",
        method: 'POST',
        dataType: 'json',
        data: {
            receipt_id: id,
            csrfmiddlewaretoken: window.csrfToken
        },
        beforeSend: function () {
            $('.loader').show();
        },
        success: function (resp) {
                if (resp.success) {
                    show_snackbar_message(resp.message, 'success',  'center');
                    row_obj.remove();
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

function create_receipt(form_obj) {
    var customer_id = form_obj.find('select[name="customer_id"]').val(),
        due_date = form_obj.find('input[name="due_date"]').val();
    $.ajax({
        url: "/dashboards/receipts/create_receipt/",
        method: 'POST',
        dataType: 'json',
        data: {
            customer_id: customer_id,
            due_date: due_date,
            csrfmiddlewaretoken: window.csrfToken
        },
        beforeSend: function () {
            $('.loader').show();
        },
        success: function (resp) {
                if (resp.success) {
                    show_snackbar_message(resp.message, 'success',  'center');
                    form_obj.remove();
                    load_receipts();
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
    load_receipts(1);
    receipt_form_html = receipt_form_html.replace('<customer_list_here>', $('#customers_select_html').html());
    $(document).on('click', '.refresh_receipts', function (e) {
        load_receipts();
    });
    $(document).on('click', '.add_receipt', function (e) {
        $(`.receipt_form_html`).append(receipt_form_html);
    });
    $(document).on('submit', '.create_receipt', function (e) {
        e.preventDefault();
        create_receipt($(this));
    });
    $(document).on('click', '.cancel_create_receipt', function (e) {
        e.preventDefault();
        $(this).closest('form').remove();
    });
    $(document).on('submit', '#search_receipt', function (e) {
        e.preventDefault();
        load_receipts();
    });
    $(document).on('click', '.show-receipt-details', function (e) {
        e.stopPropagation();
        location.href = '/dashboards/receipt_details/'+$(this).find('.receipt-id').text()+'/';
    });
    $(document).on('click', '.delete-receipt', function (e) {
        e.stopPropagation();
        var receipt_id = $(this).closest('tr').find('.receipt-id').text(),
            row_obj = $(this).closest('tr');
        delete_receipt(receipt_id, row_obj);
    });
});