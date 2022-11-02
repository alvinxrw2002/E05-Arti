async function getKaryaJson(){
    var jsonData = await fetch("/galeri/json").then((res) => res.json());
    return jsonData;
}
async function show_galeri(){
    var counter = 0
    karya = await getKaryaJson();
    console.log(karya)
    if(karya.length == 0){
        return ""
    }
    document.getElementById("karya").innerHTML = "";
    html = ""
    karya.data.forEach((element)=>{
        if(counter == 0) {
            if(element.user == element.user_loggedin || element.user_loggedin.is_supperuser){
                html += `
                <div class="carousel-item active" id=karya-${element.pk}>
                    <div class="card text-bg-info mb-3" style="width: 40rem" id='cor'>
                        <img src='/media/${element.fields.gambar}' class='d-block w-100'></img>
                        <div class="card-body">
                            <h4 id="${element.fields.id}-judul" class="card-text">${element.fields.judul}</h4>
                            <h5 id="${element.fields.id}-harga" class="card-title">Rp${element.fields.harga}</h5>
                            <p id="${element.fields.id}-deskripsi" class="card-text">${element.fields.deskripsi}</p>
                        </div>
                        <div class="card-footer text-center">
                            <button class="btn btn-outline-danger" onclick="hapusKarya(${element.pk})">Hapus</button>
                        </div>                           
                    </div>
                </div>
                `
            } else {
            html += `
            <div class="carousel-item active" id=karya-${element.pk}>
                <div class="card text-bg-info mb-3" style="width: 40rem" id='cor'>
                    <img src='/media/${element.fields.gambar}' class='d-block w-100'></img>
                    <div class="card-body">
                        <h4 id="${element.fields.id}-judul" class="card-text">${element.fields.judul}</h4>
                        <h5 id="${element.fields.id}-harga" class="card-title">Rp${element.fields.harga}</h5>
                        <p id="${element.fields.id}-deskripsi" class="card-text">${element.fields.deskripsi}</p>
                    </div>                        
                </div>
            </div>
            `
            }
        } else {
            if(element.user == element.user_loggedin || element.user_loggedin.is_supperuser){
                html += `
                <div class="carousel-item" id=karya-${element.pk}>
                    <div class="card text-bg-info mb-3" style="width: 40rem" id='cor'>
                        <img src='/media/${element.fields.gambar}' class='d-block w-100'></img>
                        <div class="card-body">
                            <h4 id="${element.fields.id}-judul" class="card-text">${element.fields.judul}</h4>
                            <h5 id="${element.fields.id}-harga" class="card-title">Rp${element.fields.harga}</h5>
                            <p id="${element.fields.id}-deskripsi" class="card-text">${element.fields.deskripsi}</p>
                        </div>
                        <div class="card-footer text-center">
                            <button class="btn btn-outline-danger" onclick="hapusKarya(${element.pk})">Hapus</button>
                        </div>                           
                    </div>
                </div>
                `
            } else {
            html += `
            <div class="carousel-item" id=karya-${element.pk}>
                <div class="card text-bg-info mb-3" style="width: 40rem" id='cor'>
                    <img src='/media/${element.fields.gambar}' class='d-block w-100'></img>
                    <div class="card-body">
                        <h4 id="${element.fields.id}-judul" class="card-text">${element.fields.judul}</h4>
                        <h5 id="${element.fields.id}-harga" class="card-title">Rp${element.fields.harga}</h5>
                        <p id="${element.fields.id}-deskripsi" class="card-text">${element.fields.deskripsi}</p>
                    </div>                        
                </div>
            </div>
            `
            }
        }
        counter++
    })
    return document.getElementById("karya").innerHTML = html
}
window.onload = show_galeri()