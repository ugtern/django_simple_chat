<template>
  <div>
      <ul v-for="room in rooms" class="room" @click="load_dialog(room.id)">
        <li>
          Создатель комнаты = {{ room.creator.username }}
        </li>
          <ul v-for="user in room.invited" class="invited">
            Приглашенные пользователи:
            <li>
           {{ user.username }}
            </li>
          </ul>
        <li>
          Дата создания комнаты: {{ room.creation_date }}
        </li>
      </ul>
  </div>
</template>

<script>
    import $ from 'jquery'
    import Dialog from '@/components/rooms/Dialog'

    export default {
        name: "Room",
        components: {
            Dialog
        },
        data() {
            return {
                rooms: '',
            }
        },
        created() {
            $.ajaxSetup({
                headers: {'Authorization': 'Token ' + sessionStorage.getItem('auth_token')}
            });
            this.load_room()
        },
        methods: {
            load_room() {
              $.ajax({
                  url: 'http://127.0.0.1:8000/api/v1/chat/room/',
                  type: 'GET',
                  success: (responce) => {
                      this.rooms = responce.data.data
                  }
              })
            },
            load_dialog(id) {
                this.$emit('load_dialog', id)
            }
        }
    }
</script>

<style scoped>
  .room {
    text-align: left;
  }
</style>
