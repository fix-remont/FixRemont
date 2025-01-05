import { defineNuxtModule, useLogger } from '@nuxt/kit'

export default defineNuxtModule({
  setup(options, nuxt) {
    const logger = useLogger('my-module')

    logger.info('Hello from my module!')
  }
})
