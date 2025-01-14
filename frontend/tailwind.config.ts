import type { Config } from 'tailwindcss'
import defaultTheme from 'tailwindcss/defaultTheme'

export default <Partial<Config>>{
  theme: {
    extend: {
      colors: {
        orange: {
          100: '#fff7c6',
          200: '#ffed88',
          300: '#ffdd4a',
          400: '#feca21',
          500: '#f9af15',
          600: '#dc8103',
          700: '#b75b06',
          800: '#94460c',
          900: '#7a3a0d',
          DEFAULT: '#f9af15'
        }
      }
    }
  }
}
