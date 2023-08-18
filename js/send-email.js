document.addEventListener("DOMContentLoaded", function() {
    console.log("testando")
    const submitButton = document.getElementById("submit-button");
    const responseDiv = document.getElementById("response");

    submitButton.addEventListener("click", function() {
        const name = document.getElementById("name").value;
        const email = document.getElementById("email").value;
        const message = document.getElementById("message").value;

        const templateParams = {
            to_email: "recipient@email.com",
            from_name: name,
            from_email: email,
            message: message
        };

        emailjs.send("service_7w59omo", "template_zqmocl9", templateParams)
            .then(function(response) {
                responseDiv.textContent = "Message sent successfully!";
            }, function(error) {
                responseDiv.textContent = "Error sending message.";
            });
    });
});
