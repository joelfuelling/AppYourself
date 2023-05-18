// ! Need to CONFIRM IDs for this to work
const dateEl = document.getElementById('id_pub_date');
M.Datepicker.init(dateEl, {
format: 'yyyy-mm-dd',
defaultDate: new Date(),
setDefaultDate: true,
autoClose: true
});