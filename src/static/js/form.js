document.addEventListener('DOMContentLoaded', function () {
    const uploadBtn = document.getElementById('uploadBtn');
    const modalUpload = document.getElementById('modal-upload-file');
    const modalLogin = document.getElementById('modal-login');
    const closeBtn = document.getElementById('closeBtn');
    const uploadForm = document.getElementById('uploadForm');
    const loginBtn = document.getElementById('loginBtn');
    const loginForm = document.getElementById('loginForm');
    

    uploadBtn.addEventListener('click', function () {
        modalUpload.style.display = 'block';
        document.body.style.overflow = 'hidden'; // Prevent background scrolling
    });

    loginBtn.addEventListener('click', function () {
        modalLogin.style.display = 'block';
        document.body.style.overflow = 'hidden'; // Prevent background scrolling
    });


    closeBtn.addEventListener('click', function () {
        if (event.target == modalUpload) {
            modalUpload.style.display = 'none';
            document.body.style.overflow = 'auto'; // Allow background scrolling
        } else if (event.target == modalLogin) {
            modalLogin.style.display = 'none';
            document.body.style.overflow = 'auto'; // Allow background scrolling
        }
    });

    window.addEventListener('click', function (event) {
        if (event.target == modalUpload) {
            modalUpload.style.display = 'none';
            document.body.style.overflow = 'auto'; // Allow background scrolling
        } else if (event.target == modalLogin) {
            modalLogin.style.display = 'none';
            document.body.style.overflow = 'auto'; // Allow background scrolling
        }
    });

    uploadForm.addEventListener('submit', function (event) {
        event.preventDefault(); // Prevent the default form submission

        const formData = new FormData(uploadForm);

        fetch('/article', { // Replace '/upload' with your server endpoint
            method: 'POST',
            body: formData
        })
            .then(response => response.json())
            .then(data => {
                modal.style.display = 'none';
                document.body.style.overflow = 'auto'; // Allow background scrolling
                window.location.reload()
            })
            .catch(error => {
                alert('An error occurred while uploading the files.');
            });
    });

    loginForm.addEventListener('submit', function (event) {
        event.preventDefault(); // Prevent form from submitting the traditional way

        // Get the values from the form
        const username = document.getElementById('username').value;
        const password = document.getElementById('password').value;

        // For demonstration purposes, let's consider a dummy username and password
        const dummyUsername = 'user';
        const dummyPassword = 'password';

        // Check if the entered username and password match the dummy ones
        if (username === dummyUsername && password === dummyPassword) {
            alert('Login successful!');
            // Here you can redirect the user to another page or perform other actions
        } else {
            document.getElementById('errorMessage').textContent = 'Invalid username or password';
        }
    });

});