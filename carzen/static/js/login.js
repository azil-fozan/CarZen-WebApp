function login(form_obj) {
    var uname = form_obj.find('input[name="username"]').val(),
        password = form_obj.find('input[name="pass"]').val(),
        original_url = get_url_params().next;
    $.ajax({
        url: "/login/",
        method: 'POST',
        dataType: 'json',
        data: {
            user: uname,
            code: password,
            original_url: original_url?original_url:'',
            csrfmiddlewaretoken: window.csrfToken
        },
        beforeSend: function () {
            $('.loader').show();
            form_obj.find('.submit-button').prop('disabled', true);
        },
        success: function (resp) {
                if (resp.success) {
                    if (resp.original_url != undefined) {
                            location.href = resp.original_url;
                    }
                    else{
                        location.reload();
                    }
                } else {
                    show_snackbar_message(resp.message, 'warning',  'center');
                }
        },
        error: function (resp) {
            show_snackbar_message('Something went wrong.', 'error', 'center');
        },
        complete: function () {
             form_obj.find('.submit-button').prop('disabled', false);
             $('.loader').hide();
        }
    });
}

function forgot_password(form_obj) {
    var uname = form_obj.find('input[name="username"]').val();
    $.ajax({
        url: "/forgot_password/",
        method: 'POST',
        dataType: 'json',
        data: {
            user: uname,
            csrfmiddlewaretoken: window.csrfToken
        },
        beforeSend: function () {
            form_obj.find('.submit-button').prop('disabled', true);
        },
        success: function (resp) {
                if (resp.success) {
                    show_snackbar_message(resp.message, 'success',  'center');
                    window.setTimeout(function () {
                        window.location='/login/';
                      }, 3000);

                } else {
                    show_snackbar_message(resp.message, 'warning',  'center');
                }
        },
        error: function (resp) {
            show_snackbar_message('Something went wrong.', 'error', 'center');
        },
        complete: function () {
             $('.loader').hide();form_obj.find('.submit-button').prop('disabled', false);
        }
    });
}

$(document).ready(function () {
    $(document).on('submit', '#login_form', function (e) {
        e.preventDefault();
        if (window.location.pathname!='/forgot_password/'){
            login($(this));
        } else {
            forgot_password($(this));
        }
    });
});