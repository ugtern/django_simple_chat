<template>
  <div>

  <mu-paper :z-depth="1" class="demo-loadmore-wrap">
        <mu-appbar full-width color="teal">
          Пользователи
          <mu-button icon slot="right" @click="refresh()">
            <mu-icon value="re"></mu-icon>
          </mu-button>
        </mu-appbar>
        <mu-container ref="container" class="demo-loadmore-content">
          <mu-load-more @refresh="refresh" :refreshing="refreshing" :loading="loading" @load="load">
            <mu-list>
              <template v-for="user in users" class="room">

                <mu-list-item-title class="users" :class="{checked_user: checking_actual(user.id)}" @click="add_user_to_room(user.id)">
                  {{ user.username }}
                </mu-list-item-title>

                <mu-divider />
              </template>
            </mu-list>
          </mu-load-more>
        </mu-container>
  </mu-paper>

  </div>
</template>

<script>
    import Dialog from '@/components/rooms/Dialog'

    export default {
        name: "Room",
        components: {
            Dialog
        },
        props: {
            id: '',
            current_rooms_users: [],
        },
        data() {
            return {
                users: '',
                refreshing: false,
                loading: false,
                text: 'List',
            }
        },
        created() {
            $.ajaxSetup({
                headers: {'Authorization': 'Token ' + sessionStorage.getItem('auth_token')}
            });
            this.load_users()
        },
        methods: {
            load_users() {
              $.ajax({
                  url: 'http://127.0.0.1:8000/api/v1/chat/users/',
                  type: 'GET',
                  success: (responce) => {
                      this.users = responce.data.data
                  }
              })
            },
            add_user_to_room(user_id) {
              $.ajax({
                  url: 'http://127.0.0.1:8000/api/v1/chat/users/',
                  type: 'POST',
                  data: {
                      user: user_id,
                      room: this.id,
                  },
                  success: (responce) => {
                      this.users = '';
                      this.load_users();
                      console.log('complite');
                  }
              })
            },
            checking_actual(id) {
                return this.current_rooms_users.includes(id)
            },

            refresh () {
              this.refreshing = true;
              this.$refs.container.scrollTop = 0;
              this.load_users();
              setTimeout(() => {
                this.refreshing = false;
                this.text = this.text === 'List' ? 'Menu' : 'List';
              }, 2000);
            },
            load () {
              this.loading = true;
              setTimeout(() => {
                this.loading = false;
              }, 2000)
            }
        }
    }
</script>

<style scoped>
  .room {
    text-align: left;
  }
  .demo-loadmore-wrap {
  width: 100%;
  max-width: 360px;
  height: 420px;
  display: flex;
  flex-direction: column;
  }
  .demo-loadmore-wrap .mu-appbar {
      width: 100%;
    }
.demo-loadmore-content {
  flex: 1;
  overflow: auto;
  -webkit-overflow-scrolling: touch;
}
  .checked_user {
    background-color: #2196f3;
    color: white;
  }

  .users {
    text-align: center;
    cursor: pointer;
  }
</style>
