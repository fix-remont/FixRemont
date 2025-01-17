export default defineAppConfig({
  ui: {
    primary: 'orange',
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
      base: 'text-center',
      font: 'font-semibold',
      rounded: 'rounded-full',
      size: {
        custom: 'text-xs sm:text-xl'
      },
      padding: {
        custom: 'px-3 py-2 sm:px-6 sm:py-6'
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
