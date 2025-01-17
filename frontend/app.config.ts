export default defineAppConfig({
  ui: {
    primary: 'yellow',
    // primary: '#f9af15',
    input: {
      // color: {
      // 	white: {
      // 		outline: 'border-none bg-[#F4F4F4] ring-[var(--c-orange)] focus:ring-[var(--c-orange)]',
      // 	},
      // 	red: {
      // 		outline: 'bg-[#F4F4F4]',
      // 	},
      // },
      size: {
        sm: 'text-[18px]'
      },
      rounded: 'rounded-[50px]',
      padding: {
        sm: 'px-[20px]  py-[10px] md:px-[45px]  md:py-[34px] '
      },
      variant: {
        none: 'bg-[#F4F4F4]',
        darkGray: 'bg-[#4A4A4A] text-sm lg:text-lg'
      }
    },
    select: {
      size: {
        sm: 'text-[18px]'
      },
      rounded: 'rounded-[50px]',
      padding: {
        sm: 'px-[20px]  py-[10px] md:px-[45px]  md:py-[34px] '
      },
      variant: {
        none: 'bg-[#F4F4F4]',
        darkGray: 'bg-[#4A4A4A] text-sm lg:text-lg'
      }
    },
    textarea: {
      size: {
        sm: 'text-[18px]'
      },
      base: 'bg-[#F4F4F4]',
      rounded: 'rounded-[50px]',
      padding: {
        sm: 'px-[20px]  py-[10px] md:px-[45px]  md:py-[34px] '
      },
      variant: {
        none: 'bg-[#F4F4F4]'
      }
    },
    notifications: {
      position: 'top-0 bottom-[unset] left-0 right-[unset]'
    },
    button: {
      rounded: 'rounded-full',
      color: {
        orange: {
          solid:
            'shadow-sm text-white bg-orange hover:bg-orange-600 disabled:bg-gray-900 aria-disabled:bg-gray-900 dark:bg-white dark:hover:bg-gray-100 dark:disabled:bg-white dark:aria-disabled:bg-white focus-visible:ring-inset focus-visible:ring-2 focus-visible:ring-primary-500 dark:focus-visible:ring-primary-400',
          link: 'text-white-900 dark:text-white underline-offset-4 hover:underline focus-visible:ring-inset focus-visible:ring-2 focus-visible:ring-primary-500 dark:focus-visible:ring-primary-400'
        }
      }
    },
    carousel: {
      // container: 'gap-[9px] sm:gap-[50px] w-full sm:w-[initial]',
      indicators: {
        wrapper: 'justify-end',
        base: 'h-[5px] w-[5px] sm:h-2 sm:w-2',
        active: 'bg-[var(--c-black)]',
        inactive: 'bg-[var(--c-gray)]'
      },
      arrows: {
        wrapper: 'flex gap-2 justify-start mt-2'
      }
    }
  }
})
