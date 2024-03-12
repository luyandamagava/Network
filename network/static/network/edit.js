if (document.readyState === "loading") {  // Loading hasn't finished yet
    document.addEventListener("DOMContentLoaded", function() {
        console.log("DOMContentLoaded event");
        let data = document.querySelector('#object').dataset.data;
        document.querySelector('#edit_post').addEventListener('click',() => {
            console.log("edit_post button clicked");
            edit_post();
        });

        document.querySelector('#cancel_edit_post').addEventListener('click',() => {
            event.preventDefault();
            console.log("cancel_edit button clicked");
            cancel_edit();
        });
    });
} else {  // `DOMContentLoaded` has already fired
    console.log("DOMContentLoaded has already fired");
    document.querySelector('#edit_post').addEventListener('click',() => {
        console.log("edit_post button clicked");
        edit_post();
    });

    document.querySelector('#cancel_edit_post').addEventListener('click',() => {
        console.log("cancel_edit button clicked");
        cancel_edit();
    });
}

function edit_post() {
    let data = document.querySelector('#object').dataset.data;
    console.log("edit_post function called");
    document.querySelector('#edit_post_form').style.display = 'block';
    document.querySelector('#content' + data).style.display = 'none';
    document.querySelector('#buttonsLCE' + data).style.display = 'none';
}

function cancel_edit() {
    let data = document.querySelector('#object').dataset.data;
    document.querySelector('#edit_post_form').style.display = 'none';
    document.querySelector('#content' + data).style.display = 'flex';
    document.querySelector('#buttonsLCE' + data).style.display = 'flex';
}
