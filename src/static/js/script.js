document.addEventListener('DOMContentLoaded', function () {
    const uploadBtn = document.getElementById('uploadBtn');
    const modalUpload = document.getElementById('modal-upload-file');
    const modalLogin = document.getElementById('modal-login');
    // const closeBtn = document.getElementById('closeBtn');
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
                modalUpload.style.display = 'none';
                document.body.style.overflow = 'auto'; // Allow background scrolling
                // window.location.reload()
                console.log(data)
            })
            .catch(error => {
                alert('An error occurred while uploading the files.');
            });
    });

    loginForm.addEventListener('submit', function (event) {
        event.preventDefault(); // Prevent form from submitting the traditional way

        // // Get the values from the form
        // const username = document.getElementById('username').value;
        // const password = document.getElementById('password').value;

        let formData = new FormData(loginForm);
        formData.append('scope', 'article:create')
        console.log(formData);

        fetch('/token', { // Replace '/upload' with your server endpoint
            method: 'POST',
            body: formData
        })
            .then(response => response.json())
            .then(data => {
                modalLogin.style.display = 'none';
                document.body.style.overflow = 'auto'; // Allow background scrolling
                document.getElementById('username').value=''
                document.getElementById('password').value=''


            })
            .catch(error => {
                alert('An error occurred while loggging in.');
            });
    });

});