module.exports = {
	apps: [
		{
			name: 'frontend',
			port: '3000',
			// exec_mode: 'cluster',
			// instances: 'max',
			// remote
			script: '/home/staging/fixremont/frontend/current/frontend/.output/server/index.mjs',
			// script: '/home/g/fixremont/frontend/.output/server/index.mjs',
		},
	],
}
// module.exports = {
// 	apps: [
// 		{
// 			name: 'frontend',
// 			script: '/home/g/fixremont/frontend/.output/server/index.mjs',
// 			instances: 'max', // или число, если хотите
// 			exec_mode: 'cluster', // если используете кластерный режим
// 			watch: true, // если хотите следить за изменениями файлов
// 			env: {
// 				NODE_ENV: 'production', // или 'development', в зависимости от вашего окружения
// 				PORT: 3000 // если ваше приложение использует переменные окружения для порта
// 			},
// 		},
// 	],
// };

