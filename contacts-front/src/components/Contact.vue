<template>
  <div key="contact" class="pl-5">
      <div key="box" class="bg-white w-2/5 rounded-md space-y-2">
        <div key="modifiers" class="flex space-x-2 bg-red-700 rounded-t-md">
            <div class="inline-block w-2/3">
                <p class="text-white pl-2 text-lg">Contact Info: </p>
            </div>
        </div>
        <div key="text" class="block text-xl pl-2">
            <h1 class="font-bold">{{ name }} {{last_name}}</h1>
            <h1 class="pl-2">{{ company }}</h1>
            <h1 class="pl-2">{{ phone_number }}</h1>
            <h1 class="pl-2">{{ email }}</h1>
        </div>
        <div key="actions" class="space-x-2 text-center pb-5 pt-4">
            <div class="inline-block pr-10">
                <button class="bg-black h-8 pl-4 pr-4 rounded-md text-white">Edit</button>
            </div>
            <div class="inline-block">
                <button class="bg-red-700 h-8 pl-4 pr-4 rounded-md text-white">Delete</button>
            </div>
        </div>
      </div>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  props: {
    name: String,
    last_name: String,
    company: String,
    phone_number: Number,
    email: String
  }
}
</script>


#gray 300
green 50
purple 100
indigo 200
