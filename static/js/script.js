document.addEventListener("DOMContentLoaded", function(event) {
    const successMessages = document.getElementsByClassName("success-message");
    if (successMessages !== null) {
        for (let message of successMessages) {
            setTimeout(function() {
                message.style.display = "none";
            }, 5000);
        }
    }
});