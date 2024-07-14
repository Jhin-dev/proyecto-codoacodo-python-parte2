const loaderOut = document.querySelector("#loader-out");
function fadeOut(element) {
  let opacity = 1;
  const timer = setInterval(function () {
    if (opacity <= 0.1) {
      clearInterval(timer);
      element.style.display = "none";
    }
    element.style.opacity = opacity;
    opacity -= opacity * 0.1;
  }, 50);
}
fadeOut(loaderOut);

function eliminarSitio(id_sitio, foto_sitio) {
  if (confirm("¿Estas seguro que deseas Eliminar el sitio?")) {
    let url = `/borrar-sitio/${id_sitio}/${foto_sitio}`;
    if (url) {
      window.location.href = url;
    }
  }
}
