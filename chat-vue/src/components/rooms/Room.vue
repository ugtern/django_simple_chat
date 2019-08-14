<template>
  <div>

  <mu-paper :z-depth="1" class="demo-loadmore-wrap">
      <mu-appbar full-width color="teal">
        Список комнат
        <mu-button icon slot="right" @click="refresh()">
          <mu-icon value="re"></mu-icon>
        </mu-button>
      </mu-appbar>
      <mu-container ref="container" class="demo-loadmore-content">
        <mu-load-more @refresh="refresh" :refreshing="refreshing" :loading="loading" @load="load">
          <mu-list>
            <template v-for="room in rooms" class="room">


              <mu-menu open-on-hover>
                  <mu-button>

                  <mu-list-item>
                    <mu-list-item-title  @click="load_dialog(room.id)" @>{{ room.creator.username }}</mu-list-item-title>
                    <mu-list-item-title  @click="load_dialog(room.id)">{{ room.creation_date }}</mu-list-item-title>
                  </mu-list-item>

                    </mu-button>

                  <mu-list slot="content">
                    <p><strong>Пользователи:</strong></p>
                    <div v-for="user in room.invited">
                      <mu-list-item>
                        <mu-list-item-title>
                          {{ user.username }}
                        </mu-list-item-title>
                      </mu-list-item>
                    </div>
                  </mu-list>
              </mu-menu>

              <mu-divider />
            </template>
          </mu-list>
        </mu-load-more>
      </mu-container>
</mu-paper>

<!--      <ul v-for="room in rooms" class="room" @click="load_dialog(room.id)">-->
<!--        <li>-->
<!--          Создатель комнаты = {{ room.creator.username }}-->
<!--        </li>-->
<!--          <ul v-for="user in room.invited" class="invited">-->
<!--            Приглашенные пользователи:-->
<!--            <li>-->
<!--           {{ user.username }}-->
<!--            </li>-->
<!--          </ul>-->
<!--        <li>-->
<!--          Дата создания комнаты: {{ room.creation_date }}-->
<!--        </li>-->
<!--      </ul>-->
  </div>
</template>

<script>
    import Dialog from '@/components/rooms/Dialog'

    export default {
        name: "Room",
        components: {
            Dialog
        },
        data() {
            return {
                rooms: '',
                refreshing: false,
                loading: false,
                text: 'List',
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
            },

            refresh () {
              this.refreshing = true;
              this.$refs.container.scrollTop = 0;
              setTimeout(() => {
                this.refreshing = false;
                this.text = this.text === 'List' ? 'Menu' : 'List';
              }, 2000)
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
</style>
