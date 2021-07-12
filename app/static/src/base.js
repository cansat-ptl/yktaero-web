var isDropdownActive = false; /* Kill me */

function menu_closeDropdowns()
{
        let dropdowns = document.getElementsByClassName("dropdown-content");
        for (let i = 0; i < dropdowns.length; i++) {
                let openDropdown = dropdowns[i];
                if (openDropdown.classList.contains('dropdown-content-show')) {
                        openDropdown.classList.remove('dropdown-content-show');
                }
        }

        let dropdown_buttons = document.getElementsByClassName("dropdown-btn");
        for (let i = 0; i < dropdown_buttons.length; i++) {
                let openDropdown = dropdown_buttons[i];
                if (openDropdown.classList.contains('dropdown-btn-active')) {
                        openDropdown.classList.remove('dropdown-btn-active');
                }
        }
}

function menu_showDropdown(e, id) 
{
        if(window.matchMedia("(pointer: coarse)").matches) { 
                if (!e.classList.contains('dropdown-btn-active') && isDropdownActive) {
                        menu_closeDropdowns();

                        isDropdownActive = false;
                }
                if (e.classList.contains('dropdown-btn-active')) {
                        document.getElementById(id).classList.remove("dropdown-content-show");
                        e.classList.remove("dropdown-btn-active");

                        isDropdownActive = false;
                }
                else {
                        document.getElementById(id).classList.add("dropdown-content-show");
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