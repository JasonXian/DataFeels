$(function () {
    $('[data-toggle="popover"]').popover()
});
var slider = document.getElementById("slider");
var output = document.getElementById("output");
output.innerHTML = slider.value / 100;

slider.oninput = function() {
  output.innerHTML = this.value / 100;
}