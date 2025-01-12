import z from 'zod'

export const useCustomFetch = async ({
  path,
  src,
  schema
}: {
  path: string
  src: string
  schema: z.ZodSchema
}) => {
  const config = useRuntimeConfig()
  const response = await useFetch(`${config.public.apiBase}${path}`)
  console.log(response.data.value)
  let zodData = []
  let zodError = false
  let responseError = false

  if (import.meta.client) {
    const toast = useToast()
    if (response.status.value !== 'success') {
      responseError = true
      const notify = `try GET ${src} => response.status.value !== "success"`
      toast.add({
        title: `${notify}. Details in console.`
      })
      console.error(notify, response.data.value)
    } else {
      const { success, data, error } = schema.safeParse(response.data.value)
      if (!success) {
        // success = false
        const notify = `try GET ${src} => response.data.value  validation Failed`
        toast.add({
          title: `${notify}. Details in console.`
        })
        console.error(notify)
        console.log(response.data.value)
        console.log(error)
        zodError = true
      } else {
        zodData = data
      }
    }
  }

  return { ...response, responseError, zodData, zodError }
}
