function signup() {
    // Get input values
    var username = $("#username").val();
    var password = $("#password").val();
    var confirmPassword = $("#confirmPassword").val();

    // Check if all fields are entered with correct data
    if (username.trim() !== '' && password.trim() !== '' && confirmPassword.trim() !== '') {
        // Check if the password and confirm password match
        if (password === confirmPassword) {
            // For demonstration purposes, assume signup is successful
            // Show the pop-up
            $("#popup").fadeIn();

            // Redirect after a delay (e.g., 2 seconds)
            setTimeout(function () {
                window.location.href = "form-page.html"; // Replace with your form page URL
            }, 2000);
        } else {
            alert("Passwords do not match.");
        }
    } else {
        alert("Please enter all required fields.");
    }
}
