function hapusKarya(idData) {
    $.ajax({
        url: `/delete-karya/${idData}`,
        success: function () {
            $(`#${idData}`).remove();
        }
    });
}

