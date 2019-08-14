<template>
  <mu-container @keyup.enter="set_login">
    <mu-container>
      <mu-text-field v-model="login" label="UserName" label-float></mu-text-field><br/>
      <mu-text-field v-model="password" label="Password" label-float error-text="" type="password"></mu-text-field>
    </mu-container>

    <mu-flex justify-content="center" align-items="center">
      <mu-button full-width color="primary" @click="set_login()">Войти</mu-button>
    </mu-flex>

    <div v-on="output_text">{{ output_text }}</div>

  </mu-container>
</template>

<script>
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
  input {
    width: 100%;
  }
</style>
