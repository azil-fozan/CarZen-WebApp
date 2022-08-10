function hire_mech(This){
    var catagory = This.find('[name="catagory"]').val(),
        car_info = This.find('[name="car_info"]').val(),
        service_info = This.find('[name="service_info"]').val();

    $.ajax({
        url: window.location.pathname,
        method: 'POST',
        dataType: 'json',
        data: {
            catagory: catagory,
            car_info: car_info,
            service_info: service_info,
            csrfmiddlewaretoken: window.csrfToken
        },
        beforeSend: function () {
            $('.loader').show();
        },
        success: function (resp) {
                if (resp.success) {
                    // $('#service_sidebar_link').click();
                    window.location = $('#service_sidebar_link').attr('href');
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
    // hire_mechload_services(1);
    $(document).on('submit', '#hire_mech_form', function (e) {
        e.preventDefault();
        hire_mech($(this));
    });
    // $(document).on('keyup', '#sevice_history_search_string', function (e) {
    //     if (!$(this).val().length){
    //         $('.cancel-search').click();
    //     }
    // });
});