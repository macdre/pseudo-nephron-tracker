<template>
  <b-container fluid>
    <b-row class="align-items-center profile-header">
      <b-col class="md-2 mb-3">
        <img
          :src="$auth.user.picture"
          alt="User's profile picture"
          class="rounded-circle img-fluid profile-picture"
        />
      </b-col>
      <b-col class="text-center text-md-left">
        <h2>{{ $auth.user.name }}</h2>
        <p class="lead text-muted">{{ $auth.user.email }}</p>
      </b-col>
    </b-row>

    <b-row>
      <pre v-highlightjs="JSON.stringify($auth.user, null, 2)" class="rounded w-100"><code class="json"></code></pre>
    </b-row>
  </b-container>
</template>
