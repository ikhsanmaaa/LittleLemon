const btnSignIn = document.querySelector(".login-btn");
btnSignIn.addEventListener("click", () => {
  window.location.href = "http://127.0.0.1:8000/admin/";
});

// Loop semua button
Array.from(document.getElementsByClassName("btn-details")).forEach(function (
  button
) {
  button.addEventListener("click", function () {
    // Cari parent card dari tombol
    const card = this.closest(".card");

    const title = card.querySelector(".card-title").innerText;
    const description = card.querySelector(".card-text").innerText;
    const price = card.querySelector(".card-subtitle").innerText;
    const image = card.querySelector(".card-image").getAttribute("src");

    const details = `
      <div class="row">
        <div class="col-md-3">
          <img src="${image}" class="img-fluid">
        </div>
        <div class="col-md">
          <ul class="list-group">
            <li class="list-group-item active" aria-current="true"><h4>${title}</h4></li>
            <li class="list-group-item"><strong>Price:</strong> ${price}</li>
            <li class="list-group-item"><strong>Description:</strong> ${description}</li>
          </ul>
        </div>
      </div>
    `;

    // Masukkan ke dalam container modal
    $(".container-list-group").html(details);
    $("#detailModal").modal("show");
  });
});
