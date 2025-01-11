module.exports = {
  apps: [
    {
      name: 'frontend',
      port: '3000',
      // exec_mode: 'cluster',
      // instances: 'max',
      // remote
      script: '/home/{{ ansible_user }}/frontend/current/frontend/.output/server/index.mjs'
      // script: '/home/g/fixremont/frontend/.output/server/index.mjs',
    },
    {
      // name: 'fastapi-backend',
      // script: 'fastapi', // Указываем команду fastapi
      // args: 'dev main.py --port 8000', // Указываем аргументы для команды
      // interpreter: 'python3', // Указываем интерпретатор для Python
      // cwd: '/home/{{ ansible_user }}/backend/current/backend/' // Указываем путь к проекту, если нужно
      // env: {
      //   PORT: 8000,
      // },

      name: 'fastapi-backend', // Имя приложения
      script: 'fastapi', // Указываем команду fastapi
      args: 'dev main.py --port 8000', // Аргументы команды
      interpreter: '/bin/bash', // Указываем оболочку для запуска команды
      cwd: '/home/admin/backend/current/backend/'
    }
  ]
}
