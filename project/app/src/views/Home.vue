<template>
  <v-container class="pa-0">
    <v-card class="pa-2" tile flat>
      <h1>Feedback list</h1>
        <v-list dense max-width="600">
            <v-list-item-group>
                <v-list-item v-for="(item, index) in List" :key="index" :to="{name: 'Detail', params: {id:index, detail: item}}" class="ma-4">
                <v-list-item-icon><v-icon>mdi-account</v-icon></v-list-item-icon>
                <v-list-item-content>
                    <v-list-item-title v-text="item.employee.name"></v-list-item-title>
                    <v-list-item-subtitle v-text="item.status"></v-list-item-subtitle>
                </v-list-item-content>
                </v-list-item>
            </v-list-item-group>
        </v-list>
    </v-card>
  </v-container>
</template>
<script>
export default {
    props:['List','account'],
}
</script>