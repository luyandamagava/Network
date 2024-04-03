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

function edit_post(data) {
    console.log("edit_post function called");
    document.querySelector('#edit_post_form' + data).style.display = 'block';
    document.querySelector('#content' + data).style.display = 'none';
    document.querySelector('#buttonsLCE' + data).style.display = 'none';
}

function cancel_edit(data) {
    console.log("cancel_edit" + data + " function called");
    document.querySelector('#edit_post_form' + data).style.display = 'none';
    document.querySelector('#content' + data).style.display = 'flex';
    document.querySelector('#buttonsLCE' + data).style.display = 'flex';
}
 