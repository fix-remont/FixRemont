import z from 'zod'
export const FeedBackFormschema = z.object({
	email: z.string({ required_error: 'Обязательное поле' }).email('Неверное значение'),
	message: z.string({ required_error: 'Обязательное поле' }).min(5, 'Не менее 5 символов'),
	phone: z.string({ required_error: 'Введите номер телефона' }).regex(/^\+?[1-9]\d{1,14}$/, 'Введите корректный номер телефона'),
	isAgree: z.boolean().refine((value) => value === true, { message: 'Вы должны согласиться с условиями' }),
})

export type FeedBackForm = z.infer<typeof FeedBackFormschema>
