function hapusKarya(idData) {
    $.ajax({
        url: `/delete-karya/${idData}`,
        success: function () {
            $(`#${idData}`).remove();
        }
    });
}

function myFunction() {
    var x = document.getElementById("myTopnav");
    if (x.className === "topnav") {
        x.className += " responsive";
    } else {
        x.className = "topnav";
    }
}