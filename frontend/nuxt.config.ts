// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
	compatibilityDate: '2024-11-01',
	devtools: { enabled: false },
	css: ['~/assets/css/global.css'],
	app: {
		head: {
			title: 'fix-remont',
		},
	},
	postcss: {
		plugins: {
			'postcss-mixins': {},
			'postcss-simple-vars': {},
			'postcss-nested': {},
			'postcss-functions': {
				functions: {
					// fn: (size: number, koefficient: number) => `${size * koefficient}px`,
				},
			},
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
