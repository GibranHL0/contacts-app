<template>
    <div key="Form" class="pl-20 pt-20">
        <div class="flex items-center h-screen w-full bg-teal-lighter">
            <div class="w-full bg-white rounded shadow-lg p-8 m-4 md:max-w-sm md:mx-auto">
                <h1 class="block w-full text-center text-grey-darkest mb-6 text-2xl font-medium">
                    New Contact
                </h1>
                <form class="mb-4 md:flex md:flex-wrap md:justify-between" action="/" method="post">
                    <div class="field-group mb-4 md:w-1/2">
                        <label class="field-label" for="first_name">First Name</label>
                        <input class="field md:mr-2" type="text" name="first_name" id="first_name">
                    </div>
                    <div class="field-group mb-4 md:w-1/2">
                        <label class="field-label md:ml-2" for="last_name">Last Name</label>
                        <input class="field md:ml-2" type="text" name="last_name" id="last_name">
                    </div>
                    <div class="field-group mb-4 md:w-full">
                        <label class="field-label" for="email">Email</label>
                        <input class="field" type="email" name="email" id="email">
                    </div>
                    <div class="field-group mb-6 md:w-full">
                        <label class="field-label" for="password">Password</label>
                        <input class="field" type="password" name="password" id="password">
                    </div>
                    <button class="btn btn-teal mx-auto" type="submit">Create Account</button>
                </form>
                <a class="link link-grey w-full text-center" href="/login">Already have an account?</a>
            </div>
        </div>
        <!-- <div key="inner" class="bg-white w-2/6">
            <div key="title" class="text-center bg-red-700 text-white">
                <p class=" text-2xl font-medium">New Contact</p>
            </div>
            <div key="square" class="table pl-3 pt-2">
                <div key="in-form" class="table-row-group">
                    <div key="second-row" class="table-row">
                        <div key="name-title" class="table-cell">
                            <p class="text-lg">Name *</p>
                        </div>
                        <div key="name-value" class="table-cell pl-2">
                            <input id="name-val" type="text" 
                            class="border-black border-2 rounded-md">
                        </div>
                    </div>
                    <div key="third-row" class="table-row">
                        <div key="last-title" class="table-cell">
                            <p>Last Name *</p>
                        </div>
                        <div key="last-value" class="table-cell">
                            <input type="text" placeholder="Hola">
                        </div>
                    </div>
                    <div key="fourth-row" class="table-row">
                        <div key="company-title" class="table-cell">
                            <p>Company</p>
                        </div>
                        <div key="company-value" class="table-cell">
                            <input type="text" placeholder="Hola">
                        </div>
                    </div>
                    <div key="fifth-row" class="table-row">
                        <div key="phone-title" class="table-cell">
                            <p>Phone *</p>
                        </div>
                        <div key="phone-value" class="table-cell">
                            <input type="text" placeholder="Hola">
                        </div>
                    </div>
                    <div key="sixth-row" class="table-row">
                        <div key="email-title" class="table-cell">
                            <p>Email *</p>
                        </div>
                        <div key="email-value" class="table-cell">
                            <input type="text" placeholder="Hola">
                        </div>
                    </div>
                </div>
            </div>
            <div key="required" class="table-cell">
                <p>* Required</p>
            </div>
            <div key="actions" class="space-x-2">
                <div key="cancel-button" class="inline-block">
                    <button class="bg-white">Cancel</button>
                </div>
                <div key="accept-button" class="inline-block">
                    <button class="bg-white">Create</button>
                </div>
            </div>
        </div> -->
    </div>
</template>

<script>
export default {
  name: 'Form',
  props: {
  },
  return: {
  },
  methods: {
  }
}
</script>
