$(document).ready(function () {
  $(this).click(function (e) {
    if (e.target.id !== "ac-icon") {
      box = document.getElementById("menu-list");
      box.style.display = "none";
    }
  });
});



// comment box style-------------------
const auto_height = (id) => {
  elem = document.getElementById(id);
  const comment = document.getElementById("comment-input");
  const err = document.getElementById("error-msg");

  elem.style.height = "1px";
  elem.style.height = elem.scrollHeight + "px";

  if (comment.value.trim() != "") {
    comment.classList.add("add-comment");
    comment.classList.remove("add-err-comment");
    err.style.display = "none";
  }
};


// handle menu icon toggle------------------

const handle_icon_toggle = (box_id) => {
  $(`#${box_id}`).toggle()
};


