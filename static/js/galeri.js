function addSaveButton(idData) {
    $('.modal-footer').html(`                
                        <button type="button" class="btn btn-primary" data-bs-dismiss="modal"onclick="editKarya(${idData})">Simpan</button>
                        `)
}

function editKarya(idData) {
    let judulBaru = $("#judul-baru").val();
    let kategoriBaru = $("#kategori-baru").val();
    let hargaBaru = $("#harga-baru").val();
    let deskripsiBaru = $("#deskripsi-baru").val();
    document.querySelector('#form-edit-karya').reset();
    $.ajax({
        type: "POST",
        url: `/edit-karya/${idData}`,
        data: {
            'judul': judulBaru,
            'kategori': kategoriBaru,
            'harga': hargaBaru,
            'deskripsi': deskripsiBaru,
        },
        success: function () {
            $(`#${idData}-judul`).text(judulBaru);
            $(`#${idData}-kategori`).text(kategoriBaru);
            $(`#${idData}-harga`).text("Rp" + hargaBaru);
            $(`#${idData}-deskripsi`).text(deskripsiBaru);
        }
    });
}

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