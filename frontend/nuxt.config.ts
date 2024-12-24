// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
	compatibilityDate: '2024-11-01',
	devtools: { enabled: false },
	css: ['~/assets/css/global.css'],
	app: {
		head: {
			title: 'fix-remont',
			htmlAttrs: {
				class: 'light',
			},
		},
	},
	postcss: {
		plugins: {
			'postcss-mixins': {},
			'postcss-nested': {},
			'postcss-simple-vars': {},
		},
	},
	modules: ['@nuxtjs/google-fonts', '@nuxt/ui'],
	googleFonts: {
		download: true,
		families: {
			Inter: {
				// regular, medium, semibold, bold, extrabold
				wght: [400, 500, 600, 700, 800],
				ital: [],
			},
		},
	},
})
