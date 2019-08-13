<template>
  <div @keyup.enter="set_login">
    <input type="text" v-model="login" placeholder="Логин"/>
    <input type="password" v-model="password" placeholder="Пороль"/>
    <button @click="set_login()" >Войти</button>
    <div v-on="output_text">{{ output_text }}</div>
  </div>
</template>

<script>
    import $ from 'jquery'

    export default {
        name: "Login",
        data() {
            return {
                login: '',
                password: '',
                output_text: '',
            }
        },
        methods: {
            set_login() {
                $.ajax({
                    url: 'http://127.0.0.1:8000/auth/token/login/',
                    type: 'POST',
                    data: {
                        username: this.login,
                        password: this.password,
                    },
                    success: (responce) => {
                        this.output_text = 'Вход успешен';
                        alert('Вход успешен');
                        sessionStorage.setItem('auth_token', responce.data.attributes.auth_token);
                        this.$router.push({name: 'home'});
                    },
                    error: (responce) => {
                        if (responce.status === 400){
                            this.output_text = 'Логин или пароль неверен';
                            alert('Логин или пароль неверен');
                        }
                    },
                })
            }
        }
    }
</script>

<style scoped>

</style>
