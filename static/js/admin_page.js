const editBtn = document.querySelectorAll('.adminEdit');
const csrftoken = getCookie('csrftoken');

editBtn.forEach(edit => edit.addEventListener('click', editClick));

function editClick(e) {
    e.target.classList.add("test");
    li = e.target.closest("li")
    console.log(li.id)
    fetch('/100devs/admin/cohort/1/', {
        method: 'POST',
        credentials: 'same-origin',
        headers:{
            'Accept': 'application/json',
            'X-Requested-With': 'XMLHttpRequest', //Necessary to work with request.is_ajax()
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({'test':'hii'})
        }
    ).then(res => {
        console.log("WOAH")
    })
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


// function editInput(edit) {
//     edit.classList.add("test")
//     edit.addEventListener('click', console.log("Hi"));
// }