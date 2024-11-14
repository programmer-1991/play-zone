// Update quantity on click
$('.update-link').click(function (e) {
    var form = $(this).prev('.update-form');
    form.submit();
})

// Remove item and reload on click
$('.remove-item').click(function (e) {
    var csrfToken = $(this).attr('data-token');
    var itemId = $(this).attr('data-id');
    var url = `/bag/remove/${itemId}/`;
    var data = {
        'csrfmiddlewaretoken': csrfToken,
    };
    $.post(url, data)
        .done(function () {
            location.reload();
        });
})