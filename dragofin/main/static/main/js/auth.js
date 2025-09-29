function toggleForm() {
    const imageSection = document.getElementById('image-section');
    const formSection = document.getElementById('form-section');
    const formContainer = document.querySelector('.form-container');

    if (formContainer.classList.contains('register')) {
        // Возврат к форме входа
        formContainer.classList.remove('register');
        formContainer.innerHTML = `
            <h2>Вход в аккаунт</h2>
            <form id="auth-form" method="post">
                {% csrf_token %}
                <input type="email" name="email" placeholder="Почта" required>
                <input type="password" name="password" placeholder="Пароль" required>
                <button type="submit" class="main-button">Войти в аккаунт</button>
            </form>
            <button type="button" class="secondary-button" onclick="toggleForm()">Нет аккаунта?</button>
        `;
        imageSection.style.order = "0";
        formSection.style.order = "1";
    } else {
        // Переход к форме регистрации
        formContainer.classList.add('register');
        formContainer.innerHTML = `
            <h2>Регистрация</h2>
            <form id="auth-form"  method="post">
                {% csrf_token %}
                <input type="text" name="name" placeholder="Имя" required>
                <input type="email" name="email" placeholder="Почта" required>
                <input type="password" name="password" placeholder="Пароль" required>
                <button type="submit" class="main-button">Зарегистрироваться</button>
            </form>
            <button type="button" class="secondary-button" onclick="toggleForm()">Уже есть аккаунт?</button>
        `;
        imageSection.style.order = "1";
        formSection.style.order = "0";
    }
}

// Установим порядок по умолчанию
document.getElementById('image-section').style.order = "0";
document.getElementById('form-section').style.order = "1";