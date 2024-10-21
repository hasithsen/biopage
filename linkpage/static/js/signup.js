document.addEventListener("DOMContentLoaded", function () {
    // Get the existing div
    var div = document.getElementById("div_id_username");

    // Get the input field
    var input = document.getElementById("id_username");

    // Create a new div for the input group
    var inputGroupDiv = document.createElement("div");
    inputGroupDiv.className = "input-group mb-3";

    // Create the span for the input group text
    var span = document.createElement("span");
    span.className = "input-group-text";
    span.id = "domain-text";
    span.textContent = document.querySelector('meta[name="domain"]').getAttribute('content') + "/";

    // Append the span and input to the new div
    inputGroupDiv.appendChild(span);
    inputGroupDiv.appendChild(input);

    // Append the new div to the original div
    div.appendChild(inputGroupDiv);
});
