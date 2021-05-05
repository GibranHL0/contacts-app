<template>
  <div key="main">
    <Form/>
    <br><br>
    <Welcome/>
    <br><br>
    <Contact :company="'UPAEP'" :last_name="'Herrera'" :name="'Gibran'" 
    :phone_number="2221056718" :email="'gibranhl2@gmail.com'"/>
  </div>
</template>

<script>
import Welcome from './components/Welcome.vue'
import Contact from './components/Contact.vue'
import Form from './components/Form.vue'

export default {
  name: 'App',
  components: {
    Welcome,
    Contact,
    Form
  }
}
</script>
