<template>
  <div>
    <h1>Чат на vue.js</h1>
    <button @click="log_in" v-if="!auth">Вход</button>
    <button @click="log_out" v-else>Выход</button>
    <Room v-if="auth" @load_dialog="load_dialog" class="left"></Room>
    <Dialog v-if="dialog.show_dialog" :id="dialog.current_room" class="right"></Dialog>
  </div>
</template>

<script>
    import Room from "@/components/rooms/Room";
    import Dialog from "@/components/rooms/Dialog";

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
            log_in() {
                this.$router.push({name: 'login'})
            },
            log_out() {
                sessionStorage.removeItem('auth_token');
                this.auth_method();
            },
            load_dialog(id) {
                this.dialog.current_room = id;
                this.dialog.show_dialog = !this.dialog.show_dialog;
            }
        }
    }
</script>

<style scoped>

</style>
