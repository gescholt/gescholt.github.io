"use strict";

// Has to be in the head tag, otherwise a flicker effect will occur.

var toggleTheme = function toggleTheme(theme) {
  if (theme == "dark") {
    setTheme("light");
  } else {
    setTheme("dark");
  }
};
var setTheme = function setTheme(theme) {
  transTheme();
  setHighlight(theme);
  setGiscusTheme(theme);
  if (theme) {
    document.documentElement.setAttribute("data-theme", theme);

    // Add class to tables.
    var tables = document.getElementsByTagName("table");
    for (var i = 0; i < tables.length; i++) {
      if (theme == "dark") {
        tables[i].classList.add("table-dark");
      } else {
        tables[i].classList.remove("table-dark");
      }
    }

    // Set jupyter notebooks themes.
    var jupyterNotebooks = document.getElementsByClassName("jupyter-notebook-iframe-container");
    for (var _i = 0; _i < jupyterNotebooks.length; _i++) {
      var bodyElement = jupyterNotebooks[_i].getElementsByTagName("iframe")[0].contentWindow.document.body;
      if (theme == "dark") {
        bodyElement.setAttribute("data-jp-theme-light", "false");
        bodyElement.setAttribute("data-jp-theme-name", "JupyterLab Dark");
      } else {
        bodyElement.setAttribute("data-jp-theme-light", "true");
        bodyElement.setAttribute("data-jp-theme-name", "JupyterLab Light");
      }
    }
  } else {
    document.documentElement.removeAttribute("data-theme");
  }
  localStorage.setItem("theme", theme);

  // Updates the background of medium-zoom overlay.
  if (typeof medium_zoom !== "undefined") {
    medium_zoom.update({
      background: getComputedStyle(document.documentElement).getPropertyValue("--global-bg-color") + "ee" // + 'ee' for trasparency.
    });
  }
};
var setHighlight = function setHighlight(theme) {
  if (theme == "dark") {
    document.getElementById("highlight_theme_light").media = "none";
    document.getElementById("highlight_theme_dark").media = "";
  } else {
    document.getElementById("highlight_theme_dark").media = "none";
    document.getElementById("highlight_theme_light").media = "";
  }
};
var setGiscusTheme = function setGiscusTheme(theme) {
  function sendMessage(message) {
    var iframe = document.querySelector("iframe.giscus-frame");
    if (!iframe) return;
    iframe.contentWindow.postMessage({
      giscus: message
    }, "https://giscus.app");
  }
  sendMessage({
    setConfig: {
      theme: theme
    }
  });
};
var transTheme = function transTheme() {
  document.documentElement.classList.add("transition");
  window.setTimeout(function () {
    document.documentElement.classList.remove("transition");
  }, 500);
};
var initTheme = function initTheme(theme) {
  if (theme == null || theme == "null") {
    var userPref = window.matchMedia;
    if (userPref && userPref("(prefers-color-scheme: dark)").matches) {
      theme = "dark";
    }
  }
  setTheme(theme);
};
initTheme(localStorage.getItem("theme"));