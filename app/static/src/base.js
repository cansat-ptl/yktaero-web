var isDropdownActive = false; /* Kill me */
var isTouch = (('ontouchstart' in window) || (navigator.msMaxTouchPoints > 0)); /* Holy crap what the hell is this */

function menu_closeDropdowns(activeBtn = null, activeDropdown = null)
{
        let dropdown_buttons = document.getElementsByClassName("dropdown-btn");
        for (let i = 0; i < dropdown_buttons.length; i++) {
                if (dropdown_buttons[i] != activeBtn && dropdown_buttons[i].classList.contains('dropdown-btn-active')) {
                        dropdown_buttons[i].classList.remove('dropdown-btn-active');
                }
        }

        let dropdowns = document.getElementsByClassName("dropdown-content");
        for (let i = 0; i < dropdowns.length; i++) {
                if (dropdowns[i] != activeDropdown && dropdowns[i].classList.contains('dropdown-content-show')) {
                        dropdowns[i].classList.remove('dropdown-content-show');
                }
        }
}

function menu_showDropdown(e, id) 
{
        if (isTouch) { 
                let dropdown = document.getElementById(id);

                if (!e.classList.contains('dropdown-btn-active') && isDropdownActive) {
                        menu_closeDropdowns(e, dropdown);

                        isDropdownActive = false;
                }
                if (e.classList.contains('dropdown-btn-active')) {
                        dropdown.classList.remove("dropdown-content-show");
                        e.classList.remove("dropdown-btn-active");

                        isDropdownActive = false;
                }
                else {
                        dropdown.classList.add("dropdown-content-show");
                        e.classList.add("dropdown-btn-active");

                        isDropdownActive = true;
                }
        }
}

window.onclick = function(event) 
{
        if (!event.target.matches('.dropdown-btn')) {
                if (isDropdownActive) {
                        menu_closeDropdowns();
                        isDropdownActive = false;
                }
        }
} 