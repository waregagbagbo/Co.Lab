$(document).on('click','.project-filter li',function(){
    $(this).addClass('[project-filter-active').siblings().removeClass('project-filter-active')
});

/* projects */
$(document).ready(function(){
    $('.list').click(function(){
        const value = $(this).attr('data-filter');
        if(value == 'all'){
            $('.project-box').show('1000')

        }
        else{
            $('.project-box').not('.'+value).hide('1000');
            $('.project-box').filter('.'+value).show('1000');
        }
    });
});

/* dark mode*/
function darkMode(){
    const element = document.body;
    element.classList.toggle('dark-mode')
}