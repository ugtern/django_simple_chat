<template>
  <mu-container>
    <mu-row v-for="dialog in dialogs">
      <mu-col span="2">{{ dialog.user.username }}</mu-col>
      <mu-col span="6">{{ dialog.text }}</mu-col>
      <mu-col span="4">{{ dialog.send_date }}</mu-col>
    </mu-row>
  </mu-container>
</template>

<script>
    import $ from 'jquery'

    export default {
        name: "Dialog",
        props: {
            id: '',
        },
        data() {
            return {
                dialogs: '',
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
            }
        }
    }
</script>

<style scoped>
  .dialogs {
    text-align: center;
  }
</style>
