import { revalidationResponseInMilliseconds } from '~/assets/variables'
import { defineStore } from 'pinia'
import { ref } from 'vue'
import { TariffSchema, type Tariff } from '~/shared/types/responses'
import { useGetSetNotifyFetch } from '~/composables/get-set-notify-fetch'

const path = '/tariffs'
const firstSrc = '/home/block_3'
const schema = TariffSchema
type Local = Tariff

export default defineStore('tariffs', () => {
  const config = useRuntimeConfig()
  const lastRequestInMilliseconds = ref<number | null>(null)
  const items = ref<Local[]>([])
  const millisecondsNow = +new Date()

  if (
    lastRequestInMilliseconds.value == null ||
    lastRequestInMilliseconds.value + revalidationResponseInMilliseconds < millisecondsNow
  ) {
    useGetSetNotifyFetch({
      items,
      lastRequestInMilliseconds,
      millisecondsNow,
      schema,
      path: `${config.public.apiBase}${path}`,
      firstSrc
    })
  }

  return { items }
})
