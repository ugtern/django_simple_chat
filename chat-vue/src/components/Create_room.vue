<template>
  <mu-container>
    <mu-text-field v-model="room_name" placeholder="Название комнаты"></mu-text-field>
    <mu-button full-width color="success">Создать</mu-button>
  </mu-container>
</template>

<script>
    export default {
        name: "Create_room",
        data() {
            return {
                room_name: ''
            }
        }
    }
</script>

<style scoped>

</style>
