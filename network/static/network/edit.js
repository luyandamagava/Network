if (document.readyState === "loading") {  // Loading hasn't finished yet
    document.addEventListener("DOMContentLoaded", function() {
        console.log("DOMContentLoaded event");
        document.querySelectorAll('.edit_post').forEach(element => {
            element.addEventListener('click',() => {
                let data = element.dataset.data;
                console.log("edit_post"+ data+ " button clicked");
                edit_post(data);
            });
        });

        document.querySelectorAll('.cancel_edit_post').forEach(element => {
            element.addEventListener('click',(event) => {
                event.preventDefault();
                let data = element.dataset.data;
                console.log("cancel_edit button clicked");
                cancel_edit(data);
            });
        });

        document.querySelectorAll('.like_post').forEach(element => {
            element.addEventListener('click',() => {
                let data = element.dataset.data;
                console.log("like button clicked");
                like_post(data);
            });
        });
    });
} else {  // `DOMContentLoaded` has already fired
    console.log("DOMContentLoaded has already fired");
    document.querySelectorAll('.edit_post').forEach(element => {
        element.addEventListener('click',() => {
            let data = element.dataset.data;
            console.log("edit_post"+ data+ " button clicked");
            edit_post(data);
        });
    });


    document.querySelectorAll('.cancel_edit_post').forEach(element => {
        element.addEventListener('click',(event) => {
            event.preventDefault();
            let data = element.dataset.data;
            console.log("cancel_edit button clicked");
            cancel_edit(data);
        });
    });
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');


function edit_post(data) {
    console.log("edit_post function called");
    document.querySelector('#edit_post_form' + data).style.display = 'block';
    document.querySelector('#content' + data).style.display = 'none';
    document.querySelector('#buttonsLCE' + data).style.display = 'none';
}

function cancel_edit(data) {
    console.log(`cancel_edit${data} function called`);
    document.querySelector('#edit_post_form' + data).style.display = 'none';
    document.querySelector('#content' + data).style.display = 'flex';
    document.querySelector('#buttonsLCE' + data).style.display = 'flex';
}

function like_post(data) {
    console.log(`like_post${data} function called`);
    let csrftoken = getCookie('csrftoken');
    let like_button = document.querySelector(`#like_post${data}`);
    // Log the value of `data` to the console
    console.log(`data: ${data}`);

    fetch(`/like_post/${data}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({
            post_id: data,
        })
    })
    .then(response => {
        // Log the server response to the console
        console.log(`Response: ${response}`);
        response.clone().text().then(text => console.log(`Response body: ${text}`));
        return response.json();
    })
    .then(result => {
        like_button.innerHTML = result.message;

    })
    .catch(error => {
        // Log any errors to the console
        console.log(`Error: ${error}`);
    });
}