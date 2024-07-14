/**
 *
 * General vista previa de imagen perfil cargada
 */
function readURL(input) {
  if (input.files && input.files[0]) {
    var imageUrl = URL.createObjectURL(input.files[0]);
    $("#imagePreview").css("background-image", "url(" + imageUrl + ")");
    $("#imagePreview").hide();
    $("#imagePreview").fadeIn(650);
  }
}

$("#imageUpload").change(function () {
  readURL(this);
});

