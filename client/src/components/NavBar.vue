<template>
  <div class="mb-3">
    <b-navbar toggleable="md" type="dark" variant="primary">
      <b-navbar-brand to="/">
        <img src="/logo.png" alt="logo" width=50>
        Pseudo-Nephron-Project
      </b-navbar-brand>
      
      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-collapse id="nav-collapse" is-nav>

        <b-navbar-nav right v-if="!$auth.isAuthenticated && !$auth.loading">
          <b-nav-item>
            <b-button class="btn btn-primary btn-margin" @click.prevent="login">Login</b-button>
          </b-nav-item>
        </b-navbar-nav>

        <b-navbar-nav class="ml-auto" v-if="$auth.isAuthenticated">
          <b-nav-item-dropdown right>

            <template slot="button-content">
              <img class="nav-user-profile rounded-circle" :src="$auth.user.picture" alt="User's profile picture" width="50"/>
            </template>

            <b-dropdown-item>
              <div class="dropdown-header">{{ $auth.user.name }}</div>
            </b-dropdown-item>

            <b-dropdown-item>
              <router-link to="/profile" class="dropdown-item dropdown-profile">
                <font-awesome-icon class="mr-3" icon="user" />Profile
              </router-link>
            </b-dropdown-item>

            <b-dropdown-item>
              <router-link to="/" class="dropdown-item" @click.native="logout">
                <font-awesome-icon class="mr-3" icon="power-off" />Log out
              </router-link>
            </b-dropdown-item>

          </b-nav-item-dropdown>
        </b-navbar-nav>

      </b-collapse>
    </b-navbar>
  </div>
</template>

<script>
  export default {
    name: "NavBar",
    methods: {
      login() {
        this.$auth.loginWithRedirect();
        this.$router.push({ path: "/" });
      },
      logout() {
        this.$auth.logout();
        this.$router.push({ path: "/" });
      }
    }
  };
</script>
