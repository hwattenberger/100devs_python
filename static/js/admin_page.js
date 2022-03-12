const editBtn = document.querySelectorAll('.adminEdit');
const saveBtn = document.querySelectorAll('.adminSave');
const csrftoken = getCookie('csrftoken');

editBtn.forEach(edit => edit.addEventListener('click', editClick));
saveBtn.forEach(save => save.addEventListener('click', saveClick));

function editClick(e) {
    e.currentTarget.classList.add('hide');   //Hide edit button
    const li = e.target.closest("li");
    const save = li.querySelector(".adminSave");
    save.classList.remove('hide');
    const input = li.querySelector("input");
    input.readOnly = false;
}

function saveClick(e) {
    const li = e.target.closest("li")
    const id = li.id.split('-')[1]
    const what_to_save = li.id.split('-')[0]
    const input = li.querySelector("input");
    fetch(`/100devs/admin/${what_to_save}/${id}/`, {
        method: 'POST',
        credentials: 'same-origin',
        headers:{
            'Accept': 'application/json',
            'X-Requested-With': 'XMLHttpRequest', //Necessary to work with request.is_ajax()
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({'value': input.value})
        }
    ).then(res => {
        const edit = li.querySelector(".adminEdit");
        const save = li.querySelector(".adminSave");
        edit.classList.remove('hide');
        save.classList.add('hide');
        input.readOnly = true;
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