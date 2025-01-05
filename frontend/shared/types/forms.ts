import z from 'zod'

const phoneShema = z
  .string({ required_error: 'Введите номер телефона' })
  .regex(/^\+?[1-9]\d{1,14}$/, 'Введите корректный номер телефона')

export const FeedBackFormschema = z.object({
  email: z.string({ required_error: 'Обязательное поле' }).email('Неверное значение'),
  message: z.string({ required_error: 'Обязательное поле' }).min(5, 'Не менее 5 символов'),
  phone: phoneShema,
  isAgree: z
    .boolean()
    .refine((value) => value === true, { message: 'Вы должны согласиться с условиями' })
})

export const ConsultationFormSchema = z.object({
  phone: phoneShema,
  messenger: z.string({ required_error: 'Обязательное поле' })
})

export type FeedBackForm = z.infer<typeof FeedBackFormschema>
export type ConsultationForm = z.infer<typeof ConsultationFormSchema>
