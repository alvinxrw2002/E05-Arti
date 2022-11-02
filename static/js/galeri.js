function hapusKarya(idData) {
    $.ajax({
        url: `/galeri/delete-karya/${idData}`,
        success: function () {
            $(`#karya-${idData}`).remove();
            show_galeri()
        }
    });
}