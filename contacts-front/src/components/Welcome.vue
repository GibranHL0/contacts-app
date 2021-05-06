<template>
  <div key="Welcome">
    <div key="content" class="grid justify-center">
      <div key="title">
        <h2 class=" flex text-4xl justify-center pt-20 text-white font-bold">
          Welcome to Gibran Contacts APP
        </h2>
      </div>
      <div key="start" class=" pt-14 pb-5 space-x-2 text-center">
          <div class="inline-block">
            <button class=" bg-black h-10 rounded-md px-2 py-2 text-white hover:bg-white hover:text-black"
             @click="toggleModal = !toggleModal">
              Add A New Contact
            </button>
          </div>
      </div>
      <div v-if="toggleModal" class="fixed overflow-x-hidden overflow-y-auto inset-0 flex justify-center items-center z-50">
        <div class="relative mx-auto w-auto max-w-2xl">
          <div key="Form" class="pl-20 pt-20">
            <div class="flex items-center h-screen w-full">
                <div class="w-full bg-white rounded shadow-lg p-8 m-4 md:max-w-sm md:mx-auto">
                    <h1 class="block w-full text-center text-black mb-6 text-2xl font-medium">
                        New Contact
                    </h1>
                    <form id="form" class="mb-4 md:flex md:flex-wrap md:justify-between" >
                        <div class="flex flex-col mb-4 md:w-1/2">
                            <label class="font-medium text-lg text-gray-900 mb-2" for="first_name">
                                Name *
                            </label>
                            <input class="border py-2 px-3 text-gray-900 md:mr-2" type="text" v-model="name" maxlength="40" pattern="[a-zA-Z]*" required>
                        </div>
                        <div class="flex flex-col mb-4 md:w-1/2">
                            <label class="font-medium text-lg text-gray-900 mb-2 md:ml-2" for="last_name">
                                Last Name *
                            </label>
                            <input class="border py-2 px-3 text-gray-900 md:ml-2" type="text" v-model="last_name" maxlength="40" pattern="[a-zA-Z]*" required>
                        </div>
                        <div class="flex flex-col mb-4 md:w-full">
                            <label class="font-medium text-lg text-gray-900 mb-2" for="company">
                                Company
                            </label>
                            <input class="border py-2 px-3 text-gray-900" type="text" v-model="company" maxlength="40">
                        </div>
                        <div class="flex flex-col mb-4 md:w-full">
                            <label class="font-medium text-lg text-gray-900 mb-2" for="phone">
                                Phone
                            </label>
                            <input class="border py-2 px-3 text-gray-900" type="number" v-model="phone" max="100">
                        </div>
                        <div class="flex flex-col mb-4 md:w-full">
                            <label class="font-medium text-lg text-gray-900 mb-2" for="email">
                                Email *
                            </label>
                            <label v-if="email_error" class="font-light text-red-600">Email Already Exists</label>
                            <label v-if="email_format" class="font-light text-red-600">This is not an email</label>
                            <input class="border py-2 px-3 text-gray-900" type="email" maxlength="40" v-model="email" required>
                            <p class="text-sm py-4">* Required</p>
                        </div>
                        <button class="bg-black hover:bg-red-400 mx-auto text-white px-2 py-2 rounded-md" @click="check()">
                          Create Account
                        </button>
                    </form>
                      <button class="pt-4 block no-underline text-sm w-full text-gray-900 text-center hover:underline" @click="toggleModal=false; email_error=false; resetValues()">
                        Cancel
                      </button>
                </div>
            </div>
          </div>
        </div>
      </div>
      <div v-if="toggleModal" class="absolute z-40 inset-0 opacity-25 bg-black"></div>
    </div> 
  </div>
</template>

<script>

import axios from 'axios';

export default {
  name: 'Welcome',
  data(){
    return {
      toggleModal: false,
      email_error: false,
      email_format: false,
      name_error: false,
      last_name_error: false,
      name : '',
      last_name: '',
      company: '',
      phone: '',
      email: '',
    }
  },
  props: {
  },
  mounted() {
    // axios.get("https://contacts-api-gibran-academy.herokuapp.com/contacts")
    //   .then(
    //     (response) => {console.log(response.data)}
    //   )
    // axios.get("https://contacts-api-gibran-academy.herokuapp.com/emails")
    // .then(
    //   (response) => {this.emails = response.data; console.log(response.data); console.log(this.emails[0])}
    // )
  },
  methods: {
    check(){
      var form = document.getElementById('form');
      if(form.checkValidity() == true){
        this.sendInfo()
      }
    },
    sendInfo(){
      axios.post("https://contacts-api-gibran-academy.herokuapp.com/contacts", {
        email: this.email,
        name: this.name,
        last_name: this.last_name,
        company: this.company, 
        phone: this.phone
      })
      .then(response => {
        if (response.data.msg == "Email already exists"){
          this.email_error = true;
        }else{
          this.toggleModal = false;
          this.email_error = false;
          this.resetValues()
        }
      });
    },
    resetValues(){
      this.email = '';
      this.name = '';
      this.last_name = '';
      this.company = '';
      this.phone = '';
    },
    validateEmail(email){
      const re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
      return re.test(String(email).toLowerCase());
    }
    }
}
</script>
