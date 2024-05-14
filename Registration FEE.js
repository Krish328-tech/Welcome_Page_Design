function validatePasswords() 
{
    var password = document.getElementById("password").value;
    var confirmPassword = document.getElementById("confirmPassword").value;

    if (password === confirmPassword) {
        alert("Thank you for registering!");
        return true;
    } else {
        alert("Passwords do not match. Please enter the same passwords.");
        return false;
    }
}