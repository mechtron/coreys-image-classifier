<template>
    <div id="app">
        <b-navbar fixed="top" toggleable="md" type="dark" variant="info">
            <b-navbar-toggle target="nav_collapse"></b-navbar-toggle>
            <b-navbar-brand href="/#/about">Corey's Image Classifier</b-navbar-brand>
            <b-collapse is-nav id="nav_collapse">
                <b-navbar-nav>
                <b-nav-item href="/#/">Classify</b-nav-item>
                <b-nav-item href="/#/top10">Top 10</b-nav-item>
                </b-navbar-nav>
                <b-navbar-nav class="ml-auto">
                <b-nav-item-dropdown right>
                    <!-- Using button-content slot -->
                    <template slot="button-content">
                    <em>User</em>
                    </template>
                    <b-dropdown-item href="#">Login</b-dropdown-item>
                    <b-dropdown-item href="#">Register</b-dropdown-item>
                    <b-dropdown-item href="#">Profile</b-dropdown-item>
                    <b-dropdown-item href="#">Signout</b-dropdown-item>
                </b-nav-item-dropdown>
                </b-navbar-nav>
            </b-collapse>
        </b-navbar>
    <main>
        <div class="content">
            <router-view></router-view>
        </div>
    </main>
  </div>
</template>

<style lang="scss">
  body {
    margin: 0;
    padding: 0;
  }
  #app {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    color: #2c3e50;
  }
  h1, h2 {
    font-weight: normal;
  }
  ul {
    list-style-type: none;
    padding: 0;
  }
  li {
    display: inline-block;
    margin: 0 10px;
  }
  header {
    top: 0;
    width: 100%;
    min-height: 90px;
    border-bottom: 1px solid #42b983;
    text-align: center;
    background: #ffffff;
  }
  .content {
    flex: 1 1 70%;
    display: flex;
    align-items: center;
    justify-content: center;
  }
  .content-centered {
    display: flex;
    height: calc(100vh - 90px);
    margin-top: 90px;
    align-items: center;
    justify-content: center;
    text-align: center;
    flex-direction: column;
    overflow: shown;
  }
  .link {
    display: block;
    text-decoration: none;
    margin-bottom: 10px;
    color: #2c3e50;
    &--home {
      text-transform: uppercase;
      margin-bottom: 30px;
    }
    &.is-active {
      color: #42b983;
    }
  }
</style>

<script>
  export default {
    data () {
      return {
        posts: [],
        endpoint: '',
      }
    }
  }
</script>
