import z, { ZodSchema } from 'zod'

interface Props {
  items?: Ref
  lastRequestInMilliseconds?: Ref
  millisecondsNow?: number
  schema: ZodSchema
  firstSrc?: string
  path: string
}

export const useGetSetNotifyFetch = async ({
  items,
  lastRequestInMilliseconds,
  millisecondsNow,
  schema,
  firstSrc,
  path
}: Props) => {
  try {
    const response = await useFetch(path)

    if (import.meta.client) {
      const toast = useToast()

      if (response.status.value !== 'success') {
        const notify = `Ошибка при получении данных с ${firstSrc}: ${response.status.value}`
        toast.add({ title: notify })
        console.error(notify, response.data.value)
        return
      }

      const { success, data, error } = z.array(schema).safeParse(response.data.value)
      if (!success) {
        const notify = `Ошибка валидации данных с ${firstSrc}: ${response.data.value}`
        toast.add({ title: notify })
        console.error(notify, error)
        return
      }

      if (lastRequestInMilliseconds && millisecondsNow && items) {
        items.value = data
        lastRequestInMilliseconds.value = millisecondsNow
      }
    }
  } catch (err) {
    console.error('Произошла ошибка при выполнении запроса:', err)
  }
}
