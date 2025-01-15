import { z } from 'zod'
import { revalidationResponseInMilliseconds } from '~/assets/variables'
import { defineStore } from 'pinia'
import { ref } from 'vue'

const TariffSchema = z.object({
  name: z.string(),
  description: z.string(),
  cost: z.string(),
  image: z.string()
})
const config = useRuntimeConfig()

const path = '/tariffs'
const src = '/home/block_3'
const schema = TariffSchema

export type Tariff = z.infer<typeof TariffSchema>

type Local = Tariff

export default defineStore('tariffs', () => {
  const lastRequestInMilliseconds = ref<number | null>(null)
  const items = ref<Local[]>([])

  const millisecondsNow = +new Date()

  const fetchTariffs = async () => {
    try {
      const response = await useFetch(`${config.public.apiBase}${path}`)

      if (import.meta.client) {
        const toast = useToast()

        if (response.status.value !== 'success') {
          const notify = `Ошибка при получении данных с ${src}: ${response.status.value}`
          toast.add({ title: notify })
          console.error(notify, response.data.value)
          return
        }

        const { success, data, error } = z.array(schema).safeParse(response.data.value)
        if (!success) {
          const notify = `Ошибка валидации данных с ${src}: ${response.data.value}`
          toast.add({ title: notify })
          console.error(notify, error)
          return
        }

        items.value = data
        lastRequestInMilliseconds.value = millisecondsNow
      }
    } catch (err) {
      console.error('Произошла ошибка при выполнении запроса:', err)
    }
  }

  if (
    lastRequestInMilliseconds.value == null ||
    lastRequestInMilliseconds.value + revalidationResponseInMilliseconds < millisecondsNow
  ) {
    fetchTariffs()
  }

  return { items }
})
