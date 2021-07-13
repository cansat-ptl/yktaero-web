var isDropdownActive = false; /* Kill me */
var isTouchSupported = (('ontouchstart' in window) || (navigator.msMaxTouchPoints > 0)); /* Holy crap what the hell is this */

var onClickTransition = null; 

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

function menu_dropdownDelayed(activeBtn, activeDropdown)
{
        if (!activeBtn.classList.contains('dropdown-btn-active') && isDropdownActive) {
                menu_closeDropdowns(activeBtn, activeDropdown);

                isDropdownActive = false;
        }
        if (activeBtn.classList.contains('dropdown-btn-active')) {
                activeDropdown.classList.remove("dropdown-content-show");
                activeBtn.classList.remove("dropdown-btn-active");

                isDropdownActive = false;
        }
        else {
                activeDropdown.classList.add("dropdown-content-show");
                activeBtn.classList.add("dropdown-btn-active");

                isDropdownActive = true;
        }

        onClickTransition = null;
}

function menu_showDropdown(e, id) 
{
        if (isTouchSupported && onClickTransition == null) { 
                let dropdown = document.getElementById(id);

                onClickTransition = setTimeout(menu_dropdownDelayed, 300, e, dropdown);
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