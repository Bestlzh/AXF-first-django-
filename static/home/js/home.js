$(function () {
    initSwiperWheel();
    initSwiperMustBuy();
})


// 第一个轮播的配置文件
function initSwiperWheel() {
    var swiper = new Swiper('#topSwiper', {
        pagination: '.swiper-pagination',
        paginationClickable: true,
        autoplay:2000,
    });
}

function initSwiperMustBuy() {
    var swiper = new Swiper('#swiperMustBuy', {
        slidesPerView:3,
    });
}