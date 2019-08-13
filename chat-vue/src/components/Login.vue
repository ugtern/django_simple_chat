<template>
  <mu-container @keyup.enter="set_login">
    <mu-row>
      <input type="text" v-model="login" placeholder="Логин"/>
    </mu-row>
    <mu-row>
      <input type="password" v-model="password" placeholder="Пароль"/>
    </mu-row>
    <mu-button color="primary" @click="set_login()">Войти</mu-button>
    <div v-on="output_text">{{ output_text }}</div>
  </mu-container>
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
                        sessionStorage.setItem('auth_token', responce.data.attributes.auth_token);
                        this.$emit('log_in', true)
                    },
                    error: (responce) => {
                        if (responce.status === 400){
                            this.output_text = 'Логин или пароль неверен';
                        }
                    },
                })
            }
        }
    }
</script>

<style scoped>

</style>
