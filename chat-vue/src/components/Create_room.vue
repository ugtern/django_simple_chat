<template>
  <mu-container>
    <mu-text-field v-model="room_name" placeholder="Название комнаты"></mu-text-field>
    <mu-button full-width color="success" @click="create_new_room">Создать</mu-button>
  </mu-container>
</template>

<script>
    export default {
        name: "Create_room",
        data() {
            return {
                room_name: ''
            }
        },
        created() {
            $.ajaxSetup({
                headers: {'Authorization': 'Token ' + sessionStorage.getItem('auth_token')}
            });
        },
        methods: {
            create_new_room() {
                $.ajax({
                  url: 'http://127.0.0.1:8000/api/v1/chat/room/',
                  type: 'POST',
                  data: {
                      room_name: this.room_name
                  },
                  success: (responce) => {
                      this.users = '';
                      this.load_users();
                  }
                })
            }
        }
    }
</script>

<style scoped>

</style>
