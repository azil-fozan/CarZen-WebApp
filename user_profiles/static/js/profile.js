$(document).ready(function () {
    $(document).on('click', '#edit_my_profile', function (e) {
        if ($(this).text()=='Edit Profile') {
            $('input').prop( "disabled", false );
            $(this).text('Save');
            $(this).addClass('btn-success');
            $(this).removeClass('btn-primary');
        } else {
            $('input').prop( "disabled", true );
            $(this).text('Edit Profile');
            $(this).removeClass('btn-success');
            $(this).addClass('btn-primary');
        }
    });
});