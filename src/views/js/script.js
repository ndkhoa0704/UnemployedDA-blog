const get_cookie = (name) => {
    return document.cookie.split(';').some(c => {
        return c.trim().startsWith(name + '=');
    });
}


document.addEventListener('DOMContentLoaded', function () {
    const uploadBtn = document.getElementById('uploadBtn');
    const modalUpload = document.getElementById('modal-upload-file');
    const modalLogin = document.getElementById('modal-login');
    const uploadForm = document.getElementById('uploadForm');
    const loginBtn = document.getElementById('loginBtn');
    const loginForm = document.getElementById('loginForm');
    const logoutBtn = document.getElementById('logoutBtn')


    if (get_cookie('logged-in-status') === true) {
        loginBtn.style.display = 'none';
        logoutBtn.style.visibility = 'visible';
        uploadBtn.style.visibility = 'visible';

    }

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
        console.log(formData)

        fetch('/article', { // Replace '/upload' with your server endpoint
            method: 'POST',
            body: formData,
        })
            .then(response => {
                if (!response.ok) {
                    alert('Cannot upload article')
                }
                return response.json()
            })
            .then(data => {
                modalUpload.style.display = 'none';
                document.body.style.overflow = 'auto'; // Allow background scrolling
                window.location.reload()
            })
            .catch(error => {
                alert('An error occurred while uploading the files.');
            });
    });

    loginForm.addEventListener('submit', function (event) {
        event.preventDefault(); // Prevent form from submitting the traditional way

        let formData = new FormData(loginForm);
        formData.append('scope', 'article:create')

        fetch('/token', {
            method: 'POST',
            body: formData
        })
            .then(response => {
                if (!response.ok) {
                    alert('Invalid username or password')
                }
            })
            .then(data => {
                modalLogin.style.display = 'none';
                document.body.style.overflow = 'auto'; // Allow background scrolling
                document.getElementById('username').value = ''
                document.getElementById('password').value = ''
                window.location.reload()
            })
            .catch(error => {
                alert('An error occurred while loggging in.');
            });
    });
    
    logoutBtn.addEventListener('click', (event) => {
        // Delete cookies and hide upload, logout button
        fetch('/revoke-token', {method: 'GET'})
        loginBtn.style.display = 'none';
        uploadBtn.style.display = 'none';
        logoutBtn.style.visibility = 'visible';
        window.location.reload()
    })

});