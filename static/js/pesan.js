$(document).ready(function(){
    

    $("#id_isi").keyup(function(){
        //character count isi txt area pesan

        var txtlength = $("#id_isi").val().length;
        $("#lettercount").empty();

        if (txtlength > 0) {
            $("#lettercount").append(txtlength+"/100");
        } 
        
        if (txtlength > 85) {
            $("#lettercount").empty();
            $("#lettercount").append('<span style="color:red;">' + txtlength + '/100</span>');
        }
        
    });


    $("#tombol-kirim").click(function(){
        //ajax untuk simpan pesan dan nampilin testi yg baru dimasukkin tsb.

        var isi = $("#id_isi").val();
        // alert(isi);
        if (isi.length > 0 && isi != "") {
            $.ajax({url: "pesanajax?q=" + isi, success: function(result){
                console.log(result);
    
                $("#divpesan").empty();
                $("#id_isi").val("");
                $("#lettercount").empty();
    
                $("#divpesan").append("<p class=\"judul-pesan\">Pesan</p>")
                $("#divpesan").append('<div class="row" id="kumpulan-pesan"></div>')
                var i;
                for (i=0; i<result.length; i++){
                    var isiPesan = result[i].fields.isi;
                    var nama = result[i].fields.nama;
                    // alert(isiPesan + nama);
                    $("#kumpulan-pesan").append('<div class="col-md-4 mb-4"> <div class="card" style="height: 200px;"><div class="card-body"><div class="pesan-textfield"><p style="padding-top: 10px;">' +isiPesan+ '</p></div><div class="pesan-nama"><p style="right: 0; position: absolute;">-' +nama+ '</p></div></div></div></div>')
                }
            }});
        } else {
            alert("Anda belum mengisi pesan!");
        }
        
    });
});
