import type { Config } from 'tailwindcss'

export default <Partial<Config>>{
  theme: {
    extend: {
      colors: {
        orange: {
          50: '#fffceb',
          100: '#fff7c6',
          200: '#ffed88',
          300: '#ffdd4a',
          400: '#feca21',
          500: '#f9af15',
          DEFAULT: '#f9af15',
          600: '#dc8103',
          700: '#b75b06',
          800: '#94460c',
          900: '#7a3a0d',
          950: '#461d02'
        },
        red: {
          50: '#fff3ec',
          100: '#ffe4d3',
          200: '#ffc6a5',
          300: '#ff9e6d',
          400: '#ff6932',
          500: '#ff420a',
          DEFAULT: '#ff420a',
          600: '#ff2600',
          700: '#cc1602',
          800: '#a1130b',
          900: '#82130c',
          950: '#460504'
        }
      }
    }
  }
}
