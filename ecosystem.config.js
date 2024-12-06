module.exports = {
	apps: [
		{
			name: 'frontend',
			port: '3000',
			// exec_mode: 'cluster',
			// instances: 'max',
			// remote
			script: './frontend/current/frontend/.output/server/index.mjs',
		},
	],
}
