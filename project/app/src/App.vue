<template>
  <v-app>
    <v-card tile class="overflow-hidden" min-height="100vh" width="100vw">
      <v-app-bar :color="color" dark fixed app>
        <v-toolbar-title><router-link class="white--text text-decoration-none" :to="{name: 'Home'}" color="white">{{siteName}}</router-link></v-toolbar-title>
        <v-spacer></v-spacer>
        <v-btn icon @click="dialog=true"><v-icon>mdi-account</v-icon></v-btn>
      </v-app-bar>
      <v-dialog v-model="dialog" max-width="320px" persistent>
        <v-card>
          <v-card-title class="blue darken-2 mb-4 white--text">Account</v-card-title>
          <v-card-text>
            <v-container>
              <v-row>
                <v-col cols="12">
                  <v-select label="Account" v-model="account" :items="Object.values(Accounts)" item-text="account.name" item-value="id" :rules="required"></v-select>
                </v-col>
                <v-col cols="12">
                  <v-text-field label="Password" v-model="password" type="password" required></v-text-field>
                </v-col>
              </v-row>
            </v-container>
          </v-card-text>
          <v-card-actions>
            <v-card-text v-if="error" class="red--text">Please enter correct Login information</v-card-text>
            <v-spacer></v-spacer>
            <v-btn :color="color" text @click="Login" dark>Login</v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
      <v-main>
        <v-container fluid class="pa-0">
          <router-view :list="List" :account="account"></router-view>
        </v-container>
      </v-main>
      <v-footer dark padless :color="color">
        <v-card class="flex" flat tile :color="color">
          <v-card-text class="py-2 white--text text-center">{{ new Date().getFullYear() }} — {{siteName}}</v-card-text>
        </v-card>
      </v-footer>
    </v-card>
  </v-app>
</template>
<script>
export default {
  data: () => ({
    required: [
      value => !!value || 'Required.'
    ],
    account: '',
    password: '',
    color: 'primary',
    siteName: 'Feedback',
    login: false,
    dialog: true,
    error: false
  }),
  created() {
    this.$store.dispatch('commitAccount')
  },
  computed: {
    Accounts() {
      return this.$store.getters.getAccount
    },
    List() {
      return this.$store.getters.getList
    }
  },
  methods: {
    Login() {
      if (this.account&&this.password) {
        this.dialog = false
        this.login = true
        this.error = false
        this.$store.dispatch('commitList', this.account)
      } else {
        this.error = true
      }
    }
  }
}
</script>