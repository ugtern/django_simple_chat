<template>
  <mu-container>
    <div v-for="dialog in dialogs">
        <mu-row direction="column"
                justify-content="start"
                align-items="end">
          <p><strong>{{ dialog.user.username }}</strong></p>
          <p>{{ dialog.text }}</p>
          <span>{{ dialog.send_date }}</span>
        </mu-row>
      </div>
    <mu-text-field v-model="text" multi-line :rows="4" full-width placeholder="Введите текст..."></mu-text-field>
    <mu-button full-width color="success" @click="send_massage">Отправить</mu-button>
  </mu-container>
</template>

<script>
    export default {
        name: "Dialog",
        props: {
            id: '',
        },
        data() {
            return {
                dialogs: '',
                text: '',
            }
        },
        created() {
            $.ajaxSetup({
                headers: {'Authorization': 'Token ' + sessionStorage.getItem('auth_token')}
            });
            this.load_dialogs()
        },
        methods: {
            load_dialogs() {
                $.ajax({
                    url: 'http://127.0.0.1:8000/api/v1/chat/dialog/',
                    type: 'GET',
                    data: {
                        room: this.id,
                    },
                    success: (responce) => {
                        this.dialogs = responce.data.data
                }
                })
            },
            send_massage() {
                $.ajax({
                    url: 'http://127.0.0.1:8000/api/v1/chat/dialog/',
                    type: 'POST',
                    data: {
                        room: this.id,
                        text: this.text,
                    },
                    success: (responce) => {
                        this.load_dialogs();
                        this.text = '';
                    },
                    error: (responce) => {
                        console.log(responce.status)
                    }
                })
            },
        }
    }
</script>

<style scoped>
  .dialogs {
    text-align: center;
  }
</style>
