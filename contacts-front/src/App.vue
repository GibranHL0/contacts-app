<template>
  <div key="main">
    <Welcome/>
    <Contact/>
  </div>
</template>

<script>
import Welcome from './components/Welcome.vue'
import Contact from './components/Contact.vue'

export default {
  name: 'App',
  components: {
    Welcome,
    Contact
  }
}
</script>
