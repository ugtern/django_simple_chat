<template>
  <mu-container>
    <mu-appbar style="width: 100%;" color="primary">
      <mu-menu slot="left">
        <mu-button flat>MENU</mu-button>
        <mu-list slot="content">
          <mu-list-item button>
            <mu-list-item-content>
              <mu-list-item-title>Главная</mu-list-item-title>
            </mu-list-item-content>
          </mu-list-item>
          <mu-list-item button>
            <mu-list-item-content>
              <mu-list-item-title>Чат</mu-list-item-title>
            </mu-list-item-content>
          </mu-list-item>
          <mu-list-item button>
            <mu-list-item-content>
              <mu-list-item-title>Парсер</mu-list-item-title>
            </mu-list-item-content>
          </mu-list-item>
        </mu-list>
      </mu-menu>
      ОАОД чат
    </mu-appbar>
    <mu-row>
      <mu-col span="3" xl="3">
        <Room v-if="auth" @load_dialog="load_dialog"></Room>
      </mu-col>
      <mu-col span="6" xl="6">
        <Dialog v-if="dialog.show_dialog" :id="dialog.current_room" :key="dialog.current_room"></Dialog>
      </mu-col>
      <mu-col span="3" xl="3">
        <mu-row>
          <Login @log_in="log_in" v-if="!auth"></Login>
        </mu-row>
        <mu-flex justify-content="center" align-items="center">
          <mu-button @click="log_out" v-if="auth" full-width color="secondary">Выход</mu-button>
        </mu-flex>
      </mu-col>
    </mu-row>
  </mu-container>
</template>

<script>
    import Room from "@/components/rooms/Room";
    import Dialog from "@/components/rooms/Dialog";
    import Login from "@/components/Login";

    export default {
        name: "Home",
        data() {
          return {
              auth: false,
              dialog: {
                  current_room: '',
                  show_dialog: false,
              },
          }
        },
        created() {
            this.auth_method();
        },
        components: {
            Room,
            Dialog,
            Login,
        },
        computed: {
        },
        methods: {
            auth_method() {
                if (sessionStorage.getItem('auth_token')) {
                    this.auth = true
                }
                else {
                    this.auth = false
                }
            },
            log_in(auth) {
                this.auth = auth;
            },
            log_out() {
                sessionStorage.removeItem('auth_token');
                this.dialog.show_dialog = false;
                this.auth_method();
            },
            load_dialog(id) {

                let show = this.dialog.show_dialog;
                let current_id = this.dialog.current_room;
                if (show) {
                    if (current_id === id) {
                        this.dialog.show_dialog = false
                    }
                    else {
                        this.dialog.current_room = id;
                    }
                }
                else {
                    this.dialog.current_room = id;
                    this.dialog.show_dialog = !this.dialog.show_dialog;
                }
            }
        }
    }
</script>

<style scoped>

</style>
