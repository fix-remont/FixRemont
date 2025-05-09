import { theme } from '#tailwind-config'

// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: '2024-11-01',
  devtools: { enabled: false },
  css: ['~/assets/css/global.css'],
  app: {
    head: {
      title: 'fix-remont',
      htmlAttrs: {
        class: 'light'
      }
    }
  },
  postcss: {
    plugins: {
      'postcss-mixins': {},
      'postcss-simple-vars': {},
      'postcss-nested': {},
      'postcss-functions': {}
    }
  },
  image: {
    format: ['avif', 'webp']
  },
  modules: ['@nuxtjs/google-fonts', '@nuxt/ui', '@nuxt/image', '@pinia/nuxt'],
  runtimeConfig: {
    public: {
      apiBase: 'http://158.160.151.235:7000/api',
      mediaPath: 'http://158.160.151.235:5000/media/'
    }
  },
  googleFonts: {
    download: true,
    families: {
      Inter: {
        // regular, medium, semibold, bold, extrabold
        wght: [400, 500, 600, 700, 800],
        ital: []
      }
    }
  }
})
