<template>
  <div key="Welcome">
    <div key="content" class="grid justify-center">
      <div key="title">
        <h2 class=" flex text-4xl justify-center pt-40 text-white font-bold">
          Welcome to Gibran Contacts APP
        </h2>
      </div>
      <div key="start" class="pt-20 pb-5 space-x-2 text-center">
          <div class="inline-block">
            <input v-model="user" type="email" id="email" size="30" required class="h-10 rounded-md"
                   v-on:keyup.enter="enter()">
          </div>
          <div class="inline-block">
            <button type="submit" class=" bg-black h-10 rounded-md w-16 text-white"
                    v-on="enter()">Start</button>
          </div>
      </div>
      <div class="text-center">
        <label for="email" class="text-white font-semibold">Put your email to start</label>
      </div>
    </div> 
  </div>
</template>

<script>
export default {
  name: 'Welcome',
  props: {
    msg: String
  },
  return: {
    user: ""
  },
  methods: {
        enter(){
            console.log(this.user)
        }
    }
}
</script>
