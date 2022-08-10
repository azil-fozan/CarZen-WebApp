function save_user_profile() {
    var profile_basics = $('.profile_basics');
    var profile_details = $('.profile_details');

    let formData = new FormData();
    formData.append('user_id', profile_basics.find('[name="user_id"]').val());
    // formData.append('full_name', profile_basics.find('[name="full_name"]').val());
    formData.append('f_name', profile_details.find('[name="f_name"]').val());
    formData.append('l_name', profile_details.find('[name="l_name"]').val());
    formData.append('phone', profile_details.find('[name="phone"]').val());
    formData.append('address', profile_details.find('[name="address"]').val());
    formData.append('Occupation', profile_details.find('[name="occupation"]').val());
    formData.append('country',  profile_details.find('[name="country"]').val());
    formData.append('state', profile_details.find('[name="state"]').val());
    formData.append('csrfmiddlewaretoken', window.csrfToken);

    formData.append('image', $('[name="profile_image"]')[0].files[0]);

    $.ajax({
        url: "/user_profile/edit_profile/",
        type: 'POST',
        data: formData,
        contentType: false,
        processData: false,
        enctype: 'multipart/form-data',
        beforeSend: function () {
            $('.loader').show();
        },
        success: function (resp) {
                if (resp.success) {
                    if (resp.new_file_url !== undefined){
                        $('.profile_image_view').attr('src', resp.new_file_url)
                    }
                    show_snackbar_message(resp.message, 'success',  'center');
                } else {
                    show_snackbar_message(resp.message, 'warning',  'center');
                    $('#edit_my_profile').click();
                }
        },
        error: function (resp) {
            show_snackbar_message('Something went wrong.', 'error', 'center');
            $('#edit_my_profile').click();
        },
        complete: function () {
             $('.loader').hide();
        }
    });
}


$(document).ready(function () {
    $(document).on('click', '#edit_my_profile', function (e) {
        if ($(this).text()=='Edit Profile') {
            $('input').prop( "disabled", false );
            $(this).text('Save');
            $('.profile_basics').find('.full_name_lable').hide();
            $('.profile_basics').find('[name="full_name"]').show();

            $('.profile_basics').find('.profile_image_view').hide();
            $('.profile_basics').find('.image_upload_div').show();

            $(this).addClass('btn-success');
            $(this).removeClass('btn-primary');
        } else {
            $('input').prop( "disabled", true );
            $(this).text('Edit Profile');

            var new_name = $('.profile_basics').find('[name="full_name"]').val();
            $('.profile_basics').find('.full_name_lable').text(new_name);
            $('.profile_basics').find('.full_name_lable').show();
            $('.profile_basics').find('[name="full_name"]').hide();

            // var new_image = $('.profile_basics').find('[name="profile_image"]').val();
            // $('.profile_basics').find('.profile_image_view').attr('src', new_image);
            $('.profile_basics').find('.profile_image_view').show();
            $('.profile_basics').find('.image_upload_div').hide();

            $(this).removeClass('btn-success');
            $(this).addClass('btn-primary');
            //    call save profile here
            save_user_profile();
        }
    });
});