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

function navbar_showDropdown(e, id) 
{
        if(window.matchMedia("(pointer: coarse)").matches) {
                menu_closeDropdowns();
                document.getElementById(id).classList.toggle("dropdown-content-show");
                e.classList.toggle("dropdown-btn-active");
        }
}

window.onclick = function(event) 
{
        if (!event.target.matches('.dropdown-btn')) {
                menu_closeDropdowns();
        }
} 