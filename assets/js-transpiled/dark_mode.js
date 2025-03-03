"use strict";

document.addEventListener('DOMContentLoaded', function () {
  var mode_toggle = document.getElementById("light-toggle");
  mode_toggle.addEventListener("click", function () {
    toggleTheme(localStorage.getItem("theme"));
  });
});