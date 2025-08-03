window.onload = function() {
    const input_obj = document.getElementById("enter_data");
    const print_btn = document.getElementById("print_and_clear");
    const printData = () => {
    if (input_obj.value.trim() !== "") {
        output_container.innerHTML = "";
        const p = document.createElement("p");
        p.textContent = input_obj.value;
        output_container.appendChild(p);
        input_obj.value = "";
    }
    };
    print_btn.addEventListener("click", printData);
}