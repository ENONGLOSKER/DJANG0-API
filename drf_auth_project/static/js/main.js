// static/js/main.js

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function login() {
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    const csrftoken = getCookie('csrftoken');

    fetch('/api/login/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        },
        body: JSON.stringify({ username, password })
    })
    .then(response => response.json())
    .then(data => {
        if (data.message === "Logged in successfully") {
            document.getElementById('login-form').style.display = 'none';
            document.getElementById('logout-button').style.display = 'block';
            document.getElementById('user-info').innerHTML = `<p>Welcome, ${username}!</p>`;
        } else {
            alert("Invalid credentials");
        }
    });
}

function logout() {
    const csrftoken = getCookie('csrftoken');

    fetch('/api/logout/', {
        method: 'POST',
        headers: {
            'X-CSRFToken': csrftoken
        }
    })
    .then(response => response.json())
    .then(data => {
        if (data.message === "Logged out successfully") {
            document.getElementById('login-form').style.display = 'block';
            document.getElementById('logout-button').style.display = 'none';
            document.getElementById('user-info').innerHTML = '';
        }
    });
}
