const body = document.querySelector("body")
const header = document.querySelector(".header")

const header_menu = document.querySelector(".header__menu")
const btn_hamburger = document.querySelector("#btn_hamburger")

const sub_menu_link = document.querySelectorAll(".with__sub__menu")
const sub_menu = document.querySelectorAll(".sub__menu")

// Desktop Submenu
sub_menu_link[0].addEventListener("mouseenter", function() {
    if (sub_menu_link[0].classList.contains("open")) {
        sub_menu_link[0].classList.remove("open")
        sub_menu[0].classList.remove("open")

        sub_menu[0].classList.remove("fade_in")
        sub_menu[0].classList.add("fade_out")
    } else {
        sub_menu_link[0].classList.add("open")
        sub_menu[0].classList.add("open")

        sub_menu[0].classList.remove("fade_out")
        sub_menu[0].classList.add("fade_in")
    }
})

sub_menu[0].addEventListener("mouseleave", function() {
    if (sub_menu_link[0].classList.contains("open")) {
        sub_menu_link[0].classList.remove("open")

        sub_menu[0].classList.remove("fade_in")
        sub_menu[0].classList.add("fade_out")
    }
})

// Mobile & Tablet Submenu
sub_menu_link[1].addEventListener("click", function() {
    if (sub_menu_link[1].classList.contains("open")) {
        sub_menu_link[1].classList.remove("open")
        sub_menu[1].classList.remove("open")

        sub_menu[1].classList.remove("fade_in")
        sub_menu[1].classList.add("fade_out")
    } else {
        sub_menu_link[1].classList.add("open")
        sub_menu[1].classList.add("open")

        sub_menu[1].classList.remove("fade_out")
        sub_menu[1].classList.add("fade_in")
    }
})

// Hamburger Menu
btn_hamburger.addEventListener("click", function() {
    if (header.classList.contains("open")) {

        header.classList.remove("open") // Close menu

        header_menu.classList.remove("fade_in")
        header_menu.classList.add("fade_out")
    } else {
        header.classList.add("open") // Open menu

        header_menu.classList.remove("fade_out")
        header_menu.classList.add("fade_in")
    }
})


// Carousel
const track = document.querySelector(".carousel__track")
const slides = Array.from(track.children)
const btn__left = document.getElementById("btn__left")
const btn__right = document.getElementById("btn__right")
// Slide index controler
var i = 0

function show_slide(slide) {
  slides[slide].style.visibility = "visible"
  slides[slide].classList.add("fade_in")
}

function hide_slide(slide) {
  slides[slide].style.visibility = "hidden"
  slides[slide].classList.remove("fade_in")
}

function show_btn(button) {
  button.style.display = "inline"
}

function hide_btn(button) {
  button.style.display = "none"
}

// Slides initial states
slides[0].style.visibility = "visible"
slides[1].style.visibility = "hidden"
slides[2].style.visibility = "hidden"
slides[3].style.visibility = "hidden"
slides[4].style.visibility = "hidden"
slides[5].style.visibility = "hidden"

// Left button initial state
if (i == 0) {
  hide_btn(btn__left)
}

// Move to the left
btn__left.addEventListener("click", function() {
  i -= 1

  hide_slide(i + 1)
  show_slide(i)

  // // Button control
  if (i == 0) {
    hide_btn(btn__left)
  } else if (i > 0 && i < 5) {
    show_btn(btn__right)
  }
})

// Move to the right
btn__right.addEventListener("click", function() {
  i += 1

  hide_slide(i - 1)
  show_slide(i)

  // Button control
  if (i == 5) {
    hide_btn(btn__right)
  } else if (i > 0 && i < 5) {
    show_btn(btn__left)
  }
})


// Initialize Google Maps
function initMap() {
  // Location data
  const location = { lat: 54.394, lng: 18.580 };

  const map = new google.maps.Map(document.getElementById("map"), {
    zoom: 15,
    center: location,
    mapId: 'f0f127a6ec79a160'
  });
  // Marker setup
  const map_marker = new google.maps.Marker({
    position: location,
    map: map,
  });
}
