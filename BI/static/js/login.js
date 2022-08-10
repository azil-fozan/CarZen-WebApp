function login(form_obj) {
    var uname = form_obj.find('input[name="username"]').val(),
        password = form_obj.find('input[name="pass"]').val(),
        is_mechanic = form_obj.find('.type_selector').first().hasClass('active') === true,
        original_url = get_url_params().next;
    $.ajax({
        url: "/login/",
        method: 'POST',
        dataType: 'json',
        data: {
            user: uname,
            code: password,
            is_mechanic: is_mechanic,
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


function signup(form_obj) {
    var uname = form_obj.find('input[name="username"]').val(),
        password = form_obj.find('input[name="pass"]').val(),
        email = form_obj.find('input[name="email"]').val(),
        expertise = form_obj.find('input[name="expertise"]').val(),
        address = form_obj.find('input[name="address"]').val(),
        first_name = form_obj.find('input[name="first_name"]').val(),
        last_name = form_obj.find('input[name="last_name"]').val(),
        is_mechanic = form_obj.find('.type_selector').first().hasClass('active') === true;

    $.ajax({
        url: "/signup/",
        method: 'POST',
        dataType: 'json',
        data: {
            user: uname,
            code: password,
            email: email,
            expertise: expertise,
            address: address,
            first_name: first_name,
            last_name: last_name,
            is_mechanic: is_mechanic,
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
                        location.href='/login/';
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
        if (window.location.pathname == '/login/'){
            login($(this));
        } else if (window.location.pathname == '/signup/'){
            signup($(this));
        } else {
            forgot_password($(this));
        }
    });
});