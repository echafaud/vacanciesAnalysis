function openNav() {
  document.querySelector(".nav").style.width = "300px";
  document.querySelector(".main__container").style.marginLeft = "300px";
  document.body.style.backgroundColor = "rgba(0,0,0,0.5)";
  document.querySelector(".imgs").classList.toggle("brightnessOn")

}

function closeNav() {
  document.querySelector(".nav").style.width = "0";
  document.querySelector(".main__container").style.marginLeft = "0px";
  document.body.style.backgroundColor = "white";
  document.querySelector(".imgs").classList.remove("brightnessOn")

}
