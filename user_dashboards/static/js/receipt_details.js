var receipt_product_form_html = `<form class="form-inline w-100 mb-3 d-flex justify-content-start add_receipt_product">
                                <options_list_here>
<!--                            <input class="form-control form-style mr-1" name="price" placeholder="Price" required type="number">-->
<!--                            <input class="form-control form-style mr-1" name="unit" type="text" placeholder="Unit" required>-->
                            <input class="form-control form-style mr-3" name="quantity" placeholder="Quantity" type="number">
<!--                            <input class="form-control form-style mr-1" name="discount" placeholder="Precentage Discount" type="number">-->
                            <span>
                                <button type="submit">
                                    <i class="fas fa-check" style="color:Green;"></i>
                                </button>                            
                                <button class="cancel_create_product">
                                    <i class="fas fa-times" style="color:Red;width: 20px;height: 20px;"></i>
                                </button>
                            </span>
                       </form>`;


function render_receipt_products(rows) {
    var row_html = '';
    if (rows.length) {
        rows.forEach(function (row) {
            row_html+= `<tr>
                            <td style="display: none">
                                <input type="hidden" class="product_id" value="${ row.id }">
                            </td>
                            <td class="column1">${ row.id }</td>
                            <td class="product_name">${ row.product_name }</td>
                            <td class="text-center">${ row.unit }</td>
                            <td class="text-center">${ row.price }</td>
                            <td class="text-center">${ row.quantity }</td>
                            <td class="text-center">${ row.discount }%</td>
                            <td class="text-center">${ row.total }</td>
                            <td class="text-center pl-2 py-2 edit-col-2">
                                <a href="#" class="remove-product no-text-decore" data-toggle="tooltip" data-placement="top" title="Remove" data-receipt-id="${ row.id }">
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

function load_receipt_products(page=1){
    // if (!$('#details_data_div').length){
    //     show_snackbar_message('No products added');
    // }
    var receipt_id = $('#receipt_id').val();
    $.ajax({
        url: "/dashboards/receipt_details/"+receipt_id+"/",
        method: 'POST',
        dataType: 'json',
        data: {
            receipt_id: receipt_id,
            search_query: $('#searchQuery').val(),
            csrfmiddlewaretoken: window.csrfToken
        },
        beforeSend: function () {
            $('.loader').show();
        },
        success: function (resp) {
                if (resp.success) {
                    var rows_html = render_receipt_products(resp.data);
                    $('#products_data_div').html(rows_html);
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

function remove_receipt_product(receipt_id, product_id) {
    $.ajax({
        url: "/dashboards/receipts/remove_product/",
        method: 'POST',
        dataType: 'json',
        data: {
            receipt_id: receipt_id,
            product_id: product_id,
            csrfmiddlewaretoken: window.csrfToken
        },
        beforeSend: function () {
            $('.loader').show();
        },
        success: function (resp) {
                if (resp.success) {
                    $(`input.product_id[value="${product_id}"]`).closest('tr').remove();
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

function add_receipt_product(form_obj) {
    var product_id = form_obj.find('select[name="product_id"]').val(),
        quantity = form_obj.find('input[name="quantity"]').val(),
        receipt_id = $('#receipt_id').val();
    $.ajax({
        url: "/dashboards/receipts/add_receipt_product/",
        method: 'POST',
        dataType: 'json',
        data: {
            receipt_id: receipt_id,
            product_id: product_id,
            quantity: quantity,
            csrfmiddlewaretoken: window.csrfToken
        },
        beforeSend: function () {
            $('.loader').show();
        },
        success: function (resp) {
                if (resp.success) {
                    form_obj.remove();
                    $('.refresh_products').click();
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
    load_receipt_products(1);
    receipt_product_form_html = receipt_product_form_html.replace('<options_list_here>', $('#products_select_html').html());
    $(document).on('click', '.refresh_products', function (e) {
        load_receipt_products();
    });
    $(document).on('submit', '.add_receipt_product', function (e) {
        e.preventDefault();
        add_receipt_product($(this));
    });
    $(document).on('click', '.remove-product', function (e) {
        var receipt_id = $('#receipt_id').val(),
            product_id = $(this).closest('tr').find('.product_id').val();
        remove_receipt_product(receipt_id, product_id);
    });
    $(document).on('submit', '#search_product', function (e) {
        e.preventDefault();
        load_receipt_products();
    });
    $(document).on('click', '.add_product', function (e) {
        $(`.product_form_html`).append(receipt_product_form_html);
    });
    $(document).on('click', '.cancel_add_product', function (e) {
        $(this).closest('form').remove();
    });
});