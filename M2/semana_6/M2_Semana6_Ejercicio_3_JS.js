document.addEventListener('DOMContentLoaded', function () {
    const yesRadio = document.getElementById('employee_yes');
    const noRadio = document.getElementById('employee_no');
    const jobPositionContainer = document.getElementById('job_position_container');
    const showJobPosition = () => {
        if (yesRadio.checked) {
            jobPositionContainer.style.display = 'flex';    
        }
    }
    const hideJobPosition = () => {
        if (noRadio.checked) {
            jobPositionContainer.style.display = 'none';
        }   
    }
    if (yesRadio) {
        yesRadio.addEventListener('change', showJobPosition);
    }
    if (noRadio) {
        noRadio.addEventListener('change', hideJobPosition);
    }
});