// ! Detay sayfası donanım ve ekspertiz raporu butonlarına tıklandığında oluşacak durumun kodları
const btnDonanım = document.querySelector(".btn-donanım");
const donanım = document.querySelector(".donanım");
const btnEkspertiz = document.querySelector(".btn-ekspertiz");
const ekspertizDurum = document.querySelector(".expertiz-durum");

btnDonanım.addEventListener("click", function(){
    donanım.classList.add("d-block");
    donanım.classList.remove("d-none");
    ekspertizDurum.classList.add("d-none");
    ekspertizDurum.classList.remove("d-block");
});

btnEkspertiz.addEventListener("click", function(){
    ekspertizDurum.classList.add("d-block");
    ekspertizDurum.classList.remove("d-none");
    donanım.classList.add("d-none");
    donanım.classList.remove("d-block");
});


// ! Detay sayfasında küçük fotoğraflara tıkladığımda büyük fotoğrafın yerine geçmesi için yazılacak kodlar
function buyukResmiDegistir(yeniResimUrl) {
    var img = document.getElementById('buyuk-resim');
    img.src = yeniResimUrl;
}

var buyukResimContainer = document.getElementById('buyuk-resim-container');
var buyukResim = document.getElementById('buyuk-resim');

buyukResimContainer.addEventListener('mousemove', function(e) {
    var boundingRect = buyukResimContainer.getBoundingClientRect();
    var offsetX = (e.clientX - boundingRect.left) / boundingRect.width;
    var offsetY = (e.clientY - boundingRect.top) / boundingRect.height;

    buyukResim.style.transformOrigin = (offsetX * 100) + '% ' + (offsetY * 100) + '%';
    buyukResim.style.transform = "scale(2)";
});

buyukResimContainer.addEventListener('mouseleave', function(e) {
    buyukResim.style.transform = "scale(1)";
});












