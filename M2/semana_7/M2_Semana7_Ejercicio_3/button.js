const button = document.getElementById('color-button');
const changeBackgroundColor = () => {
    const color_list = ['red', 'blue', 'green', 'yellow', 'cyan', 'pink'];
    const random_index = Math.floor(Math.random() * color_list.length);
    const random_color_class = color_list[random_index];
    const text_container = document.getElementById('text-container');
    const new_background_class = 'general-text-container-settings ' + random_color_class;
    text_container.className = new_background_class;
}

button.addEventListener('click', changeBackgroundColor)