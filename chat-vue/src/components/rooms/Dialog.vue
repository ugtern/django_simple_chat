<template>
  <div class="dialogs">
    <div v-for="dialog in dialogs">
      <h2>{{ dialog.username }}</h2>
      <p>{{ dialog.text }}</p>
      <span>{{ dialog.send_date }}</span>
    </div>
  </div>
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
