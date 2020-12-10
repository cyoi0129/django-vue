<template>
  <v-container>
    <h1>{{detail.employee.name}}'s performance</h1>
    <v-card flat class="ma-4">  
      <v-row>
        <h2>Performance score</h2>
        <v-col cols="12">
          <v-rating v-model="item.data.score" color="yellow darken-3" background-color="grey darken-1" empty-icon="$ratingFull" hover large></v-rating>
        </v-col>
        <v-col cols="12">
          <v-textarea name="input-7-1" label="Comment" v-model="item.data.comment"></v-textarea>
        </v-col>
        <v-col cols="12">
          <v-switch v-model="item.data.status" inset label="Done"></v-switch>
        </v-col>
        <v-col cols="12">
          <v-btn class="my-2" color="primary" dark @click="save">Save</v-btn>
        </v-col>
        <v-col cols="12">
          <router-link to="/">&lt; Back to list</router-link>
        </v-col> 
      </v-row>
    </v-card>
    <v-overlay :value="overlay">
      <v-progress-circular indeterminate size="64"></v-progress-circular>
    </v-overlay>
  </v-container>
</template>
<script>
export default {
  props:['id','detail'],
  data: () => ({
    overlay: false,
    item: {
      id: '',
      data: {},
    }
  }),
  methods: {
    save: function() {
      this.$store.dispatch('commitItem', this.item)
      this.overlay = !this.overlay
    }
  },
  watch: {
    overlay (val) {
      val && setTimeout(() => {
        this.overlay = false
      }, 1000)
    }
  },
  created() {
    this.item.id = this.id
    this.item.data = this.detail
    if (this.detail.status === 'done') {
      this.item.data.status = true
    } else {
      this.item.data.status = false
    }
  }
}
</script>