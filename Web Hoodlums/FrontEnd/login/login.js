function login() {
    // Get input values
    var username = $("#username").val();
    var password = $("#password").val();

    // Check if all fields are entered with correct data
    if (username.trim() !== '' && password.trim() !== '') {
        // For demonstration purposes, assume login is successful
        // Show the pop-up
        $("#popup").fadeIn();

        // Redirect after a delay (e.g., 2 seconds)
        setTimeout(function () {
            window.location.href = "form-page.html"; // Replace with your form page URL
        }, 2000);
    } else {
        alert("Please enter both username and password.");
    }
}