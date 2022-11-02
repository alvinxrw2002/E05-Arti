function deleteComment(string_pk){
    $.ajax({
        url: url_delete_comment,
        type: "POST",
        data:{
            'csrfmiddlewaretoken': csrf_token,
            'id': string_pk,
        },
        
    });
    alert("Berhasil menghapus comment!");
    $.ajax({
        type: "GET",
        url: url_change_comments,
        success: function(data){
            var a = "";
            a += "<div class='carousel-item active' style='border-radius: 20px;'>"
                +   "<div class='card' style='height: 250px; background-color: rgb(231, 241, 240); border-radius: 20px'>"
                +       "<div class='card-body'>"
                +   "<h5 class='card-title'>See Your Comments Here</h5>"
                + "</div> </div> </div>";
            $.each(data, function(key, value){
                a += "<div class='carousel-item' id='" + data[key].pk + "' style='border-radius: 20px;'>"
                    + "<div class='card' style='height: 250px; background-color: rgb(231, 241, 240); border-radius: 20px'>"
                    + "<div class='card-body'>"
                    + "<h5 class='card-title'>" + data[key].fields.username + "</h5>"
                    + "<p class='card-text'>" + data[key].fields.text + "</p>";
                if(user_is_staff == "True"){
                    a += "<button class='btn btn-outline-dark btn-sm' onclick='deleteComment(" + data[key].pk + ")'>Delete</a>"
                }
                    a += "</div> </div> </div>";
            });
            $("#comments_carousel").html(a);
        }
    });
    
}

function deactivateElem(){
    $("textarea").prop("readonly", true);
    $("textarea").attr("placeholder", "Silahkan login terlebih dahulu");
    $("#form_button_success").prop("disabled", true)
}

$(document).ready(function(){
    $("#button_pengguna").click(function(){
        $.ajax({
            url: url_lboard_pengguna,
            type: "GET",
            success: function(data){
                var s = "";
                        s += "<span class='border border-3' style='border-radius:20%; border-color: black!important;'>"
                            + "<div class='col text-center pt-5' id='leaderboard' style='min-width:300px'><ol>"
                        $.each(data, function(key, value){
                            s += "<li>" + data[key].fields.username + "</li>"
                        })
                        s += "</ol></div></span>"
                $('#leaderboard_pengguna').html(s);
                $('#leaderboard_pengguna').show();
                $('#leaderboard_karya').hide();
            }
        });
    });

    $("#button_karya").click(function(){
        $.ajax({
            url: url_lboard_karya,
            type: "GET",
            success: function(data){
                $("#leaderboard_karya").html(data);
                $('#leaderboard_pengguna').hide();
                $('#leaderboard_karya').show();
            }
        });
    });

    $("#form_button_success").click(function(){
        if($("textarea").val() != ""){
            $.ajax({
                data: {
                    'csrfmiddlewaretoken': csrf_token,
                    'text': $("textarea").val(),
                },
                type: "POST",
                url: url_create_comment,
                
            });
            alert("Berhasil menambahkan comment!");
            $("textarea").val('');
            $.ajax({
                type: "GET",
                url: url_change_comments,
                success: function(data){
                    var a = "";
                    a += "<div class='carousel-item active' style='border-radius: 20px;'>"
                        +   "<div class='card' style='height: 250px; background-color: rgb(231, 241, 240); border-radius: 20px'>"
                        +       "<div class='card-body'>"
                        +   "<h5 class='card-title'>See Your Comments Here</h5>"
                        + "</div> </div> </div>";
                    $.each(data, function(key, value){
                        a += "<div class='carousel-item' id='" + data[key].pk + "' style='border-radius: 20px;'>"
                            + "<div class='card' style='height: 250px; background-color: rgb(231, 241, 240); border-radius: 20px'>"
                            + "<div class='card-body'>"
                            + "<h5 class='card-title'>" + data[key].fields.username + "</h5>"
                            + "<p class='card-text'>" + data[key].fields.text + "</p>";
                        if(user_is_staff == "True"){
                            a += "<button class='btn btn-outline-dark btn-sm' onclick='deleteComment(" + data[key].pk + ")'>Delete</a>"
                        }
                            a += "</div> </div> </div>";
                    });
                    $("#comments_carousel").html(a);
                }
            });
        }
        else{
            alert("Text field tidak boleh kosong!")
        }
    });
});

