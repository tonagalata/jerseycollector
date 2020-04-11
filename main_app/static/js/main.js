document.addEventListener('DOMContentLoaded', function() {
  let simpleDrop = document.querySelector('#dropdown1');
  let dropdownOptions = {
      'closeOnClick': true,
      'hover':true
  }
  let instanceDropdown1 = M.Dropdown.init(simpleDrop, dropdownOptions);
});