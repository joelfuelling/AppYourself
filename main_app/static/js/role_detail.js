// ! Need to CONFIRM IDs for this to work
const dateEl = document.getElementById('id_date');
M.Datepicker.init(dateEl, {
format: 'yyyy-mm-dd',
defaultDate: new Date(),
setDefaultDate: true,
autoClose: true
});

document.addEventListener('DOMContentLoaded', function() {
    let elem= document.querySelector('.modal');
    let instance = M.Modal.init(elem);
    instance.close();
  });
  
  document.addEventListener('DOMContentLoaded', function() {
    let elem = document.querySelectorAll('.dropdown-trigger');
    let instance = M.Dropdown.init(elem);
  });