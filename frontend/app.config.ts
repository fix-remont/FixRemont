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
				sm: 'text-[18px]',
			},
			rounded: 'rounded-[50px]',
			padding: {
				sm: 'px-[20px]  py-[10px] md:px-[45px]  md:py-[34px] ',
			},
			variant: {
				none: 'bg-[#F4F4F4]',
			},
		},
		textarea: {
			size: {
				sm: 'text-[18px]',
			},
			base: 'bg-[#F4F4F4]',
			rounded: 'rounded-[50px]',
			padding: {
				sm: 'px-[20px]  py-[10px] md:px-[45px]  md:py-[34px] ',
			},
			variant: {
				none: 'bg-[#F4F4F4]',
			},
		},
		notifications: {
			position: 'top-0 bottom-[unset] left-0 right-[unset]',
		},
	},
})
