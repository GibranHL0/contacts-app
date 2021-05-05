<template>
    <div key="Form" class="pl-20 pt-20">
        <div class="flex items-center h-screen w-full">
            <div class="w-full bg-white rounded shadow-lg p-8 m-4 md:max-w-sm md:mx-auto">
                <h1 class="block w-full text-center text-black mb-6 text-2xl font-medium">
                    New Contact
                </h1>
                <form class="mb-4 md:flex md:flex-wrap md:justify-between" action="/" method="post">
                    <div class="flex flex-col mb-4 md:w-1/2">
                        <label class="font-medium text-lg text-gray-900 mb-2" for="first_name">
                            Name *
                        </label>
                        <input class="border py-2 px-3 text-gray-900 md:mr-2" type="text" name="first_name" id="first_name" pattern="[a-zA-Z]{1,}" required>
                    </div>
                    <div class="flex flex-col mb-4 md:w-1/2">
                        <label class="font-medium text-lg text-gray-900 mb-2 md:ml-2" for="last_name">
                            Last Name *
                        </label>
                        <input class="border py-2 px-3 text-gray-900 md:ml-2" type="text" name="last_name" id="last_name" pattern="[a-zA-Z]{1,}" required>
                    </div>
                    <div class="flex flex-col mb-4 md:w-full">
                        <label class="font-medium text-lg text-gray-900 mb-2" for="company">
                            Company
                        </label>
                        <input class="border py-2 px-3 text-gray-900" type="text" name="company" id="company">
                    </div>
                    <div class="flex flex-col mb-4 md:w-full">
                        <label class="font-medium text-lg text-gray-900 mb-2" for="phone">
                            Phone
                        </label>
                        <input class="border py-2 px-3 text-gray-900" type="number" name="phone" id="phone">
                    </div>
                    <div class="flex flex-col mb-4 md:w-full">
                        <label class="font-medium text-lg text-gray-900 mb-2" for="email">
                            Email *
                        </label>
                        <input class="border py-2 px-3 text-gray-900" type="email" name="email" id="email" required>
                        <p class="text-sm py-4">* Required</p>
                    </div>
                    <button class="bg-black hover:bg-red-400 mx-auto text-white px-2 py-2 rounded-md" type="submit">Create Account</button>
                </form>
                <a class=" block no-underline text-sm text-gray-900 w-full text-center" href="/login">Cancel</a>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
export default {
  name: 'Form',
  props: {
  },
  return: {
  },
  methods: {
      sendInfo(){
          console.log()
      },
      created(){
        const article = {title: "Vue"};
        axios.post("https://reqres.in/api/articles", article)
        .then(response => this.articleId = response.data.id);
      },
  }
}
</script>
